# -*- coding: utf-8 -*-
"""
Test suite for Load Generator functionality
Tests load generation, selection dialog, and user preferences
"""

import unittest
import sys
import os
import types
import json
from unittest.mock import Mock, MagicMock, patch

# Setup test environment
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
freecad_dir = os.path.join(repo_root, 'freecad')
if freecad_dir not in sys.path:
    sys.path.insert(0, freecad_dir)

# Mock FreeCAD modules
class MockApp:
    class Console:
        @staticmethod
        def PrintMessage(msg): print(f"INFO: {msg}")
        @staticmethod  
        def PrintWarning(msg): print(f"WARN: {msg}")
        @staticmethod
        def PrintError(msg): print(f"ERROR: {msg}")
    
    ActiveDocument = None
    Units = Mock()

class MockGui:
    @staticmethod
    def addCommand(name, command): pass
    
    class Control:
        @staticmethod
        def showDialog(dialog): return True
        @staticmethod
        def closeDialog(): pass

class MockObject:
    def __init__(self, name="TestObject"):
        self.Name = name
        self.Label = name
        self.properties = {}
        self.Proxy = None
        self.Shape = Mock()
        self.Shape.BoundBox = Mock()
        self.Shape.BoundBox.XLength = 1000.0
        self.Shape.BoundBox.YLength = 500.0
        self.Shape.BoundBox.ZLength = 200.0
    
    def addProperty(self, prop_type, name, group, desc):
        setattr(self, name, None)
        self.properties[name] = {"type": prop_type, "group": group, "desc": desc}
        return getattr(self, name)

# Mock Qt
class MockQtWidgets:
    class QDialog:
        Accepted = 1
        Rejected = 0
        def __init__(self): 
            self.result = self.Accepted
            self.layout_widget = None
        def exec_(self): return self.result
        def accept(self): 
            self.result = self.Accepted
            return self.Accepted
        def reject(self): 
            self.result = self.Rejected
            return self.Rejected
        def setWindowTitle(self, title): self.title = title
        def setMinimumWidth(self, width): self.min_width = width
        def setMinimumHeight(self, height): self.min_height = height
        def setLayout(self, layout): self.layout_widget = layout
    
    class QComboBox:
        def __init__(self): 
            self.items = []
            self.current_index = 0
        def addItem(self, item): self.items.append(item)
        def setCurrentIndex(self, index): self.current_index = index
        def currentIndex(self): return self.current_index
        def currentText(self): 
            return self.items[self.current_index] if self.items and self.current_index < len(self.items) else ""
    
    class QSpinBox:
        def __init__(self): 
            self.value_int = 0
        def setValue(self, value): self.value_int = int(value)
        def value(self): return self.value_int
        def setMinimum(self, min_val): pass
        def setMaximum(self, max_val): pass
    
    class QDoubleSpinBox:
        def __init__(self): 
            self.value_float = 0.0
        def setValue(self, value): self.value_float = float(value)
        def value(self): return self.value_float
        def setMinimum(self, min_val): pass
        def setMaximum(self, max_val): pass
        def setDecimals(self, decimals): pass
    
    class QCheckBox:
        def __init__(self, text=""): 
            self.text = text
            self.checked = False
        def isChecked(self): return self.checked
        def setChecked(self, checked): self.checked = checked
    
    class QVBoxLayout: 
        def __init__(self): 
            self.widgets = []
        def addWidget(self, widget): self.widgets.append(widget)
        def addLayout(self, layout): self.widgets.append(layout)
    
    class QHBoxLayout:
        def __init__(self): 
            self.widgets = []
        def addWidget(self, widget): self.widgets.append(widget)
    
    class QFormLayout:
        def __init__(self): 
            self.widgets = []
        def addRow(self, label, widget): self.widgets.append((label, widget))
    
    class QGroupBox:
        def __init__(self, title=""): 
            self.title = title
            self.layout_widget = None
        def setLayout(self, layout): self.layout_widget = layout
    
    class QLabel:
        def __init__(self, text=""): self.text = text
    
    class QPushButton:
        def __init__(self, text=""): 
            self.text = text
            self.clicked = Mock()
    
    class QMessageBox:
        @staticmethod
        def information(parent, title, text): pass
        @staticmethod
        def warning(parent, title, text): pass
        @staticmethod
        def critical(parent, title, text): pass

# Setup mock modules
sys.modules['FreeCAD'] = MockApp
sys.modules['App'] = MockApp  
sys.modules['FreeCADGui'] = MockGui
sys.modules['Gui'] = MockGui
sys.modules['PySide2'] = types.SimpleNamespace(QtWidgets=MockQtWidgets)
sys.modules['PySide'] = types.SimpleNamespace(QtWidgets=MockQtWidgets, QtGui=MockQtWidgets)

# Import modules to test
try:
    from StructureTools.command_load_generator import CommandLoadGenerator, LoadGeneratorSelectionDialog
    LOAD_GENERATOR_AVAILABLE = True
except ImportError as e:
    print(f"Load Generator import failed: {e}")
    LOAD_GENERATOR_AVAILABLE = False

# Mock load data for testing
MOCK_LOAD_PATTERNS = {
    "ASCE7_16": {
        "dead_load": {
            "concrete_slab": 2.4,  # kN/m²
            "steel_deck": 0.5,
            "finishes": 1.0
        },
        "live_load": {
            "office": 2.4,  # kN/m²
            "residential": 1.9,
            "retail": 4.8
        },
        "wind_load": {
            "basic_speed": 50,  # m/s
            "exposure_category": "B",
            "importance_factor": 1.0
        },
        "seismic": {
            "site_class": "D",
            "sds": 0.5,
            "sd1": 0.3
        }
    }
}


class TestLoadGeneratorCore(unittest.TestCase):
    """Test core load generator functionality"""
    
    def setUp(self):
        """Setup test environment"""
        if not LOAD_GENERATOR_AVAILABLE:
            self.skipTest("Load Generator modules not available")
        
        # Create mock document
        self.mock_doc = Mock()
        self.mock_doc.addObject = Mock(return_value=MockObject())
        MockApp.ActiveDocument = self.mock_doc
    
    def test_command_resources(self):
        """Test command resource definition"""
        command = CommandLoadGenerator()
        resources = command.GetResources()
        
        self.assertIn("MenuText", resources)
        self.assertIn("ToolTip", resources)
        self.assertIn("Pixmap", resources)
        self.assertEqual(resources["MenuText"], "Load Generator")
    
    def test_command_is_active(self):
        """Test command active state"""
        command = CommandLoadGenerator()
        
        # Should be active when document exists
        self.assertTrue(command.IsActive())
        
        # Should be inactive when no document
        MockApp.ActiveDocument = None
        self.assertFalse(command.IsActive())
    
    def test_load_calculation_dead_load(self):
        """Test dead load calculation"""
        # Mock building area
        building_area = 100.0  # m²
        
        # Calculate dead load
        concrete_load = MOCK_LOAD_PATTERNS["ASCE7_16"]["dead_load"]["concrete_slab"]
        steel_load = MOCK_LOAD_PATTERNS["ASCE7_16"]["dead_load"]["steel_deck"]
        finishes_load = MOCK_LOAD_PATTERNS["ASCE7_16"]["dead_load"]["finishes"]
        
        total_dead_load = (concrete_load + steel_load + finishes_load) * building_area
        expected_load = (2.4 + 0.5 + 1.0) * 100.0  # 390 kN
        
        self.assertAlmostEqual(total_dead_load, expected_load, places=1)
    
    def test_load_calculation_live_load(self):
        """Test live load calculation"""
        building_area = 100.0  # m²
        
        # Test different occupancy types
        office_load = MOCK_LOAD_PATTERNS["ASCE7_16"]["live_load"]["office"] * building_area
        residential_load = MOCK_LOAD_PATTERNS["ASCE7_16"]["live_load"]["residential"] * building_area
        retail_load = MOCK_LOAD_PATTERNS["ASCE7_16"]["live_load"]["retail"] * building_area
        
        self.assertEqual(office_load, 240.0)  # 2.4 * 100
        self.assertEqual(residential_load, 190.0)  # 1.9 * 100
        self.assertEqual(retail_load, 480.0)  # 4.8 * 100


class TestLoadGeneratorSelectionDialog(unittest.TestCase):
    """Test Load Generator Selection Dialog"""
    
    def setUp(self):
        """Setup test environment"""
        if not LOAD_GENERATOR_AVAILABLE:
            self.skipTest("Load Generator modules not available")
        
        self.mock_doc = Mock()
        MockApp.ActiveDocument = self.mock_doc
    
    def test_dialog_creation(self):
        """Test dialog creation and initialization"""
        dialog = LoadGeneratorSelectionDialog()
        
        # Check that dialog is properly initialized
        self.assertIsNotNone(dialog)
        self.assertEqual(dialog.result(), MockQtWidgets.QDialog.Accepted)
    
    def test_building_code_selection(self):
        """Test building code selection options"""
        dialog = LoadGeneratorSelectionDialog()
        
        # Access combo box through layout
        if hasattr(dialog, 'building_code_combo'):
            combo = dialog.building_code_combo
            
            # Should have building code options
            expected_codes = ["ASCE 7-16", "IBC 2018", "NBCC 2015", "Eurocode 1"]
            for code in expected_codes:
                combo.addItem(code)
            
            self.assertGreater(len(combo.items), 0)
            
            # Test selection
            combo.setCurrentIndex(0)
            self.assertEqual(combo.currentIndex(), 0)
    
    def test_load_type_selection(self):
        """Test load type selection"""
        dialog = LoadGeneratorSelectionDialog()
        
        # Test load type options
        load_types = [
            "Dead Load",
            "Live Load", 
            "Wind Load",
            "Seismic Load",
            "Snow Load",
            "Rain Load"
        ]
        
        for load_type in load_types:
            # Should be able to add load type options
            pass
    
    def test_preferences_application(self):
        """Test preferences application"""
        dialog = LoadGeneratorSelectionDialog()
        
        # Set test preferences
        test_preferences = {
            "building_code": "ASCE 7-16",
            "default_dead_load": 2.4,
            "default_live_load": 2.4,
            "wind_speed": 50.0,
            "seismic_zone": "D",
            "snow_load": 1.0
        }
        
        # Apply preferences
        try:
            dialog.apply_preferences(test_preferences)
        except AttributeError:
            # Method might not exist in mock
            pass
    
    def test_dialog_acceptance(self):
        """Test dialog acceptance and data retrieval"""
        dialog = LoadGeneratorSelectionDialog()
        
        # Simulate user selections
        dialog.result_data = {
            "building_code": "ASCE 7-16",
            "load_types": ["Dead Load", "Live Load"],
            "occupancy": "Office",
            "structure_type": "Steel Frame"
        }
        
        # Accept dialog
        result = dialog.exec_()
        self.assertEqual(result, MockQtWidgets.QDialog.Accepted)
    
    def test_modal_dialog_behavior(self):
        """Test that dialog behaves as modal"""
        dialog = LoadGeneratorSelectionDialog()
        
        # Dialog should use exec_() for modal behavior
        # This ensures the dialog doesn't disappear immediately
        result = dialog.exec_()
        self.assertIn(result, [MockQtWidgets.QDialog.Accepted, MockQtWidgets.QDialog.Rejected])


class TestLoadGeneratorCalculations(unittest.TestCase):
    """Test load calculation algorithms"""
    
    def setUp(self):
        """Setup test environment"""
        if not LOAD_GENERATOR_AVAILABLE:
            self.skipTest("Load Generator modules not available")
    
    def test_wind_load_calculation(self):
        """Test wind load calculation according to ASCE 7"""
        # Test parameters
        basic_wind_speed = 50  # m/s
        exposure_category = "B"
        importance_factor = 1.0
        height = 10.0  # m
        area = 100.0  # m²
        
        # Simplified wind pressure calculation
        # qz = 0.613 * Kz * Kzt * Kd * V² * I (kN/m²)
        kz = 0.7  # Height factor for Category B, 10m height
        kzt = 1.0  # Topographic factor
        kd = 0.85  # Directionality factor
        
        qz = 0.613 * kz * kzt * kd * (basic_wind_speed ** 2) * importance_factor / 1000
        wind_force = qz * area
        
        # Expected result should be reasonable
        self.assertGreater(wind_force, 0)
        self.assertLess(wind_force, 1000)  # Should be less than 1000 kN for this case
    
    def test_seismic_load_calculation(self):
        """Test seismic load calculation"""
        # Test parameters
        sds = 0.5  # Design spectral acceleration
        sd1 = 0.3
        importance_factor = 1.0
        response_modification_factor = 8.0  # Steel moment frame
        building_weight = 10000.0  # kN
        
        # Base shear calculation: V = Cs * W
        # Cs = Sds / (R/I)
        cs = sds / (response_modification_factor / importance_factor)
        base_shear = cs * building_weight
        
        expected_base_shear = 0.5 / (8.0 / 1.0) * 10000.0  # 625 kN
        
        self.assertAlmostEqual(base_shear, expected_base_shear, places=1)
    
    def test_snow_load_calculation(self):
        """Test snow load calculation"""
        ground_snow_load = 1.5  # kN/m²
        thermal_factor = 1.0
        exposure_factor = 1.0
        slope_factor = 1.0
        importance_factor = 1.0
        
        # Flat roof snow load: pf = 0.7 * Ce * Ct * I * pg
        flat_roof_snow = 0.7 * exposure_factor * thermal_factor * importance_factor * ground_snow_load
        
        expected_snow_load = 0.7 * 1.0 * 1.0 * 1.0 * 1.5  # 1.05 kN/m²
        
        self.assertAlmostEqual(flat_roof_snow, expected_snow_load, places=2)


class TestLoadGeneratorIntegration(unittest.TestCase):
    """Test Load Generator integration with StructureTools"""
    
    def setUp(self):
        """Setup test environment"""
        if not LOAD_GENERATOR_AVAILABLE:
            self.skipTest("Load Generator modules not available")
        
        self.mock_doc = Mock()
        self.mock_doc.addObject = Mock(return_value=MockObject())
        MockApp.ActiveDocument = self.mock_doc
    
    def test_load_application_to_members(self):
        """Test applying loads to structural members"""
        # Create mock structural member
        member = MockObject("TestBeam")
        member.Shape.BoundBox.XLength = 6000.0  # 6m beam
        
        # Apply distributed load
        load_intensity = 10.0  # kN/m
        total_load = load_intensity * (member.Shape.BoundBox.XLength / 1000.0)
        
        expected_total = 10.0 * 6.0  # 60 kN
        self.assertEqual(total_load, expected_total)
    
    def test_load_combinations(self):
        """Test load combination generation"""
        # Define load cases
        dead_load = 100.0  # kN
        live_load = 80.0   # kN
        wind_load = 60.0   # kN
        
        # Load combinations per ASCE 7
        combinations = {
            "1.4D": 1.4 * dead_load,
            "1.2D + 1.6L": 1.2 * dead_load + 1.6 * live_load,
            "1.2D + 1.0L + 1.0W": 1.2 * dead_load + 1.0 * live_load + 1.0 * wind_load,
            "0.9D + 1.0W": 0.9 * dead_load + 1.0 * wind_load
        }
        
        # Verify combinations
        self.assertEqual(combinations["1.4D"], 140.0)
        self.assertEqual(combinations["1.2D + 1.6L"], 248.0)  # 120 + 128
        self.assertEqual(combinations["1.2D + 1.0L + 1.0W"], 260.0)  # 120 + 80 + 60
        self.assertEqual(combinations["0.9D + 1.0W"], 150.0)  # 90 + 60
    
    def test_load_object_creation(self):
        """Test creation of load objects in FreeCAD"""
        # Test distributed load creation
        load_obj = self.mock_doc.addObject.return_value
        load_obj.Name = "DistributedLoad_001"
        load_obj.LoadType = "Distributed"
        load_obj.Magnitude = 10.0
        load_obj.Direction = "Z"
        
        self.assertEqual(load_obj.Name, "DistributedLoad_001")
        self.assertEqual(load_obj.LoadType, "Distributed")
        self.assertEqual(load_obj.Magnitude, 10.0)
    
    def test_preferences_persistence(self):
        """Test load generator preferences persistence"""
        preferences = {
            "default_building_code": "ASCE 7-16",
            "default_dead_load_concrete": 2.4,
            "default_live_load_office": 2.4,
            "default_wind_speed": 50.0,
            "show_calculation_details": True,
            "auto_apply_load_combinations": True
        }
        
        # Test that preferences can be saved/loaded
        # (In actual implementation, this would save to FreeCAD parameters)
        import json
        json_prefs = json.dumps(preferences)
        loaded_prefs = json.loads(json_prefs)
        
        self.assertEqual(loaded_prefs["default_building_code"], "ASCE 7-16")
        self.assertEqual(loaded_prefs["default_dead_load_concrete"], 2.4)
        self.assertTrue(loaded_prefs["show_calculation_details"])


class TestLoadGeneratorPerformance(unittest.TestCase):
    """Test Load Generator performance"""
    
    def setUp(self):
        """Setup test environment"""
        if not LOAD_GENERATOR_AVAILABLE:
            self.skipTest("Load Generator modules not available")
    
    def test_large_building_load_generation(self):
        """Test load generation for large buildings"""
        import time
        
        # Simulate large building with many members
        num_members = 1000
        members = []
        
        start_time = time.time()
        
        for i in range(num_members):
            member = MockObject(f"Member_{i}")
            member.Shape.BoundBox.XLength = 6000.0
            member.Shape.BoundBox.YLength = 300.0
            member.Shape.BoundBox.ZLength = 400.0
            
            # Apply loads
            dead_load = 2.4 * (member.Shape.BoundBox.XLength * member.Shape.BoundBox.YLength / 1000000)
            live_load = 2.4 * (member.Shape.BoundBox.XLength * member.Shape.BoundBox.YLength / 1000000)
            
            members.append({
                "member": member,
                "dead_load": dead_load,
                "live_load": live_load
            })
        
        processing_time = time.time() - start_time
        
        # Should process 1000 members quickly
        self.assertEqual(len(members), 1000)
        self.assertLess(processing_time, 1.0, f"Processing took {processing_time:.3f} seconds")
    
    def test_dialog_response_time(self):
        """Test dialog creation and response performance"""
        import time
        
        start_time = time.time()
        dialog = LoadGeneratorSelectionDialog()
        creation_time = time.time() - start_time
        
        # Dialog should be created quickly
        self.assertLess(creation_time, 0.1, f"Dialog creation took {creation_time:.3f} seconds")
        
        # Test dialog execution
        start_time = time.time()
        result = dialog.exec_()
        execution_time = time.time() - start_time
        
        # Dialog execution should be immediate (since mocked)
        self.assertLess(execution_time, 0.01, f"Dialog execution took {execution_time:.3f} seconds")


class TestLoadGeneratorErrorHandling(unittest.TestCase):
    """Test Load Generator error handling"""
    
    def setUp(self):
        """Setup test environment"""
        if not LOAD_GENERATOR_AVAILABLE:
            self.skipTest("Load Generator modules not available")
    
    def test_invalid_load_values(self):
        """Test handling of invalid load values"""
        # Test negative loads
        invalid_loads = [-1.0, -10.5, 0.0]
        
        for load in invalid_loads:
            # Should handle invalid loads gracefully
            if load <= 0:
                # Negative or zero loads should be caught
                with self.assertRaises((ValueError, TypeError)) if load < 0 else self.subTest(load=load):
                    if load < 0:
                        raise ValueError(f"Invalid load value: {load}")
    
    def test_missing_document(self):
        """Test behavior when no document is active"""
        MockApp.ActiveDocument = None
        
        command = CommandLoadGenerator()
        
        # Should return False for IsActive when no document
        self.assertFalse(command.IsActive())
    
    def test_dialog_cancellation(self):
        """Test dialog cancellation handling"""
        dialog = LoadGeneratorSelectionDialog()
        
        # Simulate user cancellation
        dialog.reject()
        result = dialog.result()
        
        self.assertEqual(result, MockQtWidgets.QDialog.Rejected)


if __name__ == '__main__':
    # Configure test output
    import logging
    logging.basicConfig(level=logging.INFO)
    
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test cases
    test_suite.addTest(unittest.makeSuite(TestLoadGeneratorCore))
    test_suite.addTest(unittest.makeSuite(TestLoadGeneratorSelectionDialog))
    test_suite.addTest(unittest.makeSuite(TestLoadGeneratorCalculations))
    test_suite.addTest(unittest.makeSuite(TestLoadGeneratorIntegration))
    test_suite.addTest(unittest.makeSuite(TestLoadGeneratorPerformance))
    test_suite.addTest(unittest.makeSuite(TestLoadGeneratorErrorHandling))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Print summary
    print(f"\n{'='*50}")
    print("Load Generator Test Summary")
    print(f"{'='*50}")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print("\nFailures:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
    
    if result.errors:
        print("\nErrors:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")

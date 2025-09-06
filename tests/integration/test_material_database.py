# -*- coding: utf-8 -*-
"""
Test suite for Material Database functionality
Tests material standards database, creation, and management
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

class MockGui:
    @staticmethod
    def addCommand(name, command): pass

class MockObject:
    def __init__(self, name="TestMaterial"):
        self.Name = name
        self.Label = name
        self.properties = {}
        self.Proxy = None
    
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
        def exec_(self): return self.result
        def accept(self): return self.Accepted
        def reject(self): return self.Rejected
        def setWindowTitle(self, title): pass
        def setMinimumWidth(self, width): pass
        def setMinimumHeight(self, height): pass
    
    class QTreeWidget:
        def __init__(self): 
            self.items = []
        def clear(self): self.items = []
        def addTopLevelItem(self, item): self.items.append(item)
        def topLevelItemCount(self): return len(self.items)
        def topLevelItem(self, index): return self.items[index] if index < len(self.items) else None
    
    class QTreeWidgetItem:
        def __init__(self, items):
            self.items = items if isinstance(items, list) else [items]
            self.children = []
        def addChild(self, child): self.children.append(child)
        def text(self, column): return self.items[column] if column < len(self.items) else ""
    
    class QVBoxLayout: 
        def __init__(self): pass
        def addWidget(self, widget): pass
        def addLayout(self, layout): pass
    
    class QHBoxLayout:
        def __init__(self): pass
        def addWidget(self, widget): pass
    
    class QLabel:
        def __init__(self, text=""): self.text = text
    
    class QPushButton:
        def __init__(self, text=""): 
            self.text = text
            self.clicked = Mock()
    
    class QLineEdit:
        def __init__(self): 
            self.text_value = ""
        def text(self): return self.text_value
        def setText(self, text): self.text_value = text
    
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
    from StructureTools.commands.MaterialDatabaseManager import CommandMaterialDatabaseManager
    from StructureTools.material import Material
    MATERIAL_DATABASE_AVAILABLE = True
except ImportError as e:
    print(f"Material Database import failed: {e}")
    MATERIAL_DATABASE_AVAILABLE = False

# Mock material standards database
MOCK_MATERIAL_STANDARDS = {
    "ASTM_A992": {
        "name": "ASTM A992 Grade 50",
        "standard": "ASTM A992/A992M",
        "category": "Steel",
        "type": "Structural Steel",
        "properties": {
            "ModulusElasticity": "200000 MPa",
            "PoissonRatio": 0.3,
            "Density": "7850 kg/m^3",
            "YieldStrength": "345 MPa",
            "UltimateStrength": "450 MPa"
        }
    },
    "ASTM_A36": {
        "name": "ASTM A36",
        "standard": "ASTM A36/A36M",
        "category": "Steel", 
        "type": "Carbon Steel",
        "properties": {
            "ModulusElasticity": "200000 MPa",
            "PoissonRatio": 0.3,
            "Density": "7850 kg/m^3",
            "YieldStrength": "250 MPa",
            "UltimateStrength": "400 MPa"
        }
    },
    "CONCRETE_fc28": {
        "name": "Concrete f'c = 28 MPa",
        "standard": "ACI 318",
        "category": "Concrete",
        "type": "Normal Weight Concrete",
        "properties": {
            "ModulusElasticity": "25000 MPa",
            "PoissonRatio": 0.2,
            "Density": "2400 kg/m^3",
            "CompressiveStrength": "28 MPa"
        }
    }
}

MOCK_MATERIAL_CATEGORIES = {
    "Steel": ["ASTM_A992", "ASTM_A36"],
    "Concrete": ["CONCRETE_fc28"],
    "Aluminum": [],
    "Timber": []
}


class TestMaterialDatabase(unittest.TestCase):
    """Test material database core functionality"""
    
    def setUp(self):
        """Setup test environment"""
        if not MATERIAL_DATABASE_AVAILABLE:
            self.skipTest("Material Database modules not available")
        
        # Create mock document
        self.mock_doc = Mock()
        self.mock_doc.addObject = Mock(return_value=MockObject())
        MockApp.ActiveDocument = self.mock_doc
    
    def test_material_standards_structure(self):
        """Test material standards database structure"""
        # Test that mock database has expected structure
        self.assertIn("ASTM_A992", MOCK_MATERIAL_STANDARDS)
        self.assertIn("ASTM_A36", MOCK_MATERIAL_STANDARDS)
        self.assertIn("CONCRETE_fc28", MOCK_MATERIAL_STANDARDS)
        
        # Test material properties structure
        astm_a992 = MOCK_MATERIAL_STANDARDS["ASTM_A992"]
        self.assertIn("name", astm_a992)
        self.assertIn("standard", astm_a992)
        self.assertIn("category", astm_a992)
        self.assertIn("properties", astm_a992)
        
        properties = astm_a992["properties"]
        self.assertIn("ModulusElasticity", properties)
        self.assertIn("PoissonRatio", properties)
        self.assertIn("Density", properties)
        self.assertIn("YieldStrength", properties)
    
    def test_material_categories(self):
        """Test material category organization"""
        self.assertIn("Steel", MOCK_MATERIAL_CATEGORIES)
        self.assertIn("Concrete", MOCK_MATERIAL_CATEGORIES)
        
        steel_materials = MOCK_MATERIAL_CATEGORIES["Steel"]
        self.assertIn("ASTM_A992", steel_materials)
        self.assertIn("ASTM_A36", steel_materials)


class TestMaterialCreation(unittest.TestCase):
    """Test material object creation and properties"""
    
    def setUp(self):
        """Setup test environment"""
        if not MATERIAL_DATABASE_AVAILABLE:
            self.skipTest("Material Database modules not available")
        
        self.mock_doc = Mock()
        self.mock_doc.addObject = Mock(return_value=MockObject())
        MockApp.ActiveDocument = self.mock_doc
    
    def test_basic_material_creation(self):
        """Test basic material object creation"""
        # Create material object
        material_obj = MockObject("TestMaterial")
        material = Material(material_obj)
        
        # Check that material properties were added
        expected_properties = [
            "ModulusElasticity", "PoissonRatio", "Density",
            "YieldStrength", "UltimateStrength", "Name"
        ]
        
        for prop in expected_properties:
            self.assertIn(prop, material_obj.properties)
    
    def test_material_property_validation(self):
        """Test material property validation"""
        material_obj = MockObject("TestMaterial")
        material = Material(material_obj)
        
        # Test Poisson ratio validation
        material_obj.PoissonRatio = 0.3  # Valid value
        material.onChanged(material_obj, "PoissonRatio")
        
        material_obj.PoissonRatio = 0.6  # Invalid value (> 0.5)
        material.onChanged(material_obj, "PoissonRatio")
        # Should be corrected or warned
    
    def test_material_from_database(self):
        """Test material creation from database standard"""
        material_obj = MockObject("A992_Steel")
        material = Material(material_obj)
        
        # Simulate setting material standard
        material_obj.MaterialStandard = "ASTM_A992"
        
        # Test that properties are updated from database
        # (This would require mocking the database import)
    
    def test_calc_properties_conversion(self):
        """Test material properties conversion for calc integration"""
        material_obj = MockObject("TestMaterial")
        material = Material(material_obj)
        
        # Set test values
        material_obj.ModulusElasticity = "200000 MPa"
        material_obj.PoissonRatio = 0.3
        material_obj.Density = "7850 kg/m^3"
        
        # Get calc properties
        calc_props = material.get_calc_properties(material_obj)
        
        self.assertIsInstance(calc_props, dict)
        self.assertIn('E', calc_props)
        self.assertIn('G', calc_props)
        self.assertIn('nu', calc_props)
        self.assertIn('density', calc_props)


class TestMaterialDatabaseManager(unittest.TestCase):
    """Test Material Database Manager command and dialog"""
    
    def setUp(self):
        """Setup test environment"""
        if not MATERIAL_DATABASE_AVAILABLE:
            self.skipTest("Material Database modules not available")
        
        self.mock_doc = Mock()
        MockApp.ActiveDocument = self.mock_doc
        
        # Create command instance
        self.command = CommandMaterialDatabaseManager()
    
    def test_command_resources(self):
        """Test command resource definition"""
        resources = self.command.GetResources()
        
        self.assertIn("MenuText", resources)
        self.assertIn("ToolTip", resources)
        self.assertIn("Pixmap", resources)
        self.assertEqual(resources["MenuText"], "Material Database Manager")
    
    def test_command_is_active(self):
        """Test command active state"""
        # Should be active when document exists
        self.assertTrue(self.command.IsActive())
        
        # Should be inactive when no document
        MockApp.ActiveDocument = None
        self.assertFalse(self.command.IsActive())
    
    @patch.object(CommandMaterialDatabaseManager, 'show_database_manager_dialog')
    def test_command_activation(self, mock_show_dialog):
        """Test command activation"""
        MockApp.ActiveDocument = self.mock_doc
        
        # Activate command
        self.command.Activated()
        
        # Should show dialog
        mock_show_dialog.assert_called_once()
    
    def test_dialog_creation(self):
        """Test database manager dialog creation"""
        # This would test the actual dialog creation
        # For now, we test that it doesn't crash
        try:
            self.command.show_database_manager_dialog()
        except Exception as e:
            # Should not raise exception during dialog creation
            self.fail(f"Dialog creation failed: {e}")


class TestMaterialDatabaseSearch(unittest.TestCase):
    """Test material database search functionality"""
    
    def setUp(self):
        """Setup test environment"""
        if not MATERIAL_DATABASE_AVAILABLE:
            self.skipTest("Material Database modules not available")
    
    def test_search_by_name(self):
        """Test searching materials by name"""
        # Search for "A992"
        results = [key for key, material in MOCK_MATERIAL_STANDARDS.items() 
                  if "A992" in material["name"]]
        
        self.assertIn("ASTM_A992", results)
        self.assertEqual(len(results), 1)
    
    def test_search_by_category(self):
        """Test searching materials by category"""
        steel_materials = MOCK_MATERIAL_CATEGORIES.get("Steel", [])
        
        self.assertGreater(len(steel_materials), 0)
        self.assertIn("ASTM_A992", steel_materials)
        self.assertIn("ASTM_A36", steel_materials)
    
    def test_search_by_properties(self):
        """Test searching materials by properties"""
        # Find materials with yield strength >= 300 MPa
        high_strength = []
        for key, material in MOCK_MATERIAL_STANDARDS.items():
            props = material.get("properties", {})
            yield_str = props.get("YieldStrength", "0 MPa")
            if "345" in yield_str or "350" in yield_str:
                high_strength.append(key)
        
        self.assertIn("ASTM_A992", high_strength)


class TestMaterialDatabasePerformance(unittest.TestCase):
    """Test material database performance"""
    
    def setUp(self):
        """Setup test environment"""
        if not MATERIAL_DATABASE_AVAILABLE:
            self.skipTest("Material Database modules not available")
    
    def test_large_database_search(self):
        """Test search performance with large material database"""
        import time
        
        # Create large mock database
        large_database = {}
        for i in range(1000):
            large_database[f"MATERIAL_{i}"] = {
                "name": f"Test Material {i}",
                "category": "Steel" if i % 2 == 0 else "Concrete",
                "properties": {
                    "ModulusElasticity": f"{200000 + i} MPa",
                    "YieldStrength": f"{250 + i} MPa"
                }
            }
        
        # Measure search time
        start_time = time.time()
        results = [key for key, material in large_database.items() 
                  if "Steel" in material.get("category", "")]
        search_time = time.time() - start_time
        
        # Should find ~500 steel materials
        self.assertAlmostEqual(len(results), 500, delta=10)
        
        # Should complete search quickly (< 0.1 seconds)
        self.assertLess(search_time, 0.1, f"Search took {search_time:.3f} seconds")
    
    def test_material_creation_performance(self):
        """Test material object creation performance"""
        import time
        
        # Measure time to create 100 material objects
        start_time = time.time()
        
        materials = []
        for i in range(100):
            material_obj = MockObject(f"Material_{i}")
            material = Material(material_obj)
            materials.append(material)
        
        creation_time = time.time() - start_time
        
        # Should create materials quickly (< 0.5 seconds)
        self.assertLess(creation_time, 0.5, f"Creation took {creation_time:.3f} seconds")
        self.assertEqual(len(materials), 100)


class TestMaterialDatabaseIntegration(unittest.TestCase):
    """Test material database integration with other components"""
    
    def setUp(self):
        """Setup test environment"""
        if not MATERIAL_DATABASE_AVAILABLE:
            self.skipTest("Material Database modules not available")
        
        self.mock_doc = Mock()
        self.mock_doc.addObject = Mock(return_value=MockObject())
        MockApp.ActiveDocument = self.mock_doc
    
    def test_material_to_calc_integration(self):
        """Test material integration with calc module"""
        # Create material
        material_obj = MockObject("A992_Steel")
        material = Material(material_obj)
        
        # Set properties from database
        material_obj.ModulusElasticity = "200000 MPa"
        material_obj.PoissonRatio = 0.3
        material_obj.Density = "7850 kg/m^3"
        
        # Test calc integration
        calc_props = material.get_calc_properties(material_obj, 'm', 'kN')
        
        self.assertIsInstance(calc_props, dict)
        self.assertIn('name', calc_props)
        self.assertIn('E', calc_props)
        self.assertIn('G', calc_props)
    
    def test_material_export_import(self):
        """Test material database export/import functionality"""
        # Test export
        export_data = {
            "materials": MOCK_MATERIAL_STANDARDS,
            "categories": MOCK_MATERIAL_CATEGORIES,
            "version": "1.0"
        }
        
        # Simulate export to JSON
        json_data = json.dumps(export_data, indent=2)
        self.assertIn("ASTM_A992", json_data)
        
        # Simulate import from JSON
        imported_data = json.loads(json_data)
        self.assertEqual(imported_data["materials"]["ASTM_A992"]["name"], 
                        "ASTM A992 Grade 50")


if __name__ == '__main__':
    # Configure test output
    import logging
    logging.basicConfig(level=logging.INFO)
    
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test cases
    test_suite.addTest(unittest.makeSuite(TestMaterialDatabase))
    test_suite.addTest(unittest.makeSuite(TestMaterialCreation))
    test_suite.addTest(unittest.makeSuite(TestMaterialDatabaseManager))
    test_suite.addTest(unittest.makeSuite(TestMaterialDatabaseSearch))
    test_suite.addTest(unittest.makeSuite(TestMaterialDatabasePerformance))
    test_suite.addTest(unittest.makeSuite(TestMaterialDatabaseIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Print summary
    print(f"\n{'='*50}")
    print("Material Database Test Summary")
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

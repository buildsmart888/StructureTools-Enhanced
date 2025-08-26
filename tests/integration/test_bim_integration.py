# -*- coding: utf-8 -*-
"""
Test suite for BIM Integration functionality
Tests the bridge between BIM/Arch objects and StructureTools
"""

import unittest
import sys
import os
import types
from unittest.mock import Mock, MagicMock, patch

# Setup test environment
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
freecad_dir = os.path.join(repo_root, 'freecad')
if freecad_dir not in sys.path:
    sys.path.insert(0, freecad_dir)

# Mock FreeCAD modules
class MockApp:
    class Vector:
        def __init__(self, x=0, y=0, z=0):
            self.x, self.y, self.z = x, y, z
    
    class Console:
        @staticmethod
        def PrintMessage(msg): print(f"INFO: {msg}")
        @staticmethod  
        def PrintWarning(msg): print(f"WARN: {msg}")
        @staticmethod
        def PrintError(msg): print(f"ERROR: {msg}")
    
    ActiveDocument = None
    
    @staticmethod
    def ActiveDocument():
        return MockApp.ActiveDocument

class MockGui:
    @staticmethod
    def addCommand(name, command): pass

class MockPart:
    @staticmethod
    def makeLine(start, end): 
        return Mock(Vertexes=[Mock(Point=start), Mock(Point=end)])
    
    @staticmethod
    def makeCompound(shapes):
        return Mock(shapes=shapes)

class MockObject:
    def __init__(self, name="TestObject", type_id="Part::Feature"):
        self.Name = name
        self.Label = name
        self.TypeId = type_id
        self.Shape = Mock()
        self.Shape.BoundBox = Mock(XLength=1000, YLength=200, ZLength=300)
        self.Shape.isNull = Mock(return_value=False)
        self.properties = {}
    
    def addProperty(self, prop_type, name, group, desc):
        setattr(self, name, None)
        self.properties[name] = {"type": prop_type, "group": group, "desc": desc}

# Setup mock modules
sys.modules['FreeCAD'] = MockApp
sys.modules['App'] = MockApp  
sys.modules['FreeCADGui'] = MockGui
sys.modules['Gui'] = MockGui
sys.modules['Part'] = MockPart

# Mock Qt
class MockQtWidgets:
    class QDialog:
        Accepted = 1
        Rejected = 0
        def __init__(self): pass
        def exec_(self): return self.Accepted
        def accept(self): return self.Accepted
        def reject(self): return self.Rejected

sys.modules['PySide2'] = types.SimpleNamespace(QtWidgets=MockQtWidgets)

# Import the modules to test
try:
    from StructureTools.integration.BIMIntegration import BIMStructuralIntegration, CommandBIMIntegration
    from StructureTools.material import Material
    from StructureTools.section import Section
    BIM_INTEGRATION_AVAILABLE = True
except ImportError as e:
    print(f"BIM Integration import failed: {e}")
    BIM_INTEGRATION_AVAILABLE = False


class TestBIMIntegration(unittest.TestCase):
    """Test BIM Integration functionality"""
    
    def setUp(self):
        """Setup test environment"""
        if not BIM_INTEGRATION_AVAILABLE:
            self.skipTest("BIM Integration modules not available")
        
        # Create mock document
        self.mock_doc = Mock()
        self.mock_doc.Objects = []
        MockApp.ActiveDocument = self.mock_doc
        
        # Create BIM integration instance
        self.bim_integration = BIMStructuralIntegration()
    
    def test_integration_initialization(self):
        """Test BIM integration initializes correctly"""
        self.assertIsNotNone(self.bim_integration)
        self.assertEqual(len(self.bim_integration.bim_objects), 0)
        self.assertEqual(len(self.bim_integration.structural_objects), 0)
        self.assertEqual(len(self.bim_integration.mapping), 0)
    
    def test_is_structural_bim_object(self):
        """Test detection of structural BIM objects"""
        # Test Arch Structure
        arch_structure = MockObject("Beam1", "Arch::Structure")
        arch_structure.IfcType = "IfcBeam"
        self.assertTrue(self.bim_integration.is_structural_bim_object(arch_structure))
        
        # Test regular object
        regular_obj = MockObject("RegularObj", "Part::Feature")
        self.assertFalse(self.bim_integration.is_structural_bim_object(regular_obj))
        
        # Test IFC object
        ifc_column = MockObject("Column1", "Part::Feature")
        ifc_column.IfcType = "IfcColumn"
        self.assertTrue(self.bim_integration.is_structural_bim_object(ifc_column))
    
    def test_determine_structural_type(self):
        """Test structural type determination"""
        # Test beam
        beam = MockObject("Beam1", "Arch::Structure")
        beam.IfcType = "IfcBeam"
        beam.Shape.BoundBox = Mock(XLength=5000, YLength=200, ZLength=300)
        self.assertEqual(self.bim_integration.determine_structural_type(beam), "beam")
        
        # Test column (height > width and length)
        column = MockObject("Column1", "Arch::Structure") 
        column.IfcType = "IfcColumn"
        column.Shape.BoundBox = Mock(XLength=300, YLength=300, ZLength=3000)
        self.assertEqual(self.bim_integration.determine_structural_type(column), "column")
        
        # Test slab (height < width and length)
        slab = MockObject("Slab1", "Arch::Structure")
        slab.IfcType = "IfcSlab"
        slab.Shape.BoundBox = Mock(XLength=5000, YLength=3000, ZLength=200)
        self.assertEqual(self.bim_integration.determine_structural_type(slab), "slab")
    
    def test_scan_for_bim_objects(self):
        """Test scanning for BIM objects"""
        # Create test objects
        beam = MockObject("Beam1", "Arch::Structure")
        beam.IfcType = "IfcBeam"
        
        column = MockObject("Column1", "Arch::Structure")
        column.IfcType = "IfcColumn"
        
        regular_obj = MockObject("RegularObj", "Part::Feature")
        
        self.mock_doc.Objects = [beam, column, regular_obj]
        
        # Scan for BIM objects
        bim_objects = self.bim_integration.scan_for_bim_objects()
        
        # Should find 2 structural objects
        self.assertEqual(len(bim_objects), 2)
        self.assertIn(beam, bim_objects)
        self.assertIn(column, bim_objects)
        self.assertNotIn(regular_obj, bim_objects)
    
    def test_calculate_section_properties(self):
        """Test section property calculation"""
        beam = MockObject("Beam1", "Arch::Structure")
        beam.Shape.BoundBox = Mock(XLength=5000, YLength=200, ZLength=300)
        
        props = self.bim_integration.calculate_section_properties(beam)
        
        self.assertIn('area', props)
        self.assertIn('Iy', props)
        self.assertIn('Iz', props)
        self.assertIn('J', props)
        
        # Check calculations (rectangular section)
        expected_area = 200 * 300  # width * height
        self.assertEqual(props['area'], expected_area)
    
    @patch('StructureTools.integration.BIMIntegration.Material')
    def test_extract_or_create_material(self, mock_material):
        """Test material extraction/creation"""
        # Setup mock document
        self.mock_doc.addObject = Mock(return_value=Mock())
        
        # Test BIM object with material
        beam = MockObject("Beam1", "Arch::Structure")
        bim_material = Mock()
        bim_material.Label = "Steel_A992"
        bim_material.ElasticModulus = 200000
        bim_material.PoissonRatio = 0.3
        bim_material.Density = 7850
        beam.Material = bim_material
        
        material_obj = self.bim_integration.extract_or_create_material(beam)
        
        # Should create material object
        self.assertIsNotNone(material_obj)
    
    def test_geometry_changed(self):
        """Test geometry change detection"""
        # Create objects with same geometry
        bim_obj = MockObject("Beam1", "Arch::Structure")
        bim_obj.Shape.BoundBox = Mock(XLength=5000, YLength=200, ZLength=300)
        
        structural_obj = MockObject("Beam1_Structural", "Part::Feature")
        structural_obj.Shape.BoundBox = Mock(XLength=5000, YLength=200, ZLength=300)
        
        # Should detect no change
        self.assertFalse(self.bim_integration.geometry_changed(bim_obj, structural_obj))
        
        # Change geometry
        bim_obj.Shape.BoundBox.XLength = 6000
        
        # Should detect change
        self.assertTrue(self.bim_integration.geometry_changed(bim_obj, structural_obj))


class TestBIMCommands(unittest.TestCase):
    """Test BIM command functionality"""
    
    def setUp(self):
        """Setup test environment"""
        if not BIM_INTEGRATION_AVAILABLE:
            self.skipTest("BIM Integration modules not available")
        
        self.mock_doc = Mock()
        MockApp.ActiveDocument = self.mock_doc
        
        # Create command instance
        self.command = CommandBIMIntegration()
    
    def test_command_resources(self):
        """Test command resource definition"""
        resources = self.command.GetResources()
        
        self.assertIn("MenuText", resources)
        self.assertIn("ToolTip", resources)
        self.assertEqual(resources["MenuText"], "Import from BIM")
    
    def test_command_is_active(self):
        """Test command active state"""
        # Should be active when document exists
        self.assertTrue(self.command.IsActive())
        
        # Should be inactive when no document
        MockApp.ActiveDocument = None
        self.assertFalse(self.command.IsActive())


class TestBIMIntegrationWorkflow(unittest.TestCase):
    """Test complete BIM integration workflow"""
    
    def setUp(self):
        """Setup test environment"""
        if not BIM_INTEGRATION_AVAILABLE:
            self.skipTest("BIM Integration modules not available")
        
        # Setup mock document with BIM objects
        self.mock_doc = Mock()
        self.mock_doc.addObject = Mock(return_value=Mock())
        MockApp.ActiveDocument = self.mock_doc
        
        # Create test BIM objects
        self.beam = MockObject("Beam1", "Arch::Structure")
        self.beam.IfcType = "IfcBeam"
        self.beam.Shape.BoundBox = Mock(XLength=5000, YLength=200, ZLength=300)
        
        self.column = MockObject("Column1", "Arch::Structure")
        self.column.IfcType = "IfcColumn"
        self.column.Shape.BoundBox = Mock(XLength=300, YLength=300, ZLength=3000)
        
        self.mock_doc.Objects = [self.beam, self.column]
        
        # Create integration instance
        self.bim_integration = BIMStructuralIntegration()
    
    @patch('StructureTools.integration.BIMIntegration.Material')
    @patch('StructureTools.integration.BIMIntegration.Section')
    def test_complete_import_workflow(self, mock_section, mock_material):
        """Test complete import workflow from BIM to structural"""
        # Run import process
        structural_objects = self.bim_integration.import_from_bim()
        
        # Should create structural objects
        self.assertEqual(len(structural_objects), 2)
        
        # Should create mapping
        self.assertEqual(len(self.bim_integration.mapping), 2)
        self.assertIn(self.beam, self.bim_integration.mapping)
        self.assertIn(self.column, self.bim_integration.mapping)
    
    def test_export_results_workflow(self):
        """Test export of analysis results back to BIM"""
        # Setup calc object with results
        calc_obj = Mock()
        calc_obj.MemberResults = []
        calc_obj.MaxMomentY = [1000.0, 2000.0]
        calc_obj.NameMembers = ["Beam1_Structural", "Column1_Structural"]
        
        # Setup mapping
        beam_structural = Mock()
        beam_structural.Label = "Beam1_Structural"
        self.bim_integration.mapping[self.beam] = beam_structural
        
        # Export results
        self.bim_integration.export_results_to_bim(calc_obj)
        
        # Should add properties to BIM objects
        # (This would be verified by checking if addProperty was called)


class TestBIMIntegrationPerformance(unittest.TestCase):
    """Test BIM integration performance with large models"""
    
    def setUp(self):
        """Setup test environment"""
        if not BIM_INTEGRATION_AVAILABLE:
            self.skipTest("BIM Integration modules not available")
        
        self.mock_doc = Mock()
        MockApp.ActiveDocument = self.mock_doc
        self.bim_integration = BIMStructuralIntegration()
    
    def test_large_model_scanning(self):
        """Test scanning performance with many objects"""
        import time
        
        # Create 1000 test objects (mix of structural and non-structural)
        objects = []
        for i in range(1000):
            if i % 3 == 0:  # Every 3rd object is structural
                obj = MockObject(f"Beam{i}", "Arch::Structure")
                obj.IfcType = "IfcBeam"
            else:
                obj = MockObject(f"Other{i}", "Part::Feature")
            objects.append(obj)
        
        self.mock_doc.Objects = objects
        
        # Measure scanning time
        start_time = time.time()
        bim_objects = self.bim_integration.scan_for_bim_objects()
        scan_time = time.time() - start_time
        
        # Should find ~333 structural objects
        expected_count = len([obj for obj in objects if obj.Name.startswith("Beam")])
        self.assertEqual(len(bim_objects), expected_count)
        
        # Should complete scanning in reasonable time (< 1 second)
        self.assertLess(scan_time, 1.0, f"Scanning took {scan_time:.3f} seconds")


if __name__ == '__main__':
    # Configure test output
    import logging
    logging.basicConfig(level=logging.INFO)
    
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test cases
    test_suite.addTest(unittest.makeSuite(TestBIMIntegration))
    test_suite.addTest(unittest.makeSuite(TestBIMCommands))
    test_suite.addTest(unittest.makeSuite(TestBIMIntegrationWorkflow))
    test_suite.addTest(unittest.makeSuite(TestBIMIntegrationPerformance))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Print summary
    print(f"\n{'='*50}")
    print("BIM Integration Test Summary")
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

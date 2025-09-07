# -*- coding: utf-8 -*-
"""
Integration tests for core architecture.
Tests the complete core system integration.
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# Mock FreeCAD before importing
class MockApp:
    class Console:
        @staticmethod
        def PrintError(msg):
            pass
        
        @staticmethod
        def PrintWarning(msg):
            pass
        
        @staticmethod
        def PrintMessage(msg):
            pass

sys.modules['FreeCAD'] = MockApp()
sys.modules['App'] = MockApp()


class TestCoreIntegration(unittest.TestCase):
    """Test complete core architecture integration"""
    
    def setUp(self):
        """Set up test environment"""
        # Reset any cached singletons
        import freecad.StructureTools.core as core_module
        if hasattr(core_module, '_section_manager'):
            core_module._section_manager = None
        if hasattr(core_module, '_geometry_factory'):
            core_module._geometry_factory = None
    
    def test_core_module_imports(self):
        """Test that all core module components can be imported"""
        try:
            from freecad.StructureTools.core import (
                get_section_manager,
                get_geometry_factory,
                detect_section_from_name,
                get_section_properties,
                generate_section_geometry,
                calculate_properties_from_face
            )
        except ImportError as e:
            self.fail(f"Core module imports failed: {e}")
    
    def test_singleton_section_manager(self):
        """Test section manager singleton pattern"""
        from freecad.StructureTools.core import get_section_manager
        
        manager1 = get_section_manager()
        manager2 = get_section_manager()
        
        self.assertIs(manager1, manager2)
        self.assertEqual(id(manager1), id(manager2))
    
    def test_singleton_geometry_factory(self):
        """Test geometry factory singleton pattern"""
        from freecad.StructureTools.core import get_geometry_factory
        
        factory1 = get_geometry_factory()
        factory2 = get_geometry_factory()
        
        self.assertIs(factory1, factory2)
        self.assertEqual(id(factory1), id(factory2))
    
    def test_detect_section_from_name_integration(self):
        """Test section detection convenience function"""
        from freecad.StructureTools.core import detect_section_from_name
        
        # Should work without raising exceptions
        result = detect_section_from_name("W12x26")
        self.assertIsInstance(result, str)
        
        # Should handle unknown sections
        result = detect_section_from_name("UNKNOWN_SECTION")
        self.assertEqual(result, "Custom")
    
    def test_get_section_properties_integration(self):
        """Test section properties convenience function"""
        from freecad.StructureTools.core import get_section_properties
        
        # Should work for known sections
        result = get_section_properties("W12x26")
        if result is not None:
            self.assertIsInstance(result, dict)
            self.assertIn("Area", result)
        
        # Should return None for custom sections
        result = get_section_properties("Custom")
        self.assertIsNone(result)
    
    def test_generate_section_geometry_integration(self):
        """Test geometry generation convenience function"""
        from freecad.StructureTools.core import generate_section_geometry
        
        section_properties = {
            "Type": "Wide Flange",
            "Depth": 200.0,
            "FlangeWidth": 100.0,
            "WebThickness": 10.0,
            "FlangeThickness": 15.0
        }
        
        # Should not raise exceptions (may return None if FreeCAD not available)
        try:
            result = generate_section_geometry(section_properties)
        except Exception as e:
            self.fail(f"Geometry generation failed: {e}")
    
    def test_calculate_properties_from_face_integration(self):
        """Test property calculation convenience function"""
        from freecad.StructureTools.core import calculate_properties_from_face
        
        # Should handle None input
        result = calculate_properties_from_face(None)
        self.assertEqual(result, {})
        
        # Should handle mock face
        mock_face = Mock()
        mock_face.Area = 100.0
        mock_face.CenterOfMass = Mock()
        mock_face.CenterOfMass.x = 0.0
        mock_face.CenterOfMass.y = 0.0
        mock_face.CenterOfMass.z = 0.0
        
        result = calculate_properties_from_face(mock_face)
        self.assertIsInstance(result, dict)
    
    def test_core_error_handling(self):
        """Test error handling in core functions"""
        from freecad.StructureTools.core import (
            detect_section_from_name,
            get_section_properties,
            generate_section_geometry
        )
        
        # Functions should not raise exceptions with invalid input
        try:
            detect_section_from_name(None)
            detect_section_from_name("")
            detect_section_from_name(123)  # Invalid type
        except Exception as e:
            self.fail(f"Section detection should handle invalid input: {e}")
        
        try:
            get_section_properties(None)
            get_section_properties("")
        except Exception as e:
            self.fail(f"Property getter should handle invalid input: {e}")
        
        try:
            generate_section_geometry(None)
            generate_section_geometry({})
            generate_section_geometry({"Type": "Unknown"})
        except Exception as e:
            self.fail(f"Geometry generation should handle invalid input: {e}")
    
    def test_manager_database_integration(self):
        """Test section manager database integration"""
        from freecad.StructureTools.core import get_section_manager
        
        manager = get_section_manager()
        
        # Should have database status
        self.assertIsInstance(manager.database_available, bool)
        
        if manager.database_available:
            # Should have section standards
            self.assertIsInstance(manager.section_standards, dict)
            
            # Should be able to get available sections
            sections = manager.get_available_sections()
            self.assertIsInstance(sections, list)
    
    def test_factory_generator_integration(self):
        """Test geometry factory generator integration"""
        from freecad.StructureTools.core import get_geometry_factory
        
        factory = get_geometry_factory()
        
        # Should have generators
        self.assertIsInstance(factory.generators, dict)
        
        # Should have expected generator types
        expected_types = [
            "Wide Flange", "I-Beam", "H-Beam", 
            "Rectangular HSS", "Circular HSS",
            "Equal Angle", "Unequal Angle", "Channel"
        ]
        
        for section_type in expected_types:
            if section_type in factory.generators:
                generator = factory.generators[section_type]
                self.assertTrue(hasattr(generator, 'generate'))
                self.assertTrue(hasattr(generator, 'validate_properties'))
    
    def test_end_to_end_workflow(self):
        """Test complete end-to-end workflow"""
        from freecad.StructureTools.core import (
            detect_section_from_name,
            get_section_properties,
            generate_section_geometry
        )
        
        # Step 1: Detect section from name
        section_name = detect_section_from_name("W12X26_BEAM")
        self.assertIsInstance(section_name, str)
        
        # Step 2: Get section properties
        properties = get_section_properties(section_name)
        if properties:
            self.assertIsInstance(properties, dict)
            
            # Step 3: Generate geometry
            geometry = generate_section_geometry(properties)
            # May be None if FreeCAD not available, but should not raise exception
    
    def test_backward_compatibility(self):
        """Test backward compatibility with existing code"""
        # Import should work from various paths
        try:
            from freecad.StructureTools.core.SectionManager import SectionManager
            from freecad.StructureTools.core.geometry_generators import create_geometry_generator
            from freecad.StructureTools.core import get_section_manager
            
            # Direct class instantiation should work
            manager = SectionManager()
            self.assertIsInstance(manager, SectionManager)
            
            # Factory function should work
            generator = create_geometry_generator("Wide Flange")
            if generator:
                self.assertTrue(hasattr(generator, 'generate'))
            
            # Singleton access should work
            singleton_manager = get_section_manager()
            self.assertIsInstance(singleton_manager, SectionManager)
            
        except Exception as e:
            self.fail(f"Backward compatibility test failed: {e}")
    
    def test_module_version_info(self):
        """Test module version information"""
        import freecad.StructureTools.core as core_module
        
        # Should have version info
        self.assertTrue(hasattr(core_module, '__version__'))
        self.assertTrue(hasattr(core_module, '__author__'))
        
        self.assertIsInstance(core_module.__version__, str)
        self.assertIsInstance(core_module.__author__, str)
    
    def test_module_exports(self):
        """Test module __all__ exports"""
        import freecad.StructureTools.core as core_module
        
        # Should have __all__ defined
        self.assertTrue(hasattr(core_module, '__all__'))
        self.assertIsInstance(core_module.__all__, list)
        
        # All exports should be available
        for export in core_module.__all__:
            self.assertTrue(hasattr(core_module, export), 
                          f"Export '{export}' not available")
    
    def test_performance_characteristics(self):
        """Test basic performance characteristics"""
        from freecad.StructureTools.core import (
            get_section_manager,
            detect_section_from_name,
            get_section_properties
        )
        import time
        
        # Manager instantiation should be fast
        start_time = time.time()
        manager = get_section_manager()
        end_time = time.time()
        
        self.assertLess(end_time - start_time, 0.1, "Manager instantiation too slow")
        
        # Section detection should be fast
        start_time = time.time()
        for _ in range(100):
            detect_section_from_name("W12x26")
        end_time = time.time()
        
        self.assertLess(end_time - start_time, 0.5, "Section detection too slow")
        
        # Property lookup should be fast
        start_time = time.time()
        for _ in range(100):
            get_section_properties("W12x26")
        end_time = time.time()
        
        self.assertLess(end_time - start_time, 1.0, "Property lookup too slow")


if __name__ == '__main__':
    unittest.main()
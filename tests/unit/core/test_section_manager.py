# -*- coding: utf-8 -*-
"""
Unit tests for SectionManager core functionality.
Tests the centralized section management system.
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

from freecad.StructureTools.core.SectionManager import (
    SectionManager, 
    SectionGeometryFactory, 
    SectionPropertyCalculator
)


class TestSectionManager(unittest.TestCase):
    """Test SectionManager core functionality"""
    
    def setUp(self):
        """Set up test environment"""
        self.manager = SectionManager()
    
    def test_initialization(self):
        """Test SectionManager initialization"""
        self.assertIsInstance(self.manager, SectionManager)
        self.assertIsInstance(self.manager.section_standards, dict)
        self.assertIsInstance(self.manager.validators, dict)
        self.assertIsInstance(self.manager.geometry_generators, dict)
    
    def test_detect_section_from_name_exact_match(self):
        """Test exact section name detection"""
        # Mock section standards
        self.manager.section_standards = {
            'W12x26': {'Type': 'Wide Flange'},
            'IPE200': {'Type': 'I-Beam'}
        }
        self.manager.database_available = True
        
        # Test exact matches
        self.assertEqual(self.manager.detect_section_from_name('W12x26'), 'W12x26')
        self.assertEqual(self.manager.detect_section_from_name('IPE200'), 'IPE200')
    
    def test_detect_section_from_name_pattern_match(self):
        """Test pattern-based section detection"""
        self.manager.section_standards = {
            'W12x26': {'Type': 'Wide Flange'},
            'W14x22': {'Type': 'Wide Flange'}
        }
        self.manager.database_available = True
        
        # Test pattern detection
        result = self.manager.detect_section_from_name('W12X30_BEAM')
        self.assertEqual(result, 'W12x26')  # Should find W12x26 pattern
    
    def test_detect_section_from_name_no_database(self):
        """Test section detection when database unavailable"""
        self.manager.database_available = False
        
        result = self.manager.detect_section_from_name('W12x26')
        self.assertEqual(result, 'Custom')
    
    def test_detect_section_from_name_unknown(self):
        """Test detection of unknown section"""
        self.manager.section_standards = {'W12x26': {}}
        self.manager.database_available = True
        
        result = self.manager.detect_section_from_name('UNKNOWN_SECTION')
        self.assertEqual(result, 'Custom')
    
    def test_get_section_properties_success(self):
        """Test successful section properties retrieval"""
        # Mock get_section_info method
        mock_properties = {
            'Area': 100.0,
            'Ix': 1000.0,
            'Depth': 300.0
        }
        self.manager.get_section_info = Mock(return_value=mock_properties)
        self.manager.database_available = True
        
        result = self.manager.get_section_properties('W12x26')
        
        self.assertIsInstance(result, dict)
        self.assertIn('Area', result)
        self.assertIn('Ix', result)
        # Should have derived properties
        # Should have derived properties - Zx_calculated should be added
        self.assertIn('Zx_calculated', result)  # Should have calculated plastic modulus
    
    def test_get_section_properties_custom_section(self):
        """Test properties for custom section"""
        result = self.manager.get_section_properties('Custom')
        self.assertIsNone(result)
    
    def test_get_section_properties_not_found(self):
        """Test properties retrieval for non-existent section"""
        self.manager.get_section_info = Mock(return_value=None)
        self.manager.database_available = True
        
        result = self.manager.get_section_properties('NONEXISTENT')
        self.assertIsNone(result)
    
    def test_calculate_derived_properties(self):
        """Test derived properties calculation"""
        properties = {
            'Ix': 1000.0,
            'Depth': 200.0,
            'Sx': 100.0,
            'Zx': 120.0,
            'Area': 50.0,
            'Weight': 25.0
        }
        
        result = self.manager._calculate_derived_properties(properties)
        
        # Check shape factor calculation
        expected_shape_factor = 120.0 / 100.0  # Zx / Sx
        self.assertEqual(result['ShapeFactorX'], expected_shape_factor)
        
        # Check area per weight
        expected_area_per_weight = 50.0 / 25.0
        self.assertEqual(result['AreaPerWeight'], expected_area_per_weight)
    
    def test_validate_section_properties_with_validator(self):
        """Test section validation when validator available"""
        mock_validate = Mock(return_value=(True, [], ['Test warning']))
        self.manager.validate_section = mock_validate
        
        properties = {'Area': 100.0, 'Ix': 1000.0}
        result = self.manager.validate_section_properties(properties)
        
        self.assertEqual(result, (True, [], ['Test warning']))
        mock_validate.assert_called_once_with(properties, 'AISC_360')
    
    def test_validate_section_properties_no_validator(self):
        """Test section validation when validator not available"""
        # Remove validator
        if hasattr(self.manager, 'validate_section'):
            delattr(self.manager, 'validate_section')
        
        properties = {'Area': 100.0}
        result = self.manager.validate_section_properties(properties)
        
        self.assertEqual(result[0], True)  # Should return True
        self.assertEqual(result[1], [])    # No errors
        self.assertIn('Validation not available', result[2][0])  # Warning message
    
    def test_classify_section_for_design(self):
        """Test section classification for design"""
        mock_classify = Mock(return_value='Compact')
        self.manager.classify_section = mock_classify
        
        properties = {'Depth': 200.0, 'FlangeWidth': 100.0}
        result = self.manager.classify_section_for_design(properties)
        
        self.assertEqual(result, 'Compact')
        mock_classify.assert_called_once_with(properties, 'A992')
    
    def test_get_available_sections(self):
        """Test getting available sections list"""
        self.manager.section_standards = {
            'W12x26': {'Type': 'Wide Flange', 'Depth': 300},
            'W14x22': {'Type': 'Wide Flange', 'Depth': 350},
            'IPE200': {'Type': 'I-Beam', 'Depth': 200}
        }
        self.manager.database_available = True
        
        # Test without filters
        sections = self.manager.get_available_sections()
        self.assertEqual(len(sections), 3)
        self.assertIn('W12x26', sections)
        self.assertIn('W14x22', sections)
        self.assertIn('IPE200', sections)
    
    def test_get_available_sections_with_filters(self):
        """Test getting available sections with filtering"""
        self.manager.section_standards = {
            'W12x26': {'Type': 'Wide Flange', 'Depth': 300},
            'W14x22': {'Type': 'Wide Flange', 'Depth': 350},
            'IPE200': {'Type': 'I-Beam', 'Depth': 200}
        }
        self.manager.database_available = True
        
        # Mock get_section_info for filtering
        def mock_get_section_info(name):
            return self.manager.section_standards.get(name)
        
        self.manager.get_section_info = mock_get_section_info
        
        # Test with depth filter
        filter_criteria = {'min_depth': 250}
        sections = self.manager.get_available_sections(filter_criteria)
        
        # Should include W12x26 (300) and W14x22 (350), exclude IPE200 (200)
        self.assertEqual(len(sections), 2)
        self.assertIn('W12x26', sections)
        self.assertIn('W14x22', sections)
        self.assertNotIn('IPE200', sections)


class TestSectionGeometryFactory(unittest.TestCase):
    """Test SectionGeometryFactory functionality"""
    
    def setUp(self):
        """Set up test environment"""
        self.factory = SectionGeometryFactory()
    
    def test_initialization(self):
        """Test factory initialization"""
        self.assertIsInstance(self.factory, SectionGeometryFactory)
        self.assertIsInstance(self.factory.generators, dict)
    
    def test_register_generators(self):
        """Test generator registration"""
        # Should have registered generators after initialization
        self.assertGreater(len(self.factory.generators), 0)
        
        # Should have expected generator types
        expected_types = ["Wide Flange", "I-Beam", "H-Beam", "Rectangular HSS"]
        for gen_type in expected_types:
            if gen_type in self.factory.generators:
                generator = self.factory.generators[gen_type]
                self.assertTrue(hasattr(generator, 'generate'))
    
    def test_generate_geometry_with_valid_type(self):
        """Test geometry generation with valid section type"""
        # Mock generator
        mock_generator = Mock()
        mock_generator.generate.return_value = Mock()
        self.factory.generators = {'Wide Flange': mock_generator}
        
        section_properties = {
            'Type': 'Wide Flange',
            'Depth': 200,
            'FlangeWidth': 100
        }
        
        result = self.factory.generate_geometry(section_properties)
        
        mock_generator.generate.assert_called_once_with(section_properties)
        self.assertIsNotNone(result)
    
    def test_generate_geometry_with_invalid_type(self):
        """Test geometry generation with invalid section type"""
        self.factory.generators = {}
        
        section_properties = {'Type': 'Unknown Type'}
        
        result = self.factory.generate_geometry(section_properties)
        self.assertIsNone(result)


class TestSectionPropertyCalculator(unittest.TestCase):
    """Test SectionPropertyCalculator functionality"""
    
    def test_calculate_properties_from_face_valid(self):
        """Test property calculation from valid face"""
        # Mock face object
        mock_face = Mock()
        mock_face.Area = 100.0
        # Create proper CenterOfMass as tuple/list (not Mock)
        mock_face.CenterOfMass = (0.0, 0.0, 0.0)
        
        # Mock matrix of inertia
        mock_matrix = Mock()
        mock_matrix.A = [1000, 0, 0, 0, 0, 2000]  # [Iz, Iyz, ..., Iy]
        mock_face.MatrixOfInertia = mock_matrix
        
        # Mock bounding box
        mock_bbox = Mock()
        mock_bbox.YMax = 100.0
        mock_bbox.YMin = -100.0
        mock_bbox.XMax = 50.0
        mock_bbox.XMin = -50.0
        mock_face.BoundBox = mock_bbox
        
        result = SectionPropertyCalculator.calculate_properties_from_face(mock_face)
        
        self.assertIsInstance(result, dict)
        self.assertEqual(result['Area'], 100.0)
        self.assertIn('Iy', result)
        self.assertIn('Iz', result)
        self.assertIn('Depth', result)
        self.assertIn('Width', result)
        self.assertEqual(result['Depth'], 200.0)  # YMax - YMin
        self.assertEqual(result['Width'], 100.0)  # XMax - XMin
    
    def test_calculate_properties_from_face_invalid(self):
        """Test property calculation from invalid face"""
        result = SectionPropertyCalculator.calculate_properties_from_face(None)
        self.assertEqual(result, {})
        
        # Test face without Area
        mock_face = Mock()
        del mock_face.Area  # Remove Area attribute
        result = SectionPropertyCalculator.calculate_properties_from_face(mock_face)
        self.assertEqual(result, {})
    
    def test_validate_calculated_properties_valid(self):
        """Test validation of valid calculated properties"""
        properties = {
            'Area': 100.0,
            'Iy': 1000.0,
            'Iz': 500.0,
            'Depth': 200.0,
            'Width': 100.0
        }
        
        errors, warnings = SectionPropertyCalculator.validate_calculated_properties(properties)
        
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])
    
    def test_validate_calculated_properties_errors(self):
        """Test validation with error conditions"""
        properties = {
            'Area': -50.0,  # Negative area - error
            'Iy': -1000.0,  # Negative moment - error
            'Depth': -200.0,  # Negative depth - error
            'Width': 0.0    # Zero width - error
        }
        
        errors, warnings = SectionPropertyCalculator.validate_calculated_properties(properties)
        
        self.assertGreater(len(errors), 0)
        self.assertIn('Section area must be positive', errors)
        self.assertIn('Iy cannot be negative', errors)
        self.assertIn('Section depth must be positive', errors)
        self.assertIn('Section width must be positive', errors)
    
    def test_validate_calculated_properties_warnings(self):
        """Test validation with warning conditions"""
        properties = {
            'Area': 50.0,    # Small area - warning
            'Iy': 1000.0,
            'Iz': 500.0,
            'Depth': 5.0,    # Small depth - warning
            'Width': 1500.0  # Large width - warning
        }
        
        errors, warnings = SectionPropertyCalculator.validate_calculated_properties(properties)
        
        self.assertEqual(errors, [])
        self.assertGreater(len(warnings), 0)
        self.assertTrue(any('small' in w.lower() for w in warnings))
        self.assertTrue(any('large' in w.lower() for w in warnings))


if __name__ == '__main__':
    unittest.main()
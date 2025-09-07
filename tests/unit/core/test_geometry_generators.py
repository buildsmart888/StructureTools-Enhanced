# -*- coding: utf-8 -*-
"""
Unit tests for geometry generators.
Tests the modular geometry generation system.
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
import sys
import os
import math

# Add project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# Mock FreeCAD before importing
class MockVector:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
    
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

class MockPart:
    @staticmethod
    def makePolygon(points):
        return Mock()
    
    @staticmethod
    def Face(wire):
        return Mock()
    
    @staticmethod
    def makeCircle(radius, center):
        return Mock()

class MockApp:
    Vector = MockVector

sys.modules['FreeCAD'] = MockApp()
sys.modules['App'] = MockApp()
sys.modules['Part'] = MockPart()

from freecad.StructureTools.core.geometry_generators import (
    SectionGeometryGenerator,
    IBeamGenerator,
    RectangularHSSGenerator,
    CircularHSSGenerator,
    AngleGenerator,
    ChannelGenerator,
    create_geometry_generator
)


class TestSectionGeometryGenerator(unittest.TestCase):
    """Test abstract base class"""
    
    def test_abstract_methods(self):
        """Test that abstract methods cannot be instantiated"""
        with self.assertRaises(TypeError):
            SectionGeometryGenerator()


class TestIBeamGenerator(unittest.TestCase):
    """Test I-beam geometry generator"""
    
    def setUp(self):
        """Set up test environment"""
        self.generator = IBeamGenerator()
    
    def test_validate_properties_valid(self):
        """Test validation of valid I-beam properties"""
        properties = {
            "Depth": 200.0,
            "FlangeWidth": 100.0,
            "WebThickness": 10.0,
            "FlangeThickness": 15.0
        }
        
        result = self.generator.validate_properties(properties)
        self.assertTrue(result)
    
    def test_validate_properties_missing(self):
        """Test validation with missing properties"""
        properties = {
            "Depth": 200.0,
            "FlangeWidth": 100.0
            # Missing WebThickness and FlangeThickness
        }
        
        result = self.generator.validate_properties(properties)
        self.assertFalse(result)
    
    def test_validate_i_beam_dimensions_valid(self):
        """Test validation of valid I-beam dimensions"""
        # Should not raise exception
        try:
            self.generator._validate_i_beam_dimensions(200.0, 100.0, 10.0, 15.0)
        except Exception:
            self.fail("Valid dimensions should not raise exception")
    
    def test_validate_i_beam_dimensions_negative(self):
        """Test validation with negative dimensions"""
        with self.assertRaises(ValueError) as context:
            self.generator._validate_i_beam_dimensions(-200.0, 100.0, 10.0, 15.0)
        
        self.assertIn("positive", str(context.exception))
    
    def test_validate_i_beam_dimensions_web_too_wide(self):
        """Test validation when web thickness exceeds flange width"""
        with self.assertRaises(ValueError) as context:
            self.generator._validate_i_beam_dimensions(200.0, 50.0, 60.0, 15.0)
        
        self.assertIn("Web thickness", str(context.exception))
    
    def test_validate_i_beam_dimensions_flanges_too_thick(self):
        """Test validation when flanges are too thick"""
        with self.assertRaises(ValueError) as context:
            self.generator._validate_i_beam_dimensions(200.0, 100.0, 10.0, 150.0)
        
        self.assertIn("Total flange thickness", str(context.exception))
    
    def test_validate_i_beam_dimensions_excessive_ratios(self):
        """Test validation with excessive dimension ratios"""
        # Excessive depth/width ratio
        with self.assertRaises(ValueError) as context:
            self.generator._validate_i_beam_dimensions(1000.0, 50.0, 10.0, 15.0)
        
        self.assertIn("depth/width ratio", str(context.exception))
    
    @patch('freecad.StructureTools.core.geometry_generators.FREECAD_AVAILABLE', True)
    def test_generate_valid_properties(self):
        """Test geometry generation with valid properties"""
        properties = {
            "Depth": 200.0,
            "FlangeWidth": 100.0,
            "WebThickness": 10.0,
            "FlangeThickness": 15.0
        }
        
        with patch.object(self.generator, '_create_i_beam_profile') as mock_create:
            mock_create.return_value = Mock()
            
            result = self.generator.generate(properties)
            
            mock_create.assert_called_once_with(200.0, 100.0, 10.0, 15.0)
            self.assertIsNotNone(result)
    
    def test_generate_invalid_properties(self):
        """Test geometry generation with invalid properties"""
        properties = {
            "Depth": 200.0
            # Missing required properties
        }
        
        with self.assertRaises(ValueError) as context:
            self.generator.generate(properties)
        
        self.assertIn("Missing required properties", str(context.exception))
    
    @patch('freecad.StructureTools.core.geometry_generators.FREECAD_AVAILABLE', False)
    def test_generate_no_freecad(self):
        """Test geometry generation when FreeCAD not available"""
        properties = {
            "Depth": 200.0,
            "FlangeWidth": 100.0,
            "WebThickness": 10.0,
            "FlangeThickness": 15.0
        }
        
        result = self.generator.generate(properties)
        self.assertIsNone(result)


class TestRectangularHSSGenerator(unittest.TestCase):
    """Test rectangular HSS geometry generator"""
    
    def setUp(self):
        """Set up test environment"""
        self.generator = RectangularHSSGenerator()
    
    def test_validate_properties_valid(self):
        """Test validation of valid HSS properties"""
        properties = {
            "Depth": 200.0,
            "Width": 100.0,
            "WallThickness": 10.0
        }
        
        result = self.generator.validate_properties(properties)
        self.assertTrue(result)
    
    def test_validate_properties_missing(self):
        """Test validation with missing properties"""
        properties = {
            "Depth": 200.0
            # Missing Width and WallThickness
        }
        
        result = self.generator.validate_properties(properties)
        self.assertFalse(result)
    
    def test_validate_rectangular_hss_valid(self):
        """Test validation of valid HSS dimensions"""
        try:
            self.generator._validate_rectangular_hss(200.0, 100.0, 10.0)
        except Exception:
            self.fail("Valid dimensions should not raise exception")
    
    def test_validate_rectangular_hss_wall_too_thick(self):
        """Test validation when wall thickness is too large"""
        with self.assertRaises(ValueError) as context:
            self.generator._validate_rectangular_hss(200.0, 100.0, 60.0)
        
        self.assertIn("Wall thickness", str(context.exception))
    
    def test_validate_rectangular_hss_excessive_slenderness(self):
        """Test validation with excessive slenderness"""
        with self.assertRaises(ValueError) as context:
            self.generator._validate_rectangular_hss(1000.0, 100.0, 5.0)
        
        self.assertIn("slenderness", str(context.exception))


class TestCircularHSSGenerator(unittest.TestCase):
    """Test circular HSS geometry generator"""
    
    def setUp(self):
        """Set up test environment"""
        self.generator = CircularHSSGenerator()
    
    def test_validate_properties_valid(self):
        """Test validation of valid circular HSS properties"""
        properties = {
            "Diameter": 200.0,
            "WallThickness": 10.0
        }
        
        result = self.generator.validate_properties(properties)
        self.assertTrue(result)
    
    def test_validate_properties_missing(self):
        """Test validation with missing properties"""
        properties = {
            "Diameter": 200.0
            # Missing WallThickness
        }
        
        result = self.generator.validate_properties(properties)
        self.assertFalse(result)
    
    @patch('freecad.StructureTools.core.geometry_generators.FREECAD_AVAILABLE', True)
    def test_generate_valid_properties(self):
        """Test circular HSS generation with valid properties"""
        properties = {
            "Diameter": 200.0,
            "WallThickness": 10.0
        }
        
        with patch('freecad.StructureTools.core.geometry_generators.Part') as mock_part:
            mock_circle = Mock()
            mock_face = Mock()
            mock_part.makeCircle.return_value = mock_circle
            mock_part.Face.return_value = mock_face
            
            # Mock the cut operation
            mock_result = Mock()
            mock_face.cut.return_value = mock_result
            
            result = self.generator.generate(properties)
            
            # Should create two circles and cut operation
            self.assertEqual(mock_part.makeCircle.call_count, 2)
            self.assertEqual(mock_part.Face.call_count, 2)
            mock_face.cut.assert_called_once()
            
            self.assertIsNotNone(result)
    
    def test_generate_wall_too_thick(self):
        """Test generation with wall thickness too large"""
        properties = {
            "Diameter": 200.0,
            "WallThickness": 150.0  # Too thick
        }
        
        with self.assertRaises(RuntimeError):
            self.generator.generate(properties)


class TestAngleGenerator(unittest.TestCase):
    """Test angle section geometry generator"""
    
    def setUp(self):
        """Set up test environment"""
        self.generator = AngleGenerator()
    
    def test_validate_properties_equal_legs(self):
        """Test validation for equal leg angle"""
        properties = {
            "LegWidth": 50.0,
            "Thickness": 5.0
        }
        
        result = self.generator.validate_properties(properties)
        self.assertTrue(result)
    
    def test_validate_properties_unequal_legs(self):
        """Test validation for unequal leg angle"""
        properties = {
            "LegWidth": 50.0,
            "LegHeight": 75.0,
            "Thickness": 5.0
        }
        
        result = self.generator.validate_properties(properties)
        self.assertTrue(result)
    
    def test_validate_properties_missing(self):
        """Test validation with missing properties"""
        properties = {
            "LegWidth": 50.0
            # Missing Thickness
        }
        
        result = self.generator.validate_properties(properties)
        self.assertFalse(result)
    
    @patch('freecad.StructureTools.core.geometry_generators.FREECAD_AVAILABLE', True)
    def test_generate_equal_angle(self):
        """Test generation of equal angle"""
        properties = {
            "LegWidth": 50.0,
            "Thickness": 5.0
        }
        
        with patch.object(self.generator, '_create_angle_profile') as mock_create:
            mock_create.return_value = Mock()
            
            result = self.generator.generate(properties)
            
            # Should use LegWidth for both dimensions
            mock_create.assert_called_once_with(50.0, 50.0, 5.0)
            self.assertIsNotNone(result)


class TestChannelGenerator(unittest.TestCase):
    """Test channel section geometry generator"""
    
    def setUp(self):
        """Set up test environment"""
        self.generator = ChannelGenerator()
    
    def test_validate_properties_valid(self):
        """Test validation of valid channel properties"""
        properties = {
            "Depth": 200.0,
            "FlangeWidth": 75.0,
            "WebThickness": 8.0,
            "FlangeThickness": 12.0
        }
        
        result = self.generator.validate_properties(properties)
        self.assertTrue(result)
    
    def test_validate_properties_missing(self):
        """Test validation with missing properties"""
        properties = {
            "Depth": 200.0,
            "FlangeWidth": 75.0
            # Missing thicknesses
        }
        
        result = self.generator.validate_properties(properties)
        self.assertFalse(result)
    
    @patch('freecad.StructureTools.core.geometry_generators.FREECAD_AVAILABLE', True)
    def test_generate_valid_properties(self):
        """Test channel generation with valid properties"""
        properties = {
            "Depth": 200.0,
            "FlangeWidth": 75.0,
            "WebThickness": 8.0,
            "FlangeThickness": 12.0
        }
        
        with patch.object(self.generator, '_create_channel_profile') as mock_create:
            mock_create.return_value = Mock()
            
            result = self.generator.generate(properties)
            
            mock_create.assert_called_once_with(200.0, 75.0, 8.0, 12.0)
            self.assertIsNotNone(result)
    
    def test_generate_flanges_too_thick(self):
        """Test generation with flanges too thick"""
        properties = {
            "Depth": 200.0,
            "FlangeWidth": 75.0,
            "WebThickness": 8.0,
            "FlangeThickness": 150.0  # Too thick
        }
        
        with self.assertRaises(RuntimeError):
            self.generator.generate(properties)


class TestCreateGeometryGenerator(unittest.TestCase):
    """Test geometry generator factory function"""
    
    def test_create_wide_flange_generator(self):
        """Test creation of Wide Flange generator"""
        generator = create_geometry_generator("Wide Flange")
        self.assertIsInstance(generator, IBeamGenerator)
    
    def test_create_i_beam_generator(self):
        """Test creation of I-Beam generator"""
        generator = create_geometry_generator("I-Beam")
        self.assertIsInstance(generator, IBeamGenerator)
    
    def test_create_rectangular_hss_generator(self):
        """Test creation of Rectangular HSS generator"""
        generator = create_geometry_generator("Rectangular HSS")
        self.assertIsInstance(generator, RectangularHSSGenerator)
    
    def test_create_circular_hss_generator(self):
        """Test creation of Circular HSS generator"""
        generator = create_geometry_generator("Circular HSS")
        self.assertIsInstance(generator, CircularHSSGenerator)
    
    def test_create_angle_generator(self):
        """Test creation of angle generators"""
        equal_angle = create_geometry_generator("Equal Angle")
        unequal_angle = create_geometry_generator("Unequal Angle")
        
        self.assertIsInstance(equal_angle, AngleGenerator)
        self.assertIsInstance(unequal_angle, AngleGenerator)
    
    def test_create_channel_generator(self):
        """Test creation of Channel generator"""
        generator = create_geometry_generator("Channel")
        self.assertIsInstance(generator, ChannelGenerator)
    
    def test_create_unknown_generator(self):
        """Test creation with unknown section type"""
        generator = create_geometry_generator("Unknown Type")
        self.assertIsNone(generator)


if __name__ == '__main__':
    unittest.main()
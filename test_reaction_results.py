#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unit tests for reaction results visualization functionality
"""

import unittest
import sys
import os
import tempfile

# Add the module path to sys.path
module_path = os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools')
sys.path.insert(0, module_path)

try:
    from reaction_results import ReactionResults
    HAS_REACTION_MODULE = True
except ImportError as e:
    print(f"Could not import reaction_results module: {e}")
    HAS_REACTION_MODULE = False

class MockNode:
    """Mock node class for testing."""
    def __init__(self, name, x=0, y=0, z=0):
        self.name = name
        self.X = x
        self.Y = y
        self.Z = z
        self.support_DX = True
        self.support_DY = True
        self.support_DZ = True
        self.support_RX = True
        self.support_RY = True
        self.support_RZ = True
        self.RxnFX = {"100_DL": 10.0}
        self.RxnFY = {"100_DL": 5.0}
        self.RxnFZ = {"100_DL": 2.0}
        self.RxnMX = {"100_DL": 1.0}
        self.RxnMY = {"100_DL": 0.5}
        self.RxnMZ = {"100_DL": 0.2}

class MockModel:
    """Mock model class for testing."""
    def __init__(self):
        self.nodes = {
            "N1": MockNode("N1", 0, 0, 0),
            "N2": MockNode("N2", 1000, 0, 0),
            "N3": MockNode("N3", 0, 1000, 0)
        }
        self.LoadCombos = {"100_DL": {}}

class MockCalcObject:
    """Mock calculation object for testing."""
    def __init__(self):
        self.model = MockModel()

class MockFreeCADObject:
    """Mock FreeCAD object for testing."""
    def __init__(self):
        self.Properties = {}
        
    def addProperty(self, prop_type, name, group, description):
        """Mock addProperty method."""
        self.Properties[name] = {
            'type': prop_type,
            'group': group,
            'description': description,
            'value': None
        }
        return self
        
    def __setattr__(self, name, value):
        """Mock setattr to handle property values."""
        if name == 'Properties':
            super().__setattr__(name, value)
        elif hasattr(self, 'Properties') and name in self.Properties:
            self.Properties[name]['value'] = value
        else:
            super().__setattr__(name, value)
            
    def __getattr__(self, name):
        """Mock getattr to handle property values."""
        if name == 'Properties':
            return super().__getattr__(name)
        elif hasattr(self, 'Properties') and name in self.Properties:
            return self.Properties[name]['value']
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

class TestReactionResults(unittest.TestCase):
    """Test cases for ReactionResults class."""
    
    def setUp(self):
        """Set up test fixtures."""
        if not HAS_REACTION_MODULE:
            self.skipTest("Reaction results module not available")
            
        self.mock_calc_obj = MockCalcObject()
        self.mock_fc_obj = MockFreeCADObject()
        
    def test_initialization(self):
        """Test ReactionResults initialization."""
        try:
            reaction_results = ReactionResults(self.mock_fc_obj, self.mock_calc_obj)
            
            # Check that basic properties are set
            self.assertTrue(hasattr(self.mock_fc_obj, 'ShowReactionFX'))
            self.assertTrue(hasattr(self.mock_fc_obj, 'ShowReactionFY'))
            self.assertTrue(hasattr(self.mock_fc_obj, 'ShowReactionFZ'))
            self.assertTrue(hasattr(self.mock_fc_obj, 'ShowReactionMX'))
            self.assertTrue(hasattr(self.mock_fc_obj, 'ShowReactionMY'))
            self.assertTrue(hasattr(self.mock_fc_obj, 'ShowReactionMZ'))
            
            # Check that new properties are set
            self.assertTrue(hasattr(self.mock_fc_obj, 'ShowResultantForces'))
            self.assertTrue(hasattr(self.mock_fc_obj, 'ShowResultantMoments'))
            self.assertTrue(hasattr(self.mock_fc_obj, 'AutoScaleReactions'))
            self.assertTrue(hasattr(self.mock_fc_obj, 'UseColorGradient'))
            self.assertTrue(hasattr(self.mock_fc_obj, 'MinReactionThreshold'))
            self.assertTrue(hasattr(self.mock_fc_obj, 'Language'))
            
            print("✓ ReactionResults initialization test passed")
            
        except Exception as e:
            self.fail(f"ReactionResults initialization failed: {str(e)}")
    
    def test_property_defaults(self):
        """Test that properties have correct default values."""
        if not HAS_REACTION_MODULE:
            self.skipTest("Reaction results module not available")
            
        try:
            reaction_results = ReactionResults(self.mock_fc_obj, self.mock_calc_obj)
            
            # Test basic property defaults
            self.assertEqual(self.mock_fc_obj.ShowReactionFX, True)
            self.assertEqual(self.mock_fc_obj.ShowReactionFY, True)
            self.assertEqual(self.mock_fc_obj.ShowReactionFZ, True)
            self.assertEqual(self.mock_fc_obj.ScaleReactionForces, 1.0)
            
            # Test moment property defaults
            self.assertEqual(self.mock_fc_obj.ShowReactionMX, True)
            self.assertEqual(self.mock_fc_obj.ShowReactionMY, True)
            self.assertEqual(self.mock_fc_obj.ShowReactionMZ, True)
            self.assertEqual(self.mock_fc_obj.ScaleReactionMoments, 1.0)
            
            # Test new property defaults
            self.assertEqual(self.mock_fc_obj.ShowResultantForces, False)
            self.assertEqual(self.mock_fc_obj.ShowResultantMoments, False)
            self.assertEqual(self.mock_fc_obj.AutoScaleReactions, False)
            self.assertEqual(self.mock_fc_obj.UseColorGradient, False)
            self.assertEqual(self.mock_fc_obj.MinReactionThreshold, 1e-6)
            self.assertEqual(self.mock_fc_obj.Language, "English")
            
            print("✓ Property defaults test passed")
            
        except Exception as e:
            self.fail(f"Property defaults test failed: {str(e)}")
    
    def test_resultant_reaction_properties(self):
        """Test resultant reaction properties."""
        if not HAS_REACTION_MODULE:
            self.skipTest("Reaction results module not available")
            
        try:
            reaction_results = ReactionResults(self.mock_fc_obj, self.mock_calc_obj)
            
            # Test resultant force properties
            self.assertTrue(hasattr(self.mock_fc_obj, 'ShowResultantForces'))
            self.assertTrue(hasattr(self.mock_fc_obj, 'ScaleResultantForces'))
            
            # Test resultant moment properties
            self.assertTrue(hasattr(self.mock_fc_obj, 'ShowResultantMoments'))
            self.assertTrue(hasattr(self.mock_fc_obj, 'ScaleResultantMoments'))
            
            print("✓ Resultant reaction properties test passed")
            
        except Exception as e:
            self.fail(f"Resultant reaction properties test failed: {str(e)}")
    
    def test_color_gradient_properties(self):
        """Test color gradient properties."""
        if not HAS_REACTION_MODULE:
            self.skipTest("Reaction results module not available")
            
        try:
            reaction_results = ReactionResults(self.mock_fc_obj, self.mock_calc_obj)
            
            # Test color gradient properties
            self.assertTrue(hasattr(self.mock_fc_obj, 'UseColorGradient'))
            self.assertTrue(hasattr(self.mock_fc_obj, 'MinGradientColor'))
            self.assertTrue(hasattr(self.mock_fc_obj, 'MaxGradientColor'))
            
            # Check default color values
            self.assertEqual(self.mock_fc_obj.MinGradientColor, (0.0, 1.0, 0.0, 0.0))  # Green
            self.assertEqual(self.mock_fc_obj.MaxGradientColor, (1.0, 0.0, 0.0, 0.0))  # Red
            
            print("✓ Color gradient properties test passed")
            
        except Exception as e:
            self.fail(f"Color gradient properties test failed: {str(e)}")
    
    def test_specialized_visualization_properties(self):
        """Test specialized visualization properties."""
        if not HAS_REACTION_MODULE:
            self.skipTest("Reaction results module not available")
            
        try:
            reaction_results = ReactionResults(self.mock_fc_obj, self.mock_calc_obj)
            
            # Test specialized visualization properties
            self.assertTrue(hasattr(self.mock_fc_obj, 'ShowOnlyMaximumReactions'))
            self.assertTrue(hasattr(self.mock_fc_obj, 'ShowOnlySignificantReactions'))
            self.assertTrue(hasattr(self.mock_fc_obj, 'SignificanceThreshold'))
            
            # Check default values
            self.assertEqual(self.mock_fc_obj.ShowOnlyMaximumReactions, False)
            self.assertEqual(self.mock_fc_obj.ShowOnlySignificantReactions, False)
            self.assertEqual(self.mock_fc_obj.SignificanceThreshold, 0.1)
            
            print("✓ Specialized visualization properties test passed")
            
        except Exception as e:
            self.fail(f"Specialized visualization properties test failed: {str(e)}")
    
    def test_language_support(self):
        """Test language support properties."""
        if not HAS_REACTION_MODULE:
            self.skipTest("Reaction results module not available")
            
        try:
            reaction_results = ReactionResults(self.mock_fc_obj, self.mock_calc_obj)
            
            # Test language property
            self.assertTrue(hasattr(self.mock_fc_obj, 'Language'))
            self.assertEqual(self.mock_fc_obj.Language, "English")
            
            # Test that Language is an enumeration with correct options
            # Note: In the actual implementation, this would be an enumeration
            # but in our mock it's just a string
            
            print("✓ Language support test passed")
            
        except Exception as e:
            self.fail(f"Language support test failed: {str(e)}")
    
    def test_min_reaction_threshold(self):
        """Test minimum reaction threshold property."""
        if not HAS_REACTION_MODULE:
            self.skipTest("Reaction results module not available")
            
        try:
            reaction_results = ReactionResults(self.mock_fc_obj, self.mock_calc_obj)
            
            # Test minimum reaction threshold property
            self.assertTrue(hasattr(self.mock_fc_obj, 'MinReactionThreshold'))
            self.assertEqual(self.mock_fc_obj.MinReactionThreshold, 1e-6)
            
            # Test that we can set a different threshold
            self.mock_fc_obj.MinReactionThreshold = 1e-5
            self.assertEqual(self.mock_fc_obj.MinReactionThreshold, 1e-5)
            
            print("✓ Minimum reaction threshold test passed")
            
        except Exception as e:
            self.fail(f"Minimum reaction threshold test failed: {str(e)}")
    
    def test_auto_scale_property(self):
        """Test auto-scale property."""
        if not HAS_REACTION_MODULE:
            self.skipTest("Reaction results module not available")
            
        try:
            reaction_results = ReactionResults(self.mock_fc_obj, self.mock_calc_obj)
            
            # Test auto-scale property
            self.assertTrue(hasattr(self.mock_fc_obj, 'AutoScaleReactions'))
            self.assertEqual(self.mock_fc_obj.AutoScaleReactions, False)
            
            # Test that we can enable auto-scaling
            self.mock_fc_obj.AutoScaleReactions = True
            self.assertEqual(self.mock_fc_obj.AutoScaleReactions, True)
            
            print("✓ Auto-scale property test passed")
            
        except Exception as e:
            self.fail(f"Auto-scale property test failed: {str(e)}")

def run_tests():
    """Run all tests."""
    print("Running Reaction Results Unit Tests...")
    print("=" * 50)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReactionResults)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("=" * 50)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFailures:")
        for test, traceback in result.failures:
            print(f"  {test}: {traceback}")
            
    if result.errors:
        print("\nErrors:")
        for test, traceback in result.errors:
            print(f"  {test}: {traceback}")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_tests()
    if success:
        print("\n✓ All tests passed!")
    else:
        print("\n✗ Some tests failed!")
        sys.exit(1)
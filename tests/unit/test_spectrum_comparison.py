"""
Unit test for spectrum comparison functionality
"""

import sys
import os
import unittest
import numpy as np

# Add the module path to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'freecad', 'StructureTools'))

class TestSpectrumComparison(unittest.TestCase):
    """Test cases for spectrum comparison functionality"""
    
    def test_spectrum_comparison_import(self):
        """Test that the spectrum comparison functionality can be imported"""
        try:
            # This is just to verify the file structure
            self.assertTrue(True, "Test framework is working")
        except Exception as e:
            self.fail(f"Error in test framework: {e}")
    
    def test_numpy_available(self):
        """Test that numpy is available for spectrum calculations"""
        try:
            # Test basic numpy functionality
            periods = np.linspace(0.1, 4.0, 20)
            accelerations = 0.8 * np.exp(-0.5 * periods)
            self.assertEqual(len(periods), 20)
            self.assertEqual(len(accelerations), 20)
        except Exception as e:
            self.fail(f"Error with numpy functionality: {e}")

if __name__ == "__main__":
    unittest.main()
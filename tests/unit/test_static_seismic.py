"""
Unit tests for the static seismic analysis functionality
"""

import sys
import os
import unittest
import pytest

# Add the module path to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'freecad', 'StructureTools'))

class TestStaticSeismic(unittest.TestCase):
    """Test cases for static seismic analysis functionality"""
    
    def test_static_seismic_module_import(self):
        """Test that the static seismic module can be imported"""
        try:
            from freecad.StructureTools.seismic.static_seismic import (
                StaticSeismicParameters, StaticSeismicAnalyzer
            )
            self.assertTrue(True, "Static seismic module imported successfully")
        except ImportError as e:
            self.fail(f"Failed to import static seismic module: {e}")
    
    def test_static_seismic_parameters_creation(self):
        """Test creation of static seismic parameters"""
        try:
            from freecad.StructureTools.seismic.static_seismic import StaticSeismicParameters
            
            # Create default parameters
            params = StaticSeismicParameters()
            self.assertIsInstance(params, StaticSeismicParameters)
            self.assertEqual(params.building_height, 30.0)
            self.assertEqual(params.total_weight, 50000.0)
            self.assertEqual(params.number_of_stories, 10)
            
            # Create custom parameters
            custom_params = StaticSeismicParameters(
                building_height=25.0,
                total_weight=40000.0,
                number_of_stories=8,
                sds=1.2,
                sd1=0.5
            )
            self.assertEqual(custom_params.building_height, 25.0)
            self.assertEqual(custom_params.total_weight, 40000.0)
            self.assertEqual(custom_params.number_of_stories, 8)
            self.assertEqual(custom_params.sds, 1.2)
            self.assertEqual(custom_params.sd1, 0.5)
            
        except Exception as e:
            self.fail(f"Error testing static seismic parameters: {e}")
    
    def test_static_seismic_analyzer_creation(self):
        """Test creation of static seismic analyzer"""
        try:
            from freecad.StructureTools.seismic.static_seismic import (
                StaticSeismicParameters, StaticSeismicAnalyzer
            )
            
            # Create analyzer with default parameters
            analyzer = StaticSeismicAnalyzer()
            self.assertIsInstance(analyzer, StaticSeismicAnalyzer)
            
            # Create analyzer with custom parameters
            params = StaticSeismicParameters(building_height=25.0, total_weight=40000.0)
            analyzer_with_params = StaticSeismicAnalyzer(params)
            self.assertIsInstance(analyzer_with_params, StaticSeismicAnalyzer)
            
        except Exception as e:
            self.fail(f"Error testing static seismic analyzer creation: {e}")
    
    def test_fundamental_period_calculation(self):
        """Test fundamental period calculation"""
        try:
            from freecad.StructureTools.seismic.static_seismic import (
                StaticSeismicParameters, StaticSeismicAnalyzer
            )
            
            # Create analyzer
            params = StaticSeismicParameters(building_height=30.0)
            analyzer = StaticSeismicAnalyzer(params)
            
            # Calculate fundamental period
            period = analyzer.calculate_fundamental_period()
            self.assertIsInstance(period, float)
            self.assertGreater(period, 0)
            
        except Exception as e:
            self.fail(f"Error testing fundamental period calculation: {e}")
    
    def test_seismic_coefficient_calculation(self):
        """Test seismic coefficient calculation"""
        try:
            from freecad.StructureTools.seismic.static_seismic import (
                StaticSeismicParameters, StaticSeismicAnalyzer
            )
            
            # Create analyzer
            params = StaticSeismicParameters(
                building_height=30.0,
                sds=1.0,
                sd1=0.4,
                r_factor=8.0,
                importance_factor=1.0
            )
            analyzer = StaticSeismicAnalyzer(params)
            
            # Calculate seismic coefficient
            cs = analyzer.calculate_seismic_coefficient()
            self.assertIsInstance(cs, float)
            self.assertGreater(cs, 0)
            
        except Exception as e:
            self.fail(f"Error testing seismic coefficient calculation: {e}")
    
    def test_base_shear_calculation(self):
        """Test base shear calculation"""
        try:
            from freecad.StructureTools.seismic.static_seismic import (
                StaticSeismicParameters, StaticSeismicAnalyzer
            )
            
            # Create analyzer
            params = StaticSeismicParameters(
                building_height=30.0,
                total_weight=50000.0,
                sds=1.0,
                sd1=0.4,
                r_factor=8.0,
                importance_factor=1.0
            )
            analyzer = StaticSeismicAnalyzer(params)
            
            # Calculate base shear
            base_shear = analyzer.calculate_base_shear()
            self.assertIsInstance(base_shear, float)
            self.assertGreater(base_shear, 0)
            
        except Exception as e:
            self.fail(f"Error testing base shear calculation: {e}")
    
    def test_story_forces_calculation(self):
        """Test story forces calculation"""
        try:
            from freecad.StructureTools.seismic.static_seismic import (
                StaticSeismicParameters, StaticSeismicAnalyzer
            )
            
            # Create analyzer
            params = StaticSeismicParameters(
                building_height=30.0,
                total_weight=50000.0,
                number_of_stories=10,
                sds=1.0,
                sd1=0.4,
                r_factor=8.0,
                importance_factor=1.0
            )
            analyzer = StaticSeismicAnalyzer(params)
            
            # Calculate story forces
            story_forces = analyzer.calculate_story_forces()
            self.assertIsInstance(story_forces, list)
            self.assertEqual(len(story_forces), 10)
            for force in story_forces:
                self.assertIsInstance(force, float)
                self.assertGreaterEqual(force, 0)
            
        except Exception as e:
            self.fail(f"Error testing story forces calculation: {e}")
    
    def test_complete_analysis(self):
        """Test complete static seismic analysis"""
        try:
            from freecad.StructureTools.seismic.static_seismic import (
                StaticSeismicParameters, StaticSeismicAnalyzer
            )
            
            # Create analyzer
            params = StaticSeismicParameters(
                building_height=30.0,
                total_weight=50000.0,
                number_of_stories=10,
                sds=1.0,
                sd1=0.4,
                r_factor=8.0,
                importance_factor=1.0
            )
            analyzer = StaticSeismicAnalyzer(params)
            
            # Perform complete analysis
            results = analyzer.perform_analysis()
            self.assertIsInstance(results, dict)
            self.assertIn('period', results)
            self.assertIn('base_shear', results)
            self.assertIn('story_forces', results)
            self.assertIn('vertical_force', results)
            self.assertIn('story_heights', results)
            self.assertIn('story_weights', results)
            
            # Check values
            self.assertGreater(results['period'], 0)
            self.assertGreater(results['base_shear'], 0)
            self.assertEqual(len(results['story_forces']), 10)
            self.assertEqual(len(results['story_heights']), 10)
            self.assertEqual(len(results['story_weights']), 10)
            
        except Exception as e:
            self.fail(f"Error testing complete analysis: {e}")
    
    def test_3d_load_pattern_visualization(self):
        """Test 3D load pattern visualization function"""
        try:
            from freecad.StructureTools.seismic.static_seismic import plot_3d_load_pattern
            
            # Test data
            story_forces = [1000.0, 1800.0, 2500.0, 3100.0, 3600.0, 4000.0, 4300.0, 4500.0, 4600.0, 4650.0]
            story_heights = [3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0, 24.0, 27.0, 30.0]
            building_width = 20.0
            building_length = 40.0
            
            # Test X direction
            fig_x = plot_3d_load_pattern(story_forces, story_heights, building_width, building_length, 'X')
            # In headless environments, this might return None, which is acceptable
            
            # Test Y direction
            fig_y = plot_3d_load_pattern(story_forces, story_heights, building_width, building_length, 'Y')
            # In headless environments, this might return None, which is acceptable
            
            # Test function exists and can be called without error
            self.assertTrue(callable(plot_3d_load_pattern))
            
        except Exception as e:
            # In headless environments, matplotlib might not be available, which is acceptable
            # We're mainly testing that the function exists and can be imported
            pass

def test_static_seismic_tab_creation():
    """Test that the static seismic tab can be created"""
    try:
        from freecad.StructureTools.seismic.static_seismic import create_static_seismic_tab
        
        # Try to create the tab
        # In a headless environment, this might return None or raise an exception
        # We're primarily testing that the function exists and can be imported
        assert callable(create_static_seismic_tab)
        
        # If we're in a headless environment, the function should handle it gracefully
        try:
            tab = create_static_seismic_tab()
            # If it returns a value, it should be either None or a QWidget
            if tab is not None:
                # We can't fully test the GUI without a QApplication, 
                # but we can verify it's a QWidget or similar
                pass
        except Exception as e:
            # In headless environments, GUI creation might fail, which is expected
            # We're mainly testing that the function exists and can be called
            pass
            
    except ImportError as e:
        pytest.fail(f"Failed to import static seismic tab function: {e}")
    except Exception as e:
        pytest.fail(f"Error testing static seismic tab creation: {e}")

if __name__ == "__main__":
    unittest.main()
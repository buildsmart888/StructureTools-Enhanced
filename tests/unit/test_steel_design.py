
import unittest
from unittest.mock import MagicMock, Mock
import sys
import types

# 1. Mock External Dependencies (FreeCAD, Pynite)
if 'FreeCAD' not in sys.modules:
    fc_mock = types.ModuleType('FreeCAD')
    fc_mock.Console = MagicMock()
    fc_mock.Units = MagicMock()
    sys.modules['FreeCAD'] = fc_mock

from freecad.StructureTools.analysis.steel_design import SteelDesignChecker

class TestSteelDesignChecker(unittest.TestCase):
    def setUp(self):
        # Create a mock model
        self.mock_model = MagicMock()
        self.checker = SteelDesignChecker(self.mock_model)
        
    def test_basic_check_pass(self):
        # Setup Mock Member, Material, Section
        mock_member = MagicMock()
        mock_member.material_name = 'SteelA992'
        mock_member.section_name = 'W12x26'
        
        mock_mat = MagicMock()
        mock_mat.Fy = 345000.0 # 345 MPa in kN/m2 (kPa)
        
        mock_sec = MagicMock()
        mock_sec.A = 0.00774 # m2 (approx 7740 mm2)
        mock_sec.Sy_freecad = 0.0002 # m3 (Sx) approx
        mock_sec.Sz_freecad = 0.00005 # m3 (Sy) approx
        mock_sec.Iz = 0.0002 # Fallback
        mock_sec.Iy = 0.00005 # Fallback
        
        # Populate model
        self.mock_model.members = {'Beam1': mock_member}
        self.mock_model.materials = {'SteelA992': mock_mat}
        self.mock_model.sections = {'W12x26': mock_sec}
        
        # Capacity rough calc:
        # Pn = 0.6 * 345000 * 0.00774 = 1602.18 kN
        # Mn_z = 0.66 * 345000 * 0.0002 = 45.54 kNm
        
        # Apply small forces (Pass)
        forces = {
            'P': 100.0, # 100 kN
            'Mz': 10.0, # 10 kNm
            'My': 0.0
        }
        
        ratio, details = self.checker.check_member('Beam1', forces)
        
        self.assertLess(ratio, 1.0)
        # Check almost equal with generous delta due to float/approx
        self.assertAlmostEqual(details['Pn'], 1602.18, delta=10.0)
        
    def test_basic_check_fail(self):
        # Setup similar mock
        mock_member = MagicMock()
        mock_member.material_name = 'Steel'
        mock_member.section_name = 'Sec'
        
        mock_mat = MagicMock()
        mock_mat.Fy = 250000.0 
        
        mock_sec = MagicMock()
        mock_sec.A = 0.01 
        mock_sec.Sy_freecad = 0.001 
        mock_sec.Sz_freecad = 0.001
        mock_sec.Iz = 0.001
        mock_sec.Iy = 0.001
        
        self.mock_model.members = {'Col1': mock_member}
        self.mock_model.materials = {'Steel': mock_mat}
        self.mock_model.sections = {'Sec': mock_sec}
        
        # Apply HUGE forces (Fail)
        forces = {
            'P': 10000.0, 
            'Mz': 5000.0
        }
        
        ratio, details = self.checker.check_member('Col1', forces)
        self.assertGreater(ratio, 1.0)

    def test_zero_section_properties_fallback(self):
        # Test fallback estimation when Sx/Sy are 0
        mock_member = MagicMock()
        mock_member.material_name = 'Mat'
        mock_member.section_name = 'Rect'
        
        mock_mat = MagicMock()
        mock_mat.Fy = 250000.0
        
        mock_sec = MagicMock()
        mock_sec.A = 0.01
        mock_sec.Iz = 0.0001 # 1e-4
        mock_sec.Iy = 0.0001
        # Sy_freecad missing/zero
        
        self.mock_model.members = {'BmZero': mock_member}
        self.mock_model.materials = {'Mat': mock_mat}
        self.mock_model.sections = {'Rect': mock_sec}
        
        forces = {'Mz': 10.0}
        
        ratio, details = self.checker.check_member('BmZero', forces)
        
        # Should calculate non-zero Mn
        self.assertGreater(details['Mn_z'], 0.0)

if __name__ == '__main__':
    unittest.main()

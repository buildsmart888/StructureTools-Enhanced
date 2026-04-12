
import unittest
from unittest.mock import MagicMock
from freecad.StructureTools.analysis.result_manager import ResultManager

class TestResultManagerLogic(unittest.TestCase):
    def setUp(self):
        self.mock_solver = MagicMock()
        self.manager = ResultManager(self.mock_solver)
        self.obj = MagicMock()
        self.obj.MemberResults = [] # Pre-existing or created
        
        # Setup solver mock returns
        self.mock_solver.get_node_names.return_value = ['Node1', 'Node2']
        self.mock_solver.get_member_names.return_value = ['Member1']
        
        # Reactions
        self.mock_solver.get_node_reaction.return_value = {
            'FX': 100.0, 'FY': 0.0, 'FZ': 0.0, 'MX':0.0, 'MY':0.0, 'MZ':0.0
        }
        
        # Lengths
        self.mock_solver.get_member_length.return_value = 5.0
        
        # Forces
        self.mock_solver.get_member_forces.return_value = {
            'momentY': [0, 10, 0], 'momentZ': [0,0,0],
            'shearY': [0,0,0], 'shearZ': [0,0,0],
            'axial': [0,0,0], 'torque': [0,0,0]
        }
        self.mock_solver.get_member_deflection.return_value = [0, 0.1, 0]
        self.mock_solver.get_min_max_forces.return_value = (0.0, 10.0)

    def test_prepare_results_populates_obj(self):
        config = {'moment': 3}
        self.manager.prepare_results_for_object(self.obj, '1.4DL', config)
        
        # Verify Lengths
        self.assertTrue(hasattr(self.obj, 'MemberLengths'))
        self.assertEqual(self.obj.MemberLengths, [5.0])
        
        # Verify Reactions
        self.assertTrue(hasattr(self.obj, 'ReactionNodes'))
        self.assertIn('Node1', self.obj.ReactionNodes)
        self.assertEqual(self.obj.ReactionX, [100.0, 100.0]) # Logic appends for each node
        
        # Verify Diagrams
        self.assertTrue(hasattr(self.obj, 'MomentY'))
        self.assertIn("0, 10, 0", self.obj.MomentY[0])
        
        # Verify MemberResults JSON structure
        self.assertTrue(hasattr(self.obj, 'MemberResults'))
        results = self.obj.MemberResults
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['name'], 'Member1')
        self.assertEqual(results[0]['maxMomentY'], 10.0)

if __name__ == '__main__':
    unittest.main()

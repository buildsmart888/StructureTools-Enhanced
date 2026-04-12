
import unittest
from unittest.mock import MagicMock
from freecad.StructureTools.analysis.unified_result_interface import UnifiedResultInterface

class TestUnifiedResultInterface(unittest.TestCase):
    
    def setUp(self):
        # Create a mock FreeCAD object populated with results
        self.obj = MagicMock()
        
        # Member lists
        self.obj.NameMembers = ['Member1', 'Member2']
        
        # Diagram data (string lists)
        self.obj.MomentY = ["0.0, 10.0, 0.0", "5.0, 5.0, 5.0"]
        self.obj.MomentZ = ["0.0, 0.0, 0.0", "0.0, 0.0, 0.0"]
        
        # Mix/Max envelope
        self.obj.MinMomentY = [0.0, 5.0]
        self.obj.MaxMomentY = [10.0, 5.0]
        
        # Structured results
        self.obj.MemberResults = [
            {'name': 'Member1', 'max_moment_y': 10.0},
            {'name': 'Member2', 'max_moment_y': 5.0}
        ]
        
        # Reactions
        self.obj.ReactionNodes = ['NodeA']
        self.obj.ReactionY = [100.0]
        
        self.interface = UnifiedResultInterface(self.obj)

    def test_get_all_member_names(self):
        names = self.interface.get_all_member_names()
        self.assertEqual(names, ['Member1', 'Member2'])

    def test_get_member_results(self):
        res = self.interface.get_member_results('Member1')
        self.assertIsNotNone(res)
        self.assertEqual(res['max_moment_y'], 10.0)
        
        res_none = self.interface.get_member_results('Missing')
        self.assertIsNone(res_none)

    def test_get_diagram_data(self):
        data = self.interface.get_diagram_data('Member1', 'MomentY')
        self.assertEqual(data, [0.0, 10.0, 0.0])
        
        data2 = self.interface.get_diagram_data('Member2', 'MomentY')
        self.assertEqual(data2, [5.0, 5.0, 5.0])
        
        # Missing data
        data_missing = self.interface.get_diagram_data('Member1', 'ShearY') # Not mocked
        self.assertEqual(data_missing, [])

    def test_get_min_max_values(self):
        envelope = self.interface.get_min_max_values('Member1')
        self.assertEqual(envelope['MomentY'], (0.0, 10.0))
        
    def test_get_reactions_for_node(self):
        rxn = self.interface.get_reactions_for_node('NodeA')
        self.assertEqual(rxn['FY'], 100.0)
        
        # Missing reaction
        rxn_missing = self.interface.get_reactions_for_node('NodeB')
        self.assertEqual(rxn_missing, {})

    def test_get_load_combinations(self):
        # Default mock has ActiveLoadCombination but no LoadCombination list
        self.obj.ActiveLoadCombination = 'Combo1'
        combos = self.interface.get_load_combinations()
        self.assertEqual(combos, ['Combo1'])
        
        # Add LoadCombination list
        self.obj.LoadCombination = ['Combo1', 'Combo2']
        combos2 = self.interface.get_load_combinations()
        self.assertEqual(combos2, ['Combo1', 'Combo2'])

    def test_get_reaction_node_names(self):
        # Without dynamic model, it uses stored ReactionNodes if combo matches
        self.obj.ReactionLoadCombo = 'Combo1'
        
        nodes = self.interface.get_reaction_node_names('Combo1')
        self.assertEqual(nodes, ['NodeA'])
        
        # Mismatch combo (and no dynamic model) should return empty or fallback? 
        # Current logic: returns [] if no model and mismatch
        nodes_mismatch = self.interface.get_reaction_node_names('DifferentCombo')
        self.assertEqual(nodes_mismatch, [])

    def test_get_node_coordinates(self):
        # Mocking legacy 'Nodes' dictionary input
        # Assuming Nodes is a dict of objects with X,Y,Z
        node_obj = MagicMock()
        node_obj.X = 1.0; node_obj.Y = 2.0; node_obj.Z = 3.0
        self.obj.Nodes = {'NodeA': node_obj}
        
        coords = self.interface.get_node_coordinates('NodeA')
        self.assertEqual(coords, (1.0, 2.0, 3.0))
        
        # Test 0.0 fallback
        coords_missing = self.interface.get_node_coordinates('NodeMissing')
        self.assertEqual(coords_missing, (0.0, 0.0, 0.0))

if __name__ == '__main__':
    unittest.main()

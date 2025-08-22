import os
import sys
from unittest.mock import Mock, patch

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
freecad_dir = os.path.join(root, 'freecad')
sys.path.insert(0, freecad_dir)

from StructureTools.objects.StructuralNode import StructuralNode

m = Mock()
m.addProperty = Mock()
node = StructuralNode(m)

restraint_values = {k: True for k in ['RestraintX','RestraintY','RestraintZ','RestraintRX','RestraintRY','RestraintRZ']}

def mock_getattr(o, attr, default=False):
    print('mock_getattr called for', attr)
    return restraint_values.get(attr, default)

print('Before patch, code =', node.get_restraint_code())
with patch('builtins.getattr', side_effect=mock_getattr):
    print('In patch, builtins.getattr is', type(__import__('builtins').getattr))
    print('During patch, code =', node.get_restraint_code())

print('After patch, code =', node.get_restraint_code())

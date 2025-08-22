import os
import sys
from unittest.mock import Mock, patch

# Make sure the local `freecad` package is importable like tests do
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
freecad_dir = os.path.join(root, 'freecad')
sys.path.insert(0, freecad_dir)

from StructureTools.objects.StructuralNode import StructuralNode
import builtins

m = Mock()
m.addProperty = Mock()
node = StructuralNode(m)
print('node.__dict__.keys =', list(object.__getattribute__(node, '__dict__').keys()))
print('_obj_ref present?', '_obj_ref' in object.__getattribute__(node,'__dict__'))
print('Object present?', 'Object' in object.__getattribute__(node,'__dict__'))
print('proxy object repr:', repr(node._get_proxy_object()))

restraint_values = {k: True for k in ['RestraintX','RestraintY','RestraintZ','RestraintRX','RestraintRY','RestraintRZ']}

def mock_getattr(o, attr, default=False):
    print('mock_getattr called for', attr)
    return restraint_values.get(attr, default)

with patch('builtins.getattr', side_effect=mock_getattr):
    print('After patch, builtins.getattr is', type(builtins.getattr))
    # If it's a Mock, show if it has side_effect
    try:
        print('hasattr getattr.side_effect?', hasattr(builtins.getattr, 'side_effect'))
        print('side_effect attr type:', type(object.__getattribute__(builtins.getattr, 'side_effect')))
    except Exception as e:
        print('error reading side_effect:', e)
    code = node.get_restraint_code()
    print('restraint code:', code)

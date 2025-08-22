# Quick repro for restraint symbol creation without pytest
import sys
import builtins
from unittest.mock import Mock, patch

# Ensure local package path
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'freecad'))

from StructureTools.objects.StructuralNode import StructuralNode


def run_case(name, getattr_side_effect):
    print('\n--- CASE', name, '---')
    mock_obj = Mock()
    mock_obj.addProperty = Mock()
    node = StructuralNode(mock_obj)
    mock_obj.Position = Mock()
    mock_obj.Position.x = 0
    mock_obj.Position.y = 0
    mock_obj.Position.z = 0

    with patch('builtins.getattr', side_effect=getattr_side_effect):
        with patch('StructureTools.objects.StructuralNode.Part') as mock_part:
            symbols = node._create_restraint_symbols(mock_obj)
            print('Part mock:', repr(mock_part))
            try:
                print('makeCone called:', mock_part.makeCone.called)
                print('makeCylinder called:', mock_part.makeCylinder.called)
            except Exception as e:
                print('inspect error:', e)


if __name__ == '__main__':
    # Fixed support
    def getattr_fixed(obj, attr, default=False):
        if attr in ('RestraintX', 'RestraintY', 'RestraintZ', 'RestraintRX', 'RestraintRY', 'RestraintRZ'):
            return True
        return default

    # Pinned
    def getattr_pinned(obj, attr, default=False):
        vals = {'RestraintX': True, 'RestraintY': True, 'RestraintZ': True,
                'RestraintRX': False, 'RestraintRY': False, 'RestraintRZ': False}
        return vals.get(attr, default)

    # Roller
    def getattr_roller(obj, attr, default=False):
        if attr == 'RestraintZ':
            return True
        return default

    run_case('fixed', getattr_fixed)
    run_case('pinned', getattr_pinned)
    run_case('roller', getattr_roller)

# Simple repro to inspect StructuralNode restraint symbol logic
import builtins
from unittest.mock import Mock, patch
from StructureTools.objects.StructuralNode import StructuralNode


def run_pinned():
    m = Mock()
    m.addProperty = Mock()
    node = StructuralNode(m)

    def mock_getattr(obj, attr, default=False):
        restraint_values = {
            'RestraintX': True, 'RestraintY': True, 'RestraintZ': True,
            'RestraintRX': False, 'RestraintRY': False, 'RestraintRZ': False
        }
        return restraint_values.get(attr, default)

    with patch('builtins.getattr', side_effect=mock_getattr):
        with patch('builtins.hasattr', return_value=True):
            # Also patch the Part symbol inside the module like the tests do
            with patch('StructureTools.objects.StructuralNode.Part') as mock_part:
                tx = node._safe_get(m, 'RestraintX', False)
                ty = node._safe_get(m, 'RestraintY', False)
                tz = node._safe_get(m, 'RestraintZ', False)
                rxx = node._safe_get(m, 'RestraintRX', False)
                ryy = node._safe_get(m, 'RestraintRY', False)
                rzz = node._safe_get(m, 'RestraintRZ', False)
                print('pinned flags:', tx, ty, tz, rxx, ryy, rzz)
                symbols = node._create_restraint_symbols(m)
                print('symbols count:', len(symbols))
                print('mock_part.makeCylinder.called=', getattr(mock_part, 'makeCylinder', Mock()).called)
                print('mock_part.makeCone.called=', getattr(mock_part, 'makeCone', Mock()).called)


def run_roller():
    m = Mock()
    m.addProperty = Mock()
    node = StructuralNode(m)

    def mock_getattr(obj, attr, default=False):
        if attr == 'RestraintZ':
            return True
        return default

    with patch('builtins.getattr', side_effect=mock_getattr):
        with patch('builtins.hasattr', return_value=True):
            with patch('StructureTools.objects.StructuralNode.Part') as mock_part:
                tx = node._safe_get(m, 'RestraintX', False)
                ty = node._safe_get(m, 'RestraintY', False)
                tz = node._safe_get(m, 'RestraintZ', False)
                print('roller flags:', tx, ty, tz)
                symbols = node._create_restraint_symbols(m)
                print('symbols count:', len(symbols))
                print('mock_part.makeCylinder.called=', getattr(mock_part, 'makeCylinder', Mock()).called)


if __name__ == '__main__':
    try:
        print('--- PINNED ---')
        run_pinned()
        print('--- ROLLER ---')
        run_roller()
    except Exception as e:
        import traceback
        traceback.print_exc()
        print('Exception during repro run:', e)

import pytest

result = pytest.main(['tests/unit/objects', '-q', '--showlocals', '-r', 'a'])
print('RC=', result)

import pytest
import sys
from contextlib import redirect_stdout, redirect_stderr

log_path = 'pytest_objects.log'
with open(log_path, 'w', encoding='utf-8') as f:
    with redirect_stdout(f), redirect_stderr(f):
        rc = pytest.main(['tests/unit/objects', '-q', '--showlocals', '-r', 'a'])
    # After pytest finishes, write the return code at the end
    f.write('\nPYTEST_RC=' + str(rc) + '\n')
print('Wrote', log_path, 'PYTEST_RC=', rc)

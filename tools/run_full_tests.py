import subprocess
import sys
from pathlib import Path

python = sys.executable
log = Path('full_tests.log')
xml = Path('full_tests.xml')

cmd = [python, '-m', 'pytest', '-q', '--showlocals', '-r', 'a', '--junitxml=' + str(xml)]

print('Running:', ' '.join(cmd))
res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

with log.open('w', encoding='utf-8') as f:
    f.write(res.stdout)
    f.write('\nRETURN_CODE=' + str(res.returncode) + '\n')

print('Wrote', log, 'RETURN_CODE=', res.returncode)
if xml.exists():
    print('JUnit XML:', xml)
else:
    print('No junit xml produced')

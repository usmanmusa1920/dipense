

import os
import shlex
import subprocess as sp
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

print(BASE_DIR)

rel_path = os.path.join(BASE_DIR, 'sysinfo.sh')
cmd = "sh " + rel_path


sp.run(shlex.split(cmd))

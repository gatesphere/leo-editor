#@+leo-ver=5-thin
#@+node:ekr.20240321123225.3: * @file ../scripts/install_leo_from_testpypi.py
#@@language python

"""
install_leo_from_testpypi.py: install leo from https://test.pypi.org/project/leo/.

Info item #3837 describes all distribution-related scripts.
https://github.com/leo-editor/leo-editor/issues/3837
"""

import os
import sys

print(os.path.basename(__file__))

# Make sure leo-editor is on the path.
leo_dir = os.path.abspath(os.path.join(__file__, '..', '..', '..'))
if leo_dir not in sys.path:
    sys.path.insert(0, leo_dir)
from leo.core import leoGlobals as g

g.cls()
print('install_leo_from_testpypi.py')

# Do *not* install from leo-editor!
home_dir = os.path.expanduser("~")
os.chdir(home_dir)

# Install.
command = 'python -m pip install -i https://test.pypi.org/simple/ leo'
g.execute_shell_commands(command)
#@-leo

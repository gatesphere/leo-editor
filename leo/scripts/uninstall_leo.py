#@+leo-ver=5-thin
#@+node:ekr.20240321123225.1: * @file ../scripts/uninstall_leo.py
#@@language python

"""
uninstall_leo.py: run `pip uninstall leo`.

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
print('uninstall_leo.py')

# Do *not* install from leo-editor!
home_dir = os.path.expanduser("~")
os.chdir(home_dir)

# Uninstall.    
command = 'python -m pip uninstall leo'
g.execute_shell_commands(command)
#@-leo

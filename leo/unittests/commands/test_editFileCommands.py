#@+leo-ver=5-thin
#@+node:ekr.20230705083159.1: * @file ../unittests/commands/test_editFileCommands.py
"""Tests for leo.commands.editFileCommands."""
import os
from leo.core import leoGlobals as g
from leo.commands.editFileCommands import GitDiffController
from leo.core.leoTest2 import LeoUnitTest

#@+others
#@+node:ekr.20230714143317.2: ** class TestEditFileCommands(LeoUnitTest)
class TestEditFileCommands(LeoUnitTest):
    """Unit tests for leo/commands/editCommands.py."""

    #@+others
    #@+node:ekr.20230714143317.3: *3* TestEditFileCommands.slow_test_gdc_node_history
    def slow_test_gdc_node_history(self):

        # These links are valid within leoPy.leo on EKR's machine.
        # g.findUnl:        unl:gnx://leoPy.leo#ekr.20230626064652.1
        # g.parsePathData:  unl:gnx://leoPy.leo#ekr.20230630132341.1
        
        path = g.os_path_finalize_join(g.app.loadDir, 'leoGlobals.py')
        msg = repr(path)
        self.assertTrue(os.path.exists(path), msg=msg)
        self.assertTrue(os.path.isabs(path), msg=msg)
        self.assertTrue(os.path.isfile(path), msg=msg)
        findUnl_gnx = 'ekr.20230626064652.1'
        x = GitDiffController(c=self.c)
        x.node_history(path, gnx=findUnl_gnx)
    #@+node:ekr.20230714143451.1: *3* TestEditFileCommands.diff_two_branches
    def test_diff_two_branches(self):
        c = self.c
        u = c.undoer
        x = GitDiffController(c=c)
        
        # Setup the outline.
        root = c.rootPosition()
        root.h = '@file leoGlobals.py'
        root.deleteAllChildren()
        while root.hasNext():
            root.next().doDelete()
        c.selectPosition(root)

        # Run the test in the leo-editor directory (the parent of the .git directory).
        try:
            # Change directory.
            new_dir = g.finalize_join(g.app.loadDir, '..', '..')
            old_dir = os.getcwd()
            os.chdir(new_dir)

            # Run the command.
            expected_last_headline = 'git-diff-branches master devel'
            x.diff_two_branches(
                branch1='master',
                branch2='devel',
                fn='leo/core/leoGlobals.py'  # Don't use backslashes.
            )
            self.assertEqual(c.lastTopLevel().h, expected_last_headline)
            u.undo()
            self.assertEqual(c.lastTopLevel(), root)
            u.redo()
            self.assertEqual(c.lastTopLevel().h, expected_last_headline)
        finally:
            os.chdir(old_dir)
    #@-others

#@-others
#@-leo

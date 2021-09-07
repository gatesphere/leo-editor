# -*- coding: utf-8 -*-
#@+leo-ver=5-thin
#@+node:ekr.20210906141410.1: * @file ../unittests/core/test_leoUndo.py
#@@first
"""Tests of leoUndo.py"""

import textwrap
from leo.core import leoGlobals as g
from leo.core.leoTest2 import LeoUnitTest
assert g

#@+others
#@+node:ekr.20210906141410.2: ** class TestUndo (LeoUnitTest)
class TestUndo(LeoUnitTest):
    """
    Support @shadow-test nodes.

    These nodes should have two descendant nodes: 'before' and 'after'.
    """
    #@+others
    #@+node:ekr.20210906141410.9: *3* TestUndo.runTest (Test)
    def runTest(self, before, after, i, j, func):
        """TestUndo.runTest."""
        c, w = self.c, self.c.frame.body.wrapper
        # Restore section references.
        before = before.replace('> >', '>>').replace('< <', '<<')
        after = after.replace('> >', '>>').replace('< <', '<<')
        # Set the text and selection range.
        w.setAllText(before)
        w.setSelectionRange(i, j, insert=i)
        # Test.
        self.assertNotEqual(before, after)
        result = func()
        self.assertEqual(result, after, msg='before undo1')
        c.undoer.undo()
        self.assertEqual(result, before, msg='after undo1')
        c.undoer.redo()
        self.assertEqual(result, after, msg='after redo1')
        c.undoer.undo()
        self.assertEqual(result, before, msg='after undo2')
    #@+node:ekr.20210906172626.2: *3* TestUndo.test_addComments
    def test_addComments(self):
        c = self.c
        before = textwrap.dedent("""\
            @language python
            
            def addCommentTest():
            
                if 1:
                    a = 2
                    b = 3
            
                pass
    """)
        after = textwrap.dedent("""\
            @language python
            
            def addCommentTest():
            
                # if 1:
                    # a = 2
                    # b = 3
            
                pass
    """)
        i, j = 51, 80
        func = getattr(c, 'addComments')
        self.runTest(before, after, i, j, func)
    #@+node:ekr.20210906172626.3: *3* TestUndo.test_convertAllBlanks
    def test_convertAllBlanks(self):
        c = self.c
        before = textwrap.dedent("""\
            @tabwidth -4
            
            line 1
                line 2
                  line 3
            line4
    """)
        after = textwrap.dedent("""\
            @tabwidth -4
            
            line 1
            	line 2
            	  line 3
            line4
    """)
        i, j = 13, 51
        func = getattr(c, 'convertAllBlanks')
        self.runTest(before, after, i, j, func)
    #@+node:ekr.20210906172626.4: *3* TestUndo.test_convertAllTabs
    def test_convertAllTabs(self):
        c = self.c
        before = textwrap.dedent("""\
            @tabwidth -4
            
            line 1
            	line 2
            	  line 3
            line4
    """)
        after = textwrap.dedent("""\
            @tabwidth -4
            
            line 1
                line 2
                  line 3
            line4
    """)
        i, j = 13, 45
        func = getattr(c, 'convertAllTabs')
        self.runTest(before, after, i, j, func)
    #@+node:ekr.20210906172626.5: *3* TestUndo.test_convertBlanks
    def test_convertBlanks(self):
        c = self.c
        before = textwrap.dedent("""\
            @tabwidth -4
            
            line 1
                line 2
                  line 3
            line4
    """)
        after = textwrap.dedent("""\
            @tabwidth -4
            
            line 1
            	line 2
            	  line 3
            line4
    """)
        i, j = 13, 51
        func = getattr(c, 'convertBlanks')
        self.runTest(before, after, i, j, func)
    #@+node:ekr.20210906172626.6: *3* TestUndo.test_convertTabs
    def test_convertTabs(self):
        c = self.c
        before = textwrap.dedent("""\
            @tabwidth -4
            
            line 1
            	line 2
            	  line 3
            line4
    """)
        after = textwrap.dedent("""\
            @tabwidth -4
            
            line 1
                line 2
                  line 3
            line4
    """)
        i, j = 13, 45
        func = getattr(c, 'convertTabs')
        self.runTest(before, after, i, j, func)
    #@+node:ekr.20210906172626.7: *3* TestUndo.test_dedentBody
    def test_dedentBody(self):
        c = self.c
        before = textwrap.dedent("""\
            line 1
                line 2
                line 3
            line 4
    """)
        after = textwrap.dedent("""\
            line 1
            line 2
            line 3
            line 4
    """)
        i, j = 18, 34
        func = getattr(c, 'dedentBody')
        self.runTest(before, after, i, j, func)
    #@+node:ekr.20210906172626.8: *3* TestUndo.test_deleteComments
    def test_deleteComments(self):
        c = self.c
        before = textwrap.dedent("""\
            @language python
            
            def deleteCommentTest():
            
            #     if 1:
            #         a = 2
            #         b = 3
            
                pass
    """)
        after = textwrap.dedent("""\
            @language python
            
            def deleteCommentTest():
            
                if 1:
                    a = 2
                    b = 3
            
                pass
    """)
        i, j = 56, 89
        func = getattr(c, 'deleteComments')
        self.runTest(before, after, i, j, func)
    #@+node:ekr.20210906172626.9: *3* TestUndo.test_deleteComments 2
    def test_deleteComments_2(self):
        c = self.c
        before = textwrap.dedent("""\
            @language python
            
            def deleteCommentTest():
            
            #     if 1:
            #         a = 2
            #         b = 3
            
                # if 1:
                    # a = 2
                    # b = 3
            
                pass
    """)
        after = textwrap.dedent("""\
            @language python
            
            def deleteCommentTest():
            
                if 1:
                    a = 2
                    b = 3
            
                if 1:
                    a = 2
                    b = 3
            
                pass
    """)
        i, j = 56, 142
        func = getattr(c, 'deleteComments')
        self.runTest(before, after, i, j, func)
    #@+node:ekr.20210906172626.10: *3* TestUndo.test_extract_test1
    def test_extract_test1(self):
        c = self.c
        before = textwrap.dedent("""\
            before
                < < section > >
                sec line 1
                    sec line 2 indented
            sec line 3
            after
    """)
        after = textwrap.dedent("""\
            before
                < < section > >
            after
    """)
        i, j = 25, 85
        func = getattr(c, 'extract')
        self.runTest(before, after, i, j, func)
    #@+node:ekr.20210906172626.11: *3* TestUndo.test_extract_test2
    def test_extract_test2(self):
        c = self.c
        before = textwrap.dedent("""\
            before
                < < section > >
                sec line 1
                    sec line 2 indented
            sec line 3
            after
    """)
        after = textwrap.dedent("""\
            before
                < < section > >
                sec line 1
                    sec line 2 indented
            sec line 3
            after
    """)
        i, j = 25, 40
        func = getattr(c, 'extract')
        self.runTest(before, after, i, j, func)
    #@+node:ekr.20210906172626.12: *3* TestUndo.test_extract_test3
    def test_extract_test3(self):
        c = self.c
        before = textwrap.dedent("""\
            before
                < < section > >
                sec line 1
                    sec line 2 indented
            sec line 3
            after
    """)
        after = textwrap.dedent("""\
            before
                < < section > >
            after
    """)
        i, j = 25, 85
        func = getattr(c, 'extract')
        self.runTest(before, after, i, j, func)
    #@+node:ekr.20210906172626.13: *3* TestUndo.test_extract_test4
    def test_extract_test4(self):
        c = self.c
        before = textwrap.dedent("""\
            before
                < < section > >
                sec line 1
                    sec line 2 indented
            sec line 3
            after
    """)
        after = textwrap.dedent("""\
            before
                < < section > >
                sec line 1
                    sec line 2 indented
            sec line 3
            after
    """)
        i, j = 25, 40
        func = getattr(c, 'extract')
        self.runTest(before, after, i, j, func)
    #@+node:ekr.20210906172626.14: *3* TestUndo.test_line_to_headline
    def test_line_to_headline(self):
        c = self.c
        before = textwrap.dedent("""\
            before
            headline
            after
    """)
        after = textwrap.dedent("""\
            before
            after
    """)
        i, j = 16, 16
        func = getattr(c, 'line_to_headline')
        self.runTest(before, after, i, j, func)
    #@+node:ekr.20210906172626.15: *3* TestUndo.test_restore_marked_bits
    def test_restore_marked_bits(self):
        c, p = self.c, self.c.p
        # Test of #1694.
        u, w = c.undoer, c.frame.body.wrapper
        oldText = p.b
        newText = p.b + '\n#changed'
        try:
            for marked in (True, False):
                c.undoer.clearUndoState()  # Required.
                p.setMarked() if marked else p.clearMarked()
                oldMarked = p.isMarked()
                w.setAllText(newText)  # For the new assert in w.updateAfterTyping.
                u.setUndoTypingParams(p,
                    undo_type = 'typing',
                    oldText = oldText,
                    newText = newText,
                )
                u.undo()
                assert p.b == oldText, repr(p.b)
                assert p.isMarked() == oldMarked, ('fail 1', p.isMarked(), oldMarked)
                u.redo()
                assert p.b == newText, repr(p.b)
                assert p.isMarked() == oldMarked, ('fail 2', p.isMarked(), oldMarked)
        finally:
            p.b = oldText
            p.clearMarked()
    #@+node:ekr.20210906172626.16: *3* TestUndo.test_undo_editHeadline
    def test_undo_editHeadline(self):
        # Brian Theado.
        c, p = self.c, self.c.p
        node1 = p.insertAsLastChild()
        node2 = node1.insertAfter()
        node3 = node2.insertAfter()
        node1.h = 'node 1'
        node2.h = 'node 2'
        node3.h = 'node 3'
        assert [p.h for p in p.subtree()] == ['node 1', 'node 2', 'node 3']
        # Select 'node 1' and modify the headline as if a user did it
        c.undoer.clearUndoState()
        node1 = p.copy().moveToFirstChild()
        c.selectPosition(node1)
        c.editHeadline()
        w = c.frame.tree.edit_widget(node1)
        w.insert('1.0', 'changed - ')
        c.endEditing()
        assert [p.h for p in p.subtree()] == ['changed - node 1', 'node 2', 'node 3']
        # Move the selection and undo the headline change
        c.selectPosition(node1.copy().moveToNext())
        c.undoer.undo()
        # The undo should restore the 'node 1' headline string
        assert [p.h for p in p.subtree()] == ['node 1', 'node 2', 'node 3']
        # The undo should select the edited headline.
        assert c.p == node1, f"c.p: {c.p.h}, node1: {node1.h}"
    #@+node:ekr.20210906172626.17: *3* TestUndo.test_undo_redoGroup
    def test_undo_redoGroup(self):
        c, p = self.c, self.c.p
        # This test exposed a bug with redoGroup c.undoer.bead index off-by-one
        # The first c.pasteOutline() is there to setup the test cases, but it also serves
        # an important hidden purpose of adding undo state to the undo stack. Due
        # to the wrap-around nature of python index = -1, the original redoGroup code
        # worked fine when the undo group is the first one on the undo stack.
        # There are several commands which use undoGroup. The convertAllBlanks
        # was arbitrarily chosen to expose the bug.
        c.undoer.clearUndoState()
        original = p.copy().moveToFirstChild()
        c.selectPosition(original)
        c.copyOutline()
        # Do and undo
        c.pasteOutline()
        do_and_undo = original.copy().moveToNext()
        do_and_undo.h = "do and undo"
        c.convertAllBlanks()
        c.undoer.undo()
        assert original.b == do_and_undo.b, "Undo should restore to original"
        # Do
        c.pasteOutline()
        do = do_and_undo.copy().moveToNext()
        do.h = "do"
        c.convertAllBlanks()
        # Do, undo, redo
        c.pasteOutline()
        do_undo_redo = do.copy().moveToNext()
        do_undo_redo.h = "do, undo, redo"
        c.convertAllBlanks()
        c.undoer.undo()
        c.undoer.redo()
        assert do.b == do_undo_redo.b, "Redo should do the operation again"
    #@-others
#@-others
#@-leo

#@+leo-ver=5-thin
#@+node:ekr.20140723122936.18140: * @file ../plugins/importers/csharp.py
"""The @auto importer for the csharp language."""
from leo.plugins.importers.linescanner import Importer, scan_tuple
#@+others
#@+node:ekr.20161121200106.3: ** class Csharp_Importer
class Csharp_Importer(Importer):
    """The importer for the csharp lanuage."""

    def __init__(self, c, **kwargs):
        """Csharp_Importer.__init__"""
        super().__init__(
            c,
            language='csharp',
            state_class=Csharp_ScanState,
        )

    #@+others
    #@+node:ekr.20161121200106.5: *3* csharp.compute_headline
    def compute_headline(self, s):
        """Return a cleaned up headline s."""
        s = s.strip()
        if s.endswith('{'):
            s = s[:-1].strip()
        return s
    #@-others
#@+node:ekr.20161121200106.7: ** class class Csharp_ScanState
class Csharp_ScanState:
    """A class representing the state of the csharp line-oriented scan."""

    def __init__(self, d=None):
        """Csharp_ScanState.__init__"""
        if d:
            prev = d.get('prev')
            self.context = prev.context
            self.curlies = prev.curlies
        else:
            self.context = ''
            self.curlies = 0

    def __repr__(self):  # pragma: no cover
        """Csharp_ScanState.__repr__"""
        return "Csharp_ScanState context: %r curlies: %s" % (
            self.context, self.curlies)

    __str__ = __repr__

    #@+others
    #@+node:ekr.20220729152938.1: *3* csharp_state.in_context
    def in_context(self) -> bool:
        return bool(self.context)
    #@+node:ekr.20161121200106.8: *3* csharp_state.level
    def level(self) -> int:
        """Csharp_ScanState.level."""
        return self.curlies
    #@+node:ekr.20161121200106.9: *3* csharp_state.update
    def update(self, data: scan_tuple) -> int:
        """
        Csharp_ScanState.update: Update the state using given scan_tuple.
        """
        self.context = data.context
        self.curlies += data.delta_c
        return data.i
    #@-others

#@-others
importer_dict = {
    'func': Csharp_Importer.do_import(),
    'extensions': ['.cs', '.c#'],
}
#@@language python
#@@tabwidth -4
#@-leo

from __future__ import absolute_import

import sre_compile


pat = sre_compile.compile('')
Pattern = type(pat)
Match = type(pat.match(''))
Scanner = type(pat.scanner(''))
del pat

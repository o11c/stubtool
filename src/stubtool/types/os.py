from __future__ import absolute_import

import os

from ._util import PY35


if PY35:
    s = os.scandir('/')
    ScandirIterator = type(s)
    DirEntry = type(next(s))
    del s

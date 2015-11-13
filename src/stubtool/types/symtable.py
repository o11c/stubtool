from __future__ import absolute_import

import _symtable

from ._util import PY2, PY33


if PY2 or PY33:
    symtable_entry = type(_symtable.symtable('', '<string>', 'exec'))
else:
    symtable_entry = type(next(iter(_symtable.symtable('', '<string>', 'exec').values())))

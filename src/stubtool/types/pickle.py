from __future__ import absolute_import, unicode_literals

import io

from ._util import PY2, last


if PY2:
    import cPickle


    Pickler = type(cPickle.Pickler(io.StringIO()))
    Unpickler = type(cPickle.Unpickler(io.StringIO('')))
else:
    import _pickle
    import gc


    Pdata = type(last(gc.get_referents(_pickle.Unpickler(io.StringIO('')))))
    PicklerMemoProxy = type(_pickle.Pickler(io.StringIO()).memo)
    UnpicklerMemoProxy = type(_pickle.Unpickler(io.StringIO('')).memo)

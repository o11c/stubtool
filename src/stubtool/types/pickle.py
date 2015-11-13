from __future__ import absolute_import

import sys

from ._util import PY2, last


if PY2:
    import cPickle


    Pickler = type(cPickle.Pickler(sys.stdout))
    Unpickler = type(cPickle.Unpickler(sys.stdin))
else:
    import _pickle
    import gc


    Pdata = type(last(gc.get_referents(_pickle.Unpickler(sys.stdin))))
    PicklerMemoProxy = type(_pickle.Pickler(sys.stdout).memo)
    UnpicklerMemoProxy = type(_pickle.Unpickler(sys.stdin).memo)

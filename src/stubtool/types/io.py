from __future__ import absolute_import

import gc
import io

from ._util import PY3, PY33, only


if PY33:
    BytesIOBuffer = type(io.BytesIO().getbuffer().obj)
elif PY3:
    BytesIOBuffer = type(only(gc.get_referents(io.BytesIO().getbuffer())))

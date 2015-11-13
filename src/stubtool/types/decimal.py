from __future__ import absolute_import

import decimal

from ._util import PY33, former


ContextManager = type(decimal.localcontext())

if PY33:
    SignalDict = type(decimal.getcontext().flags)
    SignalDictMixin = former(SignalDict.__bases__)

from __future__ import absolute_import

import sys


version = sys.version_info[:2]

PY2 = version < (3, 0)
PY3 = version >= (3, 0)
PY32 = version >= (3, 2)
PY33 = version >= (3, 3)
PY34 = version >= (3, 4)
PY35 = version >= (3, 5)
PY36 = version >= (3, 6)
PY37 = version >= (3, 7)

def only(x):
    x, = x
    return x

def former(x):
    x, _ = x
    return x

def latter(x):
    _, x = x
    return x

def first(x):
    for x in x:
        return x
    assert False

def last(x):
    for y in x:
        pass
    return y

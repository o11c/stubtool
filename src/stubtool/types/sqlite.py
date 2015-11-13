from __future__ import absolute_import

import gc
import _sqlite3

from ._util import only


def _init():
    global sqlite3_node
    c = _sqlite3.Cache(lambda x: x)
    class Foo: pass
    sqlite3_node = type(only(only(gc.get_referrers(c.get(Foo()))).values()))


_init()

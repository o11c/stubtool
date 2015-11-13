from __future__ import absolute_import

import gc
import threading

from ._util import only, latter


def _init():
    global local_dummy
    loc = threading.local()
    e = only(latter(gc.get_referents(loc)))
    local_dummy = type(e())


_init()

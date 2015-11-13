from __future__ import absolute_import
from __future__ import print_function

import _ctypes
import ctypes
import gc
import weakref

from ._util import only


PyCArrayType = type(_ctypes.Array)
PyCFuncPtrType = type(_ctypes.CFuncPtr)
PyCPointerType = type(_ctypes._Pointer)
PyCSimpleType = type(_ctypes._SimpleCData)
PyCStructType = type(_ctypes.Structure)
UnionType = type(_ctypes.Union)

CData = only(_ctypes._SimpleCData.__bases__)
assert CData.__name__ == '_CData'
CArgObject = type(ctypes.byref(ctypes.c_int()))

def _init():
    global CField, StgDict, CThunkObject, DictRemover
    class Foo(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int)]
    CField = type(Foo.x)
    StgDict = type(only(gc.get_referents(Foo.__dict__)))

    CThunkObject = type(only(ctypes.CFUNCTYPE(None, *())(lambda: None)._objects.values()))

    Foo_array = Foo * 1
    proxy = None
    for key in gc.get_referrers(Foo):
        if key != (Foo, 1):
            continue
        for d in gc.get_referrers(key):
            if not isinstance(d, dict):
                continue
            proxy = d.get(key)
            if isinstance(proxy, weakref.CallableProxyType):
                break
    if not isinstance(proxy, weakref.CallableProxyType):
        raise ValueError('unable to find cached array proxy')
    DictRemover = type(only(gc.get_referents(proxy)))


_init()

# TODO try 32-bit and at least one big-endian arch
c_double_be = ctypes.c_double.__ctype_be__
c_float_be = ctypes.c_float.__ctype_be__
c_int_be = ctypes.c_int.__ctype_be__
c_long_be = ctypes.c_long.__ctype_be__
c_short_be = ctypes.c_short.__ctype_be__
c_uint_be = ctypes.c_uint.__ctype_be__
c_ulong_be = ctypes.c_ulong.__ctype_be__
c_ushort_be = ctypes.c_ushort.__ctype_be__

from __future__ import absolute_import

import _socket
import gc

import stubtool.name

from . import (
    bsddb,
    collections,
    crypt,
    csv,
    ctypes,
    curses,
    dbm,
    decimal,
    elementtree,
    encodings,
    hash,
    io,
    itertools,
    multiprocessing,
    os,
    ossaudiodev,
    pickle,
    pkg_resources,
    sched,
    select,
    sqlite,
    sre,
    ssl,
    symtable,
    sys,
    thread,
    tokenize,
    urlparse,
    xmlbuilder,
    zlib,
)
from ._util import PY2, PY3, PY33, PY35, only


CapsuleType = type(_socket.CAPI)
CellType = type(only((lambda x=0: lambda: x)().__closure__))
if PY3:
    ClassMethodDescriptorType = type(int.__dict__['from_bytes'])
DictProxyType = type(type.__dict__)
EllipsisType = type(Ellipsis)
MethodDescriptorType = type(dict.values)
MethodWrapperType = type(object.__call__)
NoneType = type(None)
NotImplementedType = type(NotImplemented)
QuitterType = type(exit)
WrapperDescriptorType = type(type.__call__)

if PY2:
    StrFormatterIteratorType = type(str()._formatter_parser())
    StrFieldNameIteratorType = type(str()._formatter_field_name_split()[1])
    UnicodeFormatterIteratorType = type(unicode()._formatter_parser())
    UnicodeFieldNameIteratorType = type(unicode()._formatter_field_name_split()[1])
if PY3:
    import _string


    StrFormatterIteratorType = type(_string.formatter_parser(str()))
    StrFieldNameIteratorType = type(_string.formatter_field_name_split(str())[1])

if PY3:
    ModuleDefType = only(stubtool.name.search_for_type('builtins.moduledef', object))
    StdPrinterType = only(stubtool.name.search_for_type('builtins.stderrprinter', object))

if PY33:
    ManagedBufferType = type(only(gc.get_referents(memoryview(b''))))

if PY35:
    exec('async def func(): pass')
    coro = func()
    wrapper = coro.__await__()
    coro.close()
    CoroutineWrapperType = type(wrapper)
    del func, coro, wrapper

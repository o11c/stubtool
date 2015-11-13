'''
Utilities for dealing with the name under which a type can be imported.

This currently handles all modules in the stdlib from:
- cpython 2.7 (possibly not all old-style classes)
- cpython 3.2
- cpython 3.3
- cpython 3.4
- cpython 3.5

and some third party modules:
- pkg_resources
- six
'''


import importlib
from six import PY2, PY34, class_types


# Modules that cannot safely be imported.
# If a value is present, that module must be imported first,
# and then the main module is safe.
# If the value is None, the module cannot be imported at all.
# Additionally, any module ending with `'.__main__'` is blacklisted.
module_blacklist = {
    # Recursive imports.
    '_LWPCookieJar': 'cookielib',
    '_MozillaCookieJar': 'cookielib',
    # Appears to inspect caller to set __module__
    '_io': 'io',
    # Runs code.
    '__hello__': None,
    '__phello__': None,
    'antigravity': None,
    'idlelib.ClassBrowser': None,
    'idlelib.PyShell': None,
    'idlelib.ScriptBinding': None,
    'idlelib.idle': None,
    'idlelib.testcode': None,
    'this': None,
    # Interferes with non-dummy modules.
    'dummy_thread': None,
    'dummy_threading': None,
    # Acts funny.
    'xxlimited': None,
    # Windows specific.
    'asyncio.windows_utils': None,
    'ctypes.wintypes': None,
    'encodings.cp65001': None,
    'encodings.mbcs': None,
}


# Modules that don't have their own name.
renamed_modules = {
    '__mp_main__': '__main__',
    '_collections_abc': 'collections.abc',
    '_decimal': 'decimal',
    '_frozen_importlib': 'importlib._bootstrap',
    '_frozen_importlib_external': 'importlib._bootstrap_external',
    '_io': '_io' if PY2 else 'io',
    '_pydecimal': 'decimal',
    'os.path': importlib.import_module('os.path').__name__,
    'xml.parsers.expat.errors': 'pyexpat.errors',
    'xml.parsers.expat.model': 'pyexpat.model',
}


# Packages to completely ignore the name for.
renamed_module_packages = {
    'email.',
    'six.moves.',
}


# Types that are known to be available under another name.
type_rename = {
    '<unknown>.Purpose': 'ssl.Purpose',
    '__builtin__.BlockingIOError': '_io.BlockingIOError',
    '__builtin__.CArgObject': 'stubtool.types.ctypes.CArgObject',
    '__builtin__.CommentProxy': 'stubtool.types.elementtree.CommentProxy',
    '__builtin__.DB': 'stubtool.types.bsddb.DB',
    '__builtin__.DBCursor': 'stubtool.types.bsddb.DBCursor',
    '__builtin__.DBEnv': 'stubtool.types.bsddb.DBEnv',
    '__builtin__.DBLock': 'stubtool.types.bsddb.DBLock',
    '__builtin__.DBLogCursor': 'stubtool.types.bsddb.DBLogCursor',
    '__builtin__.DBSequence': 'stubtool.types.bsddb.DBSequence',
    '__builtin__.DBSite': 'stubtool.types.bsddb.DBSite',
    '__builtin__.DBTxn': 'stubtool.types.bsddb.DBTxn',
    '__builtin__.Element': 'stubtool.types.elementtree.cElement',
    '__builtin__.ElementTree': '_elementtree.ElementTree',
    '__builtin__.EncodingMap': 'stubtool.types.encodings.EncodingMap',
    '__builtin__.MultibyteCodec': 'stubtool.types.encodings.MultibyteCodec',
    '__builtin__.MultibyteIncrementalDecoder': '_multibytecodec.MultibyteIncrementalDecoder',
    '__builtin__.MultibyteIncrementalEncoder': '_multibytecodec.MultibyteIncrementalEncoder',
    '__builtin__.MultibyteStreamReader': '_multibytecodec.MultibyteStreamReader',
    '__builtin__.MultibyteStreamWriter': '_multibytecodec.MultibyteStreamWriter',
    '__builtin__.NoneType': 'stubtool.types.NoneType',
    '__builtin__.NotImplementedType': 'stubtool.types.NotImplementedType',
    '__builtin__.PIProxy': 'stubtool.types.elementtree.PIProxy',
    '__builtin__.PyCapsule': 'stubtool.types.CapsuleType',
    '__builtin__.StgDict': 'stubtool.types.ctypes.StgDict',
    '__builtin__.Struct': '_struct.Struct',
    '__builtin__.builtin_function_or_method': 'types.BuiltinFunctionType',
    '__builtin__.bytearray_iterator': 'stubtool.types.collections.bytearray_iterator',
    '__builtin__.callable-iterator': 'stubtool.types.collections.callable_iterator',
    '__builtin__.cell': 'stubtool.types.CellType',
    '__builtin__.classobj': 'types.ClassType',
    '__builtin__.code': 'types.CodeType',
    '__builtin__.deque_iterator': 'stubtool.types.collections.deque_iterator',
    '__builtin__.deque_reverse_iterator': 'stubtool.types.collections.deque_reverse_iterator',
    '__builtin__.dict_items': 'stubtool.types.collections.dict_items',
    '__builtin__.dict_keys': 'stubtool.types.collections.dict_keys',
    '__builtin__.dict_values': 'stubtool.types.collections.dict_values',
    '__builtin__.dictionary-itemiterator': 'stubtool.types.collections.dict_itemiterator',
    '__builtin__.dictionary-keyiterator': 'stubtool.types.collections.dict_keyiterator',
    '__builtin__.dictionary-valueiterator': 'stubtool.types.collections.dict_valueiterator',
    '__builtin__.dictproxy': 'stubtool.types.DictProxyType',
    '__builtin__.ellipsis': 'stubtool.types.EllipsisType',
    '__builtin__.fieldnameiterator': ['stubtool.types.StrFieldNameIteratorType', 'stubtool.types.UnicodeFieldNameIteratorType'],
    '__builtin__.formatteriterator': ['stubtool.types.StrFormatterIteratorType', 'stubtool.types.UnicodeFormatterIteratorType'],
    '__builtin__.frame': 'types.FrameType',
    '__builtin__.function': 'types.FunctionType',
    '__builtin__.generator': 'types.GeneratorType',
    '__builtin__.getset_descriptor': 'types.GetSetDescriptorType',
    '__builtin__.instance': 'types.InstanceType',
    '__builtin__.instancemethod': 'types.MethodType',
    '__builtin__.iterator': 'stubtool.types.collections.index_iterator',
    '__builtin__.iterparse': '_elementtree.iterparse',
    '__builtin__.listiterator': 'stubtool.types.collections.list_iterator',
    '__builtin__.listreverseiterator': 'stubtool.types.collections.list_reverseiterator',
    '__builtin__.member_descriptor': 'types.MemberDescriptorType',
    '__builtin__.method-wrapper': 'stubtool.types.MethodWrapperType',
    '__builtin__.method_descriptor': 'stubtool.types.MethodDescriptorType',
    '__builtin__.module': 'types.ModuleType',
    '__builtin__.rangeiterator': 'stubtool.types.collections.range_iterator',
    '__builtin__.setiterator': 'stubtool.types.collections.set_iterator',
    '__builtin__.sqlite3Node': 'stubtool.types.sqlite.sqlite3_node',
    '__builtin__.symtable entry': 'stubtool.types.symtable.symtable_entry',
    '__builtin__.test_structmembersType': '_testcapi._test_structmembersType',
    '__builtin__.tkapp': '_tkinter.TkappType',
    '__builtin__.tktimertoken': '_tkinter.TkttType',
    '__builtin__.traceback': 'types.TracebackType',
    '__builtin__.tupleiterator': 'stubtool.types.collections.tuple_iterator',
    '__builtin__.weakcallableproxy': '_weakref.CallableProxyType',
    '__builtin__.weakproxy': '_weakref.ProxyType',
    '__builtin__.weakref': '_weakref.ReferenceType',
    '__builtin__.wrapper_descriptor': 'stubtool.types.WrapperDescriptorType',
    '_csv.reader': 'stubtool.types.csv.reader',
    '_csv.writer': 'stubtool.types.csv.writer',
    '_ctypes.CField': 'stubtool.types.ctypes.CField',
    '_ctypes.CThunkObject': 'stubtool.types.ctypes.CThunkObject',
    '_ctypes.DictRemover': 'stubtool.types.ctypes.DictRemover',
    '_ctypes.PyCArrayType': 'stubtool.types.ctypes.PyCArrayType',
    '_ctypes.PyCFuncPtr': '_ctypes.CFuncPtr',
    '_ctypes.PyCFuncPtrType': 'stubtool.types.ctypes.PyCFuncPtrType',
    '_ctypes.PyCPointerType': 'stubtool.types.ctypes.PyCPointerType',
    '_ctypes.PyCSimpleType': 'stubtool.types.ctypes.PyCSimpleType',
    '_ctypes.PyCStructType': 'stubtool.types.ctypes.PyCStructType',
    '_ctypes.UnionType': 'stubtool.types.ctypes.UnionType',
    '_ctypes._CData': 'stubtool.types.ctypes.CData',
    '_curses.curses window': 'stubtool.types.curses.curses_window',
    '_curses_panel.curses panel': 'stubtool.types.curses.curses_panel',
    '_dbm.dbm': 'stubtool.types.dbm.ndbm',
    '_elementtree._element_iterator': 'stubtool.types.elementtree.element_iterator',
    '_gdbm.gdbm': 'stubtool.types.dbm.gdbm',
    '_hashlib.HASH': 'stubtool.types.hash.HASH',
    '_io._BytesIOBuffer': 'stubtool.types.io.BytesIOBuffer',
    '_json.Encoder': '_json.make_encoder',
    '_json.Scanner': '_json.make_scanner',
    '_md5.md5': 'stubtool.types.hash.md5',
    '_pickle.Pdata': 'stubtool.types.pickle.Pdata',
    '_pickle.PicklerMemoProxy': 'stubtool.types.pickle.PicklerMemoProxy',
    '_pickle.UnpicklerMemoProxy': 'stubtool.types.pickle.UnpicklerMemoProxy',
    '_sha.sha': 'stubtool.types.hash.sha1',
    '_sha1.sha1': 'stubtool.types.hash.sha1',
    '_sha256.sha224': 'stubtool.types.hash.sha224',
    '_sha256.sha256': 'stubtool.types.hash.sha256',
    '_sha512.sha384': 'stubtool.types.hash.sha384',
    '_sha512.sha512': 'stubtool.types.hash.sha512',
    '_sre.SRE_Match': 'stubtool.types.sre.Match',
    '_sre.SRE_Pattern': 'stubtool.types.sre.Pattern',
    '_sre.SRE_Scanner': 'stubtool.types.sre.Scanner',
    '_testimportexec.Example': '_testmultiphase.Example',
    '_testimportexec.Str': '_testmultiphase.Str',
    '_testimportexec.error': '_testmultiphase.error',
    '_thread._localdummy': 'stubtool.types.thread.local_dummy',
    '_thread.lock': '_thread.LockType',
    '_tkinter.tkapp': '_tkinter.TkappType',
    '_tkinter.tktimertoken': '_tkinter.TkttType',
    'abc.SignalDict': 'stubtool.types.decimal.SignalDict',
    'anydbm.error': 'stubtool.types.dbm.error',
    'argparse._ChoicesPseudoAction': 'argparse._SubParsersAction._ChoicesPseudoAction',
    'argparse._Section': 'argparse.HelpFormatter._Section',
    'builtins.BlockingIOError': '_io.BlockingIOError',
    'builtins.CArgObject': 'stubtool.types.ctypes.CArgObject',
    'builtins.CommentProxy': 'stubtool.types.elementtree.CommentProxy',
    'builtins.Element': 'stubtool.types.elementtree.cElement',
    'builtins.ElementTree': '_elementtree.ElementTree',
    'builtins.EncodingMap': 'stubtool.types.encodings.EncodingMap',
    'builtins.MultibyteCodec': 'stubtool.types.encodings.MultibyteCodec',
    'builtins.MultibyteIncrementalDecoder': '_multibytecodec.MultibyteIncrementalDecoder',
    'builtins.MultibyteIncrementalEncoder': '_multibytecodec.MultibyteIncrementalEncoder',
    'builtins.MultibyteStreamReader': '_multibytecodec.MultibyteStreamReader',
    'builtins.MultibyteStreamWriter': '_multibytecodec.MultibyteStreamWriter',
    'builtins.NoneType': 'stubtool.types.NoneType',
    'builtins.NotImplementedType': 'builtins.NotImplemented.__class__',
    'builtins.PIProxy': 'stubtool.types.elementtree.PIProxy',
    'builtins.PyCapsule': 'stubtool.types.CapsuleType',
    'builtins.StgDict': 'stubtool.types.ctypes.StgDict',
    'builtins.Struct': '_struct.Struct',
    'builtins.TreeBuilder': 'stubtool.types.elementtree.TreeBuilder',
    'builtins.XMLParser': 'stubtool.types.elementtree.XMLParser',
    'builtins.awaitType': '_testcapi.awaitType',
    'builtins.builtin_function_or_method': 'types.BuiltinFunctionType',
    'builtins.bytearray_iterator': 'stubtool.types.collections.bytearray_iterator',
    'builtins.bytes_iterator': 'stubtool.types.collections.bytes_iterator',
    'builtins.callable_iterator': 'stubtool.types.collections.callable_iterator',
    'builtins.cell': 'stubtool.types.CellType',
    'builtins.classmethod_descriptor': 'stubtool.types.ClassMethodDescriptorType',
    'builtins.code': 'types.CodeType',
    'builtins.coroutine': 'types.CoroutineType',
    'builtins.coroutine_wrapper': 'stubtool.types.CoroutineWrapperType',
    'builtins.deque_iterator': 'stubtool.types.collections.deque_iterator',
    'builtins.deque_reverse_iterator': 'stubtool.types.collections.deque_reverse_iterator',
    'builtins.dict_itemiterator': 'stubtool.types.collections.dict_itemiterator',
    'builtins.dict_items': 'stubtool.types.collections.dict_items',
    'builtins.dict_keyiterator': 'stubtool.types.collections.dict_keyiterator',
    'builtins.dict_keys': 'stubtool.types.collections.dict_keys',
    'builtins.dict_proxy': 'stubtool.types.DictProxyType',
    'builtins.dict_valueiterator': 'stubtool.types.collections.dict_valueiterator',
    'builtins.dict_values': 'stubtool.types.collections.dict_values',
    'builtins.ellipsis': 'stubtool.types.EllipsisType',
    'builtins.fieldnameiterator': 'stubtool.types.StrFieldNameIteratorType',
    'builtins.formatteriterator': 'stubtool.types.StrFormatterIteratorType',
    'builtins.frame': 'types.FrameType',
    'builtins.function': 'types.FunctionType',
    'builtins.generator': 'types.GeneratorType',
    'builtins.getset_descriptor': 'types.GetSetDescriptorType',
    'builtins.instancemethod': '_testcapi.instancemethod',
    'builtins.iterator': 'stubtool.types.collections.index_iterator',
    'builtins.iterparse': '_elementtree.iterparse',
    'builtins.list_iterator': 'stubtool.types.collections.list_iterator',
    'builtins.list_reverseiterator': 'stubtool.types.collections.list_reverseiterator',
    'builtins.longrange_iterator': 'stubtool.types.collections.longrange_iterator',
    'builtins.managedbuffer': 'stubtool.types.ManagedBufferType',
    'builtins.mappingproxy': 'stubtool.types.DictProxyType',
    'builtins.matmulType': '_testcapi.matmulType',
    'builtins.member_descriptor': 'types.MemberDescriptorType',
    'builtins.method': 'types.MethodType',
    'builtins.method-wrapper': 'stubtool.types.MethodWrapperType',
    'builtins.method_descriptor': 'stubtool.types.MethodDescriptorType',
    'builtins.module': 'types.ModuleType',
    'builtins.moduledef': 'stubtool.types.ModuleDefType',
    'builtins.namespace': 'types.SimpleNamespace',
    'builtins.ndarray': '_testbuffer.ndarray',
    'builtins.odict_items': 'stubtool.types.collections.odict_items',
    'builtins.odict_iterator': 'stubtool.types.collections.odict_iterator',
    'builtins.odict_keys': 'stubtool.types.collections.odict_keys',
    'builtins.odict_values': 'stubtool.types.collections.odict_values',
    'builtins.range_iterator': 'stubtool.types.collections.range_iterator',
    'builtins.set_iterator': 'stubtool.types.collections.set_iterator',
    'builtins.sqlite3Node': 'stubtool.types.sqlite.sqlite3_node',
    'builtins.staticarray': '_testbuffer.staticarray',
    'builtins.stderrprinter': 'stubtool.types.StdPrinterType',
    'builtins.str_iterator': 'stubtool.types.collections.str_iterator',
    'builtins.symtable entry': 'stubtool.types.symtable.symtable_entry',
    'builtins.test_structmembersType': '_testcapi._test_structmembersType',
    'builtins.traceback': 'types.TracebackType',
    'builtins.tuple_iterator': 'stubtool.types.collections.tuple_iterator',
    'builtins.weakcallableproxy': '_weakref.CallableProxyType',
    'builtins.weakproxy': '_weakref.ProxyType',
    'builtins.weakref': '_weakref.ReferenceType',
    'builtins.wrapper_descriptor': 'stubtool.types.WrapperDescriptorType',
    'cElementTree.ParseError': '_elementtree.ParseError',
    'cPickle.Pickler': 'stubtool.types.pickle.Pickler',
    'cPickle.Unpickler': 'stubtool.types.pickle.Unpickler',
    'cStringIO.StringI': 'cStringIO.InputType',
    'cStringIO.StringO': 'cStringIO.OutputType',
    'crypt._Method': ['crypt._Method', 'stubtool.types.crypt.BaseMethod'],
    'ctypes.c_double_be': 'stubtool.types.ctypes.c_double_be',
    'ctypes.c_float_be': 'stubtool.types.ctypes.c_float_be',
    'ctypes.c_int_be': 'stubtool.types.ctypes.c_int_be',
    'ctypes.c_long_be': 'stubtool.types.ctypes.c_long_be',
    'ctypes.c_short_be': 'stubtool.types.ctypes.c_short_be',
    'ctypes.c_uint_be': 'stubtool.types.ctypes.c_uint_be',
    'ctypes.c_ulong_be': 'stubtool.types.ctypes.c_ulong_be',
    'ctypes.c_ushort_be': 'stubtool.types.ctypes.c_ushort_be',
    'dbm.error': ['dbm.error', 'stubtool.types.dbm.error'],
    'decimal.Clamped': ['decimal.Clamped', '_pydecimal.Clamped'],
    'decimal.Context': ['decimal.Context', '_pydecimal.Context'],
    'decimal.ContextManager': 'stubtool.types.decimal.ContextManager',
    'decimal.ConversionSyntax': ['decimal.ConversionSyntax', '_pydecimal.ConversionSyntax'],
    'decimal.Decimal': ['decimal.Decimal', '_pydecimal.Decimal'],
    'decimal.DecimalException': ['decimal.DecimalException', '_pydecimal.DecimalException'],
    'decimal.DecimalTuple': ['decimal.DecimalTuple', '_pydecimal.DecimalTuple'],
    'decimal.DivisionByZero': ['decimal.DivisionByZero', '_pydecimal.DivisionByZero'],
    'decimal.DivisionImpossible': ['decimal.DivisionImpossible', '_pydecimal.DivisionImpossible'],
    'decimal.DivisionUndefined': ['decimal.DivisionUndefined', '_pydecimal.DivisionUndefined'],
    'decimal.FloatOperation': ['decimal.FloatOperation', '_pydecimal.FloatOperation'],
    'decimal.Inexact': ['decimal.Inexact', '_pydecimal.Inexact'],
    'decimal.InvalidContext': ['decimal.InvalidContext', '_pydecimal.InvalidContext'],
    'decimal.InvalidOperation': ['decimal.InvalidOperation', '_pydecimal.InvalidOperation'],
    'decimal.Overflow': ['decimal.Overflow', '_pydecimal.Overflow'],
    'decimal.Rounded': ['decimal.Rounded', '_pydecimal.Rounded'],
    'decimal.SignalDictMixin': 'stubtool.types.decimal.SignalDictMixin',
    'decimal.Subnormal': ['decimal.Subnormal', '_pydecimal.Subnormal'],
    'decimal.Underflow': ['decimal.Underflow', '_pydecimal.Underflow'],
    'decimal._ContextManager': ['decimal._ContextManager', '_pydecimal._ContextManager'],
    'decimal._Log10Memoize': ['decimal._Log10Memoize', '_pydecimal._Log10Memoize'],
    'decimal._WorkRep': ['decimal._WorkRep', '_pydecimal._WorkRep'],
    'functools.CacheInfo': 'functools._CacheInfo',
    'imaplib.abort': 'imaplib.IMAP4.abort',
    'imaplib.error': 'imaplib.IMAP4.error',
    'imaplib.readonly': 'imaplib.IMAP4.readonly',
    'importlib._bootstrap.DecimalTuple': '_decimal.DecimalTuple',
    'itertools._grouper': 'stubtool.types.itertools.grouper',
    'itertools.tee': 'stubtool.types.itertools.tee',
    'itertools.tee_dataobject': 'stubtool.types.itertools.tee_dataobject',
    'multiprocessing.managers.PoolProxy': ['multiprocessing.managers.PoolProxy', 'multiprocessing.managers.BasePoolProxy'],
    'multiprocessing.process._MainProcess': 'stubtool.types.multiprocessing.MainProcess',
    'ossaudiodev.oss_audio_device': 'stubtool.types.ossaudiodev.oss_audio_device',
    'ossaudiodev.oss_mixer_device': 'stubtool.types.ossaudiodev.oss_mixer_device',
    'parser.st': ['parser.ASTType', 'parser.STType'],
    'pkg_resources._vendor.packaging._structures.Infinity': 'stubtool.types.pkg_resources.Infinity',
    'pkg_resources._vendor.packaging._structures.NegativeInfinity': 'stubtool.types.pkg_resources.NegativeInfinity',
    'pkg_resources.manifest_mod': 'pkg_resources.MemoizedZipManifests.manifest_mod',
    'posix.DirEntry': 'stubtool.types.os.DirEntry',
    'posix.ScandirIterator': 'stubtool.types.os.ScandirIterator',
    'profile.fake_code': 'profile.Profile.fake_code',
    'profile.fake_frame': 'profile.Profile.fake_frame',
    'pyexpat.xmlparser': 'pyexpat.XMLParserType',
    'sched.Event': ['sched.Event', 'stubtool.types.sched.BaseEvent'],
    'select.poll': 'stubtool.types.select.poll',
    'shutil.usage': 'shutil._ntuple_diskusage',
    'site.Quitter': 'stubtool.types.QuitterType',
    'site.setquit.<locals>.Quitter': 'stubtool.types.QuitterType',
    'ssl._ASN1Object': ['ssl._ASN1Object', 'stubtool.types.ssl.BaseASN1Object'],
    'sys.flags': 'stubtool.types.sys.FlagsType',
    'sys.float_info': 'stubtool.types.sys.FloatInfoType',
    'sys.hash_info': 'stubtool.types.sys.HashInfoType',
    'sys.int_info': 'stubtool.types.sys.IntInfoType',
    'sys.long_info': 'stubtool.types.sys.LongInfoType',
    'sys.thread_info': 'stubtool.types.sys.ThreadInfoType',
    'sys.version_info': 'stubtool.types.sys.VersionInfoType',
    'thread.lock': 'thread.LockType',
    'tokenize.TokenInfo': ['tokenize.TokenInfo', 'stubtool.types.tokenize.BaseTokenInfo'],
    'typing.typing.io': 'typing.io',
    'typing.typing.re': 'typing.re',
    'unittest.util.Mismatch': 'unittest.util._Mismatch',
    'urllib.parse.DefragResult': ['urllib.parse.DefragResult', 'urllib.parse._DefragResultBase'],
    'urllib.parse.ParseResult': ['urllib.parse.ParseResult', 'urllib.parse._ParseResultBase'],
    'urllib.parse.SplitResult': ['urllib.parse.SplitResult', 'urllib.parse._SplitResultBase'],
    'urlparse.ParseResult': ['urlparse.ParseResult', 'stubtool.types.urlparse.BaseParseResult'],
    'urlparse.SplitResult': ['urlparse.SplitResult', 'stubtool.types.urlparse.BaseSplitResult'],
    'xml.dom.xmlbuilder._AsyncDeprecatedProperty': 'stubtool.types.xmlbuilder.AsyncDeprecatedProperty',
    'xml.etree.ElementTree.Element': ['xml.etree.ElementTree.Element', '_elementtree.Element', 'xml.etree.ElementTree._Element_Py', 'xml.etree.ElementTree._Element'],
    'xml.etree.ElementTree.ElementTree': ['xml.etree.ElementTree.ElementTree', 'stubtool.types.elementtree.BaseElementTree'],
    'zlib.Compress': 'stubtool.types.zlib.Compress',
    'zlib.Decompress': 'stubtool.types.zlib.Decompress',
}


# Types that exist, but don't have any known name.
# This is often generated by looking at `object.__subclasses__()`,
# but also occasionally for module-level objects created from <locals>.
known_locals, known_unknown = {
    # Types that have been verified as using <locals>.
    'ctypes.CDLL.__init__.<locals>._FuncPtr': ['_ctypes.PyCFuncPtr'],
    'ctypes.CFUNCTYPE.<locals>.CFunctionType': ['_ctypes.PyCFuncPtr'],
    'ctypes.CFunctionType': ['_ctypes.PyCFuncPtr'],
    'ctypes.PYFUNCTYPE.<locals>.CFunctionType': ['_ctypes.PyCFuncPtr'],
    'ctypes._FuncPtr': ['_ctypes.PyCFuncPtr'],
}, {
    # Types that still require further investigation.
    #
    # I have already checked that none of these:
    #   * is a top-level entity of any module under any name.
    #   * is the type of any top-level entity of any module.
    #   * has any subclasses that is known.
}


def import_module(name):
    '''
    Import a module, but only if it is not in the blacklist.

    Also verify that its name matches what is expected.
    '''
    if name.endswith('.__init__'):
        raise ImportError('Module %r cannot be safely imported' % name)
    if name.endswith('.__main__'):
        raise ImportError('Module %r cannot be safely imported' % name)
    black = module_blacklist.get(name, Ellipsis)
    if black is None:
        raise ImportError('Module %r cannot be safely imported' % name)
    if black is not Ellipsis:
        importlib.import_module(black)
    rv = importlib.import_module(name)
    if not any(name.startswith(n) for n in renamed_module_packages):
        assert rv.__name__ == renamed_modules.get(name, name), (name, rv.__name__)
    return rv


def get_object(name):
    '''
    Given a dotted name, import any necessary modules, then call getattr.
    '''
    bits = name.split('.')
    try:
        for i, bit in enumerate(bits, 0):
            mod = import_module('.'.join(bits[:i + 1]))
    except ImportError:
        if i == 0:
            raise
    else:
        i += 1
    obj = mod
    for i, bit in enumerate(bits[i:], i):
        obj = getattr(obj, bit)
    return obj


def get_declared_name(typ):
    '''
    Return a class's `__module__'.'__name__`.

    Note that __qualname__ will be used if available, but only if
    it ends with `'.'__name__`.
    '''
    assert isinstance(typ, class_types)
    mod = typ.__module__
    if mod == 'exceptions':
        mod = '__builtin__'
    name = typ.__name__
    qualname = getattr(typ, '__qualname__', '')
    if qualname.endswith('.' + name):
        name = qualname
    return '%s.%s' % (mod, name)


def is_generic_instance(elem):
    if getattr(elem, '__origin__', None):
        # Normal generic
        return True
    if getattr(elem, '__union_params__', None):
        # Union
        return True
    import ctypes
    if issubclass(elem, ctypes._Pointer) and elem is not ctypes._Pointer:
        # ctypes.POINTER(elem._type_)
        return True
    return False


def get_importable_name(typ):
    '''
    Get the name under which a type may be imported.

    Many C classes, and some Python classes, are not actually present
    in the module that they declare in their __module__ attribute, or
    are only available under a different name. Here, such objects are
    referred to as "deleted".

    An attempt is made to use a hard-coded mapping to fix this.
    If, after that, the type object is not found under that name,
    an exception will be raised.
    '''
    name = get_declared_name(typ)
    if is_generic_instance(typ):
        raise TypeError('generic: %r' % typ)
    if name in known_locals:
        raise TypeError('local: %r' % typ)
    names = type_rename.get(name, name)
    if isinstance(names, list):
        for name in names:
            try:
                obj = get_object(name)
            except (ImportError, AttributeError):
                continue
            if typ is obj:
                return name
        raise TypeError('no match: %r' % names)
    else:
        name = names
    try:
        obj = get_object(name)
    except (ImportError, AttributeError):
        actual_bases = [get_declared_name(b) for b in typ.__bases__]
        expected_bases = known_unknown.get(name, None)
        if expected_bases is None:
            raise TypeError('unknown unknown: %s: %r' % (name, actual_bases))
        if expected_bases == []:
            expected_bases = ['builtins.object']
        if PY2:
            expected_bases = [b.replace('builtins.', '__builtin__.') for b in expected_bases]
        assert actual_bases == expected_bases, (name, actual_bases)
        raise TypeError('known unknown: %s' % name)
    else:
        if obj is not typ:
            raise TypeError('mismatched object: %s' % name)
    if name in known_unknown:
        raise TypeError('unknown known: %s' % name)
    return name


def get_stub_name(typ):
    '''
    Get the name that should be used for stubs.

    This is likely to differ from the importable name for generics.
    '''
    return get_importable_name(typ)


def search_for_type(name, base):
    '''
    Search for a type by name, given a base class.

    This is mostly useful for hunting down unknowns for debugging.
    '''
    rv = []
    for typ in type(base).__subclasses__(base):
        if name == get_declared_name(typ):
            rv.append(typ)
    return rv

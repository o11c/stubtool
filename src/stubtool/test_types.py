from __future__ import print_function

import six
import sys


import stubtool.name
from stubtool.name import get_declared_name, known_unknown


all_modules = list(sys.builtin_module_names) + '''
BaseHTTPServer
Bastion
CDROM
CGIHTTPServer
Canvas
ConfigParser
Cookie
DLFCN
Dialog
DocXMLRPCServer
FileDialog
FixTk
HTMLParser
IN
MimeWriter
Queue
ScrolledText
SimpleDialog
SimpleHTTPServer
SimpleXMLRPCServer
SocketServer
StringIO
TYPES
Tix
Tkconstants
Tkdnd
Tkinter
UserDict
UserList
UserString
_LWPCookieJar
_MozillaCookieJar
__future__
_abcoll
_bootlocale
_bsddb
_bz2
_codecs_cn
_codecs_hk
_codecs_iso2022
_codecs_jp
_codecs_kr
_codecs_tw
_collections_abc
_compat_pickle
_compression
_crypt
_csv
_ctypes
_ctypes_test
_curses
_curses_panel
_dbm
_decimal
_dummy_thread
_elementtree
_gdbm
_hashlib
_hotshot
_json
_lsprof
_lzma
_markupbase
_multibytecodec
_multiprocessing
_opcode
_osx_support
_pydecimal
_pyio
_pytest
_pytest._argcomplete
_pytest._pluggy
_pytest.assertion
_pytest.assertion.newinterpret
_pytest.assertion.oldinterpret
_pytest.assertion.reinterpret
_pytest.assertion.rewrite
_pytest.assertion.util
_pytest.cacheprovider
_pytest.capture
_pytest.config
_pytest.doctest
_pytest.genscript
_pytest.helpconfig
_pytest.hookspec
_pytest.junitxml
_pytest.main
_pytest.mark
_pytest.monkeypatch
_pytest.nose
_pytest.pastebin
_pytest.pdb
_pytest.pytester
_pytest.python
_pytest.recwarn
_pytest.resultlog
_pytest.runner
_pytest.skipping
_pytest.standalonetemplate
_pytest.terminal
_pytest.tmpdir
_pytest.unittest
_pytest.vendored_packages
_pytest.vendored_packages.pluggy
_sitebuiltins
_sqlite3
_ssl
_strptime
_sysconfigdata
_sysconfigdata_d
_sysconfigdata_dm
_sysconfigdata_m
_sysconfigdata_nd
_testbuffer
_testcapi
_testimportmultiple
_testmultiphase
_threading_local
_tkinter
_weakrefset
abc
aifc
anydbm
argparse
ast
asynchat
asyncio
asyncio.base_events
asyncio.base_subprocess
asyncio.compat
asyncio.constants
asyncio.coroutines
asyncio.events
asyncio.futures
asyncio.locks
asyncio.log
asyncio.proactor_events
asyncio.protocols
asyncio.queues
asyncio.selector_events
asyncio.sslproto
asyncio.streams
asyncio.subprocess
asyncio.tasks
asyncio.test_utils
asyncio.transports
asyncio.unix_events
asyncio.windows_events
asyncore
atexit
audiodev
audioop
base64
bdb
binhex
bisect
bsddb
bsddb.db
bsddb.dbobj
bsddb.dbrecio
bsddb.dbshelve
bsddb.dbtables
bsddb.dbutils
bz2
cProfile
calendar
cgi
cgitb
chunk
cmath
cmd
code
codecs
codeop
collections
collections.abc
colorsys
commands
compileall
compiler
compiler.ast
compiler.consts
compiler.future
compiler.misc
compiler.pyassem
compiler.pycodegen
compiler.symbols
compiler.syntax
compiler.transformer
compiler.visitor
concurrent
concurrent.futures
concurrent.futures._base
concurrent.futures.process
concurrent.futures.thread
configparser
contextlib
cookielib
copy
copy_reg
copyreg
crypt
csv
ctypes
ctypes._endian
ctypes.util
curses
curses.ascii
curses.has_key
curses.panel
curses.textpad
curses.wrapper
datetime
dbhash
dbm
dbm.dumb
dbm.gnu
dbm.ndbm
decimal
difflib
dircache
dis
distutils
distutils._msvccompiler
distutils.archive_util
distutils.bcppcompiler
distutils.ccompiler
distutils.cmd
distutils.command
distutils.command.bdist
distutils.command.bdist_dumb
distutils.command.bdist_msi
distutils.command.bdist_rpm
distutils.command.bdist_wininst
distutils.command.build
distutils.command.build_clib
distutils.command.build_ext
distutils.command.build_py
distutils.command.build_scripts
distutils.command.check
distutils.command.clean
distutils.command.config
distutils.command.install
distutils.command.install_data
distutils.command.install_egg_info
distutils.command.install_headers
distutils.command.install_lib
distutils.command.install_scripts
distutils.command.register
distutils.command.sdist
distutils.command.upload
distutils.config
distutils.core
distutils.cygwinccompiler
distutils.debug
distutils.dep_util
distutils.dir_util
distutils.dist
distutils.emxccompiler
distutils.errors
distutils.extension
distutils.fancy_getopt
distutils.file_util
distutils.filelist
distutils.log
distutils.msvc9compiler
distutils.msvccompiler
distutils.spawn
distutils.sysconfig
distutils.text_file
distutils.unixccompiler
distutils.util
distutils.version
distutils.versionpredicate
doctest
dumbdbm
email
email._encoded_words
email._header_value_parser
email._parseaddr
email._policybase
email.base64mime
email.charset
email.contentmanager
email.encoders
email.errors
email.feedparser
email.generator
email.header
email.headerregistry
email.iterators
email.message
email.mime
email.mime.application
email.mime.audio
email.mime.base
email.mime.image
email.mime.message
email.mime.multipart
email.mime.nonmultipart
email.mime.text
email.parser
email.policy
email.quoprimime
email.utils
encodings
encodings.aliases
encodings.ascii
encodings.base64_codec
encodings.big5
encodings.big5hkscs
encodings.bz2_codec
encodings.charmap
encodings.cp037
encodings.cp1006
encodings.cp1026
encodings.cp1125
encodings.cp1140
encodings.cp1250
encodings.cp1251
encodings.cp1252
encodings.cp1253
encodings.cp1254
encodings.cp1255
encodings.cp1256
encodings.cp1257
encodings.cp1258
encodings.cp273
encodings.cp424
encodings.cp437
encodings.cp500
encodings.cp720
encodings.cp737
encodings.cp775
encodings.cp850
encodings.cp852
encodings.cp855
encodings.cp856
encodings.cp857
encodings.cp858
encodings.cp860
encodings.cp861
encodings.cp862
encodings.cp863
encodings.cp864
encodings.cp865
encodings.cp866
encodings.cp869
encodings.cp874
encodings.cp875
encodings.cp932
encodings.cp949
encodings.cp950
encodings.euc_jis_2004
encodings.euc_jisx0213
encodings.euc_jp
encodings.euc_kr
encodings.gb18030
encodings.gb2312
encodings.gbk
encodings.hex_codec
encodings.hp_roman8
encodings.hz
encodings.idna
encodings.iso2022_jp
encodings.iso2022_jp_1
encodings.iso2022_jp_2
encodings.iso2022_jp_2004
encodings.iso2022_jp_3
encodings.iso2022_jp_ext
encodings.iso2022_kr
encodings.iso8859_1
encodings.iso8859_10
encodings.iso8859_11
encodings.iso8859_13
encodings.iso8859_14
encodings.iso8859_15
encodings.iso8859_16
encodings.iso8859_2
encodings.iso8859_3
encodings.iso8859_4
encodings.iso8859_5
encodings.iso8859_6
encodings.iso8859_7
encodings.iso8859_8
encodings.iso8859_9
encodings.johab
encodings.koi8_r
encodings.koi8_t
encodings.koi8_u
encodings.kz1048
encodings.latin_1
encodings.mac_arabic
encodings.mac_centeuro
encodings.mac_croatian
encodings.mac_cyrillic
encodings.mac_farsi
encodings.mac_greek
encodings.mac_iceland
encodings.mac_latin2
encodings.mac_roman
encodings.mac_romanian
encodings.mac_turkish
encodings.palmos
encodings.ptcp154
encodings.punycode
encodings.quopri_codec
encodings.raw_unicode_escape
encodings.rot_13
encodings.shift_jis
encodings.shift_jis_2004
encodings.shift_jisx0213
encodings.string_escape
encodings.tis_620
encodings.undefined
encodings.unicode_escape
encodings.unicode_internal
encodings.utf_16
encodings.utf_16_be
encodings.utf_16_le
encodings.utf_32
encodings.utf_32_be
encodings.utf_32_le
encodings.utf_7
encodings.utf_8
encodings.utf_8_sig
encodings.uu_codec
encodings.zlib_codec
ensurepip
ensurepip._uninstall
enum
filecmp
fileinput
fnmatch
formatter
fpectl
fpformat
fractions
ftplib
functools
future_builtins
gdbm
genericpath
getopt
getpass
gettext
glob
gzip
hashlib
heapq
hmac
hotshot
hotshot.log
hotshot.stats
hotshot.stones
html
html.entities
html.parser
htmlentitydefs
htmllib
http
http.client
http.cookiejar
http.cookies
http.server
httplib
idlelib
idlelib.AutoComplete
idlelib.AutoCompleteWindow
idlelib.AutoExpand
idlelib.Bindings
idlelib.CallTipWindow
idlelib.CallTips
idlelib.CodeContext
idlelib.ColorDelegator
idlelib.Debugger
idlelib.Delegator
idlelib.EditorWindow
idlelib.FileList
idlelib.FormatParagraph
idlelib.GrepDialog
idlelib.HyperParser
idlelib.IOBinding
idlelib.IdleHistory
idlelib.MultiCall
idlelib.MultiStatusBar
idlelib.ObjectBrowser
idlelib.OutputWindow
idlelib.ParenMatch
idlelib.PathBrowser
idlelib.Percolator
idlelib.PyParse
idlelib.RemoteDebugger
idlelib.RemoteObjectBrowser
idlelib.ReplaceDialog
idlelib.RstripExtension
idlelib.ScrolledList
idlelib.SearchDialog
idlelib.SearchDialogBase
idlelib.SearchEngine
idlelib.StackViewer
idlelib.ToolTip
idlelib.TreeWidget
idlelib.UndoDelegator
idlelib.WidgetRedirector
idlelib.WindowList
idlelib.ZoomHeight
idlelib.aboutDialog
idlelib.configDialog
idlelib.configHandler
idlelib.configHelpSourceEdit
idlelib.configSectionNameDialog
idlelib.dynOptionMenuWidget
idlelib.help
idlelib.idle_test
idlelib.idle_test.mock_idle
idlelib.idle_test.mock_tk
idlelib.idle_test.test_calltips
idlelib.idle_test.test_config_name
idlelib.idle_test.test_delegator
idlelib.idle_test.test_formatparagraph
idlelib.idle_test.test_grep
idlelib.idle_test.test_idlehistory
idlelib.idle_test.test_pathbrowser
idlelib.idle_test.test_rstrip
idlelib.idle_test.test_searchengine
idlelib.idle_test.test_text
idlelib.idle_test.test_warning
idlelib.idlever
idlelib.keybindingDialog
idlelib.macosxSupport
idlelib.rpc
idlelib.run
idlelib.tabbedpages
idlelib.textView
ihooks
imaplib
imghdr
imp
importlib
importlib._bootstrap
importlib._bootstrap_external
importlib.abc
importlib.machinery
importlib.util
imputil
inspect
io
ipaddress
json
json.decoder
json.encoder
json.scanner
json.tool
keyword
lib2to3
lib2to3.btm_matcher
lib2to3.btm_utils
lib2to3.fixer_base
lib2to3.fixer_util
lib2to3.fixes
lib2to3.fixes.fix_apply
lib2to3.fixes.fix_asserts
lib2to3.fixes.fix_basestring
lib2to3.fixes.fix_buffer
lib2to3.fixes.fix_callable
lib2to3.fixes.fix_dict
lib2to3.fixes.fix_except
lib2to3.fixes.fix_exec
lib2to3.fixes.fix_execfile
lib2to3.fixes.fix_exitfunc
lib2to3.fixes.fix_filter
lib2to3.fixes.fix_funcattrs
lib2to3.fixes.fix_future
lib2to3.fixes.fix_getcwdu
lib2to3.fixes.fix_has_key
lib2to3.fixes.fix_idioms
lib2to3.fixes.fix_import
lib2to3.fixes.fix_imports
lib2to3.fixes.fix_imports2
lib2to3.fixes.fix_input
lib2to3.fixes.fix_intern
lib2to3.fixes.fix_isinstance
lib2to3.fixes.fix_itertools
lib2to3.fixes.fix_itertools_imports
lib2to3.fixes.fix_long
lib2to3.fixes.fix_map
lib2to3.fixes.fix_metaclass
lib2to3.fixes.fix_methodattrs
lib2to3.fixes.fix_ne
lib2to3.fixes.fix_next
lib2to3.fixes.fix_nonzero
lib2to3.fixes.fix_numliterals
lib2to3.fixes.fix_operator
lib2to3.fixes.fix_paren
lib2to3.fixes.fix_print
lib2to3.fixes.fix_raise
lib2to3.fixes.fix_raw_input
lib2to3.fixes.fix_reduce
lib2to3.fixes.fix_reload
lib2to3.fixes.fix_renames
lib2to3.fixes.fix_repr
lib2to3.fixes.fix_set_literal
lib2to3.fixes.fix_standarderror
lib2to3.fixes.fix_sys_exc
lib2to3.fixes.fix_throw
lib2to3.fixes.fix_tuple_params
lib2to3.fixes.fix_types
lib2to3.fixes.fix_unicode
lib2to3.fixes.fix_urllib
lib2to3.fixes.fix_ws_comma
lib2to3.fixes.fix_xrange
lib2to3.fixes.fix_xreadlines
lib2to3.fixes.fix_zip
lib2to3.main
lib2to3.patcomp
lib2to3.pgen2
lib2to3.pgen2.conv
lib2to3.pgen2.driver
lib2to3.pgen2.grammar
lib2to3.pgen2.literals
lib2to3.pgen2.parse
lib2to3.pgen2.pgen
lib2to3.pgen2.token
lib2to3.pgen2.tokenize
lib2to3.pygram
lib2to3.pytree
lib2to3.refactor
linecache
linuxaudiodev
locale
logging
logging.config
logging.handlers
lzma
macpath
macurl2path
mailbox
mailcap
markupbase
md5
mhlib
mimetools
mimetypes
mimify
mmap
modulefinder
multifile
multiprocessing
multiprocessing.connection
multiprocessing.context
multiprocessing.dummy
multiprocessing.dummy.connection
multiprocessing.forking
multiprocessing.forkserver
multiprocessing.heap
multiprocessing.managers
multiprocessing.pool
multiprocessing.popen_fork
multiprocessing.popen_forkserver
multiprocessing.popen_spawn_posix
multiprocessing.popen_spawn_win32
multiprocessing.process
multiprocessing.queues
multiprocessing.reduction
multiprocessing.resource_sharer
multiprocessing.semaphore_tracker
multiprocessing.sharedctypes
multiprocessing.spawn
multiprocessing.synchronize
multiprocessing.util
mutex
netrc
new
nis
nntplib
ntpath
nturl2path
numbers
opcode
operator
optparse
os
os2emxpath
ossaudiodev
parser
pathlib
pdb
pickle
pickletools
pipes
pkgutil
platform
plistlib
popen2
poplib
posixfile
posixpath
pprint
profile
pstats
pty
py
py.__metainfo
py._apipkg
py._builtin
py._code
py._code._assertionnew
py._code._assertionold
py._code._py2traceback
py._code.assertion
py._code.code
py._code.source
py._error
py._iniconfig
py._io
py._io.capture
py._io.saferepr
py._io.terminalwriter
py._log
py._log.log
py._log.warning
py._path
py._path.cacheutil
py._path.common
py._path.local
py._path.svnurl
py._path.svnwc
py._process
py._process.cmdexec
py._process.forkedfunc
py._process.killproc
py._std
py._xmlgen
py.test
py_compile
pyclbr
pydoc
pydoc_data
pydoc_data.topics
pyexpat
pytest
queue
quopri
random
re
readline
repr
reprlib
resource
rexec
rfc822
rlcompleter
robotparser
runpy
sched
selectors
sets
sgmllib
sha
shelve
shlex
shutil
signal
site
sitecustomize
smtpd
smtplib
sndhdr
socket
socketserver
sqlite3
sqlite3.dbapi2
sqlite3.dump
sre
sre_compile
sre_constants
sre_parse
ssl
stat
statistics
statvfs
string
stringold
stringprep
struct
stubtool.types
subprocess
sunau
sunaudio
symbol
symtable
sysconfig
test
test.pystone
test.regrtest
test.support
test.support.script_helper
test.test_support
tabnanny
tarfile
telnetlib
tempfile
termios
textwrap
threading
timeit
tkColorChooser
tkCommonDialog
tkFileDialog
tkFont
tkMessageBox
tkSimpleDialog
tkinter
tkinter._fix
tkinter.colorchooser
tkinter.commondialog
tkinter.constants
tkinter.dialog
tkinter.dnd
tkinter.filedialog
tkinter.font
tkinter.messagebox
tkinter.scrolledtext
tkinter.simpledialog
tkinter.tix
tkinter.ttk
toaiff
token
tokenize
trace
traceback
tracemalloc
ttk
tty
turtle
turtledemo
turtledemo.bytedesign
turtledemo.chaos
turtledemo.clock
turtledemo.colormixer
turtledemo.forest
turtledemo.fractalcurves
turtledemo.lindenmayer
turtledemo.minimal_hanoi
turtledemo.nim
turtledemo.paint
turtledemo.peace
turtledemo.penrose
turtledemo.planet_and_moon
turtledemo.round_dance
turtledemo.tree
turtledemo.two_canvases
turtledemo.wikipedia
turtledemo.yinyang
types
typing
unittest
unittest.case
unittest.loader
unittest.main
unittest.mock
unittest.result
unittest.runner
unittest.signals
unittest.suite
unittest.util
urllib
urllib.error
urllib.parse
urllib.request
urllib.response
urllib.robotparser
urllib2
urlparse
user
uu
uuid
venv
warnings
wave
weakref
webbrowser
whichdb
wsgiref
wsgiref.handlers
wsgiref.headers
wsgiref.simple_server
wsgiref.util
wsgiref.validate
xdrlib
xml
xml.dom
xml.dom.NodeFilter
xml.dom.domreg
xml.dom.expatbuilder
xml.dom.minicompat
xml.dom.minidom
xml.dom.pulldom
xml.dom.xmlbuilder
xml.etree
xml.etree.ElementInclude
xml.etree.ElementPath
xml.etree.ElementTree
xml.etree.cElementTree
xml.parsers
xml.parsers.expat
xml.sax
xml.sax._exceptions
xml.sax.expatreader
xml.sax.handler
xml.sax.saxutils
xml.sax.xmlreader
xmllib
xmlrpc
xmlrpc.client
xmlrpc.server
xmlrpclib
zipapp
zipfile
'''.split()


def check_unknowns(seen=set(), modules=set()):
    mod_diff = set(sys.modules) - modules
    if not mod_diff:
        return
    modules |= mod_diff
    mod_diff = sorted([m for m in mod_diff if sys.modules[m] is not None])

    for type_name, base_names in known_unknown.items():
        if type_name in seen:
            continue
        base_names = base_names or ['builtins.object']
        if six.PY2:
            base_names = [b.replace('builtins.', '__builtin__.') for b in base_names]
        for base in base_names:
            try:
                base = stubtool.name.get_object(base)
                break
            except (ImportError, AttributeError):
                continue
        else:
            continue
        if stubtool.name.search_for_type(type_name, base):
            print('%r found in %r' % (type_name, mod_diff))
            seen.add(type_name)


def import_everything():
    check_unknowns()
    assert sys.modules.get('docutils', None) is None
    sys.modules['docutils'] = None

    import datetime
    if '_datetime' in sys.modules:
        assert __import__('_datetime').datetime is datetime.datetime
        try:
            del datetime._EPOCH
        except AttributeError:
            pass

    check_unknowns()
    for name in all_modules:
        try:
            stubtool.name.import_module(name)
        except ImportError as e:
            if e.args and e.args[0].startswith('No module named'):
                continue
            raise
        check_unknowns()

    # Needed to get rid of temporary classes.
    import gc
    gc.collect()


class PrintOnExceptContext:
    def __init__(self):
        self.msg = ''


    def __enter__(self):
        return self


    def __exit__(self, typ, val, tb):
        if val and self.msg:
            print(self.msg)


def maybe_print(mes, _seen = set()):
    if mes not in _seen:
        print(mes)
        _seen.add(mes)


def check_name(typ):
    try:
        stubtool.name.get_stub_name(typ)
    except TypeError as e:
        if e.args[0].startswith('local:'):
            return
        if e.args[0].startswith('generic:'):
            return
        if e.args[0].startswith('known unknown:'):
            subclasses = getattr(typ, '__subclasses__', lambda: [])()
            subclasses = [get_declared_name(scls) for scls in subclasses]
            subclasses = [scls for scls in subclasses if scls not in known_unknown]
            TPFLAGS_HEAP = 1 << 9
            if hasattr(typ, '__flags__'):
                if typ.__flags__ & TPFLAGS_HEAP:
                    flags = '(heap)'
                else:
                    flags = '(noheap)'
            else:
                flags = '(unknown)'
            maybe_print('TODO: %r %s: %r' % (typ, flags, subclasses))
            return
        raise


def do_modules():
    with PrintOnExceptContext() as e:
        for name in sorted(sys.modules):
            try:
                mod = stubtool.name.import_module(name)
            except ImportError:
                # Possible for None values as well as the blacklist.
                continue
            for k, v in sorted(mod.__dict__.items()):
                e.msg = '%s.%s = %r' % (name, k, v)
                if isinstance(v, six.class_types):
                    check_name(v)
                e.msg = 'instance ' + e.msg
                check_name(type(v))
                if getattr(v, '__class__', type(v)) is not type(v):
                    check_name(v.__class__)


def do_subclasses():
    open = {object}
    closed = set()
    while open:
        elem = open.pop()
        closed.add(elem)
        for e2 in type(elem).__subclasses__(elem):
            if e2 in closed:
                continue
            open.add(e2)
    closed = sorted(closed, key=lambda cls: cls.__name__)
    for cls in closed:
        check_name(cls)


def test():
    print('test: begin all')
    print('test: begin imported')
    import_everything()
    print('test: end imported')
    print('test: begin modules')
    do_modules()
    print('test: end modules')
    print('test: begin subclasses')
    do_subclasses()
    print('test: end subclasses')
    print('test: end all')


if __name__ == '__main__':
    test()

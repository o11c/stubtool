from __future__ import absolute_import

import sys

from ._util import PY2, PY3, PY33


FlagsType = type(sys.flags)
FloatInfoType = type(sys.float_info)
if PY3:
    HashInfoType = type(sys.hash_info)
    IntInfoType = type(sys.int_info)
if PY2:
    LongInfoType = type(sys.long_info)
if PY33:
    ThreadInfoType = type(sys.thread_info)
VersionInfoType = type(sys.version_info)

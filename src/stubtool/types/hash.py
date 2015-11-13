from __future__ import absolute_import

import _hashlib

from ._util import PY2, PY33


if PY2:
    import _md5
    import _sha
    import _sha256
    import _sha512


    md5 = type(_md5.new())
    sha1 = type(_sha.new())
    sha224 = type(_sha256.sha224())
    sha256 = type(_sha256.sha256())
    sha384 = type(_sha512.sha384())
    sha512 = type(_sha512.sha512())
elif PY33:
    import _md5
    import _sha1
    import _sha256
    import _sha512


    md5 = type(_md5.md5())
    sha1 = type(_sha1.sha1())
    sha224 = type(_sha256.sha224())
    sha256 = type(_sha256.sha256())
    sha384 = type(_sha512.sha384())
    sha512 = type(_sha512.sha512())

HASH = type(_hashlib.new('md5'))

from __future__ import absolute_import

from ._util import PY2, PY34, only


if PY2 or PY34:
    import ssl


    BaseASN1Object = only(ssl._ASN1Object.__bases__)
    BaseASN1Object._fields
    assert BaseASN1Object.__name__ == '_ASN1Object'

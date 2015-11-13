from __future__ import absolute_import

import crypt

from ._util import PY33, only


if PY33:
    BaseMethod = only(crypt._Method.__bases__)
    BaseMethod._fields
    assert BaseMethod.__name__ == '_Method'

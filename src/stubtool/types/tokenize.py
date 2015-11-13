from __future__ import absolute_import

from ._util import PY3, only


if PY3:
    import tokenize


    BaseTokenInfo = only(tokenize.TokenInfo.__bases__)
    BaseTokenInfo._fields
    assert BaseTokenInfo.__name__ == 'TokenInfo'

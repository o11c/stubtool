from __future__ import absolute_import

from ._util import PY2, former


if PY2:
    import urlparse


    BaseParseResult = former(urlparse.ParseResult.__bases__)
    BaseParseResult._fields
    assert BaseParseResult.__name__ == 'ParseResult'
    BaseSplitResult = former(urlparse.SplitResult.__bases__)
    BaseSplitResult._fields
    assert BaseSplitResult.__name__ == 'SplitResult'

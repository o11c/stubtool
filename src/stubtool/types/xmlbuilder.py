from __future__ import absolute_import

import xml.dom.xmlbuilder

from ._util import PY35, PY37


if PY35 and not PY37:
    AsyncDeprecatedProperty = type(xml.dom.xmlbuilder.DocumentLS.__dict__['async'])

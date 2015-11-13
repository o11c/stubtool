from __future__ import absolute_import

import _elementtree
import xml.etree.ElementTree
import xml.etree.cElementTree

from ._util import PY32, PY33, PY34, only


if not PY33:
    # Old-style class in PY2, can't use type().
    CommentProxy = _elementtree.Comment.__class__
    PIProxy = _elementtree.PI.__class__

if PY33 and not PY34:
    BaseElementTree = only(xml.etree.ElementTree.ElementTree.__bases__)
    assert BaseElementTree.__name__ == 'ElementTree', BaseElementTree.__name__

cElement = type(xml.etree.cElementTree.Element('foo'))

if PY33:
    element_iterator = type(_elementtree.Element('foo').iter())

if PY32 and not PY33:
    TreeBuilder = type(_elementtree.TreeBuilder())
    XMLParser = type(_elementtree.XMLParser())

from __future__ import absolute_import

import collections
import six

from ._util import PY3


# Most of these are present but undocumented in _collections_abc
# (module name varies between versions)

deque_iterator = type(iter(collections.deque()))
deque_reverse_iterator = type(reversed(collections.deque()))

bytearray_iterator = type(iter(bytearray()))
if PY3:
    bytes_iterator = type(iter(bytes()))
dict_items = type(six.viewitems(dict()))
dict_keys = type(six.viewkeys(dict()))
dict_values = type(six.viewvalues(dict()))
dict_itemiterator = type(six.iteritems(dict()))
dict_keyiterator = type(six.iterkeys(dict()))
dict_valueiterator = type(six.itervalues(dict()))
list_iterator = type(iter(list()))
list_reverseiterator = type(reversed(list()))
range_iterator = type(iter(six.moves.range(0)))
if PY3:
    longrange_iterator = type(iter(range(1 << 64)))
set_iterator = type(iter(set()))
if PY3:
    str_iterator = type(iter(str()))
tuple_iterator = type(iter(tuple()))

class _IndexIterable:
    def __getitem__(self, idx):
        raise IndexError

# In python2 this is used for `str`.
index_iterator = type(iter(_IndexIterable()))
callable_iterator = type(iter(lambda: None, None))

odict_items = type(collections.OrderedDict().items())
odict_keys = type(collections.OrderedDict().keys())
odict_values = type(collections.OrderedDict().values())
# This is used for iter of all 3 of the above.
odict_iterator = type(iter(collections.OrderedDict()))

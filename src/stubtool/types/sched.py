from __future__ import absolute_import

import sched

from ._util import PY3, only


if PY3:
    BaseEvent = only(sched.Event.__bases__)
    BaseEvent._fields
    assert BaseEvent.__name__ == 'Event'

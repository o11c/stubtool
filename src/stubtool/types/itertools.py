from __future__ import absolute_import

import gc
import itertools

from ._util import PY33, only, former, latter


grouper = type(latter(only(itertools.groupby(['']))))
tee = type(former(itertools.tee([])))
if not PY33:
    tee_dataobject = type(only(gc.get_referents(former(itertools.tee([])))))

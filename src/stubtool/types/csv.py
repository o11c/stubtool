from __future__ import absolute_import

import _csv
import sys


reader = type(_csv.reader(sys.stdin))
writer = type(_csv.writer(sys.stdout))

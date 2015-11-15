from __future__ import absolute_import, unicode_literals

import _csv
import io


reader = type(_csv.reader(io.StringIO('')))
writer = type(_csv.writer(io.StringIO()))

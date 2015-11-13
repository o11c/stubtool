from __future__ import absolute_import

import multiprocessing.process


MainProcess = type(multiprocessing.process._current_process)

from __future__ import absolute_import

import os.path
import shutil
import tempfile


from ._util import PY2, first


if PY2:
    import anydbm


    error = first(anydbm.error)
else:
    import dbm
    import _dbm
    try:
        import _gdbm
    except ImportError:
        _gdbm = None


    error = first(dbm.error)

    try:
        tmpdir = tempfile.mkdtemp()

        ndbm = type(_dbm.open(os.path.join(tmpdir, 'ndbm'), 'n'))
        if _gdbm is not None:
            gdbm = type(_gdbm.open(os.path.join(tmpdir, 'gdbm'), 'n'))
    finally:
        shutil.rmtree(tmpdir, True)
        del tmpdir

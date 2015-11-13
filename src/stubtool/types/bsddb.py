from __future__ import absolute_import

import shutil
import tempfile

from ._util import PY2


def _init():
    import _bsddb
    global DB, DBCursor, DBEnv, DBLock, DBLogCursor, DBSequence, DBSite, DBTxn
    try:
        tmpdir = tempfile.mkdtemp()

        db = _bsddb.DB()
        db.open(None, _bsddb.DB_BTREE, _bsddb.DB_CREATE)
        cursor = db.cursor()
        env = _bsddb.DBEnv()
        env.open(tmpdir, _bsddb.DB_CREATE | _bsddb.DB_PRIVATE | _bsddb.DB_INIT_LOCK | _bsddb.DB_INIT_REP | _bsddb.DB_INIT_TXN)
        lock = env.lock_get(env.lock_id(), None, _bsddb.DB_LOCK_READ)
        log_cursor = env.log_cursor()
        seq = _bsddb.DBSequence(db)
        site = env.repmgr_site('localhost', 1)
        txn = env.txn_begin()
        txn.abort()

        DB = type(db)
        DBCursor = type(cursor)
        DBEnv = type(env)
        DBLock = type(lock)
        DBLogCursor = type(log_cursor)
        DBSequence = type(seq)
        DBSite = type(site)
        DBTxn = type(txn)
    finally:
        shutil.rmtree(tmpdir, True)


if PY2:
    _init()

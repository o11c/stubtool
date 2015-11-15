from __future__ import absolute_import

import _curses
import _curses_panel
import os


_STDOUT_FILENO = 1

def _init():
    real_term = os.getenv('TERM')
    master, slave, savestdout = -1, -1, -1
    try:
        os.putenv('TERM', 'ansi')
        master, slave = os.openpty()
        savestdout = os.dup(_STDOUT_FILENO)

        os.dup2(slave, _STDOUT_FILENO)
        win = _curses.initscr()
        panel = _curses_panel.new_panel(win)
        win_type = type(win)
        panel_type = type(panel)
        _curses.endwin()
        return win_type, panel_type
    finally:
        os.dup2(savestdout, _STDOUT_FILENO)
        os.close(savestdout)
        os.close(slave)
        os.close(master)
        if real_term is not None:
            os.putenv('TERM', real_term)
        else:
            os.unsetenv('TERM')


curses_window, curses_panel = _init()

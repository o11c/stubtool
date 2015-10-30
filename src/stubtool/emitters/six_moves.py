from __future__ import print_function

from functools import partial
import six
import types

from .module import ModuleEmitter


class SixMovesEmitter(ModuleEmitter):
    def __init__(self, mod_name, parent):
        super(SixMovesEmitter, self).__init__(mod_name, parent)
        assert mod_name.startswith('six.moves')

    def import_module(self, mod_name):
        return six._importer.known_modules[mod_name]

    def is_package(self):
        name = self.mod_name
        if name.startswith('six.moves.tkinter'):
            return False
        if name == 'six.moves.dbm_gnu':
            return False
        rv = super(SixMovesEmitter, self).is_package()
        assert rv == (name in ('six.moves', 'six.moves.urllib'))
        return rv

    def emit(self, out):
        name = self.mod_name
        mod = self.module
        if isinstance(mod, six._LazyModule):
            if name != mod.__name__:
                do1(out, mod)
            else:
                do2(out, mod)
        elif isinstance(mod, types.ModuleType):
            assert name == mod.__name__, name
            do0(out, mod)
        elif isinstance(mod, six.MovedModule):
            do3(out, mod)
        else:
            assert False, type(mod).mro()

    def list_children(self):
        prefix = self.mod_name + '.'
        prefix_len = len(prefix)
        children = []
        for mod in six._importer.known_modules:
            if not mod.startswith(prefix):
                continue
            mod = mod[prefix_len:]
            if '.' in mod:
                continue
            children.append(mod)
        return children


def do0(out, mod):
    assert mod.__name__ == 'six.moves.urllib'
    p = partial(print, file=out)
    for name in dir(mod):
        attr = getattr(mod, name)
        assert isinstance(attr, six._LazyModule), '%s is a %s' % (name, type(attr).mro())
        p('import %s.%s as %s' % (mod.__name__, name, name))


def do1(out, mod):
    p = partial(print, file=out)
    p('from %s import (' % mod.__name__)
    for a in mod._moved_attributes:
        name = a.name
        assert not name.startswith('__')
        p('    %s as %s,' % (name, name))
    p(')')


def do2(out, mod):
    p = partial(print, file=out)
    for a in mod._moved_attributes:
        if isinstance(a, six.MovedModule):
            assert '%s.%s' % (mod.__name__, a.name) in six._importer.known_modules
            p('import %s.%s as %s' % (mod.__name__, a.name, a.name))
            continue
        assert isinstance(a, six.MovedAttribute)
        p('from %s import %s as %s' % (a.mod, a.attr, a.name))


def do3(out, mod):
    p = partial(print, file=out)
    p('from %s import *' % mod.mod)


def set_repr():
    # Useful for interactive use.
    def __repr__(self):
        return 'MovedModule(name=%s, mod=%s)' % (self.name, self.mod)
    six.MovedModule.__repr__ = __repr__

    def __repr__(self):
        return 'MovedAttribute(name=%s, mod=%s, attr=%s)' % (self.name, self.mod, self.attr)
    six.MovedAttribute.__repr__ = __repr__

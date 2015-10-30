from abc import ABCMeta, abstractmethod
from six import with_metaclass


class AbstractEmitter(with_metaclass(ABCMeta)):
    '''
    Interface for stub emitter.

    Besides actually emitting, emitters are also used to walk parent modules.

    Normally you want to subclass `ModuleEmitter` instead.
    '''
    @abstractmethod
    def __init__(self, mod_name, parent):
        '''
        Called to construct the emitter.

        `mod_name` is the full name of this module.
        `parent` is the emitter object used for the parent package. This
        may be `None` only if this module is a top-level module.

        Note that the parent emitter might not have actually been *used* -
        in such cases it may often be a `NullEmitter`.

        For more control, override `__new__` or pass a function as
        the factory and also override `create_child`.
        '''
        self.mod_name = mod_name
        self.parent = parent

    @abstractmethod
    def is_package(self):
        '''
        Called to check if this emitter is a package.

        According to PEP 302, a module is a package if it has a `__path__`
        attribute, regardless of value (but the value should be a list).

        Sometimes, a module is inserted into `sys.modules` without creating
        `__path__` appropriately - for example, `os.path`. In cases like this,
        it may be necessary to override this function.
        '''

    @abstractmethod
    def emit(self, out):
        '''
        Called to emit stubs for the module.

        This might not be called if `stubtool`'s caller is only interested
        in modules *within* this package.

        `out` is an open file-like object.
        '''

    @abstractmethod
    def list_children(self):
        '''
        Called to list modules within this package.

        This can only be called if `is_package` returned `True`.

        This should return the short name, with no dots.
        '''

    @abstractmethod
    def create_child(self, factory, mod_name):
        '''
        Called to create an emitter for a module within this package.

        This can only be called if `is_package` returned `True`.

        `factory` is `type(self)` unless the context has an override.
        `mod_name` is the full module name of the child.
        '''

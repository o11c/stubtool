from abc import abstractmethod
import importlib
import os
import pkg_resources

from .. import errors

from .abstract import AbstractEmitter


class ModuleEmitter(AbstractEmitter):
    '''
    Base class that implements most functions based on an imported module.
    '''
    def __init__(self, mod_name, parent):
        super(ModuleEmitter, self).__init__(mod_name, parent)
        try:
            self.module = self.import_module(mod_name)
        except ImportError:
            raise errors.StubImportError(mod_name)

    def import_module(self, mod_name):
        '''
        Called to import the module.
        '''
        return importlib.import_module(mod_name)

    def is_package(self):
        return hasattr(self.module, '__path__')

    @abstractmethod
    def emit(self, out):
        pass

    def list_children(self):
        provider = pkg_resources.get_provider(self.mod_name)
        children = []
        for f in provider.resource_listdir('.'):
            if f.endswith('.py'):
                children.append(f[:-3])
            elif '.' not in f and provider.has_resource(os.path.join(f, '__init__.py')):
                children.append(f)
        return sorted(set(children))

    def create_child(self, factory, mod_name):
        return factory(mod_name, self)

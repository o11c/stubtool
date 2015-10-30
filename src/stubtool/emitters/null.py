from .. import errors

from .module import ModuleEmitter


class NullEmitter(ModuleEmitter):
    '''
    An module-based emitter that cowardly refuses to actually emit anything.

    It still can be used as a parent emitter, however.
    '''
    def emit(self, out):
        raise errors.StubNotImplementedError(self.mod_name)

from abc import ABCMeta, abstractmethod

from six import with_metaclass


class StubError(with_metaclass(ABCMeta, Exception)):
    '''
    Base class for all exceptions.
    '''
    @abstractmethod
    def __init__(self, mes):
        super(StubError, self).__init__(mes)


class StubFileError(StubError):
    '''
    Something went wrong with files.
    '''
    def __init__(self, path, mes):
        super(StubFileError, self).__init__('%s: %r' % (mes, path))


class StubImportError(StubError):
    '''
    A module could not be imported.
    '''
    def __init__(self, mod):
        super(StubImportError, self).__init__('module %r could not be imported' % (mod))


class StubNotPackageError(StubError):
    '''
    Tried to recurse into a non-package.
    '''
    def __init__(self, mod, target):
        super(StubNotPackageError, self).__init__(
            'module %r is not a package (cannot continue to %r)' % (mod, target))


class StubNotImplementedError(StubError):
    '''
    A stub emitter was not implemented.
    '''
    def __init__(self, mod):
        super(StubNotImplementedError, self).__init__('module %r emitter not implemented' % (mod))


class StubUnknownError(StubError):
    '''
    Some other exception happened unexpectedly.
    '''
    def __init__(self, mes):
        super(StubUnknownError, self).__init__(mes)

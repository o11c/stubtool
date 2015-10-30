import os


def makedirs(dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)


def remove(file):
    try:
        os.remove(file)
    except OSError:
        pass

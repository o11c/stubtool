# stubtool
Scripts for generating and maintaining PEP 484 stubs

Stubs are stored in [typeshed](https://github.com/python/typeshed)

[This repository is community-maintained.](https://github.com/o11c/stubtool/issues/1)

[IRC on FreeNode ##mypy](https://webchat.freenode.net/?channels=##mypy)

## Scope

The scripts in this package produce one or more .pyi files from some sort
of input. Possible sources of input include:

* Modules loaded in the current python interpreter.
* Previously-generated .pyi files.
* Some machine-readable file format (such as XML or JSON).

For example, a script could take stubs for multiple python versions,
and produce a unified stub with `if` conditions.

Every script in this repo *must* be compatible with both Python2 and Python3.

All scripts should produce the same header format.

All scripts should take the output directory as the first positional argument,
and fail if it is not passed.

We should make a library to handle this, and add a setup.py.

We should use `tox` to test things maybe and enable travis.

## Other stub tools

* mypy.stubgen is closely tied to mypy, so can't be moved here.

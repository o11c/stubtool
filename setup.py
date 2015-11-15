#!/usr/bin/env python

from setuptools import setup, find_packages

version_globals = {}
with open('src/stubtool/version.py') as f:
    exec(f.read(), version_globals)

setup(
    name='stubtool',
    version=version_globals['__version__'],
    description='Scripts for generating and maintaining PEP 484 stubs',
    author='Ben Longbons',
    author_email='brlongbons@gmail.com',
    url=version_globals['REPO'],
    license='MIT License',
    platforms=['POSIX'],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
    ],
    zip_safe=True,
)

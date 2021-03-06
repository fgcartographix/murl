#!/usr/bin/env python
# coding: utf-8

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


# Taken from kennethreitz/requests/setup.py
package_directory = os.path.realpath(os.path.dirname(__file__))

def get_file_contents(file_path):
    """Get the context of the file using full path name."""
    full_path = os.path.join(package_directory, file_path)
    return open(full_path, 'r').read()

setup(
    name='murl',
    version='0.2',
    description='murl is a tiny wrapper for the Python module urlparse.',
    long_description=get_file_contents('PYPI.rst'),
    author='Berker Peksag',
    author_email='berker.peksag@gmail.com',
    url='https://github.com/berkerpeksag/murl',
    py_modules=['murl'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    license='Mozilla Public License, v. 2.0',
    classifiers=(
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
    ),
    test_suite='nose.collector',
)

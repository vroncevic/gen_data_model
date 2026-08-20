# -*- coding: UTF-8 -*-

'''
Module
    setup.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_data_model is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_data_model is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines setup for tool gen_data_model.
'''

from __future__ import annotations

from os import walk
from os.path import abspath, dirname, join, relpath
from setuptools import setup, find_packages

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_data_model'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_data_model/blob/dev/LICENSE'
__version__ = '2.3.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

THIS_DIR: str = abspath(dirname(__file__))
long_description: str | None = None

with open(join(THIS_DIR, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()

PROGRAMMING_LANG: str = 'Programming Language :: Python ::'
VERSIONS: list[str] = ['3.12', '3.13', '3.14']
SUPPORTED_PY_VERSIONS: list[str] = [f'{PROGRAMMING_LANG} {VERSION}' for VERSION in VERSIONS]
PYP_CLASSIFIERS: list[str] = SUPPORTED_PY_VERSIONS

def find_package_data(pkg: str) -> list[str]:
    '''
        Finds all files in package to include in package_data.

        :param pkg: The package folder name.
        :return: The list of package files relative to the package folder.
        :exceptions: None.
    '''
    package_data: list[str] = []

    for root, dirs, files in walk(pkg):
        dirs[:] = [d for d in dirs if d != '__pycache__']

        for file in files:
            if file.endswith('.pyc') or file == '.editorconfig':
                continue

            full_path: str = join(root, file)
            rel_path: str = relpath(full_path, pkg)
            package_data.append(rel_path)

    return package_data

setup(
    name='gen_data_model',
    version='2.3.7',
    description='Python package for generation of data model',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_data_model',
    license='GPL-3.0-or-later',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='setup, python, install, django, flask, sqlalchemy, generator',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=find_packages(exclude=['tests', 'tests.*', '*.*.pyc', '*.pyo']),
    install_requires=['ats-utilities'],
    package_data={'gen_data_model': find_package_data('gen_data_model')}
)

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
 Module
     setup.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined setup for gen_data_model tool package.
'''

from sys import argv, version_info, prefix, exit
from os.path import abspath, dirname, join, exists
from site import getusersitepackages
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/gen_data_model'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_data_model/blob/master/LICENSE'
__version__ = '1.4.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

def install_directory():
    '''
        Return the installation directory, or None.

        :return: path (success) | None.
        :rtype: <str> | <NoneType>
        :exceptions: None
    '''
    py_version = '{0}.{1}'.format(version_info[0], version_info[1])
    if '--github' in argv:
        index = argv.index('--github')
        argv.pop(index)
        paths = (
            '{0}/lib/python{1}/dist-packages/'.format(prefix, py_version),
            '{0}/lib/python{1}/site-packages/'.format(prefix, py_version)
        )
    else:
        paths = (s for s in (
            '{0}/local/lib/python{1}/dist-packages/'.format(
                prefix, py_version
            ),
            '{0}/local/lib/python{1}/site-packages/'.format(
                prefix, py_version
            )
        ))
    for path in paths:
        print('[setup] check path {0}'.format(path))
        if exists(path):
            print('[setup] using path {0}'.format(path))
            return path
    print('[setup] no installation path found, check {0}\n'.format(prefix))
    return None

INSTALL_DIR = install_directory()

if not INSTALL_DIR:
    print('[setup] force exit from install process')
    exit(127)

THIS_DIR, LONG_DESCRIPTION = abspath(dirname(__file__)), None
with open(join(THIS_DIR, 'README.md')) as readme:
    LONG_DESCRIPTION = readme.read()

PROGRAMMING_LANG = 'Programming Language :: Python ::'
VERSIONS = ['2.7', '3', '3.2', '3.3', '3.4']
SUPPORTED_PY_VERSIONS = [
    '{0} {1}'.format(PROGRAMMING_LANG, VERSION) for VERSION in VERSIONS
]

LICENSE_PREFIX = 'License :: OSI Approved ::'
LICENSES = [
    'GNU Lesser General Public License v2 (LGPLv2)',
    'GNU Lesser General Public License v2 or later (LGPLv2+)',
    'GNU Lesser General Public License v3 (LGPLv3)',
    'GNU Lesser General Public License v3 or later (LGPLv3+)',
    'GNU Library or Lesser General Public License (LGPL)'
]
APPROVED_LICENSES = [
    '{0} {1}'.format(LICENSE_PREFIX, LICENSE) for LICENSE in LICENSES
]

PYP_CLASSIFIERS = SUPPORTED_PY_VERSIONS + APPROVED_LICENSES

setup(
    name='gen_data_model',
    version='1.4.0',
    description='Python App/Tool/Script Utilities',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_data_model/',
    license='GPL 2017 Free software to use and distributed it.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords='data model, django, flask, sqlalchemy',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=['gen_data_model', 'gen_data_model.pro'],
    install_requires=[
        'ats-utilities',
        'Flask',
        'Flask-Migrate',
        'Flask-Script',
        'coverage',
        'WTForms',
        'Flask-Login',
        'Flask-BCrypt',
        'Flask-Bootstrap',
        'Flask-DebugToolbar',
        'Flask-SQLAlchemy',
        'Flask-Testing',
        'Flask-WTF',
        'Django',
        'SQLAlchemy'
    ],
    data_files=[
        ('/usr/local/bin/', ['gen_data_model/run/gen_data_model_run.py']),
        (
            '{0}{1}'.format(INSTALL_DIR, 'gen_data_model/conf/'),
            ['gen_data_model/conf/gen_data_model.cfg']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'gen_data_model/conf/'),
            ['gen_data_model/conf/gen_data_model_util.cfg']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'gen_data_model/conf/'),
            ['gen_data_model/conf/data_model_types.yaml']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'gen_data_model/conf/template/'),
            ['gen_data_model/conf/template/django.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'gen_data_model/conf/template/'),
            ['gen_data_model/conf/template/flask.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'gen_data_model/conf/template/'),
            ['gen_data_model/conf/template/sqlalchemy.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'gen_data_model/conf/template/'),
            ['gen_data_model/conf/template/django_base_model.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'gen_data_model/conf/template/'),
            ['gen_data_model/conf/template/flask_base_model.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'gen_data_model/conf/template/'),
            ['gen_data_model/conf/template/sqlalchemy_base_model.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'gen_data_model/log/'),
            ['gen_data_model/log/gen_data_model.log']
        )
    ]
)

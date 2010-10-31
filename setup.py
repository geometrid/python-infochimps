#!/usr/bin/python2.4
#
# Copyright 2010 The Python-Infochimps Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''The setup and build script for the python-infochimps library.'''

__author__ = 'eric@hurricaneparty.com'
__version__ = '0.1-devel'


# The base package metadata to be used by both distutils and setuptools
METADATA = dict(
  name = "python-infochimps",
  version = __version__,
  packages = ['infochimps'],
  author='The Python-Infochimps Developers',
  author_email='eric@hurricaneparty.com',
  description='A python wrapper around the Infochimps API',
  license='Apache License 2.0',
  keywords='infochimps api',
)


def Main():

  # Use setuptools if available, otherwise fallback and use distutils
  try:
    import setuptools
    setuptools.setup(**METADATA)
  except ImportError:
    import distutils.core
    distutils.core.setup(**METADATA)


if __name__ == '__main__':
  Main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# setup.py

# requirements:
#  python -m pip install wheel setuptools

# Usage:
#  python setup.py create

# install wheel
#   python -m pip install --force-reinstall ./dist/*.whl

# unittest
#  python -m unittest discover --catch --verbose

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

""" Project structure
.                               # project directory
├── <your Python project>       # name of your project
│   ├── __init__.py             # indicates to Python this is a package
│   ├── __version__.py          # optional
│   ├── <project code>.py   
│   └── ...
├── doc
|   └── ...
├── test
│   └── <test_project code>.py  # create a test
│   └── ...
├── LICENSE.txt
├── MANIFEST.in
├── pyproject.toml
├── README.md                   # good description of the project
└── setup.py                    # this file
"""

# Package meta-data.
NAME = 'playwright-apirequest-builder'
DESCRIPTION = 'Playwright APIRequest builder'
URL = 'https://github.com/w13b3/playwright-apirequest-builder'
EMAIL = 'wiebe at email dot com'  # prevent warning 'missing meta-data'
AUTHOR = 'Wiebe'
REQUIRES_PYTHON = '>=3.8.0, <4'
VERSION = '1.0.0'  # change this
# If you do change the License, remember to change the Trove Classifier for that!
LICENSE = "Mozilla Public License Version 2.0"

# If your package is a single module, use this instead of 'packages':
PY_MODULES = [
    'playwright_request'
]

# What packages are required for this module to be executed?
REQUIRED = [
    "playwright>=1.26.0"
]

# What packages are optional?
EXTRAS = {
    # None
}

# Trove Classifiers
CLASSIFIERS = [  # https://pypi.org/classifiers/
    "Development Status :: 5 - Production/Stable",
    "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3 :: Only",
    "Typing :: Typed",
    "Intended Audience :: Developers",
    "Topic :: Software Development",
    "Topic :: Software Development :: Build Tools",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
keywords = [
    "builder",
    "builder-pattern",
    "web-request",
    "playwright",
    "playwright-api",
    "playwright-python"
]

if not bool(VERSION) and len(VERSION) <= 0:
    raise Exception("Forgot to change the version")

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


class CreateCommand(Command):
    """Support setup.py create."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…\n')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))
        self.status("\nReady to upload to PyPI.")
        sys.exit()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=[
        "test",  "*.test",  "*.test.*",  "test.*",
        "tests", "*.tests", "*.tests.*", "tests.*",
        "doc",   "*.doc",   "*.doc.*",   "doc.*",
    ]),
    py_modules=PY_MODULES,
    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    # $ setup.py create support.
    cmdclass={
        'create': CreateCommand,
    },
)
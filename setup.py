import os
import sys

from distutils.core import setup
from setuptools.command.test import test as TestCommand

here = os.path.abspath(os.path.dirname(__file__))

# Long description.
with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

about = {}
# Get meta-data from __version__.py
with open(os.path.join(here, 'wasserstoff', '__version__.py')) as f:
    exec(f.read(), about)


class PyTest(TestCommand):
    """Custom command for running test using setup.py test"""

    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name=about['__title__'],
    version=about['__version__'],
    packages=['tests', 'wasserstoff'],
    url=about['__url__'],
    license=about['__license__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    description=about['__description__'],
    keywords=[
        'wasserstoff',
        'config',
        'json',
        'objects',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Topic :: Software Development :: Testing',
    ],
    tests_require=[
        'pytest',
        'flake8-builtins',
        'flake8-commas',
        'flake8-quotes',
        'pytest-flake8',
    ],
    cmdclass={'test': PyTest},
)

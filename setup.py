#!/usr/bin/env python

import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

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
    name='larger',
    version='0.1',
    description="Lazy function arguments",
    author="Josh Bode",
    author_email='joshbode@gmail.com',
    packages=find_packages(),
    install_requires=['decorator'],
    tests_require=['pytest'],
    license='LICENSE.rst',
    long_description=open('README.rst', 'r').read(),
    cmdclass={'test': PyTest},
)

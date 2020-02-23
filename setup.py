# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    # noinspection PyShadowingBuiltins
    license = f.read()

setup(
    name='regress',
    version='0.1.0',
    description='Python module to import data from regressi files',
    long_description=readme,
    author='Robinson Besson',
    url='https://github.com/nosseb/regress.py',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

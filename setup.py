# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='a1 zoo',
    version='0.1.0',
    description='A1 Zoo',
    long_description=readme,
    author='Misha M.-Kupriyanov',
    author_email='m.kupriyanov@gmail.com',
    url='https://github.com/printminion/a1_zoo',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

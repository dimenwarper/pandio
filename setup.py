#!/usr/bin/env python
from setuptools import setup

setup(
    name='pandio',
    version='0.0.1',
    description='Apply arbitrary commands to a dataframe in a CSV using pandas',
    author='Pablo Cordero',
    author_email='dimenwarper@gmail.com',
    license='MIT',
    packages=['pandio'],
    entry_points={
        'console_scripts': [
            'pandio = pandio.main:execute',
        ]
    },
    install_requires=['pandas', 'numpy', 'scipy']
)

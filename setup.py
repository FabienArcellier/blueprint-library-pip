#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

setup(
    name='mylib',
    version='1.0.0',
    packages=find_packages(exclude=["*_tests"]),
    license='MIT license',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires = [
    ],
    extras_require={
        'dev': [
            'pylint',
            'coverage',
            'tox',
            'twine'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Environment :: Console"
    ]
)

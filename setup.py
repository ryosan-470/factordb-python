#!/usr/bin/env python
from setuptools import setup


def _read_from_requirements():
    with open('requirements.txt') as f:
        return [r.strip() for r in f.readlines()]


setup_options = dict(
    name='factordb-pycli',
    version='0.0.1',
    description='',
    long_description=open('README.md').read(),
    author='Ryosuke SATO (@ryo-san470)',
    url='https://github.com/ryo-san470/factordb-pycli',
    py_modules=['factordb'],
    entry_points='''
    [console_scripts]
    factordb=factordb:main
    ''',
    install_requires=_read_from_requirements(),
    setup_requires=['pytest-runner'],
    test_require=['pytest'],
    license="MIT License",
    classifiers=(
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Utilities",
    ),
)

setup(**setup_options)

#!/usr/bin/env python
from setuptools import setup, find_packages


def _read_from_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


def _load_description():
    with open("README.md", "r") as fh:
        return fh.read()


setup_options = dict(
    name='factordb-python',
    version='1.3.0',
    description='The FactorDB client library with Python',
    long_description=_load_description(),
    long_description_content_type='text/markdown',
    author='Ryosuke SATO (@ryosan-470)',
    author_email='rskjtwp@gmail.com',
    url='https://github.com/ryosan-470/factordb-python',
    py_modules=['factordb'],
    packages=find_packages(),
    entry_points={
        'console_scripts': 'factordb = factordb.cli:main'
    },
    install_requires=_read_from_requirements(),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
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
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
    ),
)

setup(**setup_options)

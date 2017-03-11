#!/usr/bin/env python
from setuptools import setup, find_packages


def _read_from_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup_options = dict(
    name='factordb-pycli',
    version='1.0.0',
    description='The FactorDB CLI',
    long_description=open('README.md').read(),
    author='Ryosuke SATO (@ryo-san470)',
    author_email='rskjtwp@gmail.com',
    url='https://github.com/ryo-san470/factordb-pycli',
    py_modules=['factordb'],
    packages=find_packages(),
    entry_points={
        'console_scripts': 'factordb = factordb.cli:main'
    },
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

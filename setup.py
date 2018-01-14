#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import unicode_literals
import os
import glob

from setuptools import setup, find_packages
# from distutils.extension import Extension
# from Cython.Distutils import build_ext
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy as np

try:
    with open('readme.md') as f:
        readme = f.read()
except IOError:
    readme = ''


def _requires_from_file(filename):
    return open(filename).read().splitlines()


extensions = [
    Extension(
        "src.jupiter.cython.make_bid",
        ["src/jupiter/cython/make_bid.pyx"],
        include_dirs=[np.get_include()],
    ),
]

# version
here = os.path.dirname(os.path.abspath(__file__)) + '/src'

version = next((line.split('=')[1].strip().replace("'", '')
                for line in open(os.path.join(here,
                                              'Jupiter',
                                              '__init__.py'))
                if line.startswith('__version__ = ')),
               '0.0.dev0')

# data_files
here = os.path.dirname(os.path.abspath(__file__)) + '/src'
domain_dir = os.path.join(here, 'domain')
datafiles = []
for filename in glob.glob(os.path.join(domain_dir, '*')):
    if os.path.isdir(filename):
        datafiles.append((filename[len(domain_dir) - 10:],
                          glob.glob(os.path.join(filename, '*.xml'))))
# datafiles = glob.glob(os.path.join(domain_dir, '**/*.xml'))

sourcefiles = ['src/jupiter/cython/make_bid.pyx']
setup(
    name="jupiter",
    version=version,
    url='https://github.com/TomoyaFukui/Jupiter',
    author='TomoyaFukui',
    author_email='sumabura6581@gmail.com',
    maintainer='TomoyaFukui',
    maintainer_email='sumabura6581@gmail.com',
    description='Simulator for automatically negotiation',
    long_description=readme,
    packages=find_packages(),
    ext_modules=cythonize(extensions),
    data_files=datafiles,
    install_requires=_requires_from_file('requirements.txt'),
    license="MIT",
    keywords="negotiation, jupiter",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        "console_scripts": [
            "jupiter=src.__main__:main"
        ]
    },
)

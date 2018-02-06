#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import unicode_literals
import os
import glob
import site

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
        "jupiter.simulator.cython.make_bid",
        ["jupiter/simulator/cython/make_bid.pyx"],
        include_dirs=[np.get_include()],
    ),
]

# version
here = os.path.dirname(os.path.abspath(__file__)) + '/jupiter'
version = next((line.split('=')[1].strip().replace("'", '')
                for line in open(os.path.join(here,
                                              'simulator',
                                              '__init__.py'))
                if line.startswith('__version__ = ')),
               '0.0.dev5')

# data_files
# site-packageディレクトリのパスを取得
# ※リストの先頭に"C:\Python34"が入ってるみたいなので最後がsite-packageだと想定して処理します（確実ではなさそうなのでいい方法があったら教えてください）
site_dir = os.path.join(site.getsitepackages()[-1], "jupiter-negotiation")
domain_dir = os.path.join(here, 'domain')
datafiles = []
for filename in glob.glob(os.path.join(domain_dir, '*')):
    if os.path.isdir(filename):
        # datafiles.append((site_dir,
        #                   glob.glob(os.path.join(filename, '*.xml'))))
        datafiles.append((os.path.join(site_dir, filename[len(domain_dir) - 6:]),
                          glob.glob(os.path.join(filename, '*.xml'))))
agents_dir = os.path.join(here, 'agents')
datafiles.append((os.path.join(site_dir, 'agents'),
                  glob.glob(os.path.join(agents_dir, '*.py'))))
# for filename in glob.glob(os.path.join(agents_dir, '*')):
#     datafiles.append((os.path.join(site_dir, filename[len(domain_dir) - 6:]),
#                       glob.glob(os.path.join(filename, '*.py'))))
# datafiles = glob.glob(os.path.join(domain_dir, '**/*.xml'))
# sourcefiles = ['jupiter/simulator/cython/make_bid.pyx']
print(datafiles)
# print("test:", glob.glob(os.path.join(agents_dir, '*.py')))
# print("site:", os.path.join(site_dir, 'agents'))


setup(
    name="jupiter-negotiation",
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
    # package_data=datafiles,
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
            "jupiter=jupiter.__main__:main"
        ]
    },
)

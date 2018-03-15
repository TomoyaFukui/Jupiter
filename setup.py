#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import unicode_literals
import os
import sys
import glob
import site

from setuptools import setup, find_packages
# from distutils.extension import Extension
# from Cython.Distutils import build_ext
from setuptools.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
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
        sources=["jupiter/simulator/cython/make_bid.pyx"],
        include_dirs=[np.get_include()],
    ),
]

# version
# here = os.path.dirname(os.path.abspath(__file__)) + '/jupiter'
here = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'jupiter')
version = next((line.split('=')[1].strip().replace("'", '')
                for line in open(os.path.join(here,
                                              'simulator',
                                              '__init__.py'))
                if line.startswith('__version__ = ')),
               '1.0.2')

# data_files
# site-packageディレクトリのパスを取得
# ※リストの先頭に"C:\Python34"が入ってるみたいなので最後がsite-packageだと想定して処理します（確実ではなさそうなのでいい方法があったら教えてください）
site_dir = os.path.join(site.getsitepackages()[-1], "jupiter-negotiation")
domain_dir = os.path.join(here, 'domain')
datafiles = []
for filename in glob.glob(os.path.join(domain_dir, '*')):
    if os.path.isdir(filename):
        xmlfile_list = []
        for xmlfile_path in glob.glob(os.path.join(filename, '*.xml')):
            xmlfile_list.append(xmlfile_path[xmlfile_path.find("jupiter"):])
        domain_path = site_dir + "/" + filename[len(domain_dir):]
        datafiles.append((domain_path, xmlfile_list))

agents_list = []
agents_dir = os.path.join(here, 'agents')
for i in glob.glob(os.path.join(agents_dir, '*.py')):
    if i.find("__init__.py") > 0:
        continue
    agents_list.append(i[i.find("jupiter"):])
agents_dir_save = os.path.join(site_dir, "agents")
datafiles.append((agents_dir_save, agents_list))
print("-" * 100)
for i in datafiles:
    print(i[0])
    print("\t", i[1])
print("-" * 100)

setup(
    name="jupiter-negotiation",
    version=version,
    url='https://github.com/TomoyaFukui/Jupiter',
    author='TomoyaFukui',
    author_email='sumabura6581@gmail.com',
    maintainer='TomoyaFukui',
    maintainer_email='sumabura6581@gmail.com',
    description='Simulator for automated negotiation',
    long_description=readme,
    packages=find_packages(),
    ext_modules=cythonize(extensions),

    # data_files=datafiles,
    include_package_data=True,

    install_requires=_requires_from_file('requirements.txt'),
    license="MIT",
    keywords="negotiation, jupiter",
    classifiers=[
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        "console_scripts": [
            "jupiter=jupiter.__main__:main"
        ],
    },
    # cmdclass={'build_ext': build_ext}
)

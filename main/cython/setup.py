from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

import numpy as np
# import random
# sourcefiles = ['cython_pyx_code.pyx','cython_c_code.c']
sourcefiles = ['make_bid.pyx']

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("make_bid", sourcefiles, include_dirs=[np.get_include()])],
)

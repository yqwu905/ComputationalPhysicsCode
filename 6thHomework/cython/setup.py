from setuptools import setup
from Cython.Build import cythonize

setup(
 
    ext_modules = cythonize("main_Cython.pyx", annotate=True)
)
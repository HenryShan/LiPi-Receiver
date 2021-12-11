from setuptools import setup
from Cython.Build import cythonize

setup(
    name='LiPi app',
    ext_modules=cythonize("transmit.py"),
    zip_safe=False,
)
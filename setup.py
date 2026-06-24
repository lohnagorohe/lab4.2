from setuptools import setup, Extension
import pybind11

ext_module = Extension(
    'spisok_pybind',
    sources=['spisok_pybind.cpp'],
    include_dirs=[pybind11.get_include()],
    language='c++',
    extra_compile_args=['/std:c++11'],
)

setup(
    name='spisok_pybind',
    version='1.0.0',
    ext_modules=[ext_module],
)
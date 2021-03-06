"""
This type stub file was generated by pyright.
"""

import sys
import re
from distutils.extension import Extension as old_Extension
from typing import Any, Optional

"""distutils.extension

Provides the Extension class, used to describe C/C++ extension
modules in setup scripts.

Overridden to support f2py.

"""
if sys.version_info[0] >= 3:
    basestring = str
cxx_ext_re = re.compile(r'.*[.](cpp|cxx|cc)\Z', re.I).match
fortran_pyf_ext_re = re.compile(r'.*[.](f90|f95|f77|for|ftn|f|pyf)\Z', re.I).match
class Extension(old_Extension):
    def __init__(self, name, sources, include_dirs: Optional[Any] = ..., define_macros: Optional[Any] = ..., undef_macros: Optional[Any] = ..., library_dirs: Optional[Any] = ..., libraries: Optional[Any] = ..., runtime_library_dirs: Optional[Any] = ..., extra_objects: Optional[Any] = ..., extra_compile_args: Optional[Any] = ..., extra_link_args: Optional[Any] = ..., export_symbols: Optional[Any] = ..., swig_opts: Optional[Any] = ..., depends: Optional[Any] = ..., language: Optional[Any] = ..., f2py_options: Optional[Any] = ..., module_dirs: Optional[Any] = ..., extra_f77_compile_args: Optional[Any] = ..., extra_f90_compile_args: Optional[Any] = ...):
        self.sources = ...
        self.swig_opts = ...
        self.depends = ...
        self.language = ...
        self.f2py_options = ...
        self.module_dirs = ...
        self.extra_f77_compile_args = ...
        self.extra_f90_compile_args = ...
    
    def has_cxx_sources(self):
        ...
    
    def has_f2py_sources(self):
        ...
    



"""
This type stub file was generated by pyright.
"""

from __future__ import absolute_import, division, print_function
from .__version__ import version as __version__
from . import ccompiler, unixccompiler
from .info import __doc__
from .npy_pkg_config import *
from typing import Any, Optional

def customized_fcompiler(plat: Optional[Any] = ..., compiler: Optional[Any] = ...):
    ...

def customized_ccompiler(plat: Optional[Any] = ..., compiler: Optional[Any] = ...):
    ...

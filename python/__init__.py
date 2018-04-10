from __future__ import absolute_import

__title__ = 'python-learn'
from python.version import __version__
__author__ = 'Aditya Singhania'
__license__ = 'Apache License 2.0'
__copyright__ = 'Copyright 2018'

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
print(__version__)

from python.data import Data
from python.library import Library
from python.syntax import Syntax

__all__ = [
    'Data', 'Library', 'Syntax'
]

user = Syntax.User()
print(user)


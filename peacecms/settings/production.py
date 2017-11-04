from __future__ import absolute_import, unicode_literals

from .base import *

from .secrets import DEBUG 

try:
    from .local import *
except ImportError:
    pass

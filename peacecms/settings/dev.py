from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
from .secrets import DEBUG 

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k+qkl%)da%vn3^nf9^sq37b!kmobf(mcen5z(-$-7y_9snfsbi'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass

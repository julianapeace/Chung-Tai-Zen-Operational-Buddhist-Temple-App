# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )
from djblog.settings.base import *

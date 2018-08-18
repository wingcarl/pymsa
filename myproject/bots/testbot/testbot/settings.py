import os
import sys

from django.core.wsgi import get_wsgi_application

DJANGO_PROJECT_PATH = '/usr/local/msa/pymsa/myproject'
DJANGO_SETTINGS_MODULE = 'myproject.settings'

sys.path.insert(0, DJANGO_PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = DJANGO_SETTINGS_MODULE
application = get_wsgi_application()

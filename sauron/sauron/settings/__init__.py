# -*- coding: utf-8 -*-
"""
    Settings
    ~~~~~~~~~~~~~~

    A divided settings module.

    :copyright: (c) 2014 by arruda.
"""

import sys
import os


MAIN_APP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DJANGO_ROOT = os.path.dirname(MAIN_APP_ROOT)
SITE_ROOT = os.path.dirname(DJANGO_ROOT)
sys.path.append(DJANGO_ROOT)


from config import *
from installed_apps import *
from logging import *
from utils import get_local_setting

SECRET_KEY = get_local_setting('SECRET_KEY')
#')i1lik@q^ls@$koedw!)#$x#21==_kc7-2w9lz^gmk4@m3!9g9'

ENV_SETTINGS = get_local_setting('ENV_SETTINGS')


NO_DEPRECATION_WARNINGS=False

if ENV_SETTINGS == 'local':
    NO_DEPRECATION_WARNINGS=True
    from env_local import *
elif ENV_SETTINGS == 'vagrant':
    from env_vagrant import *
elif ENV_SETTINGS == 'heroku':
    from env_heroku import *


INSTALLED_APPS += MORE_INSTALLED_APPS

if NO_DEPRECATION_WARNINGS:
    import warnings
    warnings.simplefilter('ignore', DeprecationWarning)



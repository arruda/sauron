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

SECRET_KEY = ')i1lik@q^ls@$koedw!)#$x#21==_kc7-2w9lz^gmk4@m3!9g9'

ON_PRODUCTION = os.environ.has_key('ON_PRODUCTION')

from config import *
from installed_apps import *
from logging import *

NO_DEPRECATION_WARNINGS=False
if not ON_PRODUCTION:
    NO_DEPRECATION_WARNINGS=True
    from env_dev import *
else:
    from env_prod import *

if NO_DEPRECATION_WARNINGS:
    import warnings
    warnings.simplefilter('ignore', DeprecationWarning)


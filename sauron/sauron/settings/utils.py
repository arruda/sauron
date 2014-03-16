# -*- coding: utf-8 -*-
import os
import json
from django.core.exceptions import ImproperlyConfigured

MAIN_APP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DJANGO_ROOT = os.path.dirname(MAIN_APP_ROOT)
SITE_ROOT = os.path.dirname(DJANGO_ROOT)

LOCAL = lambda x: os.path.join(DJANGO_ROOT, x)

CONFS_JSON_PATH = LOCAL('confs.json')
print ">>>", CONFS_JSON_PATH
with open(CONFS_JSON_PATH) as f:
    secrets = json.loads(f.read())

def get_local_setting(key, secrets=secrets):
    "returns a local settings from the file CONFS_JSON_PATH"
    try:
        return secrets[key]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(key)
        raise ImproperlyConfigured(error_msg)

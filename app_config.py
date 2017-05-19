#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
Project-wide application configuration.

DO NOT STORE SECRETS, PASSWORDS, ETC. IN THIS FILE.
They will be exposed to users. Use environment variables instead.
See get_secrets() below for a fast way to access them.
"""

import logging
import os

from authomatic.providers import oauth2
from authomatic import Authomatic

PROJECT_SLUG = 'sitemap_generator'

"""
COPY EDITING
"""
COPY_GOOGLE_DOC_KEY = '1nPQyD797qB0w_9m6R0EEmlh-KE9PsN-fv-ljfEs0yT4'
COPY_PATH = 'data/copy.xlsx'
SITEMAP_PATH = 'data/sitemap_apps.xml'

"""
OAUTH
"""

GOOGLE_OAUTH_CREDENTIALS_PATH = '~/.google_oauth_credentials'

authomatic_config = {
    'google': {
        'id': 1,
        'class_': oauth2.Google,
        'consumer_key': os.environ.get('GOOGLE_OAUTH_CLIENT_ID'),
        'consumer_secret': os.environ.get('GOOGLE_OAUTH_CONSUMER_SECRET'),
        'scope': ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/userinfo.email'],
        'offline': True,
    },
}

authomatic = Authomatic(authomatic_config, os.environ.get('AUTHOMATIC_SALT'))

"""
Logging
"""
LOG_FORMAT = '%(levelname)s:%(name)s:%(asctime)s: %(message)s'

def get_secrets():
    """
    A method for accessing our secrets.
    """
    secrets_dict = {}

    for k, v in os.environ.items():
        if k.startswith(PROJECT_SLUG):
            k = k[len(PROJECT_SLUG) + 1:]
            secrets_dict[k] = v

    return secrets_dict

def configure_targets(deployment_target):
    """
    Configure deployment targets. Abstracted so this can be
    overriden for rendering before deployment.
    """
    global DEPLOYMENT_TARGET
    global LOG_LEVEL


    if deployment_target == 'production':
        LOG_LEVEL = logging.WARNING
    elif deployment_target == 'staging':
        LOG_LEVEL = logging.INFO
    else:
        LOG_LEVEL = logging.INFO

    DEPLOYMENT_TARGET = deployment_target

"""
Run automated configuration
"""
DEPLOYMENT_TARGET = os.environ.get('DEPLOYMENT_TARGET', None)

configure_targets(DEPLOYMENT_TARGET)

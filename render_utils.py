#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import codecs
from datetime import datetime
import json
import logging
import time
import urllib
import subprocess

from flask import Markup, g, render_template, request

import app_config
import copytext

logging.basicConfig(format=app_config.LOG_FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(app_config.LOG_LEVEL)


def flatten_app_config():
    """
    Returns a copy of app_config containing only
    configuration variables.
    """
    config = {}

    # Only all-caps [constant] vars get included
    for k, v in app_config.__dict__.items():
        if k.upper() == k:
            config[k] = v

    return config


def make_context(asset_depth=0):
    """
    Create a base-context for rendering views.
    Includes app_config and JS/CSS includers.

    `asset_depth` indicates how far into the url hierarchy
    the assets are hosted. If 0, then they are at the root.
    If 1 then at /foo/, etc.
    """
    context = flatten_app_config()

    try:
        context['COPY'] = copytext.Copy(app_config.COPY_PATH)
    except copytext.CopyException:
        pass

    return context


def urlencode_filter(s):
    """
    Filter to urlencode strings.
    """
    if type(s) == 'Markup':
        s = s.unescape()

    # Evaulate COPY elements
    if type(s) is not unicode:
        s = unicode(s)

    s = s.encode('utf8')
    s = urllib.quote_plus(s)

    return Markup(s)

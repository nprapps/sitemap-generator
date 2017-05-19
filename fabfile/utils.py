#!/usr/bin/env python
# coding: utf-8
from fabric.api import prompt
from distutils.util import strtobool


def prep_bool_arg(arg):
    return bool(strtobool(str(arg)))


def confirm(message):
    """
    Verify a users intentions.
    """
    answer = prompt(message, default="Not at all")

    if answer.lower() not in ('y', 'yes', 'buzz off', 'screw you'):
        exit()

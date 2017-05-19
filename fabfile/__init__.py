#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import logging
import text
import spreadsheet
import parse_copy
import smb
from fabric.api import task

LOG_FORMAT = '%(levelname)s:%(name)s:%(asctime)s: %(message)s'
LOG_LEVEL = logging.INFO
logging.basicConfig(format=LOG_FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)


@task
def update():
    """
    Update copy
    """
    text.update()


@task
def sitemap():
    """
    Generate sitemap
    """
    text.update()
    parse_copy.generateSitemap()

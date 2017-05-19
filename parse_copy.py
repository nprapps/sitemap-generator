#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import app_config
from jinja2 import Environment, FileSystemLoader
from render_utils import make_context


env = Environment(loader=FileSystemLoader('templates'))


def generateSitemap():
    """
    Generate sitemap from copy
    """
    template_context = make_context()
    template = env.get_template('sitemap.xml')
    output = template.render(**template_context)
    with open(app_config.SITEMAP_PATH, 'wb') as writefile:
        writefile.write(output)

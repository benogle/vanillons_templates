import os
import sys

from paste.script.command import Command
from paste.script.templates import Template
from paste.util.template import paste_script_template_renderer

class VanillonsTemplate(Template):
    _template_dir = 'vanillons'
    summary = 'Vanillons templates! Yeah!'
    template_renderer = staticmethod(paste_script_template_renderer)
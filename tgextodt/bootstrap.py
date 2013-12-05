# -*- coding: utf-8 -*-
"""Setup the tgextodt application"""

from tgextodt import model
from tgext.pluggable import app_model

def bootstrap(command, conf, vars):
    print 'Bootstrapping tgextodt...'

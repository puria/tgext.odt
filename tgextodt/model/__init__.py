# -*- coding: utf-8 -*-
import logging
import tg
from tgext.pluggable import PluggableSession

log = logging.getLogger(__name__)

DBSession = PluggableSession()

def init_model(app_session):
    DBSession.configure(app_session)


def configure_models():
    pass

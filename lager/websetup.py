"""Setup the lager application"""
import logging

from lager.config.environment import load_environment

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup lager here"""
    load_environment(conf.global_conf, conf.local_conf)

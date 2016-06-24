#!/usr/bin/env python
# encoding: utf-8
# vim:ft=python.django:

from .defaults import *

DEBUG = True
BOOTSTRAP3_FORCE_SRC = True
INSTALLED_APPS += ['django_extensions', ]

SPATIALITE_LIBRARY_PATH = 'mod_spatialite'

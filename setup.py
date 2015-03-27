#! /usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import os

try:
    from setuptools import setup
    setuptools_available = True
except:
    from distutils.core import setup
    setuptools_available = False

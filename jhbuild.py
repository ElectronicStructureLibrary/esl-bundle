#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import __builtin__

pkgdatadir = None
datadir = None
import jhbuild
srcdir = os.path.abspath(os.path.join(os.path.dirname(jhbuild.__file__), '..'))

__builtin__.__dict__['PKGDATADIR'] = pkgdatadir
__builtin__.__dict__['DATADIR'] = datadir
__builtin__.__dict__['SRCDIR'] = srcdir

import jhbuild.main
jhbuild.main.main(sys.argv[1:])

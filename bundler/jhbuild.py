#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
if sys.version_info[0] == 2:
    import __builtin__ as builtins
else:
    import builtins

#USE_CHECKOUT_SRC = True

#if USE_CHECKOUT_SRC:
#    sys.path.insert(0, '/home/caliste/local/jhbuild')
#    pkgdatadir = None
#    datadir = None
#    import jhbuild
#    srcdir = os.path.abspath(os.path.join(os.path.dirname(jhbuild.__file__), '..'))
#else:
#    pkgdatadir = "@pkgdatadir@"
#    datadir = "@datadir@"
#    srcdir = "@srcdir@"
#    if '@pythondir@' not in sys.path:
#        sys.path.insert(0, '@pythondir@')
#    try:
#        import jhbuild
#    except ImportError:
#        sys.path.insert(0, srcdir)
pkgdatadir = None
datadir = None
import jhbuild
srcdir = os.path.abspath(os.path.join(os.path.dirname(jhbuild.__file__), '../..'))

builtins.__dict__['PKGDATADIR'] = pkgdatadir
builtins.__dict__['DATADIR'] = datadir
builtins.__dict__['SRCDIR'] = srcdir

import jhbuild.main
jhbuild.main.main(sys.argv[1:])

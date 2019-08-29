#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

if sys.version_info[0] > 2:
    import builtins
    esl_python_ok = True
else:
    import __builtin__ as builtins
    esl_python_ok = False

pkgdatadir = None
datadir = None
srcdir = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0])))

builtins.__dict__['PKGDATADIR'] = pkgdatadir
builtins.__dict__['DATADIR'] = datadir
builtins.__dict__['SRCDIR'] = srcdir

if esl_python_ok:
    sys.path.insert(0, os.path.join(srcdir, "python3"))
else:
    sys.path.insert(0, os.path.join(srcdir, "python2"))

import jhbuild.main
jhbuild.main.main(sys.argv[1:])

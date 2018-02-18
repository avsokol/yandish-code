#!/usr/bin/python

# -*- coding: utf-8 -*-

import sys, os
curdir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.dirname(curdir))

from opts import AppOptions

appOpts = AppOptions()

appOpts.setRcFileName(".yadisktest")

print("Test cfg file: '%s'" % appOpts.getRcFileName())

# ya.saveParamsToRcFile()
# ya.readParamsFromRcFile()

appOpts.printParams()

appOpts.setParam("StartMinimized", 0)
appOpts.setParam("HideOnMinimize", 0)
appOpts.setParam("autorefresh", 30)


appOpts.saveParamsToRcFile()
appOpts.readParamsFromRcFile()

appOpts.printParams()

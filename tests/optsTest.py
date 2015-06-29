#!/usr/bin/python

# -*- coding: utf-8 -*-

import sys, os
curdir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0,os.path.dirname(curdir))

from opts import YaOptions

ya = YaOptions()

ya.setRcFileName(".yadisktest")

print("Test cfg file: '%s'" % ya.getRcFileName())

#ya.saveParamsToRcFile()
#ya.readParamsFromRcFile()

ya.printParams()

ya.setParam("StartMinimized", 0)
ya.setParam("HideOnMinimize", 0)
ya.setParam("autorefresh", 30)


ya.saveParamsToRcFile()
ya.readParamsFromRcFile()

ya.printParams()

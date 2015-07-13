# -*- coding: utf-8 -*-

import os

class AppOptions():
    RCFILE_NAME = ".yandishrc"

    params = {"StartMinimized": "1",
              "HideOnMinimize": "1",
              "autorefresh": "15",
              "yandex-cfg": ""}

    def __init__(self):
        self.readParamsFromRcFile()

    def getRcFileName(self):
        return self.RCFILE_NAME

    def setRcFileName(self,fn):
        self.RCFILE_NAME = fn

    def getRcPath(self):
        return os.path.join(os.environ["HOME"],self.RCFILE_NAME)

    def getParam(self,param):
        if self.params.has_key(param):
            return self.params[param]
        else:
            return "-1"

    def setParam(self,param,value):
        if self.params.has_key(param):
            self.params[param] = value

    def printParams(self):
        for k,v in self.params.items():
            print("'%s' -> '%s'" % (k,v))

    def readParamsFromRcFile(self):
        if os.path.exists(self.getRcPath()) == 0:
            self.saveParamsToRcFile()

        with open(self.getRcPath(), "r") as f:
            for line in f:
                if line.strip() == "":
                    continue
                elements = line.split("=")
                if len(elements) != 2:
                    continue
                key,value = elements[0],elements[1]
                if self.params.has_key(key):
                    self.params[key] = value

    def saveParamsToRcFile(self):
        with open(self.getRcPath(), "w") as f:
            for k,v in self.params.items():
                line = k + "=" + str(v) + "\n"
                f.write(line)

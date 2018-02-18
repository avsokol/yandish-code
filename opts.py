# -*- coding: utf-8 -*-

import os


class AppOptions(object):
    RCFILE_NAME = ".yandishrc"

    params = {
        "StartMinimized": "1",
        "HideOnMinimize": "1",
        "autorefresh": "15",
        "startServiceAtStart": "1",
        "yandex-cfg": ""
    }

    def __init__(self):
        self.readParamsFromRcFile()

    def getRcFileName(self):
        return self.RCFILE_NAME

    def setRcFileName(self, fn):
        self.RCFILE_NAME = fn

    def getRcPath(self):
        return os.path.join(os.environ["HOME"], self.RCFILE_NAME)

    def getParam(self, param):
        if param in self.params.keys():
            return self.params[param]
        else:
            return "-1"

    def setParam(self, param, value):
        if param in self.params.keys():
            self.params[param] = value

    def printParams(self):
        for k, v in self.params.items():
            print("'%s' -> '%s'" % (k, v))

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
                key, value = elements[0], elements[1]
                if key in self.params.keys():
                    self.params[key] = value

    def saveParamsToRcFile(self):
        fn = self.getRcPath()
        fnTmp = fn + ".tmp"
        with open(fnTmp, "w") as f:
            for k, v in self.params.items():
                v = str(v)
                v = v.strip()
                line = k + "=" + v + "\n"
                f.write(line)

        os.rename(fnTmp, fn)

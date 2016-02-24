#!/usr/bin/python

import sys, os, argparse
from subprocess import Popen, PIPE
from opts import AppOptions
from actions import GetAuthFromCfgFile, GetYandexCfgFromCfgFile, GetExcludeDirsFromCfgFile, GetRootDirFromCfgFile, GetProxyFromCfgFile, DoAction, ProcessResult

#############################################################################

def getDefaultParams(action):
    daemon = WhichPrg(action)
    params = {"config": "~/.config/yandex-disk/config.cfg",
              "auth": "~/.config/yandex-disk/passwd",
              "exclude-dirs": [],
              "rootdir": "~/Yandex.Disk",
              "prg": daemon,
              "proxy": "auto"}

    return params

#############################################################################

def showDlg(errMsg):

    from PyQt4 import QtCore, QtGui

    app = QtGui.QApplication(sys.argv)
    msg = QtGui.QMessageBox()
    msg.setIcon(QtGui.QMessageBox.Critical)

    msg.setText("Couldn't find yandex-disk daemon")
    msg.setInformativeText("You have to install yandex-disk daemon from Yandex site.")
    msg.setWindowTitle("Error")
    msg.setDetailedText(errMsg)
    msg.setStandardButtons(QtGui.QMessageBox.Ok)
    sys.exit(msg.exec_())

#############################################################################

def WhichPrg(action):

    PRG = ""

    executable = "yandex-disk"

    proc = Popen(["which", executable], stdout=PIPE, stderr=PIPE)
    return_code = proc.wait()
    if return_code == 0:
        PRG = proc.stdout.read()
        PRG = PRG.strip()
        return PRG.decode("utf8")
    else:
        if action == "widget":
            showDlg("Error " + str(return_code) + ":\nCouldn't find " + executable + " executable\n" + proc.stderr.read())
        else:
            raise Exception("Error %s: Couldn't find '%s' executable\n%s" % (return_code, executable, proc.stderr.read()))

#############################################################################

def ArgParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--program", default="")
    parser.add_argument("-c", "--config", default="")
    parser.add_argument("-d", "--dir", default="")
    parser.add_argument("-a", "--auth", default="")
    parser.add_argument("--proxy", default="")
    parser.add_argument("-x","--exclude-dirs",default=[])
    parser.add_argument("--action",choices=["start","stop","status","widget"],default="widget")

    return parser

#############################################################################

def ShowWidget(params):

    from PyQt4 import QtCore, QtGui
    from PyQt4.QtGui import (QApplication, QFileSystemModel, QTreeView, QTreeWidgetItem, QDirModel)
    from PyQt4.QtCore import pyqtSlot, QObject, QDir, Qt, QModelIndex
    from qt.window import Window
    from opts import AppOptions

    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(os.path.realpath(__file__)), "ico/yandex-disk.xpm")))

    window = Window(params)

    window.initApp()

    sys.exit(app.exec_())

#############################################################################

def tuneParams(params, action):

    defParams = getDefaultParams(action)

    if params["prg"] == "":
        params["prg"] = defParams["prg"]

    if params["config"] == "":
        appOpts = AppOptions()
        appCfg = appOpts.getRcPath()
        params["config"] = GetYandexCfgFromCfgFile(appCfg,0)
    if params["config"] == "":
        params["config"] = defParams["config"]
    params["config"] = os.path.expanduser(params["config"])

    if params["auth"] == "":
        params["auth"] = GetAuthFromCfgFile(params["config"],0)
    if params["auth"] == "":
        params["auth"] = defParams["auth"]
    params["auth"] = os.path.expanduser(params["auth"])

    if params["rootdir"] == "":
        params["rootdir"] = GetRootDirFromCfgFile(params["config"],0)
    if params["rootdir"] == "":
        params["rootdir"] = defParams["rootdir"]
    params["rootdir"] = os.path.expanduser(params["rootdir"])

    if params["proxy"] == "":
        params["proxy"] = GetProxyFromCfgFile(params["config"],0)
    if params["proxy"] == "":
        params["proxy"] = defParams["proxy"]

    if len(params["exclude-dirs"]) == 0:
        params["exclude-dirs"] = GetExcludeDirsFromCfgFile(params["config"],0)
        if params["exclude-dirs"] == [""]:
            params["exclude-dirs"] = []
    else:
        params["exclude-dirs"] = ",".join(params["exclude-dirs"])
    

#############################################################################

def main(argv):

    params = {}

    parser = ArgParser()
    pArgs = parser.parse_args(argv[0:])

    action = pArgs.action
 
    params["prg"] = pArgs.program

    params["config"] = pArgs.config
    params["rootdir"] = pArgs.dir
    params["auth"] = pArgs.auth
    params["exclude-dirs"] = pArgs.exclude_dirs
    params["proxy"] = pArgs.proxy

    tuneParams(params, action)

    if action == "widget":
        ShowWidget(params)
    else:
        res,msg = DoAction(action,params)
        ProcessResult(res,action,msg,params)
        exit(res)

#############################################################################   

if __name__ == "__main__":
    main(sys.argv[1:])

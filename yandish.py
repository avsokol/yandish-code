#!/usr/bin/python

import sys, os, argparse
from subprocess import Popen, PIPE
from opts import AppOptions

#############################################################################

def getDefaultParams():
    daemon = WhichPrg()
    params = {"config": "~/.config/yandex-disk/config.cfg",
              "auth": "~/.config/yandex-disk/passwd",
              "exclude_dirs": [],
              "rootdir": "~/Yandex.Disk",
              "prg": daemon,
              "proxy": "no"}

    return params

#############################################################################

def WhichPrg():

    PRG = ""

    executable = "yandex-disk"

    proc = Popen(["which", executable], stdout=PIPE, stderr=PIPE)
    return_code = proc.wait()
    if return_code == 0:
        PRG = proc.stdout.read()
        PRG = PRG.strip()
        return PRG
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

    appOpts = AppOptions()
    startMinimized = appOpts.getParam("StartMinimized")
    if startMinimized == 0:
        window.show()
    window.updateTrayMenuState()
    window.refreshStatus()

    sys.exit(app.exec_())

#############################################################################

def main(argv):

    from actions import GetAuthFromCfgFile, GetYandexCfgFromCfgFile, GetExcludeDirsFromCfgFile, GetRootDirFromCfgFile, DoAction, ProcessResult

    defParams = getDefaultParams()

    parser = ArgParser()
    pArgs = parser.parse_args(argv[0:])
 
    prg = pArgs.program
    cfgfile = pArgs.config
    rootdir = pArgs.dir
    auth = pArgs.auth
    exclude_dirs = pArgs.exclude_dirs
    proxy = pArgs.proxy
    action = pArgs.action

    if prg == "":
        prg = defParams["prg"]

    if cfgfile == "":
        appOpts = AppOptions()
        appCfg = appOpts.getRcPath()
        cfgfile = GetYandexCfgFromCfgFile(appCfg,0)
    if cfgfile == "":
        cfgfile = defParams["config"]
    cfgfile = os.path.expanduser(cfgfile)

    if auth == "":
        auth = GetAuthFromCfgFile(cfgfile,0)
    if auth == "":
        auth = defParams["auth"]
    auth = os.path.expanduser(auth)

    if rootdir == "":
        rootdir = GetRootDirFromCfgFile(cfgfile,0)
    if rootdir == "":
        rootdir = defParams["rootdir"]
    rootdir = os.path.expanduser(rootdir)

    if proxy == "":
        proxy = defParams["proxy"]

    if len(exclude_dirs) == 0:
        exclude_dirs = GetExcludeDirsFromCfgFile(cfgfile,0)
        if exclude_dirs == [""]:
            exclude_dirs = []
    else:
        exclude_dirs = ",".join(exclude_dirs)

    params = {"prg": prg,
              "config": cfgfile,
              "auth": auth,
              "exclude-dirs": exclude_dirs,
              "dir": rootdir,
              "proxy": proxy}

    if action == "widget":
        ShowWidget(params)
    else:
        res,msg = DoAction(action,params)
        ProcessResult(res,action,msg,params)
        exit(res)

#############################################################################   

if __name__ == "__main__":
    main(sys.argv[1:])

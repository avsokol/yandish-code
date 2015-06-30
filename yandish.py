#!/usr/bin/python

import sys, os

#############################################################################

def ParseArgs(argv):

    if len(argv) == 0:
        return "widget"

    if len(argv) > 1:
        raise Exception("Only one argument can be accepted")

    known_actions = ["start","stop","status","widget"]
    action = argv[0]

    result = next((i for i, v in enumerate(known_actions) if v == action), None)

    if result == None:
        raise Exception("Possible values: '%s'" % ",".join(known_actions))

    return action

#############################################################################

def ShowWidget():

    from PyQt4 import QtCore, QtGui
    from PyQt4.QtGui import (QApplication, QFileSystemModel, QTreeView, QTreeWidgetItem, QDirModel)
    from PyQt4.QtCore import pyqtSlot, QObject, QDir, Qt, QModelIndex
    from qt.window import Window
    from actions import FindRootDir
    from opts import YaOptions

    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(os.path.realpath(__file__)), "ico/yandex-disk.xpm")))

    window = Window()

    window.initApp(FindRootDir())

    yaOpts = YaOptions()
    startMinimized = yaOpts.getParam("StartMinimized")
    if startMinimized == 0:
        window.show()
    window.updateTrayMenuState()
    window.refreshStatus()

    sys.exit(app.exec_())

#############################################################################

def main(argv):

    action = ParseArgs(argv)

    import init
    from actions import AppendExcludedDir, FindExcludedDirs
    is_running,message = init.Init()

    excl_dirs = FindExcludedDirs()
    for element in excl_dirs:
        if element != "":
            init.AppendExcludedDir(element)

    if action == "widget":
        ShowWidget()
    else:
        import actions
        res,msg = actions.DoAction(action)
        actions.ProcessResult(res,action,msg)
        exit(res)

#############################################################################   

if __name__ == "__main__":
    main(sys.argv[1:])

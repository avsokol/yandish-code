import os, re
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import *

from wlayout import Ui_MainWindow
import actions
from about import Ui_Dialog
from trayIcon import SystemTrayIcon
from opts import YaOptions

import threading

class About(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

class Window(QMainWindow, Ui_MainWindow):

    _removeItems = []

    _geometry = None

    _prg = None
    _config = None
    _dir = None
    _auth = None
    _exclude_dirs = None

    def __init__(self, params, parent = None):

        self._prg = params["prg"]
        self._config = params["config"]
        self._dir = params["dir"]
        self._auth = params["auth"]
        self._exclude_dirs = params["exclude-dirs"]

        QMainWindow.__init__(self, parent)

        self.setupUi(self)
        self.setSignals()
        self.tIcon = SystemTrayIcon(self)

        self.uTimer = QtCore.QTimer()
        QtCore.QObject.connect(self.uTimer, QtCore.SIGNAL("timeout()"), self.refreshStatus)

        is_running,message = actions.IsDaemonRunning(self._prg)
        if is_running:
            self.startTimer()

    def getParams(self):
        return {"prg": self._prg,
                "config": self._config,
                "auth": self._auth,
                "exclude-dirs": self._exclude_dirs,
                "dir": self._dir}

    def startTimer(self):
        if self.refreshTimeout.value() > 0 and self.isTimerActive() == False:
            self.uTimer.start(self.refreshTimeout.value() * 1000)
        if self.refreshTimeout.value() == 0 and self.isTimerActive():
            self.uTimer.stop()

    def stopTimer(self):
        self.uTimer.stop()

    def isTimerActive(self):
        return self.uTimer.isActive()

    def restartTimer():
        if self.isTimerActive():
            self.stopTimer()
        self.startTimer()

    def closeEvent(self, event):
        self.hide()
        event.ignore()

    def event(self, event):
        if (event.type() == QtCore.QEvent.WindowStateChange and self.isMinimized()):
            yaOpts = YaOptions()
            HideOnMinimize = yaOpts.getParam("HideOnMinimize")
            if HideOnMinimize:
                self.hide()
            return True
        else:
            return super(Window, self).event(event)

    def screenGeometry(self):
        g = QApplication.desktop().screenGeometry()
        return g.width(), g.height()

    def hide(self):
        self._geometry = self.saveGeometry()
        super(Window, self).hide()

    def show(self):
        if self._geometry == None:
            X,Y = self.screenGeometry()
            w = 640
            h = 480
            x = (X-w)/2
            y = (Y-w)/2
            self.setGeometry(QtCore.QRect(x, y, w, h))
        else:
            self.restoreGeometry(self._geometry)
        super(Window, self).show()

    def updateTrayMenuState(self):
        self.tIcon.updateTrayMenuState()

    def fillOptionsTab(self):
        self.yandex_exec.setText(self._prg)
        self.yandex_exec.setEnabled(False)
        self.yandex_cfg.setText(self._config)
        self.yandex_cfg.setEnabled(False)
        self.yandex_root.setText(self._dir)
        self.yandex_root.setReadOnly(True)
        self.yandex_auth.setText(self._auth)
        self.yandex_auth.setReadOnly(True)

        yaOpts = YaOptions()
        HideOnMinimize = yaOpts.getParam("HideOnMinimize")
        StartMinimized = yaOpts.getParam("StartMinimized")
        refreshPeriod = yaOpts.getParam("autorefresh")
        self.checkBox_1.setChecked(StartMinimized)
        self.checkBox_2.setChecked(HideOnMinimize)
        self.refreshTimeout.setProperty("value", refreshPeriod)

    def reloadOptions(self):
        self.fillOptionsTab()
        root = self.treeWidget.invisibleRootItem()
        self.checkChildren(root)
        for path in self._exclude_dirs:
            self.uncheckPath(path, 0)

    def saveYandexOptions(self):
        yandex_cfg = self.yandex_cfg.text()
        yandex_root = self.yandex_root.text()
        yandex_auth = self.yandex_auth.text()

        self._excluded_dirs = self.getExcludedDirsFromTree()
        dirs = ",".join(self._exclude_dirs)

        params = {"auth": yandex_auth, "dir": yandex_root, "exclude-dirs": dirs}
        actions.SaveParamsInCfgFile(params,self._config)

    def saveWindowOptions(self):
        yaOpts = YaOptions()
        StartMinimized = self.checkBox_1.isChecked()
        HideOnMinimize = self.checkBox_2.isChecked()
        refreshPeriod =  self.refreshTimeout.value()
        yaOpts.setParam("HideOnMinimize",HideOnMinimize)
        yaOpts.setParam("StartMinimized",StartMinimized)
        yaOpts.setParam("autorefresh",refreshPeriod)
        yaOpts.saveParamsToRcFile()

    def saveOptions(self):
        self.saveYandexOptions()
        self.saveWindowOptions()

    def chooseRootDir(self):
        dirname = QtGui.QFileDialog.getExistingDirectory(self, "Select Directory to be the root for Yandex Disk", self.yandex_root.text())
        if dirname != "":
            self._dir = str(dirname)
            self.yandex_root.setText(dirname)

    def chooseAuthFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, "Select Yandex Auth File", os.environ["HOME"])
        if filename != "":
            self._auth = str(filename)
            self.yandex_auth.setText(filename)

    def getPathFromItem(self,item):
        path = []

        text = str(item.text(0).toUtf8())
        text = re.sub(" ->.*","",text)
        path.insert(0, text)

        while item.parent() != None:
            text = str(item.parent().text(0).toUtf8())
            text = re.sub(" ->.*","",text)
            path.insert(0, text)
            item = item.parent()

        path = "/".join(path)
        return path

    def isChildToBeRemoved(self, path):
        try:
            os.lstat(path)
            exists = 1
        except:
            exists = 0

        if exists == 0 or (exists == 1 and os.path.isdir(path) and os.path.exists(path) == 0 ):
            return 1
        else:
            return 0

    def rmItem(self,parent,item):
        parent.removeChild(item)

    def addItem(self,parentItem,path,properties,exists):

        child = self.findPathItem(path, 0)
        if child == "" or child == None:
            child = self.createChild(parentItem,path)
            self.setItemProperties(child,properties)
            if exists:
                threadAdd = threading.Thread(target=self.addDirAsTreeItem, args = (path,child))
                threadAdd.daemon = True
                threadAdd.start()

    def checkAndRmUnusedTreeItem(self,parentItem=""):
        if parentItem == "" or parentItem == None:
            parentItem = self.treeWidget.invisibleRootItem()

        for i in range(parentItem.childCount()):
            child = parentItem.child(i)
            try:
                path = self.getPathFromItem(child)
            except:
                continue
            path = os.path.join(self._dir,path)

            res = self.isChildToBeRemoved(path)

            if res:
                self._removeItems.append(path)
            else:
                self.checkAndRmUnusedTreeItem(child)

    def getPathProperties(self,path):
        exists = 0
        is_link = 0
        target = ""

        if os.path.isdir(path):
            exists = 1
        if os.path.islink(path):
            is_link = 1
            target = os.readlink(path)
            if os.path.exists(target):
                exists = 1
            else:
                exists = 0

        if path in self._exclude_dirs:
            exists = 0

        return exists,is_link,target

    def prepareItemProperties(self,text,exists,is_link,target):

        properties = {"itemText": text.decode("utf8"),
                      "foreground": Qt.black,
                      "checkable": 1,
                      "state": Qt.Unchecked}

        if is_link:
            text = text + " -> " + target
        properties["itemText"] = text.decode("utf8")

        if is_link == 1 and exists == 0:
            properties["foreground"] = Qt.red
            properties["checkable"] = 0

        if exists:
            properties["state"] = Qt.Checked

        return properties

    def setItemProperties(self,child,properties):
        child.setText(0, properties["itemText"])
        child.setForeground(0, properties["foreground"])
        if properties["checkable"]:
            child.setFlags(child.flags()|Qt.ItemIsUserCheckable|Qt.ItemIsSelectable)
        else:
            child.setFlags(child.flags()^Qt.ItemIsUserCheckable^Qt.ItemIsSelectable)
        child.setCheckState(0, properties["state"])

    def isChildToBeCreated(self,path):
        path = path.lstrip(self._dir)

        child = self.findPathItem(path, 0)

        if child == "" or child == None:
            return 1
        else:
            return 0

    def createChild(self,parentItem,path):
        if parentItem == "root":
            child = QTreeWidgetItem(self.treeWidget)
            self.treeWidget.itemBelow(child)
        else:
            child = QTreeWidgetItem(parentItem)
            parentItem.addChild(child)

        return child

    def addDirAsTreeItem(self,parentDir="",parentItem="root"):
        if parentDir == "":
            parentDir = self._dir

        if os.path.exists(parentDir) == 0:
            return

        dirs = os.listdir(parentDir)
        for d in sorted(dirs):
            path = os.path.join(parentDir,d)

            if os.path.isfile(path):
                pass
            elif d == ".sync":
                pass
            else:
                exists,is_link,target = self.getPathProperties(path)
                properties = self.prepareItemProperties(d,exists,is_link,target)
                if self.isChildToBeCreated(path):
                    self.emit(QtCore.SIGNAL("addChild"),parentItem,path,properties,exists)

    def findUncheckedItemsAmongChildren(self, items, parentItem, column=0):
        if parentItem == "" or parentItem == None:
            parentItem = self.treeWidget.invisibleRootItem()

        for i in range(parentItem.childCount()):
            if parentItem.child(i).checkState(0) == 0:
                items.append(parentItem.child(i))
            else:
                self.findUncheckedItemsAmongChildren(items, parentItem.child(i), column)
        return items

    def findItemAmongChildren(self, parentItem, textToFind, column=0):
        if parentItem == "" or parentItem == None:
            parentItem = self.treeWidget.invisibleRootItem()

        for i in range(parentItem.childCount()):
            if re.search(textToFind + "( ->.)*", parentItem.child(i).text(column).toUtf8()):
                return parentItem.child(i)

    def findPathItem(self, pathToFind, column = 0):
        path = pathToFind.split("/")

        index = ""
        for i in path:
            try:
                index = self.findItemAmongChildren(index, i, column)
            except:
                return None

        return index

    def changeCheckStateForPath(self, pathToFind, state, column=0):
        item = self.findPathItem(pathToFind, column)
        if item == "" or item == None:
            pass
        else:
            item.setCheckState(column, state)

    def checkPath(self, pathToFind, column=0):
        self.changeCheckStateForPath(pathToFind, Qt.Checked, column=0)

    def uncheckPath(self, pathToFind, column=0):
        self.changeCheckStateForPath(pathToFind, Qt.Unchecked, column=0)

    def checkChildren(self,item):
        for i in range(item.childCount()):
            if item.child(i).flags() & QtCore.Qt.ItemIsUserCheckable:
                item.child(i).setCheckState(0, Qt.Checked)
                if item.child(i).childCount() > 0:
                    self.checkChildren(item.child(i))
        
    def checkParent(self,item):
        if item.parent() <> None:
            item.parent().setCheckState(0, Qt.Checked)
            self.checkParent(item.parent())

    def handleItemChecked(self,item):
        self.checkChildren(item)
        self.checkParent(item)

    def handleItemUnchecked(self,item):
        for i in range(item.childCount()):
            item.child(i).setCheckState(0, Qt.Unchecked)
            if item.child(i).childCount() > 0:
                self.handleItemUnchecked(item.child(i))

    def handleitemChanged(self,item):
        self.treeWidget.blockSignals(True)
        if item.checkState(0) == QtCore.Qt.Checked:
            self.handleItemChecked(item)
        elif item.checkState(0) == QtCore.Qt.Unchecked:
            self.handleItemUnchecked(item)
        self.treeWidget.blockSignals(False)

    def getExcludedDirsFromTree(self):
        paths = []
        items = []
        items = self.findUncheckedItemsAmongChildren(items,"")
        for item in items:
            path = self.getPathFromItem(item)
            paths.append(path)

        return paths

    def saveTreeExcludedDirs(self):
        self._excluded_dirs = self.getExcludedDirsFromTree()
        actions.SaveExcludedDirs(self._exclude_dirs,self._config)

    def refreshTree(self):
        if os.path.exists(self._dir) == False:
            os.mkdir(self._dir)
        self.treeWidget.clear()
        self.refreshStatus()

    def initApp(self):
        self.fillOptionsTab()
        self.refreshTree()

        self.treeWidget.expandToDepth(False)
        self.treeWidget.itemChanged.connect(self.handleitemChanged)
        self.updateActionButtons()

    def actionWaitCursor(function):
        def new_function(self,action):
            QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
            self.setButtonInState(action,"disabled")

            QtGui.QApplication.processEvents()
            QtGui.QApplication.processEvents()

            function(self,action)

            self.setButtonInState(action,"enabled")
            QApplication.restoreOverrideCursor()
            self.updateActionButtons()
        return new_function

    def waitCursor(function):
        def new_function(self):
            QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

            QtGui.QApplication.processEvents()
            QtGui.QApplication.processEvents()

            function(self)

            QApplication.restoreOverrideCursor()
        return new_function

    @actionWaitCursor
    def actService(self,action):
        if action == "start":
            self.saveTreeExcludedDirs()
        params = self.getParams()
        res,msg = actions.DoAction(action,params)
        text_msg = actions.ProcessResult(res,action,msg,params,0)

        cur_text = self.textEdit.toPlainText()
        new_text = text_msg.decode("utf8")

        if new_text != cur_text:
            self.textEdit.clear()
            self.textEdit.append(new_text)
            self.tIcon.updateToolTip(new_text)

        is_running,message = actions.IsDaemonRunning(self._prg)
        if is_running:
            self.startTimer()
        else:
            self.stopTimer()

    def refreshStatus(self):
        self.actService("status")

        if self.isHidden() == False:
            self.connect(self, QtCore.SIGNAL("addChild"), self.addItem)

            threadAdd = threading.Thread(target=self.addDirAsTreeItem)
            threadAdd.daemon = True
            threadAdd.start()

            threadRm = threading.Thread(target=self.checkAndRmUnusedTreeItem)
            threadRm.daemon = True
            threadRm.start()
            threadRm.join()

            for path in self._removeItems:
                path = path.lstrip(self._dir)
                child = self.findPathItem(path, 0)
                if child != None:
                    parent = child.parent()
                    if parent == None:
                        parent = self.treeWidget.invisibleRootItem()
                    parent.removeChild(child)
            self._removeItems = []

    def handleSpinChange(self):
        self.refreshStatus()
        self.restartTimer()

    #@waitCursor
    def showAbout(self):
        about = About()
        about.exec_()

    def updateActionButtons(self):
        is_running,message = actions.IsDaemonRunning(self._prg)
        if is_running:
            self.setButtonInState("start","disabled")
            self.setButtonInState("stop","enabled")
        else:
            self.setButtonInState("stop","disabled")
            self.setButtonInState("start","enabled")

    def setButtonInState(self,button,state):
        if button == "start":
            btn = self.btnStart
        elif button == "stop":
            btn = self.btnStop
        elif button == "status":
            return
        else:
            raise Exception("Unknown button '%s'" % button)

        if state == "disabled":
            btn.setEnabled(False)
        elif state == "enabled":
            btn.setEnabled(True)
        else:
            pass

    def setSignals(self):
        QtCore.QObject.connect(self.btnExit, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)

        QtCore.QObject.connect(self.btnStart, QtCore.SIGNAL("clicked()"), lambda: self.actService("start"))
        QtCore.QObject.connect(self.btnStop, QtCore.SIGNAL("clicked()"), lambda: self.actService("stop"))
        QtCore.QObject.connect(self.btnStatus, QtCore.SIGNAL("clicked()"), self.refreshStatus)

        QtCore.QObject.connect(self.actionStart, QtCore.SIGNAL("activated()"), lambda: self.actService("start"))
        QtCore.QObject.connect(self.actionStop, QtCore.SIGNAL("activated()"), lambda: self.actService("stop"))
        QtCore.QObject.connect(self.actionStatus, QtCore.SIGNAL("activated()"), self.refreshStatus)

        QtCore.QObject.connect(self.actionReloadCfg, QtCore.SIGNAL("activated()"), self.reloadOptions)
        QtCore.QObject.connect(self.actionSaveCfg, QtCore.SIGNAL("activated()"), self.saveOptions)

        QtCore.QObject.connect(self.ch_yandex_root, QtCore.SIGNAL("clicked()"), self.chooseRootDir)
        QtCore.QObject.connect(self.ch_yandex_auth, QtCore.SIGNAL("clicked()"), self.chooseAuthFile)

        QtCore.QObject.connect(self.actionAbout, QtCore.SIGNAL("activated()"), self.showAbout)

        QtCore.QObject.connect(self.refreshTimeout, QtCore.SIGNAL("editingFinished()"), self.handleSpinChange)

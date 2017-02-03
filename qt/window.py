import os
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import *

from .wlayout import Ui_MainWindow
import actions
from .about import Ui_Dialog
from .trayIcon import SystemTrayIcon
from opts import AppOptions
from yandish import getDefaultParams, tuneParams
from .runWiz import yaWizard

import threading

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class About(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)


class Window(QMainWindow, Ui_MainWindow):

    _removeItems = []
    _threads = []

    _geometry = None

    _prg = None
    _config = None
    _rootdir = None
    _auth = None
    _exclude_dirs = None
    _proxy = None

    _service_err = 0

    def __init__(self, params, parent=None):

        self.paramsInit(params)

        QMainWindow.__init__(self, parent)

        self.setupUi(self)
        self.setSignals()
        self.tIcon = SystemTrayIcon(self)

        self.uTimer = QtCore.QTimer()
        QtCore.QObject.connect(self.uTimer, QtCore.SIGNAL("timeout()"), self.refreshStatus)

        #is_running,message = actions.IsDaemonRunning(self._prg)
        #if is_running:
        self.startTimer()

    def paramsInit(self,params):
        self._prg = params["prg"]
        self._config = params["config"]
        self._rootdir = params["rootdir"]
        self._auth = params["auth"]
        self._exclude_dirs = params["exclude-dirs"]
        self._proxy = params["proxy"]

    def getParams(self):
        return {"prg": self._prg,
                "config": self._config,
                "auth": self._auth,
                "exclude-dirs": self._exclude_dirs,
                "rootdir": self._rootdir}

    def startTimer(self):
        if self.refreshTimeout.value() > 0 and self.isTimerActive() == False:
            self.uTimer.start(self.refreshTimeout.value() * 1000)

        if self.refreshTimeout.value() == 0 and self.isTimerActive():
            self.uTimer.stop()

    def stopTimer(self):
        self.uTimer.stop()

    def isTimerActive(self):
        return self.uTimer.isActive()

    def restartTimer(self):
        if self.isTimerActive():
            self.stopTimer()

        self.startTimer()

    def closeEvent(self, event):
        self.hide()
        event.ignore()

    def event(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange and self.isMinimized():
            appOpts = AppOptions()
            HideOnMinimize = int(appOpts.getParam("HideOnMinimize"))
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
            w = self.width()
            h = self.height()
            x = (X-w)/2
            y = (Y-w)/2
            self.setGeometry(QtCore.QRect(x, y, w, h))
        else:
            self.restoreGeometry(self._geometry)

        super(Window, self).show()

    def updateTrayMenuState(self):
        self.tIcon.updateTrayMenuState()

    def fillOptions(self):
        self.yandex_exec.setText(self._prg)
        self.yandex_exec.setEnabled(False)
        self.yandex_cfg.setText(self._config)
        self.yandex_cfg.setReadOnly(True)
        self.yandex_root.setText(self._rootdir)
        self.yandex_root.setReadOnly(True)
        self.yandex_auth.setText(self._auth)
        self.yandex_auth.setReadOnly(True)

        if self._proxy == "no":
            self.proxyNone.setChecked(1)
            self.proxyDisable()
        elif self._proxy == "auto":
            self.proxyAuto.setChecked(1)
            self.proxyDisable()
        else:
            self.proxyManual.setChecked(1)
            self.proxyEnable()
            proxy_params = self._proxy.split(",")

            pType = proxy_params[0].upper()
            server = proxy_params[1]
            port = proxy_params[2]

            pTypes = [ self.proxyType.itemText(i) for i in range(self.proxyType.count()) ]
            if pType in pTypes:
                self.proxyType.setCurrentIndex(pTypes.index(pType))

            self.srvName.setText(server)
            self.portNumber.setText(port)

            if pType in [ "HTTPS", "SOCKS5" ]:
                self.srvPasswordReq.setEnabled(True)

                login = ""
                password = ""

                if len(proxy_params) > 3:
                    login = proxy_params[3]
                if len(proxy_params) > 4:
                    password = proxy_params[4]

                if login == "" and password == "":
                    self.srvPasswordReq.setChecked(0)
                else:
                    self.srvPasswordReq.setChecked(1)

                self.srvLogin.setText(login)
                self.srvPassword.setText(password)
            else:
                self.srvPasswordReq.setEnabled(False)

            self.toggleProxyAuthReq()

        appOpts = AppOptions()
        HideOnMinimize = int(appOpts.getParam("HideOnMinimize"))
        StartMinimized = int(appOpts.getParam("StartMinimized"))
        startServiceAtStart = int(appOpts.getParam("startServiceAtStart"))
        refreshPeriod = int(appOpts.getParam("autorefresh"))
        self.startHidden.setChecked(StartMinimized)
        self.hideOnMinimize.setChecked(HideOnMinimize)
        self.startServiceAtStart.setChecked(startServiceAtStart)
        self.refreshTimeout.setProperty("value", refreshPeriod)

    def reloadOptions(self):
        self.fillOptions()

        self.refreshTree(0,1)

        root = self.treeWidget.invisibleRootItem()
        self.checkChildren(root)
        for path in self._exclude_dirs:
            self.uncheckPath(path, 0)

    def getProxyCfg(self):
        if self.proxyNone.isChecked():
            self._proxy = "none"
        elif self.proxyAuto.isChecked():
            self._proxy = "auto"
        elif self.proxyManual.isChecked():
            proxy_params = []
            pType = str(self.proxyType.currentText()).lower()
            proxy_params.append(pType)

            server = str(self.srvName.text())
            port = str(self.portNumber.text())

            proxy_params.append(server)
            proxy_params.append(port)

            if self.srvPasswordReq.isEnabled() and self.srvPasswordReq.isChecked():
                login = str(self.srvLogin.text())
                password = str(self.srvPassword.text())
                proxy_params.append(login)
                proxy_params.append(password)

            self._proxy = ",".join(proxy_params)
        else:
            raise Exception("Unexpected proxy configuration")

    def saveYandexOptions(self):

        self.getProxyCfg()

        yandex_cfg = self.yandex_cfg.text()
        yandex_root = self.yandex_root.text()
        yandex_auth = self.yandex_auth.text()
        yandex_proxy = self._proxy

        self._exclude_dirs = self.getExcludeDirsFromTree()
        dirs = ",".join(self._exclude_dirs)

        params = {"auth": yandex_auth, "dir": yandex_root, "exclude-dirs": dirs, "proxy": yandex_proxy}
        actions.SaveParamsInCfgFile(params,self._config)

    def saveAppOptions(self):
        appOpts = AppOptions()
        if self.startHidden.isChecked():
            StartMinimized = "1"
        else:
            StartMinimized = "0"

        if self.hideOnMinimize.isChecked():
            HideOnMinimize = "1"
        else:
            HideOnMinimize = "0"

        if self.startServiceAtStart.isChecked():
            startServiceAtStart = "1"
        else:
            startServiceAtStart = "0"

        refreshPeriod =  str(self.refreshTimeout.value())

        yandex_cfg = self.yandex_cfg.text()

        defParams = getDefaultParams("widget")

        yandexcfg = yandex_cfg

        appOpts.setParam("HideOnMinimize",HideOnMinimize)
        appOpts.setParam("StartMinimized",StartMinimized)
        appOpts.setParam("autorefresh",refreshPeriod)
        appOpts.setParam("startServiceAtStart",startServiceAtStart)
        appOpts.setParam("yandex-cfg",yandexcfg)
        appOpts.saveParamsToRcFile()

    def saveOptions(self):
        self.saveYandexOptions()
        self.saveAppOptions()

    def chooseRootDir(self):
        dirname = QtGui.QFileDialog.getExistingDirectory(self, "Select Directory to be the root for Yandex Disk",
                                                         self.yandex_root.text())
        if dirname != "":
            self._rootdir = str(dirname.toUtf8())
            self.yandex_root.setText(dirname)
            self.refreshTree(1,1)

    def chooseAuthFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, "Select Yandex Auth File", os.environ["HOME"])
        if filename != "":
            self._auth = str(filename)
            self.yandex_auth.setText(filename)

    def chooseCfgFile(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, "Select Yandex Configuration File", os.environ["HOME"])
        if filename != "":
            self._config = str(filename)
            self.yandex_cfg.setText(filename)

            self.saveOptions()

    def getPathFromItem(self,item):
        path = []

        text = str(item.text(0).toUtf8())
        path.insert(0, text)

        while item.parent() is not None:
            text = str(item.parent().text(0).toUtf8())
            path.insert(0, text)
            item = item.parent()

        path = "/".join(path)
        return path

    def addItem(self,path,properties):
        item = self.findPathItem(path)
        if item == None:
            item = self.createChild(path)
        if item != None:
            self.setItemProperties(item,properties)

    def modifyItem(self,path,properties):
        item = self.findPathItem(path)
        if item == None:
            pass
        else:
            modifyState = 0
            if properties['checkable'] == 0:
                modifyState = 1

            self.setItemProperties(item,properties, modifyState=modifyState)
            if properties["checkable"] == 0:
                for i in range(item.childCount()):
                    child = item.child(i)
                    item.removeChild(child)

    def removeItem(self, path):
        item = self.findPathItem(path)
        if item is None:
            if path in self._removeItems:
                self._removeItems.remove(path)
        else:
            parent = item.parent()
            if parent is None:
                parent = self.treeWidget.invisibleRootItem()
            parent.removeChild(item)
            if path in self._removeItems:
                self._removeItems.remove(path)
            if path in self._exclude_dirs:
                self._exclude_dirs.remove(path)

    def checkAndRmUnusedTreeItem(self, parentItem=""):
        if parentItem == "" or parentItem is None:
            parentItem = self.treeWidget.invisibleRootItem()

        for i in range(parentItem.childCount()):
            child = parentItem.child(i)
            try:
                path = self.getPathFromItem(child)
            except:
                continue
            path = os.path.join(self._rootdir,path)

            if self.isChildToBeRemoved(path):
                path = path.lstrip(self._rootdir)
                if path in self._removeItems:
                    pass
                else:
                    self._removeItems.append(path)
                    #self.emit(QtCore.SIGNAL("removeChild"),path)
            else:
                self.checkAndRmUnusedTreeItem(child)

    def getItemProperties(self, item):
        properties = {"itemText": [str(item.text(0).toUtf8()), str(item.text(1).toUtf8())],
                      "foreground": item.foreground(0),
                      "checkable": 1,
                      "state": item.checkState(0)}

        if item.flags() & QtCore.Qt.ItemIsUserCheckable:
            properties["checkable"] = 1
        else:
            properties["checkable"] = 0

        return properties

    def getPathProperties(self,path):
        exists = 0
        is_link = 0
        target = ""
        state = Qt.Checked

        if os.path.isdir(path):
            exists = 1
        if os.path.islink(path):
            is_link = 1
            target = os.readlink(path)
            if os.path.exists(target):
                exists = 1
            else:
                exists = 0

        if path.lstrip(self._rootdir) in self._exclude_dirs:
            state = Qt.Unchecked

        return exists,is_link,target,state

    def prepareItemProperties(self, path, text, exists, is_link, target, state):

        properties = {"itemText": [text, ""],
                      "foreground": Qt.black,
                      "checkable": 1,
                      "state": state}

        while path != "":
            if path in self._exclude_dirs:
                properties["state"] = Qt.Unchecked
                break
            path = os.path.dirname(path)

        text0 = text.decode("utf8")
        text1 = ""
        if is_link:
            text1 = " -> " + target
        properties["itemText"] = [text0,text1.decode("utf8")]

        if is_link == 1 and exists == 0:
            properties["foreground"] = Qt.red
            properties["checkable"] = 0

        return properties

    def setItemProperties(self, child, properties, modifyState=1):
        child.setText(0, properties["itemText"][0])
        child.setText(1, properties["itemText"][1])
        child.setForeground(0, properties["foreground"])
        child.setForeground(1, properties["foreground"])
        child.setToolTip(0, properties["itemText"][0])
        child.setToolTip(1, properties["itemText"][1])

        if modifyState:
            child.setCheckState(0, properties["state"])

        if properties["checkable"]:
            folderIcon = QtGui.QIcon()
            folderIcon.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                                      "../ico/folder_closed.png"))),
                                 QtGui.QIcon.Normal, QtGui.QIcon.Off)
            folderIcon.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                                      "../ico/folder.png"))),
                                 QtGui.QIcon.Normal, QtGui.QIcon.On)
            child.setIcon(0, folderIcon)
            child.setFlags(child.flags()|Qt.ItemIsUserCheckable|Qt.ItemIsSelectable)
        else:
            errIcon = QtGui.QIcon()
            errIcon.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                                   "../ico/folder_error.png"))),
                              QtGui.QIcon.Normal, QtGui.QIcon.Off)
            child.setIcon(0, errIcon)
            child.setFlags(child.flags()^Qt.ItemIsUserCheckable^Qt.ItemIsSelectable)

    def isChildExists(self, path):

        child = self.findPathItem(path)

        if child is None:
            return 0
        else:
            return 1

    def isChildToBeRemoved(self, path):
        try:
            os.lstat(path)
            exists = 1
        except:
            exists = 0

        if exists == 0 or (exists == 1 and os.path.isdir(path) and os.path.exists(path) == 0):
            return 1
        else:
            return 0

    def isChildToBeModified(self, path, properties):
        child = self.findPathItem(path)
        if child == None:
            return 0

        itemProp = self.getItemProperties(child)

        for key in properties.keys():
            if key == "itemText":
                if properties[key][0] != itemProp[key][0].decode("utf8") or \
                                properties[key][1] != itemProp[key][1].decode("utf8"):
                    return 1
            else:
                if properties[key] != itemProp[key]:
                    return 1

        return 0

    def createChild(self, path):

        updir = os.path.dirname(path)

        if updir == "":
            parentItem = "root"
        else:
            parentItem = self.findPathItem(updir)

        if parentItem == "root":
            child = QTreeWidgetItem(self.treeWidget)
            self.treeWidget.itemBelow(child)
        elif parentItem is None:
            child = None
        else:
            child = QTreeWidgetItem(parentItem)
            parentItem.addChild(child)

        return child

    def addDirAsTreeItem(self, parentDir="", startup=0):
        if parentDir == "":
            parentDir = self._rootdir

        c = threading.currentThread()

        if c not in self._threads:
            self._threads.append(c)

        if os.path.exists(parentDir):
            dirs = os.listdir(parentDir)

            if len(dirs):
                for d in sorted(dirs):
                    path = os.path.join(parentDir,d)

                    if os.path.isfile(path) == 0 and d != ".sync":
                        lpath = path.lstrip(self._rootdir)
                        exists,is_link,target,state = self.getPathProperties(path)
                        properties = self.prepareItemProperties(lpath, d, exists, is_link, target,state)

                        if self.isChildExists(lpath) == 0:
                            if startup:
                                self.addItem(lpath,properties)
                            else:
                                self.emit(QtCore.SIGNAL("addChild"), lpath, properties)
                        elif self.isChildToBeModified(lpath,properties):
                            self.emit(QtCore.SIGNAL("modifyChild"), lpath, properties)

                        self.addDirAsTreeItem(path,startup)

        if c in self._threads:
            self._threads.remove(c)

    def findUncheckedItemsAmongChildren(self, items, parentItem, column=0):
        if parentItem == "" or parentItem is None:
            parentItem = self.treeWidget.invisibleRootItem()

        for i in range(parentItem.childCount()):
            if parentItem.child(i).checkState(0) == 0:
                items.append(parentItem.child(i))
            else:
                self.findUncheckedItemsAmongChildren(items, parentItem.child(i), column)
        return items

    def findItemAmongChildren(self, parentItem, textToFind, column=0):
        if parentItem == "" or parentItem is None:
            parentItem = self.treeWidget.invisibleRootItem()

        for i in range(parentItem.childCount()):
            if textToFind == parentItem.child(i).text(column).toUtf8():
                return parentItem.child(i)

    def findPathItem(self, pathToFind, column = 0):
        path = pathToFind.split("/")

        index = None
        for i in path:
            try:
                index = self.findItemAmongChildren(index, i, column)
            except:
                return None

        return index

    def changeCheckStateForPath(self, pathToFind, state, column=0):
        item = self.findPathItem(pathToFind, column)
        if item == None:
            pass
        else:
            item.setCheckState(column, state)

    def checkPath(self, pathToFind, column=0):
        self.changeCheckStateForPath(pathToFind, Qt.Checked, column=0)

    def uncheckPath(self, pathToFind, column=0):
        self.changeCheckStateForPath(pathToFind, Qt.Unchecked, column=0)

    def checkChildren(self, item):
        for i in range(item.childCount()):
            if item.child(i).flags() & QtCore.Qt.ItemIsUserCheckable:
                item.child(i).setCheckState(0, Qt.Checked)
                if item.child(i).childCount() > 0:
                    self.checkChildren(item.child(i))
        
    def checkParent(self, item):
        if item.parent() is not None:
            item.parent().setCheckState(0, Qt.Checked)
            self.checkParent(item.parent())

    def handleItemChecked(self, item):
        self.checkChildren(item)
        self.checkParent(item)

    def handleItemUnchecked(self, item):
        for i in range(item.childCount()):
            item.child(i).setCheckState(0, Qt.Unchecked)
            if item.child(i).childCount() > 0:
                self.handleItemUnchecked(item.child(i))

    def handleitemChanged(self, item):
        self.treeWidget.blockSignals(True)
        if item.checkState(0) == QtCore.Qt.Checked:
            self.handleItemChecked(item)
        elif item.checkState(0) == QtCore.Qt.Unchecked:
            self.handleItemUnchecked(item)
        self.treeWidget.blockSignals(False)

    def getExcludeDirsFromTree(self):
        paths = []
        items = []
        items = self.findUncheckedItemsAmongChildren(items, "")
        for item in items:
            path = self.getPathFromItem(item)
            paths.append(path)

        return paths

    def saveTreeExcludeDirs(self):
        self._exclude_dirs = self.getExcludeDirsFromTree()
        actions.SaveExcludeDirs(self._exclude_dirs,self._config)

    def refreshTree(self,force=0,clear=0):
        if not os.path.exists(self._rootdir):
            try:
                os.mkdir(self._rootdir)
            except:
                return

        if not self.isHidden() or force == 1:

            #for thread in self._threads:
            #    thread._Thread__stop()

            if clear:
                self.treeWidget.clear()

            self.connect(self, QtCore.SIGNAL("addChild"), self.addItem)
            self.connect(self, QtCore.SIGNAL("modifyChild"), self.modifyItem)
            #self.connect(self, QtCore.SIGNAL("removeChild"), self.removeItem)

            threadAdd = threading.Thread(target=self.addDirAsTreeItem)
            threadAdd.daemon = True
            threadAdd.start()

            threadRm = threading.Thread(target=self.checkAndRmUnusedTreeItem)
            threadRm.daemon = True
            threadRm.start()
            threadRm.join()

            for path in self._removeItems:
                self.removeItem(path.lstrip(self._rootdir))

    def initApp(self):
        self.fillOptions()
        if self.startServiceAtStart.isChecked():
            self.addDirAsTreeItem("", 1)
            self.actService("start")
        else:
            self.refreshStatus(1)

        if self._service_err == 3:
            self.runWizard()
        else:
            self.treeWidget.expandToDepth(False)
            self.treeWidget.itemChanged.connect(self.handleitemChanged)
            self.updateActionButtons()

            appOpts = AppOptions()
            startMinimized = int(appOpts.getParam("StartMinimized"))

            if startMinimized == 0:
                self.show()

            self.updateTrayMenuState()
            self.refreshStatus()

    def actionWaitCursor(function):
        def new_function(self, action):
            QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
            self.setButtonInState(action, "disabled")

            QtGui.QApplication.processEvents()
            QtGui.QApplication.processEvents()

            function(self, action)

            self.setButtonInState(action, "enabled")
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
    def actService(self, action):
        if action == "start":
            self.saveTreeExcludeDirs()
        params = self.getParams()
        res,msg = actions.DoAction(action, params)

        self._service_err = res

        cur_text = self.textEdit.toPlainText()
        new_text = actions.ProcessResult(res, action, msg, params, 0)

        if new_text != cur_text:
            self.textEdit.clear()
            self.textEdit.append(new_text)
            self.tIcon.updateToolTip(new_text)

            yStatus = actions.getStatusFromMsg(new_text)
            self.tIcon.setIcon(yStatus)

    def refreshStatus(self, force=0, clear=0):

        self.stopTimer()

        for thread in self._threads:
            thread._Thread__stop()

        self.actService("status")
        self.refreshTree(force,clear)

        self.startTimer()

    def handleSpinChange(self):
        self.refreshStatus()
        self.restartTimer()

    def proxyEnable(self):
        self.proxyManualWidget.setEnabled(True)

    def proxyDisable(self):
        self.proxyManualWidget.setEnabled(False)

    def toggleProxyAuth(self):
        if self.srvPasswordReq.isEnabled() and self.srvPasswordReq.isChecked():
            self.srvLogin.setEnabled(True)
            self.srvPassword.setEnabled(True)
        else:
            self.srvLogin.setEnabled(False)
            self.srvPassword.setEnabled(False)

    def toggleProxyAuthReq(self):
        if self.proxyType.currentText() in ["HTTPS", "SOCKS5"]:
            self.srvPasswordReq.setEnabled(True)
        else:
            self.srvPasswordReq.setEnabled(False)
        self.toggleProxyAuth()

    #@waitCursor
    def showAbout(self):
        about = About()
        about.exec_()

    def updateActionButtons(self):
        is_running, message = actions.IsDaemonRunning(self._prg)
        if is_running:
            self.setButtonInState("start", "disabled")
            self.setButtonInState("stop", "enabled")
        else:
            self.setButtonInState("stop", "disabled")
            self.setButtonInState("start", "enabled")

    def setButtonInState(self, button, state):
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

    def runWizard(self):

        self.hide()

        params = {}
        params["prg"] = self._prg
        params["config"] = self._config
        params["rootdir"] = self._rootdir
        params["auth"] = self._auth
        params["exclude-dirs"] = ""
        params["proxy"] = self._proxy

        yaWiz = yaWizard(params)

        yaWiz.setWindowModality(Qt.ApplicationModal)
        yaWiz.show()
        #yaWiz.button(yaWiz.NextButton).setEnabled(False)

        wizResult = yaWiz.exec_()

        self.show()

        if wizResult == 0:
            return

        params["prg"] = ""
        params["config"] = ""
        params["rootdir"] = ""
        params["auth"] = ""
        params["exclude-dirs"] = ""
        params["proxy"] = ""

        tuneParams(params,"widget")
        self.paramsInit(params)
        self.reloadOptions()

    def setSignals(self):
        QtCore.QObject.connect(self.btnExit, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)

        QtCore.QObject.connect(self.btnStart, QtCore.SIGNAL("clicked()"), lambda: self.actService("start"))
        QtCore.QObject.connect(self.btnStop, QtCore.SIGNAL("clicked()"), lambda: self.actService("stop"))
        QtCore.QObject.connect(self.btnStatus, QtCore.SIGNAL("clicked()"), self.refreshStatus)

        QtCore.QObject.connect(self.actionStart, QtCore.SIGNAL("activated()"), lambda: self.actService("start"))
        QtCore.QObject.connect(self.actionStop, QtCore.SIGNAL("activated()"), lambda: self.actService("stop"))
        QtCore.QObject.connect(self.actionStatus, QtCore.SIGNAL("activated()"), self.refreshStatus)

        QtCore.QObject.connect(self.actionSetup_Wizard, QtCore.SIGNAL("activated()"), self.runWizard)

        QtCore.QObject.connect(self.actionHide, QtCore.SIGNAL("activated()"), self.hide)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("activated()"), QtGui.qApp.quit)

        QtCore.QObject.connect(self.actionReloadCfg, QtCore.SIGNAL("activated()"), self.reloadOptions)
        QtCore.QObject.connect(self.actionSaveCfg, QtCore.SIGNAL("activated()"), self.saveOptions)

        QtCore.QObject.connect(self.ch_yandex_root, QtCore.SIGNAL("clicked()"), self.chooseRootDir)
        QtCore.QObject.connect(self.ch_yandex_auth, QtCore.SIGNAL("clicked()"), self.chooseAuthFile)
        QtCore.QObject.connect(self.ch_yandex_cfg, QtCore.SIGNAL("clicked()"), self.chooseCfgFile)

        QtCore.QObject.connect(self.actionAbout, QtCore.SIGNAL("activated()"), self.showAbout)

        QtCore.QObject.connect(self.refreshTimeout, QtCore.SIGNAL("editingFinished()"), self.handleSpinChange)

        QtCore.QObject.connect(self.proxyNone, QtCore.SIGNAL("clicked()"), self.proxyDisable)
        QtCore.QObject.connect(self.proxyAuto, QtCore.SIGNAL("clicked()"), self.proxyDisable)
        QtCore.QObject.connect(self.proxyManual, QtCore.SIGNAL("clicked()"), self.proxyEnable)

        QtCore.QObject.connect(self.srvPasswordReq, QtCore.SIGNAL("clicked()"), self.toggleProxyAuth)
        QtCore.QObject.connect(self.proxyType, QtCore.SIGNAL("currentIndexChanged(QString)"), self.toggleProxyAuthReq)

import sys, os
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import  QTimer

class SystemTrayIcon(QtGui.QSystemTrayIcon):

    _parent = None

    def setParent(self,parent):
        self._parent = parent

    def getParent(self):
        return self._parent

    def __init__(self, parent=None):

        self.setParent(parent)

        QtGui.QSystemTrayIcon.__init__(self, parent)

        if QtGui.QSystemTrayIcon.isSystemTrayAvailable():
            icon = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/yandex-disk_1.xpm")
            self.trayIcon = QtGui.QSystemTrayIcon(QtGui.QIcon(icon), parent)
            menu = QtGui.QMenu(parent)
            self.showAction = menu.addAction("Show")
            self.hideAction = menu.addAction("Hide")
            menu.addSeparator()
            exitAction = menu.addAction("Exit")
            QtCore.QObject.connect(self.showAction, QtCore.SIGNAL("activated()"), self.toggleWindow)
            QtCore.QObject.connect(self.hideAction, QtCore.SIGNAL("activated()"), self.toggleWindow)
            QtCore.QObject.connect(exitAction, QtCore.SIGNAL("activated()"), QtGui.qApp.quit)

            self.updateToolTip("Yandex Disk")
            self.trayIcon.activated.connect(self.onTrayIconActivated) 
            self.trayIcon.setContextMenu(menu)
            self.trayIcon.show()

            self.disambiguateTimer = QTimer(self)
            self.disambiguateTimer.setSingleShot(True)
            self.disambiguateTimer.timeout.connect(self.disambiguateTimerTimeout) 

            self.updateTrayMenuState()

    def updateTrayMenuState(self):
        parent = self.getParent()
        if parent.isVisible():
            self.showAction.setEnabled(False)
            self.hideAction.setEnabled(True)
        elif parent.isHidden():
            self.showAction.setEnabled(True)
            self.hideAction.setEnabled(False)

    def updateToolTip(self,msg):
        self.trayIcon.setToolTip(msg)

    def onTrayIconActivated(self, reason):
        if reason == QtGui.QSystemTrayIcon.Trigger:
            #self.disambiguateTimer.start(QtGui.qApp.doubleClickInterval())
            self.disambiguateTimer.start(0)
        elif reason == QtGui.QSystemTrayIcon.DoubleClick:
            self.disambiguateTimer.stop()
            #self.toggleWindow()

    def disambiguateTimerTimeout(self):
        self.toggleWindow()

    def toggleWindow(self):
        parent = self.getParent()
        if parent.isVisible():
            parent.hide()
        elif parent.isHidden():
            parent.show()
            parent.showNormal()

        self.updateTrayMenuState()

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wlayout.ui'
#
# Created: Tue Jul 14 22:30:42 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(641, 620)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.verticalLayout_1 = QtGui.QVBoxLayout(self.tab_1)
        self.verticalLayout_1.setObjectName(_fromUtf8("verticalLayout_1"))
        self.textEdit = QtGui.QTextEdit(self.tab_1)
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_1.addWidget(self.textEdit)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/tab_status.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_1, icon, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.treeWidget = QtGui.QTreeWidget(self.tab_2)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.verticalLayout_2.addWidget(self.treeWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/tab_folders.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon1, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox_1 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_1.setObjectName(_fromUtf8("groupBox_1"))
        self.horizontalLayout_1 = QtGui.QHBoxLayout(self.groupBox_1)
        self.horizontalLayout_1.setObjectName(_fromUtf8("horizontalLayout_1"))
        self.yandex_exec = QtGui.QLineEdit(self.groupBox_1)
        self.yandex_exec.setObjectName(_fromUtf8("yandex_exec"))
        self.horizontalLayout_1.addWidget(self.yandex_exec)
        self.verticalLayout_3.addWidget(self.groupBox_1)
        self.groupBox_2 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.yandex_cfg = QtGui.QLineEdit(self.groupBox_2)
        self.yandex_cfg.setObjectName(_fromUtf8("yandex_cfg"))
        self.horizontalLayout_2.addWidget(self.yandex_cfg)
        self.ch_yandex_cfg = QtGui.QToolButton(self.groupBox_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/folder_edit.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ch_yandex_cfg.setIcon(icon2)
        self.ch_yandex_cfg.setObjectName(_fromUtf8("ch_yandex_cfg"))
        self.horizontalLayout_2.addWidget(self.ch_yandex_cfg)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.yandex_root = QtGui.QLineEdit(self.groupBox_3)
        self.yandex_root.setObjectName(_fromUtf8("yandex_root"))
        self.horizontalLayout_3.addWidget(self.yandex_root)
        self.ch_yandex_root = QtGui.QToolButton(self.groupBox_3)
        self.ch_yandex_root.setIcon(icon2)
        self.ch_yandex_root.setObjectName(_fromUtf8("ch_yandex_root"))
        self.horizontalLayout_3.addWidget(self.ch_yandex_root)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.yandex_auth = QtGui.QLineEdit(self.groupBox_4)
        self.yandex_auth.setObjectName(_fromUtf8("yandex_auth"))
        self.horizontalLayout_4.addWidget(self.yandex_auth)
        self.ch_yandex_auth = QtGui.QToolButton(self.groupBox_4)
        self.ch_yandex_auth.setIcon(icon2)
        self.ch_yandex_auth.setObjectName(_fromUtf8("ch_yandex_auth"))
        self.horizontalLayout_4.addWidget(self.ch_yandex_auth)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_5 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.checkBox_1 = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox_1.setObjectName(_fromUtf8("checkBox_1"))
        self.horizontalLayout_5.addWidget(self.checkBox_1)
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.horizontalLayout_5.addWidget(self.checkBox_2)
        self.l_refresh_1 = QtGui.QLabel(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_refresh_1.sizePolicy().hasHeightForWidth())
        self.l_refresh_1.setSizePolicy(sizePolicy)
        self.l_refresh_1.setObjectName(_fromUtf8("l_refresh_1"))
        self.horizontalLayout_5.addWidget(self.l_refresh_1)
        self.refreshTimeout = QtGui.QSpinBox(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshTimeout.sizePolicy().hasHeightForWidth())
        self.refreshTimeout.setSizePolicy(sizePolicy)
        self.refreshTimeout.setMaximum(300)
        self.refreshTimeout.setProperty("value", 15)
        self.refreshTimeout.setObjectName(_fromUtf8("refreshTimeout"))
        self.horizontalLayout_5.addWidget(self.refreshTimeout)
        self.l_refresh_2 = QtGui.QLabel(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_refresh_2.sizePolicy().hasHeightForWidth())
        self.l_refresh_2.setSizePolicy(sizePolicy)
        self.l_refresh_2.setObjectName(_fromUtf8("l_refresh_2"))
        self.horizontalLayout_5.addWidget(self.l_refresh_2)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/tab_opts.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.ctrFrame = QtGui.QFrame(self.centralwidget)
        self.ctrFrame.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctrFrame.sizePolicy().hasHeightForWidth())
        self.ctrFrame.setSizePolicy(sizePolicy)
        self.ctrFrame.setMinimumSize(QtCore.QSize(250, 50))
        self.ctrFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ctrFrame.setAutoFillBackground(True)
        self.ctrFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ctrFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.ctrFrame.setObjectName(_fromUtf8("ctrFrame"))
        self.hboxlayout = QtGui.QHBoxLayout(self.ctrFrame)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.btnStart = QtGui.QPushButton(self.ctrFrame)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/start.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStart.setIcon(icon4)
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.hboxlayout.addWidget(self.btnStart)
        self.btnStop = QtGui.QPushButton(self.ctrFrame)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/stop.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStop.setIcon(icon5)
        self.btnStop.setObjectName(_fromUtf8("btnStop"))
        self.hboxlayout.addWidget(self.btnStop)
        self.btnStatus = QtGui.QPushButton(self.ctrFrame)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/status.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStatus.setIcon(icon6)
        self.btnStatus.setObjectName(_fromUtf8("btnStatus"))
        self.hboxlayout.addWidget(self.btnStatus)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.btnExit = QtGui.QPushButton(self.ctrFrame)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/exit.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExit.setIcon(icon7)
        self.btnExit.setObjectName(_fromUtf8("btnExit"))
        self.hboxlayout.addWidget(self.btnExit)
        self.verticalLayout.addWidget(self.ctrFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAction = QtGui.QMenu(self.menubar)
        self.menuAction.setObjectName(_fromUtf8("menuAction"))
        self.menuCfg = QtGui.QMenu(self.menubar)
        self.menuCfg.setObjectName(_fromUtf8("menuCfg"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionStart = QtGui.QAction(MainWindow)
        self.actionStart.setIcon(icon4)
        self.actionStart.setObjectName(_fromUtf8("actionStart"))
        self.actionStop = QtGui.QAction(MainWindow)
        self.actionStop.setIcon(icon5)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))
        self.actionStatus = QtGui.QAction(MainWindow)
        self.actionStatus.setIcon(icon6)
        self.actionStatus.setObjectName(_fromUtf8("actionStatus"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setIcon(icon7)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSaveCfg = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/save.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveCfg.setIcon(icon8)
        self.actionSaveCfg.setObjectName(_fromUtf8("actionSaveCfg"))
        self.actionReloadCfg = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/reload.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReloadCfg.setIcon(icon9)
        self.actionReloadCfg.setObjectName(_fromUtf8("actionReloadCfg"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/about.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon9)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuAction.addAction(self.actionStart)
        self.menuAction.addAction(self.actionStop)
        self.menuAction.addAction(self.actionStatus)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.actionExit)
        self.menuCfg.addAction(self.actionSaveCfg)
        self.menuCfg.addAction(self.actionReloadCfg)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAction.menuAction())
        self.menubar.addAction(self.menuCfg.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Yandex Disk Service Helper", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Service Status", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Directories to Sync", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Sync Dirs", None))
        self.groupBox_1.setTitle(_translate("MainWindow", "yandex-disk executable path", None))
        self.yandex_exec.setToolTip(_translate("MainWindow", "yandex-disk executable path", None))
        self.yandex_exec.setStatusTip(_translate("MainWindow", "yandex-disk executable path", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Configuration file path", None))
        self.yandex_cfg.setToolTip(_translate("MainWindow", "Path to yandex disk configuration file", None))
        self.yandex_cfg.setStatusTip(_translate("MainWindow", "Path to yandex disk configuration file", None))
        self.ch_yandex_cfg.setToolTip(_translate("MainWindow", "Change Yandex Configuration File Path", None))
        self.ch_yandex_cfg.setStatusTip(_translate("MainWindow", "Change Yandex Configuration File Path", None))
        self.ch_yandex_cfg.setText(_translate("MainWindow", "...", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Yandex Disk root directory", None))
        self.yandex_root.setToolTip(_translate("MainWindow", "Root directory for synchronization", None))
        self.yandex_root.setStatusTip(_translate("MainWindow", "Root directory for synchronization", None))
        self.ch_yandex_root.setToolTip(_translate("MainWindow", "Change Yandex Disk Root Directory", None))
        self.ch_yandex_root.setStatusTip(_translate("MainWindow", "Change Yandex Disk Root Directory", None))
        self.ch_yandex_root.setText(_translate("MainWindow", "...", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Yandex Disk auth file path", None))
        self.yandex_auth.setToolTip(_translate("MainWindow", "Yandex Disk authorization file path", None))
        self.yandex_auth.setStatusTip(_translate("MainWindow", "Yandex Disk authorization file path", None))
        self.ch_yandex_auth.setToolTip(_translate("MainWindow", "Change Yandex Authorization File Path", None))
        self.ch_yandex_auth.setStatusTip(_translate("MainWindow", "Change Yandex Authorization File Path", None))
        self.ch_yandex_auth.setText(_translate("MainWindow", "...", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Application Options", None))
        self.checkBox_1.setToolTip(_translate("MainWindow", "Start Application Hidden in a System Tray", None))
        self.checkBox_1.setStatusTip(_translate("MainWindow", "Start Application Hidden in a System Tray", None))
        self.checkBox_1.setText(_translate("MainWindow", "Start Hidden", None))
        self.checkBox_2.setToolTip(_translate("MainWindow", "Remove Application From TaskBar when minimized", None))
        self.checkBox_2.setStatusTip(_translate("MainWindow", "Remove Application From TaskBar when minimized", None))
        self.checkBox_2.setText(_translate("MainWindow", "Hide On Minimize", None))
        self.l_refresh_1.setText(_translate("MainWindow", "Status autorefresh", None))
        self.refreshTimeout.setToolTip(_translate("MainWindow", "Timeout after which status will be autorefreshed. Zero - no autorefresh", None))
        self.refreshTimeout.setStatusTip(_translate("MainWindow", "Timeout after which status will be autorefreshed. Zero - no autorefresh", None))
        self.l_refresh_2.setText(_translate("MainWindow", "sec", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Options", None))
        self.btnStart.setToolTip(_translate("MainWindow", "Start Service", None))
        self.btnStart.setStatusTip(_translate("MainWindow", "Start Service", None))
        self.btnStart.setText(_translate("MainWindow", "Start", None))
        self.btnStop.setToolTip(_translate("MainWindow", "Stop Service", None))
        self.btnStop.setStatusTip(_translate("MainWindow", "Stop Service", None))
        self.btnStop.setText(_translate("MainWindow", "Stop", None))
        self.btnStatus.setToolTip(_translate("MainWindow", "Check Service Status", None))
        self.btnStatus.setStatusTip(_translate("MainWindow", "Check Service Status", None))
        self.btnStatus.setText(_translate("MainWindow", "Status", None))
        self.btnExit.setToolTip(_translate("MainWindow", "Exit Application", None))
        self.btnExit.setStatusTip(_translate("MainWindow", "Exit Application", None))
        self.btnExit.setText(_translate("MainWindow", "Exit", None))
        self.menuAction.setTitle(_translate("MainWindow", "&Service", None))
        self.menuCfg.setTitle(_translate("MainWindow", "&Configuration", None))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help", None))
        self.actionStart.setText(_translate("MainWindow", "&Start", None))
        self.actionStart.setStatusTip(_translate("MainWindow", "Start Service", None))
        self.actionStop.setText(_translate("MainWindow", "Sto&p", None))
        self.actionStop.setStatusTip(_translate("MainWindow", "Stop Service", None))
        self.actionStatus.setText(_translate("MainWindow", "S&tatus", None))
        self.actionStatus.setStatusTip(_translate("MainWindow", "Check Service Status", None))
        self.actionExit.setText(_translate("MainWindow", "E&xit", None))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit Application", None))
        self.actionSaveCfg.setText(_translate("MainWindow", "&Save", None))
        self.actionSaveCfg.setStatusTip(_translate("MainWindow", "Save Current Configuration", None))
        self.actionReloadCfg.setText(_translate("MainWindow", "&Reload", None))
        self.actionReloadCfg.setStatusTip(_translate("MainWindow", "Reload Configuration From Config File(s)", None))
        self.actionAbout.setText(_translate("MainWindow", "&About", None))
        self.actionAbout.setStatusTip(_translate("MainWindow", "About Application", None))

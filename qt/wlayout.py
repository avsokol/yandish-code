# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/wlayout.ui'
#
# Created: Tue Apr  5 12:02:37 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import os
from PySide2 import QtCore
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QSizePolicy, QWidget, QVBoxLayout, QTabWidget, QTextEdit, QTreeWidget, QGroupBox, \
    QHBoxLayout, QLineEdit, QToolButton, QRadioButton, QGridLayout, QLabel, QComboBox, QCheckBox, QFormLayout, \
    QSpinBox, QFrame, QPushButton, QSpacerItem, QMenuBar, QMenu, QStatusBar, QAction


class UiMainWindow(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(515, 475)
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(size_policy)
        main_window.setMinimumSize(QtCore.QSize(515, 475))
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_1 = QVBoxLayout(self.tab_1)
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.textEdit = QTextEdit(self.tab_1)
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_1.addWidget(self.textEdit)
        icon = QIcon()
        icon.addPixmap(
            QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/tab_status.png")),
            QIcon.Normal,
            QIcon.Off
        )
        self.tabWidget.addTab(self.tab_1, icon, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeWidget = QTreeWidget(self.tab_2)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setDefaultSectionSize(240)
        self.verticalLayout_2.addWidget(self.treeWidget)
        icon1 = QIcon()
        icon1.addPixmap(
            QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/tab_folders.png")),
            QIcon.Normal,
            QIcon.Off
        )
        self.tabWidget.addTab(self.tab_2, icon1, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_1 = QGroupBox(self.tab_3)
        self.groupBox_1.setObjectName("groupBox_1")
        self.horizontalLayout_1 = QHBoxLayout(self.groupBox_1)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.yandex_exec = QLineEdit(self.groupBox_1)
        self.yandex_exec.setObjectName("yandex_exec")
        self.horizontalLayout_1.addWidget(self.yandex_exec)
        self.verticalLayout_3.addWidget(self.groupBox_1)
        self.groupBox_2 = QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.yandex_cfg = QLineEdit(self.groupBox_2)
        self.yandex_cfg.setObjectName("yandex_cfg")
        self.horizontalLayout_2.addWidget(self.yandex_cfg)
        self.ch_yandex_cfg = QToolButton(self.groupBox_2)
        icon2 = QIcon()
        icon2.addPixmap(
            QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/folder_edit.png")),
            QIcon.Normal,
            QIcon.Off
        )
        self.ch_yandex_cfg.setIcon(icon2)
        self.ch_yandex_cfg.setObjectName("ch_yandex_cfg")
        self.horizontalLayout_2.addWidget(self.ch_yandex_cfg)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.yandex_root = QLineEdit(self.groupBox_3)
        self.yandex_root.setObjectName("yandex_root")
        self.horizontalLayout_3.addWidget(self.yandex_root)
        self.ch_yandex_root = QToolButton(self.groupBox_3)
        self.ch_yandex_root.setIcon(icon2)
        self.ch_yandex_root.setObjectName("ch_yandex_root")
        self.horizontalLayout_3.addWidget(self.ch_yandex_root)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.yandex_auth = QLineEdit(self.groupBox_4)
        self.yandex_auth.setObjectName("yandex_auth")
        self.horizontalLayout_4.addWidget(self.yandex_auth)
        self.ch_yandex_auth = QToolButton(self.groupBox_4)
        self.ch_yandex_auth.setIcon(icon2)
        self.ch_yandex_auth.setObjectName("ch_yandex_auth")
        self.horizontalLayout_4.addWidget(self.ch_yandex_auth)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        icon3 = QIcon()
        icon3.addPixmap(
            QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/tab_conf.png")),
            QIcon.Normal,
            QIcon.Off
        )
        self.tabWidget.addTab(self.tab_3, icon3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_4 = QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_5 = QGroupBox(self.tab_4)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.proxyNone = QRadioButton(self.groupBox_5)
        self.proxyNone.setObjectName("proxyNone")
        self.verticalLayout_5.addWidget(self.proxyNone)
        self.proxyAuto = QRadioButton(self.groupBox_5)
        self.proxyAuto.setChecked(True)
        self.proxyAuto.setObjectName("proxyAuto")
        self.verticalLayout_5.addWidget(self.proxyAuto)
        self.proxyManual = QRadioButton(self.groupBox_5)
        self.proxyManual.setObjectName("proxyManual")
        self.verticalLayout_5.addWidget(self.proxyManual)
        self.proxyManualWidget = QWidget(self.groupBox_5)
        self.proxyManualWidget.setEnabled(False)
        self.proxyManualWidget.setObjectName("proxyManualWidget")
        self.gridLayout = QGridLayout(self.proxyManualWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName("gridLayout")
        self.srvLogin = QLineEdit(self.proxyManualWidget)
        self.srvLogin.setEnabled(False)
        self.srvLogin.setObjectName("srvLogin")
        self.gridLayout.addWidget(self.srvLogin, 4, 2, 1, 1)
        self.proxyTypeLabel = QLabel(self.proxyManualWidget)
        self.proxyTypeLabel.setObjectName("proxyTypeLabel")
        self.gridLayout.addWidget(self.proxyTypeLabel, 0, 0, 1, 1)
        self.proxyType = QComboBox(self.proxyManualWidget)
        self.proxyType.setObjectName("proxyType")
        self.proxyType.addItem("")
        self.proxyType.addItem("")
        self.proxyType.addItem("")
        self.gridLayout.addWidget(self.proxyType, 0, 2, 1, 1)
        self.portLabel = QLabel(self.proxyManualWidget)
        self.portLabel.setObjectName("portLabel")
        self.gridLayout.addWidget(self.portLabel, 2, 3, 1, 1)
        self.srvLoginLabel = QLabel(self.proxyManualWidget)
        self.srvLoginLabel.setObjectName("srvLoginLabel")
        self.gridLayout.addWidget(self.srvLoginLabel, 4, 0, 1, 1)
        self.srvLabel = QLabel(self.proxyManualWidget)
        self.srvLabel.setObjectName("srvLabel")
        self.gridLayout.addWidget(self.srvLabel, 2, 0, 1, 1)
        self.srvName = QLineEdit(self.proxyManualWidget)
        self.srvName.setObjectName("srvName")
        self.gridLayout.addWidget(self.srvName, 2, 2, 1, 1)
        self.portNumber = QLineEdit(self.proxyManualWidget)
        self.portNumber.setMinimumSize(QtCore.QSize(50, 0))
        self.portNumber.setMaximumSize(QtCore.QSize(50, 16777215))
        self.portNumber.setObjectName("portNumber")
        self.gridLayout.addWidget(self.portNumber, 2, 4, 1, 1)
        self.srvPasswordReq = QCheckBox(self.proxyManualWidget)
        self.srvPasswordReq.setObjectName("srvPasswordReq")
        self.gridLayout.addWidget(self.srvPasswordReq, 3, 2, 1, 1)
        self.srvPasswordLabel = QLabel(self.proxyManualWidget)
        self.srvPasswordLabel.setObjectName("srvPasswordLabel")
        self.gridLayout.addWidget(self.srvPasswordLabel, 5, 0, 1, 1)
        self.srvPassword = QLineEdit(self.proxyManualWidget)
        self.srvPassword.setEnabled(False)
        self.srvPassword.setEchoMode(QLineEdit.Password)
        self.srvPassword.setObjectName("srvPassword")
        self.gridLayout.addWidget(self.srvPassword, 5, 2, 1, 1)
        self.verticalLayout_5.addWidget(self.proxyManualWidget)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        icon4 = QIcon()
        icon4.addPixmap(
            QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/tab_proxy.png")),
            QIcon.Normal,
            QIcon.Off
        )
        self.tabWidget.addTab(self.tab_4, icon4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_2 = QGridLayout(self.tab_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_6 = QGroupBox(self.tab_5)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.formLayout = QFormLayout(self.groupBox_6)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.startHidden = QCheckBox(self.groupBox_6)
        self.startHidden.setObjectName("startHidden")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.startHidden)
        self.hideOnMinimize = QCheckBox(self.groupBox_6)
        self.hideOnMinimize.setObjectName("hideOnMinimize")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.hideOnMinimize)
        self.l_refresh_1 = QLabel(self.groupBox_6)
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.l_refresh_1.sizePolicy().hasHeightForWidth())
        self.l_refresh_1.setSizePolicy(size_policy)
        self.l_refresh_1.setObjectName("l_refresh_1")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.l_refresh_1)
        self.refreshTimeout = QSpinBox(self.groupBox_6)
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.refreshTimeout.sizePolicy().hasHeightForWidth())
        self.refreshTimeout.setSizePolicy(size_policy)
        self.refreshTimeout.setMaximum(300)
        self.refreshTimeout.setProperty("value", 15)
        self.refreshTimeout.setObjectName("refreshTimeout")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.refreshTimeout)
        self.startServiceAtStart = QCheckBox(self.groupBox_6)
        self.startServiceAtStart.setObjectName("startServiceAtStart")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.startServiceAtStart)
        self.gridLayout_2.addWidget(self.groupBox_6, 0, 0, 1, 1)
        icon5 = QIcon()
        icon5.addPixmap(
            QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/tab_opts.png")),
            QIcon.Normal,
            QIcon.Off
        )
        self.tabWidget.addTab(self.tab_5, icon5, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.ctrFrame = QFrame(self.centralwidget)
        self.ctrFrame.setEnabled(True)
        size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.ctrFrame.sizePolicy().hasHeightForWidth())
        self.ctrFrame.setSizePolicy(size_policy)
        self.ctrFrame.setMinimumSize(QtCore.QSize(250, 50))
        self.ctrFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ctrFrame.setAutoFillBackground(True)
        self.ctrFrame.setFrameShape(QFrame.StyledPanel)
        self.ctrFrame.setFrameShadow(QFrame.Raised)
        self.ctrFrame.setObjectName("ctrFrame")
        self.hboxlayout = QHBoxLayout(self.ctrFrame)
        self.hboxlayout.setObjectName("hboxlayout")
        self.btnStart = QPushButton(self.ctrFrame)
        icon6 = QIcon()
        icon6.addPixmap(
            QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/start.png")),
            QIcon.Normal,
            QIcon.Off
        )
        self.btnStart.setIcon(icon6)
        self.btnStart.setObjectName("btnStart")
        self.hboxlayout.addWidget(self.btnStart)
        self.btnStop = QPushButton(self.ctrFrame)
        icon7 = QIcon()
        icon7.addPixmap(
            QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/stop.png")),
            QIcon.Normal,
            QIcon.Off
        )
        self.btnStop.setIcon(icon7)
        self.btnStop.setObjectName("btnStop")
        self.hboxlayout.addWidget(self.btnStop)
        self.btnStatus = QPushButton(self.ctrFrame)
        icon8 = QIcon()
        icon8.addPixmap(
            QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/status.png")),
            QIcon.Normal,
            QIcon.Off
        )
        self.btnStatus.setIcon(icon8)
        self.btnStatus.setObjectName("btnStatus")
        self.hboxlayout.addWidget(self.btnStatus)
        spacer_item = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacer_item)
        self.btnExit = QPushButton(self.ctrFrame)
        icon9 = QIcon()
        icon9.addPixmap(
            QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/exit.png")),
            QIcon.Normal,
            QIcon.Off
        )
        self.btnExit.setIcon(icon9)
        self.btnExit.setObjectName("btnExit")
        self.hboxlayout.addWidget(self.btnExit)
        self.verticalLayout.addWidget(self.ctrFrame)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 27))
        self.menubar.setObjectName("menubar")
        self.menuService = QMenu(self.menubar)
        self.menuService.setObjectName("menuService")
        self.menuCfg = QMenu(self.menubar)
        self.menuCfg.setObjectName("menuCfg")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuApplication = QMenu(self.menubar)
        self.menuApplication.setObjectName("menuApplication")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.actionStart = QAction(main_window)
        self.actionStart.setIcon(icon6)
        self.actionStart.setObjectName("actionStart")
        self.actionStop = QAction(main_window)
        self.actionStop.setIcon(icon7)
        self.actionStop.setObjectName("actionStop")
        self.actionStatus = QAction(main_window)
        self.actionStatus.setIcon(icon8)
        self.actionStatus.setObjectName("actionStatus")
        self.actionExit = QAction(main_window)
        self.actionExit.setIcon(icon9)
        self.actionExit.setObjectName("actionExit")
        self.actionSaveCfg = QAction(main_window)
        icon10 = QIcon()
        icon10.addPixmap(
            QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/save.png")),
            QIcon.Normal,
            QIcon.Off
        )
        self.actionSaveCfg.setIcon(icon10)
        self.actionSaveCfg.setObjectName("actionSaveCfg")
        self.actionReloadCfg = QAction(main_window)
        icon11 = QIcon()
        icon11.addPixmap(
            QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/reload.png")),
            QIcon.Normal,
            QIcon.Off
        )
        self.actionReloadCfg.setIcon(icon11)
        self.actionReloadCfg.setObjectName("actionReloadCfg")
        self.actionAbout = QAction(main_window)
        icon12 = QIcon()
        icon12.addPixmap(
            QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/about.png")),
            QIcon.Normal,
            QIcon.Off
        )
        self.actionAbout.setIcon(icon12)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHide = QAction(main_window)
        self.actionHide.setObjectName("actionHide")
        self.actionSetup_Wizard = QAction(main_window)
        icon13 = QIcon()
        icon13.addPixmap(
            QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/wizard.png")),
            QIcon.Normal,
            QIcon.Off
        )
        self.actionSetup_Wizard.setIcon(icon13)
        self.actionSetup_Wizard.setObjectName("actionSetup_Wizard")
        self.menuService.addAction(self.actionStart)
        self.menuService.addAction(self.actionStop)
        self.menuService.addAction(self.actionStatus)
        self.menuService.addSeparator()
        self.menuCfg.addAction(self.actionSaveCfg)
        self.menuCfg.addAction(self.actionReloadCfg)
        self.menuHelp.addAction(self.actionAbout)
        self.menuApplication.addAction(self.actionSetup_Wizard)
        self.menuApplication.addSeparator()
        self.menuApplication.addAction(self.actionHide)
        self.menuApplication.addAction(self.actionExit)
        self.menubar.addAction(self.menuApplication.menuAction())
        self.menubar.addAction(self.menuService.menuAction())
        self.menubar.addAction(self.menuCfg.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Yandex Disk Service Helper", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("main_window", "Service Status", None))
        self.treeWidget.headerItem().setText(0, _translate("main_window", "Directories to Sync", None))
        self.treeWidget.headerItem().setText(1, _translate("main_window", "", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("main_window", "Sync Dirs", None))
        self.groupBox_1.setTitle(_translate("main_window", "yandex-disk executable path", None))
        self.yandex_exec.setToolTip(_translate("main_window", "yandex-disk executable path", None))
        self.yandex_exec.setStatusTip(_translate("main_window", "yandex-disk executable path", None))
        self.groupBox_2.setTitle(_translate("main_window", "Configuration file path", None))
        self.yandex_cfg.setToolTip(_translate("main_window", "Path to yandex disk configuration file", None))
        self.yandex_cfg.setStatusTip(_translate("main_window", "Path to yandex disk configuration file", None))
        self.ch_yandex_cfg.setToolTip(_translate("main_window", "Change Yandex Configuration File Path", None))
        self.ch_yandex_cfg.setStatusTip(_translate("main_window", "Change Yandex Configuration File Path", None))
        self.ch_yandex_cfg.setText(_translate("main_window", "...", None))
        self.groupBox_3.setTitle(_translate("main_window", "Yandex Disk root directory", None))
        self.yandex_root.setToolTip(_translate("main_window", "Root directory for synchronization", None))
        self.yandex_root.setStatusTip(_translate("main_window", "Root directory for synchronization", None))
        self.ch_yandex_root.setToolTip(_translate("main_window", "Change Yandex Disk Root Directory", None))
        self.ch_yandex_root.setStatusTip(_translate("main_window", "Change Yandex Disk Root Directory", None))
        self.ch_yandex_root.setText(_translate("main_window", "...", None))
        self.groupBox_4.setTitle(_translate("main_window", "Yandex Disk auth file path", None))
        self.yandex_auth.setToolTip(_translate("main_window", "Yandex Disk authorization file path", None))
        self.yandex_auth.setStatusTip(_translate("main_window", "Yandex Disk authorization file path", None))
        self.ch_yandex_auth.setToolTip(_translate("main_window", "Change Yandex Authorization File Path", None))
        self.ch_yandex_auth.setStatusTip(_translate("main_window", "Change Yandex Authorization File Path", None))
        self.ch_yandex_auth.setText(_translate("main_window", "...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("main_window", "Configuration", None))
        self.proxyNone.setText(_translate("main_window", "None", None))
        self.proxyAuto.setText(_translate("main_window", "Auto", None))
        self.proxyManual.setText(_translate("main_window", "Manual", None))
        self.srvLogin.setToolTip(_translate("main_window", "Proxy server login", None))
        self.srvLogin.setStatusTip(_translate("main_window", "Proxy server login", None))
        self.proxyTypeLabel.setText(_translate("main_window", "Type:", None))
        self.proxyType.setToolTip(_translate("main_window", "Proxy type", None))
        self.proxyType.setStatusTip(_translate("main_window", "Choose proxy type", None))
        self.proxyType.setItemText(0, _translate("main_window", "HTTPS", None))
        self.proxyType.setItemText(1, _translate("main_window", "SOCKS4", None))
        self.proxyType.setItemText(2, _translate("main_window", "SOCKS5", None))
        self.portLabel.setText(_translate("main_window", "Port:", None))
        self.srvLoginLabel.setText(_translate("main_window", "Login:", None))
        self.srvLabel.setText(_translate("main_window", "Server:", None))
        self.srvName.setToolTip(_translate("main_window", "Proxy server", None))
        self.srvName.setStatusTip(_translate("main_window", "Proxy server hostname or IP address", None))
        self.portNumber.setToolTip(_translate("main_window", "Proxy port", None))
        self.portNumber.setStatusTip(_translate("main_window", "Proxy port", None))
        self.srvPasswordReq.setToolTip(_translate("main_window", "Proxy server authorization", None))
        self.srvPasswordReq.setStatusTip(_translate("main_window", "Proxy server authorization", None))
        self.srvPasswordReq.setText(_translate("main_window", "Server Credentials", None))
        self.srvPasswordLabel.setText(_translate("main_window", "Password:", None))
        self.srvPassword.setToolTip(_translate("main_window", "Proxy server password", None))
        self.srvPassword.setStatusTip(_translate("main_window", "Proxy server password", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("main_window", "Proxy", None))
        self.startHidden.setToolTip(_translate("main_window", "Start Application Hidden in a System Tray", None))
        self.startHidden.setStatusTip(_translate("main_window", "Start Application Hidden in a System Tray", None))
        self.startHidden.setText(_translate("main_window", "Start Hidden", None))
        self.hideOnMinimize.setToolTip(_translate("main_window", "Remove Application From TaskBar when minimized", None))
        self.hideOnMinimize.setStatusTip(_translate("main_window", "Remove Application From TaskBar when minimized", None))
        self.hideOnMinimize.setText(_translate("main_window", "Hide On Minimize", None))
        self.l_refresh_1.setText(_translate("main_window", "Status autorefresh in sec", None))
        self.refreshTimeout.setToolTip(_translate("main_window", "Timeout after which status will be autorefreshed. Zero - no autorefresh", None))
        self.refreshTimeout.setStatusTip(_translate("main_window", "Timeout after which status will be autorefreshed. Zero - no autorefresh", None))
        self.startServiceAtStart.setToolTip(_translate("main_window", "Start yandex-disk daemon on application start", None))
        self.startServiceAtStart.setStatusTip(_translate("main_window", "Start yandex-disk daemon on application start", None))
        self.startServiceAtStart.setText(_translate("main_window", "Start Service At Application Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("main_window", "Options", None))
        self.btnStart.setToolTip(_translate("main_window", "Start Service", None))
        self.btnStart.setStatusTip(_translate("main_window", "Start Service", None))
        self.btnStart.setText(_translate("main_window", "Start", None))
        self.btnStop.setToolTip(_translate("main_window", "Stop Service", None))
        self.btnStop.setStatusTip(_translate("main_window", "Stop Service", None))
        self.btnStop.setText(_translate("main_window", "Stop", None))
        self.btnStatus.setToolTip(_translate("main_window", "Check Service Status", None))
        self.btnStatus.setStatusTip(_translate("main_window", "Check Service Status", None))
        self.btnStatus.setText(_translate("main_window", "Status", None))
        self.btnExit.setToolTip(_translate("main_window", "Exit Application", None))
        self.btnExit.setStatusTip(_translate("main_window", "Exit Application", None))
        self.btnExit.setText(_translate("main_window", "Exit", None))
        self.menuService.setTitle(_translate("main_window", "&Service", None))
        self.menuCfg.setTitle(_translate("main_window", "&Configuration", None))
        self.menuHelp.setTitle(_translate("main_window", "&Help", None))
        self.menuApplication.setTitle(_translate("main_window", "&Application", None))
        self.actionStart.setText(_translate("main_window", "&Start", None))
        self.actionStart.setStatusTip(_translate("main_window", "Start Service", None))
        self.actionStop.setText(_translate("main_window", "Sto&p", None))
        self.actionStop.setStatusTip(_translate("main_window", "Stop Service", None))
        self.actionStatus.setText(_translate("main_window", "S&tatus", None))
        self.actionStatus.setStatusTip(_translate("main_window", "Check Service Status", None))
        self.actionExit.setText(_translate("main_window", "E&xit", None))
        self.actionExit.setStatusTip(_translate("main_window", "Exit Application", None))
        self.actionSaveCfg.setText(_translate("main_window", "&Save", None))
        self.actionSaveCfg.setStatusTip(_translate("main_window", "Save Current Configuration", None))
        self.actionReloadCfg.setText(_translate("main_window", "&Reload", None))
        self.actionReloadCfg.setStatusTip(_translate("main_window", "Reload Configuration From Config File(s)", None))
        self.actionAbout.setText(_translate("main_window", "&About", None))
        self.actionAbout.setStatusTip(_translate("main_window", "About Application", None))
        self.actionHide.setText(_translate("main_window", "&Hide", None))
        self.actionSetup_Wizard.setText(_translate("main_window", "Setup &wizard", None))

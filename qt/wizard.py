# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wizard.ui'
#
# Created: Wed Jul 15 14:28:48 2015
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

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName(_fromUtf8("Wizard"))
        Wizard.resize(417, 492)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Wizard.sizePolicy().hasHeightForWidth())
        Wizard.setSizePolicy(sizePolicy)
        Wizard.setMinimumSize(QtCore.QSize(417, 492))
        Wizard.setMaximumSize(QtCore.QSize(417, 492))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../ico/yandex-disk_1.xpm")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Wizard.setWindowIcon(icon)
        Wizard.setWizardStyle(QtGui.QWizard.ClassicStyle)
        self.wizardPage1 = QtGui.QWizardPage()
        self.wizardPage1.setObjectName(_fromUtf8("wizardPage1"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.wizardPage1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.logoFrame_1 = QtGui.QFrame(self.wizardPage1)
        self.logoFrame_1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.logoFrame_1.setFrameShadow(QtGui.QFrame.Raised)
        self.logoFrame_1.setObjectName(_fromUtf8("logoFrame_1"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.logoFrame_1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.logoPixmap_1 = QtGui.QLabel(self.logoFrame_1)
        self.logoPixmap_1.setEnabled(True)
        self.logoPixmap_1.setText(_fromUtf8(""))
        self.logoPixmap_1.setPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../ico/yandex_disk_logo_1.png"))))
        self.logoPixmap_1.setScaledContents(False)
        self.logoPixmap_1.setAlignment(QtCore.Qt.AlignCenter)
        self.logoPixmap_1.setObjectName(_fromUtf8("logoPixmap_1"))
        self.horizontalLayout_4.addWidget(self.logoPixmap_1)
        self.verticalLayout_3.addWidget(self.logoFrame_1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.accountGroupBox = QtGui.QGroupBox(self.wizardPage1)
        self.accountGroupBox.setMaximumSize(QtCore.QSize(16777215, 176))
        self.accountGroupBox.setObjectName(_fromUtf8("accountGroupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.accountGroupBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loginFfame = QtGui.QFrame(self.accountGroupBox)
        self.loginFfame.setMaximumSize(QtCore.QSize(464, 140))
        self.loginFfame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.loginFfame.setFrameShadow(QtGui.QFrame.Raised)
        self.loginFfame.setObjectName(_fromUtf8("loginFfame"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.loginFfame)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.loginLabelsFrame = QtGui.QFrame(self.loginFfame)
        self.loginLabelsFrame.setMaximumSize(QtCore.QSize(79, 120))
        self.loginLabelsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.loginLabelsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.loginLabelsFrame.setObjectName(_fromUtf8("loginLabelsFrame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.loginLabelsFrame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.loginLabel = QtGui.QLabel(self.loginLabelsFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.loginLabel.setFont(font)
        self.loginLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.loginLabel.setObjectName(_fromUtf8("loginLabel"))
        self.verticalLayout.addWidget(self.loginLabel)
        self.passLabel = QtGui.QLabel(self.loginLabelsFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.passLabel.setFont(font)
        self.passLabel.setObjectName(_fromUtf8("passLabel"))
        self.verticalLayout.addWidget(self.passLabel)
        self.horizontalLayout_3.addWidget(self.loginLabelsFrame)
        self.loginEntryFrame = QtGui.QFrame(self.loginFfame)
        self.loginEntryFrame.setMaximumSize(QtCore.QSize(16777215, 120))
        self.loginEntryFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.loginEntryFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.loginEntryFrame.setObjectName(_fromUtf8("loginEntryFrame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.loginEntryFrame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.yaLoginFrame = QtGui.QFrame(self.loginEntryFrame)
        self.yaLoginFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.yaLoginFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.yaLoginFrame.setObjectName(_fromUtf8("yaLoginFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.yaLoginFrame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.yaLogin = QtGui.QLineEdit(self.yaLoginFrame)
        self.yaLogin.setMinimumSize(QtCore.QSize(119, 0))
        self.yaLogin.setMaximumSize(QtCore.QSize(119, 16777215))
        self.yaLogin.setObjectName(_fromUtf8("yaLogin"))
        self.horizontalLayout.addWidget(self.yaLogin)
        self.yandexRu = QtGui.QLabel(self.yaLoginFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.yandexRu.setFont(font)
        self.yandexRu.setObjectName(_fromUtf8("yandexRu"))
        self.horizontalLayout.addWidget(self.yandexRu)
        self.verticalLayout_2.addWidget(self.yaLoginFrame)
        self.yaPassFrame = QtGui.QFrame(self.loginEntryFrame)
        self.yaPassFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.yaPassFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.yaPassFrame.setObjectName(_fromUtf8("yaPassFrame"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.yaPassFrame)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.yaPass = QtGui.QLineEdit(self.yaPassFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yaPass.sizePolicy().hasHeightForWidth())
        self.yaPass.setSizePolicy(sizePolicy)
        self.yaPass.setMinimumSize(QtCore.QSize(119, 0))
        self.yaPass.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.yaPass.setEchoMode(QtGui.QLineEdit.Password)
        self.yaPass.setObjectName(_fromUtf8("yaPass"))
        self.horizontalLayout_11.addWidget(self.yaPass)
        self.pushButton = QtGui.QPushButton(self.yaPassFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_11.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.yaPassFrame)
        self.horizontalLayout_3.addWidget(self.loginEntryFrame)
        self.horizontalLayout_2.addWidget(self.loginFfame)
        self.verticalLayout_3.addWidget(self.accountGroupBox)
        self.stepLabel_1 = QtGui.QLabel(self.wizardPage1)
        self.stepLabel_1.setObjectName(_fromUtf8("stepLabel_1"))
        self.verticalLayout_3.addWidget(self.stepLabel_1)
        Wizard.addPage(self.wizardPage1)
        self.wizardPage2 = QtGui.QWizardPage()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.wizardPage2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.logoFrame_2 = QtGui.QFrame(self.wizardPage2)
        self.logoFrame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.logoFrame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.logoFrame_2.setObjectName(_fromUtf8("logoFrame_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.logoFrame_2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.logoPixmap_2 = QtGui.QLabel(self.logoFrame_2)
        self.logoPixmap_2.setEnabled(True)
        self.logoPixmap_2.setText(_fromUtf8(""))
        self.logoPixmap_2.setPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../ico/yandex_disk_logo_1.png"))))
        self.logoPixmap_2.setScaledContents(False)
        self.logoPixmap_2.setAlignment(QtCore.Qt.AlignCenter)
        self.logoPixmap_2.setObjectName(_fromUtf8("logoPixmap_2"))
        self.horizontalLayout_5.addWidget(self.logoPixmap_2)
        self.verticalLayout_5.addWidget(self.logoFrame_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.yaRootGroupBox = QtGui.QGroupBox(self.wizardPage2)
        self.yaRootGroupBox.setObjectName(_fromUtf8("yaRootGroupBox"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.yaRootGroupBox)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.defRootLabel = QtGui.QLabel(self.yaRootGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.defRootLabel.sizePolicy().hasHeightForWidth())
        self.defRootLabel.setSizePolicy(sizePolicy)
        self.defRootLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.defRootLabel.setObjectName(_fromUtf8("defRootLabel"))
        self.verticalLayout_6.addWidget(self.defRootLabel)
        self.yaRootFrame = QtGui.QFrame(self.yaRootGroupBox)
        self.yaRootFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.yaRootFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.yaRootFrame.setObjectName(_fromUtf8("yaRootFrame"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.yaRootFrame)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.yaRoot = QtGui.QLineEdit(self.yaRootFrame)
        self.yaRoot.setObjectName(_fromUtf8("yaRoot"))
        self.horizontalLayout_6.addWidget(self.yaRoot)
        self.yaRootCh = QtGui.QToolButton(self.yaRootFrame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../ico/folder_edit.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yaRootCh.setIcon(icon1)
        self.yaRootCh.setObjectName(_fromUtf8("yaRootCh"))
        self.horizontalLayout_6.addWidget(self.yaRootCh)
        self.verticalLayout_6.addWidget(self.yaRootFrame)
        self.verticalLayout_5.addWidget(self.yaRootGroupBox)
        self.stepLabel_2 = QtGui.QLabel(self.wizardPage2)
        self.stepLabel_2.setObjectName(_fromUtf8("stepLabel_2"))
        self.verticalLayout_5.addWidget(self.stepLabel_2)
        Wizard.addPage(self.wizardPage2)
        self.wizardPage = QtGui.QWizardPage()
        self.wizardPage.setObjectName(_fromUtf8("wizardPage"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.wizardPage)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.logoFrame_3 = QtGui.QFrame(self.wizardPage)
        self.logoFrame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.logoFrame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.logoFrame_3.setObjectName(_fromUtf8("logoFrame_3"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.logoFrame_3)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.logoPixmap_3 = QtGui.QLabel(self.logoFrame_3)
        self.logoPixmap_3.setEnabled(True)
        self.logoPixmap_3.setText(_fromUtf8(""))
        self.logoPixmap_3.setPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../ico/yandex_disk_logo_1.png"))))
        self.logoPixmap_3.setScaledContents(False)
        self.logoPixmap_3.setAlignment(QtCore.Qt.AlignCenter)
        self.logoPixmap_3.setObjectName(_fromUtf8("logoPixmap_3"))
        self.horizontalLayout_7.addWidget(self.logoPixmap_3)
        self.verticalLayout_7.addWidget(self.logoFrame_3)
        self.yaCfgGroupBox = QtGui.QGroupBox(self.wizardPage)
        self.yaCfgGroupBox.setObjectName(_fromUtf8("yaCfgGroupBox"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.yaCfgGroupBox)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.defCfgLabel = QtGui.QLabel(self.yaCfgGroupBox)
        self.defCfgLabel.setObjectName(_fromUtf8("defCfgLabel"))
        self.verticalLayout_8.addWidget(self.defCfgLabel)
        self.yaCfgFrame = QtGui.QFrame(self.yaCfgGroupBox)
        self.yaCfgFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.yaCfgFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.yaCfgFrame.setObjectName(_fromUtf8("yaCfgFrame"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.yaCfgFrame)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.yaCfg = QtGui.QLineEdit(self.yaCfgFrame)
        self.yaCfg.setObjectName(_fromUtf8("yaCfg"))
        self.horizontalLayout_8.addWidget(self.yaCfg)
        self.yaCfgCh = QtGui.QToolButton(self.yaCfgFrame)
        self.yaCfgCh.setIcon(icon1)
        self.yaCfgCh.setObjectName(_fromUtf8("yaCfgCh"))
        self.horizontalLayout_8.addWidget(self.yaCfgCh)
        self.verticalLayout_8.addWidget(self.yaCfgFrame)
        self.verticalLayout_7.addWidget(self.yaCfgGroupBox)
        self.yaAuthGroupBox = QtGui.QGroupBox(self.wizardPage)
        self.yaAuthGroupBox.setObjectName(_fromUtf8("yaAuthGroupBox"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.yaAuthGroupBox)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.defAuthLabel = QtGui.QLabel(self.yaAuthGroupBox)
        self.defAuthLabel.setObjectName(_fromUtf8("defAuthLabel"))
        self.verticalLayout_9.addWidget(self.defAuthLabel)
        self.yaAuthFrame = QtGui.QFrame(self.yaAuthGroupBox)
        self.yaAuthFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.yaAuthFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.yaAuthFrame.setObjectName(_fromUtf8("yaAuthFrame"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.yaAuthFrame)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.yaAuth = QtGui.QLineEdit(self.yaAuthFrame)
        self.yaAuth.setObjectName(_fromUtf8("yaAuth"))
        self.horizontalLayout_9.addWidget(self.yaAuth)
        self.yaAuthCh = QtGui.QToolButton(self.yaAuthFrame)
        self.yaAuthCh.setIcon(icon1)
        self.yaAuthCh.setObjectName(_fromUtf8("yaAuthCh"))
        self.horizontalLayout_9.addWidget(self.yaAuthCh)
        self.verticalLayout_9.addWidget(self.yaAuthFrame)
        self.verticalLayout_7.addWidget(self.yaAuthGroupBox)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.stepLabel_3 = QtGui.QLabel(self.wizardPage)
        self.stepLabel_3.setObjectName(_fromUtf8("stepLabel_3"))
        self.verticalLayout_7.addWidget(self.stepLabel_3)
        Wizard.addPage(self.wizardPage)
        self.wizardPage_2 = QtGui.QWizardPage()
        self.wizardPage_2.setObjectName(_fromUtf8("wizardPage_2"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.wizardPage_2)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.logoFrame_4 = QtGui.QFrame(self.wizardPage_2)
        self.logoFrame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.logoFrame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.logoFrame_4.setObjectName(_fromUtf8("logoFrame_4"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.logoFrame_4)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.logoPixmap_4 = QtGui.QLabel(self.logoFrame_4)
        self.logoPixmap_4.setEnabled(True)
        self.logoPixmap_4.setText(_fromUtf8(""))
        self.logoPixmap_4.setPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../ico/yandex_disk_logo_1.png"))))
        self.logoPixmap_4.setScaledContents(False)
        self.logoPixmap_4.setAlignment(QtCore.Qt.AlignCenter)
        self.logoPixmap_4.setObjectName(_fromUtf8("logoPixmap_4"))
        self.horizontalLayout_10.addWidget(self.logoPixmap_4)
        self.verticalLayout_10.addWidget(self.logoFrame_4)
        self.proxyGroupBox = QtGui.QGroupBox(self.wizardPage_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proxyGroupBox.sizePolicy().hasHeightForWidth())
        self.proxyGroupBox.setSizePolicy(sizePolicy)
        self.proxyGroupBox.setObjectName(_fromUtf8("proxyGroupBox"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.proxyGroupBox)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.radioButton = QtGui.QRadioButton(self.proxyGroupBox)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout_11.addWidget(self.radioButton)
        self.verticalLayout_10.addWidget(self.proxyGroupBox)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem3)
        self.stepLabel_4 = QtGui.QLabel(self.wizardPage_2)
        self.stepLabel_4.setObjectName(_fromUtf8("stepLabel_4"))
        self.verticalLayout_10.addWidget(self.stepLabel_4)
        Wizard.addPage(self.wizardPage_2)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        Wizard.setWindowTitle(_translate("Wizard", "Yandex Disk Service Helper Setup", None))
        self.accountGroupBox.setTitle(_translate("Wizard", "Yandex Account:", None))
        self.loginLabel.setText(_translate("Wizard", "Login:", None))
        self.passLabel.setText(_translate("Wizard", "Password:", None))
        self.yandexRu.setText(_translate("Wizard", "@yandex.ru", None))
        self.pushButton.setText(_translate("Wizard", "Login", None))
        self.stepLabel_1.setText(_translate("Wizard", "Step 1 of 4", None))
        self.yaRootGroupBox.setTitle(_translate("Wizard", "Select a directory for Yandex.Disk location:", None))
        self.defRootLabel.setText(_translate("Wizard", "Default: ~/Yandex.Disk (recommended)", None))
        self.yaRootCh.setText(_translate("Wizard", "...", None))
        self.stepLabel_2.setText(_translate("Wizard", "Step 2 of 4", None))
        self.yaCfgGroupBox.setTitle(_translate("Wizard", "Yandex Disk Service configuration file:", None))
        self.defCfgLabel.setText(_translate("Wizard", "Default: ~/.config/yandex-disk/config.cfg (recommended)", None))
        self.yaCfgCh.setText(_translate("Wizard", "...", None))
        self.yaAuthGroupBox.setTitle(_translate("Wizard", "Yandex Disk Service authorization file:", None))
        self.defAuthLabel.setText(_translate("Wizard", "Default: ~/.config/yandex-disk/passwd (recommended)", None))
        self.yaAuthCh.setText(_translate("Wizard", "...", None))
        self.stepLabel_3.setText(_translate("Wizard", "Step 3 of 4", None))
        self.proxyGroupBox.setTitle(_translate("Wizard", "Proxy configuration:", None))
        self.radioButton.setText(_translate("Wizard", "None", None))
        self.stepLabel_4.setText(_translate("Wizard", "Step 4 of 4", None))

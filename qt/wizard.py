# Form implementation generated from reading ui file 'wizard.ui'
#
# Created: Sun Aug  2 00:06:49 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import os
from PySide2 import QtCore
from PySide2.QtCore import QSize, QMetaObject
from PySide2.QtGui import QIcon, QPixmap, Qt, QFont
from PySide2.QtWidgets import QSizePolicy, QWizardPage, QVBoxLayout, QFrame, QHBoxLayout, QLabel, QGroupBox, \
    QRadioButton, QWidget, QGridLayout, QComboBox, QLineEdit, QCheckBox, QSpacerItem, QToolButton, \
    QPushButton


class UiWizard(object):
    def setup_ui(self, wizard):
        wizard.setObjectName("wizard")
        wizard.resize(417, 520)
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(wizard.sizePolicy().hasHeightForWidth())
        wizard.setSizePolicy(size_policy)
        wizard.setMinimumSize(QSize(417, 520))
        wizard.setMaximumSize(QSize(417, 520))
        icon = QIcon()
        icon.addPixmap(
            QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/yandex-disk.xpm")),
            QIcon.Normal,
            QIcon.Off
        )
        wizard.setWindowIcon(icon)
        self.wizardPage1 = QWizardPage()
        self.wizardPage1.setObjectName("wizardPage1")
        self.verticalLayout_4 = QVBoxLayout(self.wizardPage1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QFrame(self.wizardPage1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_12 = QHBoxLayout(self.frame)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label = QLabel(self.frame)
        self.label.setText("")
        self.label.setPixmap(
            QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/yandex_disk_logo.png"))
        )
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_12.addWidget(self.label)
        self.verticalLayout_4.addWidget(self.frame)
        self.proxyGroupBox = QGroupBox(self.wizardPage1)
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.proxyGroupBox.sizePolicy().hasHeightForWidth())
        self.proxyGroupBox.setSizePolicy(size_policy)
        self.proxyGroupBox.setObjectName("proxyGroupBox")
        self.verticalLayout_11 = QVBoxLayout(self.proxyGroupBox)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.proxyNone = QRadioButton(self.proxyGroupBox)
        self.proxyNone.setObjectName("proxyNone")
        self.verticalLayout_11.addWidget(self.proxyNone)
        self.proxyAuto = QRadioButton(self.proxyGroupBox)
        self.proxyAuto.setChecked(True)
        self.proxyAuto.setObjectName("proxyAuto")
        self.verticalLayout_11.addWidget(self.proxyAuto)
        self.proxyManual = QRadioButton(self.proxyGroupBox)
        self.proxyManual.setObjectName("proxyManual")
        self.verticalLayout_11.addWidget(self.proxyManual)
        self.proxyManualWidget = QWidget(self.proxyGroupBox)
        self.proxyManualWidget.setEnabled(False)
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.proxyManualWidget.sizePolicy().hasHeightForWidth())
        self.proxyManualWidget.setSizePolicy(size_policy)
        self.proxyManualWidget.setObjectName("proxyManualWidget")
        self.gridLayout = QGridLayout(self.proxyManualWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName("gridLayout")
        self.srvLabel = QLabel(self.proxyManualWidget)
        self.srvLabel.setObjectName("srvLabel")
        self.gridLayout.addWidget(self.srvLabel, 1, 0, 1, 1)
        self.proxyTypeLabel = QLabel(self.proxyManualWidget)
        self.proxyTypeLabel.setObjectName("proxyTypeLabel")
        self.gridLayout.addWidget(self.proxyTypeLabel, 0, 0, 1, 1)
        self.proxyType = QComboBox(self.proxyManualWidget)
        self.proxyType.setObjectName("proxyType")
        self.proxyType.addItem("")
        self.proxyType.addItem("")
        self.proxyType.addItem("")
        self.gridLayout.addWidget(self.proxyType, 0, 1, 1, 1)
        self.portLabel = QLabel(self.proxyManualWidget)
        self.portLabel.setObjectName("portLabel")
        self.gridLayout.addWidget(self.portLabel, 1, 2, 1, 1)
        self.srvName = QLineEdit(self.proxyManualWidget)
        self.srvName.setObjectName("srvName")
        self.gridLayout.addWidget(self.srvName, 1, 1, 1, 1)
        self.srvPasswordReq = QCheckBox(self.proxyManualWidget)
        self.srvPasswordReq.setObjectName("srvPasswordReq")
        self.gridLayout.addWidget(self.srvPasswordReq, 2, 1, 1, 1)
        self.portNumber = QLineEdit(self.proxyManualWidget)
        self.portNumber.setMinimumSize(QSize(50, 0))
        self.portNumber.setMaximumSize(QSize(50, 16777215))
        self.portNumber.setObjectName("portNumber")
        self.gridLayout.addWidget(self.portNumber, 1, 3, 1, 1)
        self.srvLoginLabel = QLabel(self.proxyManualWidget)
        self.srvLoginLabel.setObjectName("srvLoginLabel")
        self.gridLayout.addWidget(self.srvLoginLabel, 3, 0, 1, 1)
        self.srvLogin = QLineEdit(self.proxyManualWidget)
        self.srvLogin.setEnabled(False)
        self.srvLogin.setObjectName("srvLogin")
        self.gridLayout.addWidget(self.srvLogin, 3, 1, 1, 1)
        self.srvPasswordLabel = QLabel(self.proxyManualWidget)
        self.srvPasswordLabel.setObjectName("srvPasswordLabel")
        self.gridLayout.addWidget(self.srvPasswordLabel, 4, 0, 1, 1)
        self.srvPassword = QLineEdit(self.proxyManualWidget)
        self.srvPassword.setEnabled(False)
        self.srvPassword.setEchoMode(QLineEdit.Password)
        self.srvPassword.setObjectName("srvPassword")
        self.gridLayout.addWidget(self.srvPassword, 4, 1, 1, 1)
        self.verticalLayout_11.addWidget(self.proxyManualWidget)
        self.verticalLayout_4.addWidget(self.proxyGroupBox)
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacer_item)
        self.stepLabel_1 = QLabel(self.wizardPage1)
        self.stepLabel_1.setObjectName("stepLabel_1")
        self.verticalLayout_4.addWidget(self.stepLabel_1)
        wizard.addPage(self.wizardPage1)
        self.wizardPage2 = QWizardPage()
        self.wizardPage2.setObjectName("wizardPage2")
        self.verticalLayout_3 = QVBoxLayout(self.wizardPage2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.logoFrame_1 = QFrame(self.wizardPage2)
        self.logoFrame_1.setFrameShape(QFrame.StyledPanel)
        self.logoFrame_1.setFrameShadow(QFrame.Raised)
        self.logoFrame_1.setObjectName("logoFrame_1")
        self.horizontalLayout_4 = QHBoxLayout(self.logoFrame_1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.logoPixmap_1 = QLabel(self.logoFrame_1)
        self.logoPixmap_1.setEnabled(True)
        self.logoPixmap_1.setText("")
        self.logoPixmap_1.setPixmap(
            QPixmap((os.path.join(os.path.dirname(os.path.realpath(__file__))), "../ico/yandex_disk_logo.png"))
        )
        self.logoPixmap_1.setScaledContents(False)
        self.logoPixmap_1.setAlignment(Qt.AlignCenter)
        self.logoPixmap_1.setObjectName("logoPixmap_1")
        self.horizontalLayout_4.addWidget(self.logoPixmap_1)
        self.verticalLayout_3.addWidget(self.logoFrame_1)
        spacer_item1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacer_item1)
        self.accountGroupBox = QGroupBox(self.wizardPage2)
        self.accountGroupBox.setMaximumSize(QSize(16777215, 176))
        self.accountGroupBox.setObjectName("accountGroupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.accountGroupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.loginFfame = QFrame(self.accountGroupBox)
        self.loginFfame.setMaximumSize(QSize(464, 140))
        self.loginFfame.setFrameShape(QFrame.StyledPanel)
        self.loginFfame.setFrameShadow(QFrame.Raised)
        self.loginFfame.setObjectName("loginFfame")
        self.horizontalLayout_3 = QHBoxLayout(self.loginFfame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.loginLabelsFrame = QFrame(self.loginFfame)
        self.loginLabelsFrame.setMaximumSize(QSize(79, 120))
        self.loginLabelsFrame.setFrameShape(QFrame.StyledPanel)
        self.loginLabelsFrame.setFrameShadow(QFrame.Raised)
        self.loginLabelsFrame.setObjectName("loginLabelsFrame")
        self.verticalLayout = QVBoxLayout(self.loginLabelsFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loginLabel = QLabel(self.loginLabelsFrame)
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.loginLabel.setFont(font)
        self.loginLabel.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.loginLabel.setObjectName("loginLabel")
        self.verticalLayout.addWidget(self.loginLabel)
        self.passLabel = QLabel(self.loginLabelsFrame)
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.passLabel.setFont(font)
        self.passLabel.setObjectName("passLabel")
        self.verticalLayout.addWidget(self.passLabel)
        self.horizontalLayout_3.addWidget(self.loginLabelsFrame)
        self.loginEntryFrame = QFrame(self.loginFfame)
        self.loginEntryFrame.setMaximumSize(QSize(16777215, 120))
        self.loginEntryFrame.setFrameShape(QFrame.StyledPanel)
        self.loginEntryFrame.setFrameShadow(QFrame.Raised)
        self.loginEntryFrame.setObjectName("loginEntryFrame")
        self.verticalLayout_2 = QVBoxLayout(self.loginEntryFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.yaLoginFrame = QFrame(self.loginEntryFrame)
        self.yaLoginFrame.setFrameShape(QFrame.StyledPanel)
        self.yaLoginFrame.setFrameShadow(QFrame.Raised)
        self.yaLoginFrame.setObjectName("yaLoginFrame")
        self.horizontalLayout = QHBoxLayout(self.yaLoginFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yaLogin = QLineEdit(self.yaLoginFrame)
        self.yaLogin.setMinimumSize(QSize(119, 0))
        self.yaLogin.setMaximumSize(QSize(119, 16777215))
        self.yaLogin.setObjectName("yaLogin")
        self.horizontalLayout.addWidget(self.yaLogin)
        self.yandexRu = QLabel(self.yaLoginFrame)
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.yandexRu.setFont(font)
        self.yandexRu.setObjectName("yandexRu")
        self.horizontalLayout.addWidget(self.yandexRu)
        self.verticalLayout_2.addWidget(self.yaLoginFrame)
        self.yaPassFrame = QFrame(self.loginEntryFrame)
        self.yaPassFrame.setFrameShape(QFrame.StyledPanel)
        self.yaPassFrame.setFrameShadow(QFrame.Raised)
        self.yaPassFrame.setObjectName("yaPassFrame")
        self.horizontalLayout_11 = QHBoxLayout(self.yaPassFrame)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.yaPass = QLineEdit(self.yaPassFrame)
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.yaPass.sizePolicy().hasHeightForWidth())
        self.yaPass.setSizePolicy(size_policy)
        self.yaPass.setMinimumSize(QSize(119, 0))
        self.yaPass.setInputMethodHints(Qt.ImhHiddenText | Qt.ImhNoAutoUppercase | Qt.ImhNoPredictiveText)
        self.yaPass.setEchoMode(QLineEdit.Password)
        self.yaPass.setObjectName("yaPass")
        self.horizontalLayout_11.addWidget(self.yaPass)
        self.loginButton = QPushButton(self.yaPassFrame)
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout_11.addWidget(self.loginButton)
        self.verticalLayout_2.addWidget(self.yaPassFrame)
        self.horizontalLayout_3.addWidget(self.loginEntryFrame)
        self.horizontalLayout_2.addWidget(self.loginFfame)
        self.verticalLayout_3.addWidget(self.accountGroupBox)
        spacer_item2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacer_item2)
        self.loginResult = QLabel(self.wizardPage2)
        self.loginResult.setText("")
        self.loginResult.setAlignment(Qt.AlignCenter)
        self.loginResult.setWordWrap(True)
        self.loginResult.setObjectName("loginResult")
        self.verticalLayout_3.addWidget(self.loginResult)
        self.stepLabel_2 = QLabel(self.wizardPage2)
        self.stepLabel_2.setObjectName("stepLabel_2")
        self.verticalLayout_3.addWidget(self.stepLabel_2)
        wizard.addPage(self.wizardPage2)
        self.wizardPage3 = QWizardPage()
        self.wizardPage3.setObjectName("wizardPage3")
        self.verticalLayout_5 = QVBoxLayout(self.wizardPage3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.logoFrame_2 = QFrame(self.wizardPage3)
        self.logoFrame_2.setFrameShape(QFrame.StyledPanel)
        self.logoFrame_2.setFrameShadow(QFrame.Raised)
        self.logoFrame_2.setObjectName("logoFrame_2")
        self.horizontalLayout_5 = QHBoxLayout(self.logoFrame_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.logoPixmap_2 = QLabel(self.logoFrame_2)
        self.logoPixmap_2.setEnabled(True)
        self.logoPixmap_2.setText("")
        self.logoPixmap_2.setPixmap(
            QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/yandex_disk_logo.png"))
        )
        self.logoPixmap_2.setScaledContents(False)
        self.logoPixmap_2.setAlignment(Qt.AlignCenter)
        self.logoPixmap_2.setObjectName("logoPixmap_2")
        self.horizontalLayout_5.addWidget(self.logoPixmap_2)
        self.verticalLayout_5.addWidget(self.logoFrame_2)
        spacer_item3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacer_item3)
        self.yaRootGroupBox = QGroupBox(self.wizardPage3)
        self.yaRootGroupBox.setObjectName("yaRootGroupBox")
        self.verticalLayout_6 = QVBoxLayout(self.yaRootGroupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.defRootLabel = QLabel(self.yaRootGroupBox)
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.defRootLabel.sizePolicy().hasHeightForWidth())
        self.defRootLabel.setSizePolicy(size_policy)
        self.defRootLabel.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.defRootLabel.setObjectName("defRootLabel")
        self.verticalLayout_6.addWidget(self.defRootLabel)
        self.yaRootFrame = QFrame(self.yaRootGroupBox)
        self.yaRootFrame.setFrameShape(QFrame.StyledPanel)
        self.yaRootFrame.setFrameShadow(QFrame.Raised)
        self.yaRootFrame.setObjectName("yaRootFrame")
        self.horizontalLayout_6 = QHBoxLayout(self.yaRootFrame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.yaRoot = QLineEdit(self.yaRootFrame)
        self.yaRoot.setObjectName("yaRoot")
        self.horizontalLayout_6.addWidget(self.yaRoot)
        self.yaRootCh = QToolButton(self.yaRootFrame)
        icon1 = QIcon()
        icon1.addPixmap(
            QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/folder_edit.png")),
            QIcon.Normal,
            QIcon.Off
        )
        self.yaRootCh.setIcon(icon1)
        self.yaRootCh.setObjectName("yaRootCh")
        self.horizontalLayout_6.addWidget(self.yaRootCh)
        self.verticalLayout_6.addWidget(self.yaRootFrame)
        spacer_item4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacer_item4)
        self.verticalLayout_5.addWidget(self.yaRootGroupBox)
        self.stepLabel_3 = QLabel(self.wizardPage3)
        self.stepLabel_3.setObjectName("stepLabel_3")
        self.verticalLayout_5.addWidget(self.stepLabel_3)
        wizard.addPage(self.wizardPage3)
        self.wizardPage4 = QWizardPage()
        self.wizardPage4.setObjectName("wizardPage4")
        self.verticalLayout_7 = QVBoxLayout(self.wizardPage4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.logoFrame_3 = QFrame(self.wizardPage4)
        self.logoFrame_3.setFrameShape(QFrame.StyledPanel)
        self.logoFrame_3.setFrameShadow(QFrame.Raised)
        self.logoFrame_3.setObjectName("logoFrame_3")
        self.horizontalLayout_7 = QHBoxLayout(self.logoFrame_3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.logoPixmap_3 = QLabel(self.logoFrame_3)
        self.logoPixmap_3.setEnabled(True)
        self.logoPixmap_3.setText("")
        self.logoPixmap_3.setPixmap(
            QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/yandex_disk_logo.png"))
        )
        self.logoPixmap_3.setScaledContents(False)
        self.logoPixmap_3.setAlignment(Qt.AlignCenter)
        self.logoPixmap_3.setObjectName("logoPixmap_3")
        self.horizontalLayout_7.addWidget(self.logoPixmap_3)
        self.verticalLayout_7.addWidget(self.logoFrame_3)
        self.yaCfgGroupBox = QGroupBox(self.wizardPage4)
        self.yaCfgGroupBox.setObjectName("yaCfgGroupBox")
        self.verticalLayout_8 = QVBoxLayout(self.yaCfgGroupBox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.defCfgLabel = QLabel(self.yaCfgGroupBox)
        self.defCfgLabel.setObjectName("defCfgLabel")
        self.verticalLayout_8.addWidget(self.defCfgLabel)
        self.yaCfgFrame = QFrame(self.yaCfgGroupBox)
        self.yaCfgFrame.setFrameShape(QFrame.StyledPanel)
        self.yaCfgFrame.setFrameShadow(QFrame.Raised)
        self.yaCfgFrame.setObjectName("yaCfgFrame")
        self.horizontalLayout_8 = QHBoxLayout(self.yaCfgFrame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.yaCfg = QLineEdit(self.yaCfgFrame)
        self.yaCfg.setObjectName("yaCfg")
        self.horizontalLayout_8.addWidget(self.yaCfg)
        self.yaCfgCh = QToolButton(self.yaCfgFrame)
        self.yaCfgCh.setIcon(icon1)
        self.yaCfgCh.setObjectName("yaCfgCh")
        self.horizontalLayout_8.addWidget(self.yaCfgCh)
        self.verticalLayout_8.addWidget(self.yaCfgFrame)
        self.verticalLayout_7.addWidget(self.yaCfgGroupBox)
        self.yaAuthGroupBox = QGroupBox(self.wizardPage4)
        self.yaAuthGroupBox.setObjectName("yaAuthGroupBox")
        self.verticalLayout_9 = QVBoxLayout(self.yaAuthGroupBox)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.defAuthLabel = QLabel(self.yaAuthGroupBox)
        self.defAuthLabel.setObjectName("defAuthLabel")
        self.verticalLayout_9.addWidget(self.defAuthLabel)
        self.yaAuthFrame = QFrame(self.yaAuthGroupBox)
        self.yaAuthFrame.setFrameShape(QFrame.StyledPanel)
        self.yaAuthFrame.setFrameShadow(QFrame.Raised)
        self.yaAuthFrame.setObjectName("yaAuthFrame")
        self.horizontalLayout_9 = QHBoxLayout(self.yaAuthFrame)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.yaAuth = QLineEdit(self.yaAuthFrame)
        self.yaAuth.setObjectName("yaAuth")
        self.horizontalLayout_9.addWidget(self.yaAuth)
        self.yaAuthCh = QToolButton(self.yaAuthFrame)
        self.yaAuthCh.setIcon(icon1)
        self.yaAuthCh.setObjectName("yaAuthCh")
        self.horizontalLayout_9.addWidget(self.yaAuthCh)
        self.verticalLayout_9.addWidget(self.yaAuthFrame)
        self.verticalLayout_7.addWidget(self.yaAuthGroupBox)
        spacer_item5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacer_item5)
        self.stepLabel_4 = QLabel(self.wizardPage4)
        self.stepLabel_4.setObjectName("stepLabel_4")
        self.verticalLayout_7.addWidget(self.stepLabel_4)
        wizard.addPage(self.wizardPage4)

        self.retranslate_ui(wizard)
        QMetaObject.connectSlotsByName(wizard)

    def retranslate_ui(self, wizard):
        _translate = QtCore.QCoreApplication.translate
        wizard.setWindowTitle(_translate("wizard", "Yandex Disk Service Helper Setup", None))
        self.proxyGroupBox.setTitle(_translate("wizard", "Proxy configuration:", None))
        self.proxyNone.setText(_translate("wizard", "None", None))
        self.proxyAuto.setText(_translate("wizard", "Auto", None))
        self.proxyManual.setText(_translate("wizard", "Manual", None))
        self.srvLabel.setText(_translate("wizard", "Server:", None))
        self.proxyTypeLabel.setText(_translate("wizard", "Type:", None))
        self.proxyType.setItemText(0, _translate("wizard", "HTTPS", None))
        self.proxyType.setItemText(1, _translate("wizard", "SOCKS4", None))
        self.proxyType.setItemText(2, _translate("wizard", "SOCKS5", None))
        self.portLabel.setText(_translate("wizard", "Port:", None))
        self.srvPasswordReq.setText(_translate("wizard", "Server Credentials", None))
        self.srvLoginLabel.setText(_translate("wizard", "Login:", None))
        self.srvPasswordLabel.setText(_translate("wizard", "Password:", None))
        self.stepLabel_1.setText(_translate("wizard", "Step 1 of 4", None))
        self.accountGroupBox.setTitle(_translate("wizard", "Yandex Account:", None))
        self.loginLabel.setText(_translate("wizard", "Login:", None))
        self.passLabel.setText(_translate("wizard", "Password:", None))
        self.yandexRu.setText(_translate("wizard", "@yandex.ru", None))
        self.loginButton.setText(_translate("wizard", "Login", None))
        self.stepLabel_2.setText(_translate("wizard", "Step 2 of 4", None))
        self.yaRootGroupBox.setTitle(_translate("wizard", "Select a directory for Yandex.Disk location:", None))
        self.defRootLabel.setText(_translate("wizard", "Default: ~/Yandex.Disk (recommended)", None))
        self.yaRootCh.setText(_translate("wizard", "...", None))
        self.stepLabel_3.setText(_translate("wizard", "Step 3 of 4", None))
        self.yaCfgGroupBox.setTitle(_translate("wizard", "Yandex Disk Service configuration file:", None))
        self.defCfgLabel.setText(_translate("wizard", "Default: ~/.config/yandex-disk/config.cfg (recommended)", None))
        self.yaCfgCh.setText(_translate("wizard", "...", None))
        self.yaAuthGroupBox.setTitle(_translate("wizard", "Yandex Disk Service authorization file:", None))
        self.defAuthLabel.setText(_translate("wizard", "Default: ~/.config/yandex-disk/passwd (recommended)", None))
        self.yaAuthCh.setText(_translate("wizard", "...", None))
        self.stepLabel_4.setText(_translate("wizard", "Step 4 of 4", None))

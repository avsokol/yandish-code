# Form implementation generated from reading ui file 'about.ui'
#
# Created: Tue Jun 30 22:57:57 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
from PySide2 import QtCore
from PySide2.QtCore import QObject, SIGNAL, QCoreApplication
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QSizePolicy, QVBoxLayout, QLabel, QPushButton


class UiDialog(object):
    def setup_ui(self, dialog):
        dialog.setObjectName("dialog")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.resize(340, 150)
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(dialog.sizePolicy().hasHeightForWidth())
        dialog.setSizePolicy(size_policy)
        dialog.setAutoFillBackground(True)
        self.verticalLayout_2 = QVBoxLayout(dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QLabel(dialog)
        size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(size_policy)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.pushButton = QPushButton(dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.retranslate_ui(dialog)
        QObject.connect(self.pushButton, SIGNAL("clicked()"), dialog.close)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslate_ui(self, dialog):
        _translate = QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "About", None))
        self.label.setText(
            _translate(
                "dialog",
                "<html><head/><body><p align=\"center\">Yandex Disk Service Helper.</p>"
                "<p align=\"center\"><a href=\"https://sourceforge.net/projects/yandish/\">"
                "<span style=\" text-decoration: underline; color:#0000ff;\">"
                "https://sourceforge.net/projects/yandish/"
                "</span></a></p><p align=\"center\">Alexander Sokolov</p></body></html>",
                None
            )
        )
        self.pushButton.setText(_translate("dialog", "Ok", None))

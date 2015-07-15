# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import *

from  wizard import Ui_Wizard

class yaWizard(QWizard,  Ui_Wizard):
    def __init__(self, parent = None):
        QWizard.__init__(self, parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    yaWiz = yaWizard()
    yaWiz.show()
    sys.exit(app.exec_())

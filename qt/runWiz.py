# -*- coding: utf-8 -*-

import sys,os


rpath = os.path.realpath(__file__)
print(rpath)
dirname = os.path.dirname(rpath)
rjoin = os.path.join(dirname,"../")
sys.path.append(rjoin)

print(sys.path)

from subprocess import Popen, PIPE

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import *

from wizard import Ui_Wizard

from yandish import WhichPrg

class yaWizard(QWizard,  Ui_Wizard):
    def __init__(self, parent = None):
        QWizard.__init__(self, parent)
        self.setupUi(self)
        self.setSignals()

    def loginToYandex(self):
        login = str(self.yaLogin.text())
        passw = self.yaPass.text()

        login = login.rstrip("@yandex.ru")

        hint = ""

        if login != "":
            login = login + "@yandex.ru"

        if login == "" or passw == "":
            if login == "":
                hint = hint + "Login is Empty"
            if passw == "":
                if hint != "":
                    hint = hint + "\n"
                hint = hint + "Password is empty"

            self.setLoginStatus(2,hint)
            return

        prg = WhichPrg()

        proc = Popen([prg, "token",
                      "-p", passw,
                      login,
                      "/tmp/yandish.tmp"],
                     stdout=PIPE, stderr=PIPE)
        return_code = proc.wait()

        if return_code != 0:
            hint = hint.strip(proc.stdout.read())

        self.setLoginStatus(return_code,hint)

    def setLoginStatus(self,status,hint=""):

        palette = QtGui.QPalette()

        if status == 0:
            message = "Login Ok!"
            palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.darkGreen)
        elif status == 1:
            message = "Login Failled!"
            palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
        elif status == 2:
            message = "Not enough credentials"
            palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)

        self.loginResult.setPalette(palette)
        self.loginResult.setText(message)
        self.loginResult.setToolTip(hint)

    def setSignals(self):
        QtCore.QObject.connect(self.loginButton, QtCore.SIGNAL("clicked()"), self.loginToYandex)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    yaWiz = yaWizard()
    yaWiz.show()
    #sys.exit(app.exec_())
    sys.exit(yaWiz.exec_())

# -*- coding: utf-8 -*-

import sys,os, shutil

rpath = os.path.realpath(__file__)
dirname = os.path.dirname(rpath)
rjoin = os.path.join(dirname,"../")
sys.path.append(rjoin)

from subprocess import Popen, PIPE

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import *

from wizard import Ui_Wizard
from yandish import WhichPrg, getDefaultParams
from opts import AppOptions
import actions

class yaWizard(QWizard,  Ui_Wizard):

    _prg = None
    _config = None
    _dir = None
    _auth = None
    _exclude_dirs = None
    _proxy = None

    _default_auth = "/tmp/yandish_auth.tmp"

    def __init__(self, params, parent = None):

        self._prg = params["prg"]
        self._config = params["config"]
        self._dir = params["rootdir"]
        self._auth = params["auth"]
        self._proxy = params["proxy"]

        QWizard.__init__(self, parent)
        self.setupUi(self)

        self.yaRoot.setText(self._dir)
        self.yaCfg.setText(self._config)
        self.yaAuth.setText(self._auth)
        
        self.setSignals()

    def loginToYandex(self):
        login = str(self.yaLogin.text())
        login = login.rstrip("@yandex.ru")
        passw = self.yaPass.text()

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

        proc = Popen([self._prg, "token",
                      "-p", passw,
                      login,
                      self._default_auth],
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

        if status == 0:
            self.button(self.NextButton).setEnabled(True)
        else:
            self.button(self.NextButton).setEnabled(False)

    def saveAuthFile(self):
        shutil.move(self._default_auth,os.path.expanduser(self._auth))

    def wizardFinish(self):
        yandex_cfg = os.path.expanduser(self._config)
        yandex_root = os.path.expanduser(self._dir)
        yandex_auth = os.path.expanduser(self._auth)
        #yandex_proxy = self._proxy

        self.saveAuthFile()

        params = {"auth": yandex_auth, "dir": yandex_root}
        actions.SaveParamsInCfgFile(params,yandex_cfg)

        appOpts = AppOptions()
        defParams = getDefaultParams()
        yandexcfg = yandex_cfg
        if yandex_cfg == os.path.expanduser(defParams["config"]):
            yandexcfg = ""
        appOpts.setParam("yandex-cfg",yandexcfg)
        appOpts.saveParamsToRcFile()

    def setSignals(self):
        QtCore.QObject.connect(self.loginButton, QtCore.SIGNAL("clicked()"), self.loginToYandex)
        QtCore.QObject.connect(self.button(self.FinishButton), QtCore.SIGNAL("clicked()"), self.wizardFinish)

if __name__ == "__main__":

    params = getDefaultParams()

    app = QtGui.QApplication(sys.argv)
    yaWiz = yaWizard(params)

    yaWiz.show()
    yaWiz.button(yaWiz.NextButton).setEnabled(False)

    sys.exit(yaWiz.exec_())

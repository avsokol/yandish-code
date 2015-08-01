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
    _rootdir = None
    _auth = None
    _exclude_dirs = None
    _proxy = None

    _default_auth = "/tmp/yandish_auth.tmp"

    def __init__(self, params, parent = None):

        self._prg = params["prg"]
        self._config = params["config"]
        self._rootdir = params["rootdir"]
        self._auth = params["auth"]
        self._proxy = params["proxy"]

        QWizard.__init__(self, parent)
        self.setupUi(self)

        self.yaRoot.setText(self._rootdir)
        self.yaCfg.setText(self._config)
        self.yaAuth.setText(self._auth)

        self.setProxy()

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
        if self.proxyType.currentText() in [ "HTTPS", "SOCKS5" ]:
            self.srvPasswordReq.setEnabled(True)
        else:
            self.srvPasswordReq.setEnabled(False)
        self.toggleProxyAuth()

    def setProxy(self):
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

    def getProxyCfg(self):
        if self.proxyNone.isChecked():
            self._proxy="none"
        elif self.proxyAuto.isChecked():
            self._proxy="auto"
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

    def wizardFinish(self):
        yandex_cfg = str(self.yaCfg.text())
        yandex_root = str(self.yaRoot.text())
        yandex_auth = str(self.yaAuth.text())

        self.getProxyCfg()

        yandex_proxy = self._proxy

        try:
            self.saveAuthFile()
        except IOError:
            print("Couldn't write Yandex authorization file")
            sys.exit(2)

        params = {"auth": yandex_auth, "dir": yandex_root, "proxy": yandex_proxy}

        try:
            actions.SaveParamsInCfgFile(params,yandex_cfg)
        except IOError:
            print("Couldn't write Yandex configuration file")
            sys.exit(3)

        appOpts = AppOptions()
        defParams = getDefaultParams()
        yandexcfg = yandex_cfg
        if yandex_cfg == os.path.expanduser(defParams["config"]):
            yandexcfg = ""
        appOpts.setParam("yandex-cfg",yandexcfg)

        try:
            appOpts.saveParamsToRcFile()
        except IOError:
            print("Couldn't write App configuration file")
            sys.exit(4)

    def setSignals(self):
        QtCore.QObject.connect(self.loginButton, QtCore.SIGNAL("clicked()"), self.loginToYandex)
        QtCore.QObject.connect(self.button(self.FinishButton), QtCore.SIGNAL("clicked()"), self.wizardFinish)

        QtCore.QObject.connect(self.proxyNone, QtCore.SIGNAL("clicked()"), self.proxyDisable)
        QtCore.QObject.connect(self.proxyAuto, QtCore.SIGNAL("clicked()"), self.proxyDisable)
        QtCore.QObject.connect(self.proxyManual, QtCore.SIGNAL("clicked()"), self.proxyEnable)

        QtCore.QObject.connect(self.srvPasswordReq, QtCore.SIGNAL("clicked()"), self.toggleProxyAuth)
        QtCore.QObject.connect(self.proxyType, QtCore.SIGNAL("currentIndexChanged(QString)"), self.toggleProxyAuthReq)

if __name__ == "__main__":

    params = getDefaultParams()

    app = QtGui.QApplication(sys.argv)
    yaWiz = yaWizard(params)

    yaWiz.show()
    yaWiz.button(yaWiz.NextButton).setEnabled(False)

    sys.exit(yaWiz.exec_())

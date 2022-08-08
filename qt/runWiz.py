import sys
import os
import shutil
from PySide2.QtGui import QPalette

rpath = os.path.realpath(__file__)
dirname = os.path.dirname(rpath)
rjoin = os.path.join(dirname, "../")
sys.path.append(rjoin)

from subprocess import Popen, PIPE
from PySide2.QtWidgets import QWizard, QApplication
from PySide2.QtCore import Qt, SIGNAL, QObject
from .wizard import UiWizard
from yandish import get_default_params
from lib.opts import AppOptions
from lib import actions


class YaWizard(QWizard, UiWizard):

    _prg = None
    _config = None
    _rootdir = None
    _auth = None
    _exclude_dirs = None
    _proxy = None

    _default_auth = "/tmp/yandish_auth.tmp"
    _login_error = 1

    def __init__(self, params, parent=None):

        self._prg = params["prg"]
        self._config = params["config"]
        self._rootdir = params["rootdir"]
        self._auth = params["auth"]
        self._proxy = params["proxy"]

        QWizard.__init__(self, parent)
        self.setup_ui(self)

        self.yaRoot.setText(self._rootdir)
        self.yaCfg.setText(self._config)
        self.yaAuth.setText(self._auth)

        self.set_proxy()

        self.set_signals()

    def login_to_yandex(self):

        self.save_proxy_cfg()

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

            self.set_login_status(2, hint)
            return

        proc = Popen([self._prg, "token",
                      "-p", passw,
                      login,
                      self._default_auth],
                     stdout=PIPE, stderr=PIPE)
        return_code = proc.wait()

        if return_code != 0:
            hint = hint.strip(proc.stdout.read())

        self.set_login_status(return_code, hint)

    def set_login_status(self, status, hint=""):

        self._login_error = status

        palette = QPalette()

        message = ""

        if status == 0:
            message = "Login Ok!"
            palette.setColor(QPalette.Foreground, Qt.darkGreen)
        elif status == 1:
            message = "Login Failed!"
            palette.setColor(QPalette.Foreground, Qt.red)
        elif status == 2:
            message = "Not enough credentials"
            palette.setColor(QPalette.Foreground, Qt.red)

        self.loginResult.setPalette(palette)
        self.loginResult.setText(message)
        self.loginResult.setToolTip(hint)

        if status == 0:
            self.button(self.NextButton).setEnabled(True)
        else:
            self.button(self.NextButton).setEnabled(False)

    def save_auth_file(self):
        shutil.move(self._default_auth, os.path.expanduser(self._auth))

    def proxy_enable(self):
        self.proxyManualWidget.setEnabled(True)

    def proxy_disable(self):
        self.proxyManualWidget.setEnabled(False)

    def toggle_proxy_auth(self):
        if self.srvPasswordReq.isEnabled() and self.srvPasswordReq.isChecked():
            self.srvLogin.setEnabled(True)
            self.srvPassword.setEnabled(True)
        else:
            self.srvLogin.setEnabled(False)
            self.srvPassword.setEnabled(False)

    def toggle_proxy_auth_req(self):
        if self.proxyType.currentText() in ["HTTPS", "SOCKS5"]:
            self.srvPasswordReq.setEnabled(True)
        else:
            self.srvPasswordReq.setEnabled(False)
        self.toggle_proxy_auth()

    def set_proxy(self):
        if self._proxy == "no":
            self.proxyNone.setChecked(1)
            self.proxy_disable()

        elif self._proxy == "auto":
            self.proxyAuto.setChecked(1)
            self.proxy_disable()

        else:
            self.proxyManual.setChecked(1)
            self.proxy_enable()
            proxy_params = self._proxy.split(",")

            p_type = proxy_params[0].upper()
            server = proxy_params[1]
            port = proxy_params[2]

            p_types = [self.proxyType.itemText(i) for i in range(self.proxyType.count())]
            if p_type in p_types:
                self.proxyType.setCurrentIndex(p_types.index(p_type))

            self.srvName.setText(server)
            self.portNumber.setText(port)

            if p_type in ["HTTPS", "SOCKS5"]:
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

            self.toggle_proxy_auth_req()

    def get_proxy_cfg(self):
        if self.proxyNone.isChecked():
            self._proxy = "no"

        elif self.proxyAuto.isChecked():
            self._proxy = "auto"

        elif self.proxyManual.isChecked():
            proxy_params = []
            p_type = str(self.proxyType.currentText()).lower()
            proxy_params.append(p_type)

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

    def save_proxy_cfg(self):
        self.get_proxy_cfg()

        yandex_cfg = str(self.yaCfg.text())

        yandex_proxy = self._proxy
        params = {"proxy": yandex_proxy}

        try:
            actions.save_params_in_cfg_file(params, yandex_cfg)
        except IOError:
            print("Couldn't write Yandex configuration file")
            sys.exit(3)

    def set_next_button_state(self, id):
        if id == 1 and self._login_error:
            state = False
        else:
            state = True
        self.button(self.NextButton).setEnabled(state)

    def wizard_finish(self):
        yandex_cfg = str(self.yaCfg.text())
        yandex_root = str(self.yaRoot.text())
        yandex_auth = str(self.yaAuth.text())

        self.get_proxy_cfg()

        yandex_proxy = self._proxy

        try:
            self.save_auth_file()

        except IOError:
            print("Couldn't write Yandex authorization file")
            sys.exit(2)

        params = {"auth": yandex_auth, "dir": yandex_root, "proxy": yandex_proxy}

        try:
            actions.save_params_in_cfg_file(params, yandex_cfg)

        except IOError:
            print("Couldn't write Yandex configuration file")
            sys.exit(3)

        app_opts = AppOptions()
        def_params = get_default_params("widget")
        yandexcfg = yandex_cfg
        if yandex_cfg == os.path.expanduser(def_params["config"]):
            yandexcfg = ""
        app_opts.set_param("yandex-cfg", yandexcfg)

        try:
            app_opts.save_params_to_rc_file()

        except IOError:
            print("Couldn't write App configuration file")
            sys.exit(4)

    def set_signals(self):
        QObject.connect(self.loginButton, SIGNAL("clicked()"), self.login_to_yandex)
        QObject.connect(self.button(self.FinishButton), SIGNAL("clicked()"), self.wizard_finish)

        QObject.connect(self.proxyNone, SIGNAL("clicked()"), self.proxy_disable)
        QObject.connect(self.proxyAuto, SIGNAL("clicked()"), self.proxy_disable)
        QObject.connect(self.proxyManual, SIGNAL("clicked()"), self.proxy_enable)

        QObject.connect(self.srvPasswordReq, SIGNAL("clicked()"), self.toggle_proxy_auth)
        QObject.connect(self.proxyType, SIGNAL("currentIndexChanged(QString)"), self.toggle_proxy_auth_req)
        QObject.connect(self, SIGNAL("currentIdChanged(int)"), self.set_next_button_state)


if __name__ == "__main__":

    params = get_default_params("widget")

    app = QApplication(sys.argv)
    yaWiz = YaWizard(params)

    yaWiz.show()

    sys.exit(yaWiz.exec_())

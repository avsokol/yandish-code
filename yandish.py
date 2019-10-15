#!/usr/bin/python

import sys
import os
import argparse
from subprocess import Popen, PIPE

from PySide2.QtWidgets import QMessageBox

from lib.opts import AppOptions
from lib.actions import get_auth_from_cfg_file, get_yandex_cfg_from_cfg_file, get_exclude_dirs_from_cfg_file, get_root_dir_from_cfg_file,\
    get_proxy_from_cfg_file, save_params_in_cfg_file, do_action, process_result


def get_default_params(action):
    daemon = which_prg(action)
    params = {"config": "~/.config/yandex-disk/config.cfg",
              "auth": "~/.config/yandex-disk/passwd",
              "exclude-dirs": [],
              "rootdir": "~/Yandex.Disk",
              "prg": daemon,
              "proxy": "auto"}

    return params


def show_dlg(err_msg):
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("Couldn't find yandex-disk daemon")
    msg.setInformativeText("You have to install yandex-disk daemon from Yandex site.")
    msg.setWindowTitle("Error")
    msg.setDetailedText(err_msg)
    msg.setStandardButtons(QMessageBox.Ok)
    sys.exit(msg.exec_())


def which_prg(action):

    executable = "yandex-disk"

    proc = Popen(["which", executable], stdout=PIPE, stderr=PIPE)
    return_code = proc.wait()
    if return_code == 0:
        prg = proc.stdout.read()
        prg = prg.strip()
        prg = prg.decode("UTF-8")
        return prg

    else:
        err_output = proc.stderr.read()
        err_output = err_output.strip()
        err_output = err_output.decode("UTF-8")
        if action == "widget":
            show_dlg("Error " + str(return_code) + ":\nCouldn't find " + executable + " executable\n" + err_output)
        else:
            raise Exception("Error %s: Couldn't find '%s' executable\n%s" % (return_code, executable, err_output))


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--program", default="")
    parser.add_argument("-c", "--config", default="")
    parser.add_argument("-d", "--dir", default="")
    parser.add_argument("-a", "--auth", default="")
    parser.add_argument("--proxy", default="")
    parser.add_argument("-x", "--exclude-dirs", default=[])
    parser.add_argument("--action", choices=["start", "stop", "status", "widget"], default="widget")

    return parser


def show_widget(params):

    from PySide2 import QtGui
    from qt.window import Window
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(os.path.realpath(__file__)), "ico/yandex-disk.xpm")))

    window = Window(params)

    window.init_app()

    sys.exit(app.exec_())


def tune_params(params, action):

    # TODO: to be refactored
    def_params = get_default_params(action)

    ya_params = {}

    if params["prg"] == "":
        params["prg"] = def_params["prg"]

    if params["config"] == "":
        app_opts = AppOptions()
        app_cfg = app_opts.get_rc_path()
        params["config"] = get_yandex_cfg_from_cfg_file(app_cfg, 0)

    if params["config"] == "":
        params["config"] = def_params["config"]

    params["config"] = os.path.expanduser(params["config"])

    if params["auth"] == "":
        params["auth"] = get_auth_from_cfg_file(params["config"], 0)

    if params["auth"] == "":
        params["auth"] = def_params["auth"]

    params["auth"] = os.path.expanduser(params["auth"])
    ya_params["auth"] = params["auth"]

    if params["rootdir"] == "":
        params["rootdir"] = get_root_dir_from_cfg_file(params["config"], 0)

    if params["rootdir"] == "":
        params["rootdir"] = def_params["rootdir"]

    params["rootdir"] = os.path.expanduser(params["rootdir"])
    ya_params["dir"] = params["rootdir"]

    if params["proxy"] == "":
        params["proxy"] = get_proxy_from_cfg_file(params["config"], 0)

    if params["proxy"] == "":
        params["proxy"] = def_params["proxy"]

    ya_params["proxy"] = params["proxy"]

    if len(params["exclude-dirs"]) == 0:
        params["exclude-dirs"] = get_exclude_dirs_from_cfg_file(params["config"], 0)
        if params["exclude-dirs"] == [""]:
            params["exclude-dirs"] = []
            ya_params["exclude-dirs"] = ""

    else:
        params["exclude-dirs"] = ",".join(params["exclude-dirs"])
        ya_params["exclude-dirs"] = params["exclude-dirs"]

    save_params_in_cfg_file(ya_params, params["config"])


def main(argv):
    params = {}

    parser = arg_parser()
    p_args = parser.parse_args(argv[0:])

    action = p_args.action
 
    params["prg"] = p_args.program

    params["config"] = p_args.config
    params["rootdir"] = p_args.dir
    params["auth"] = p_args.auth
    params["exclude-dirs"] = p_args.exclude_dirs
    params["proxy"] = p_args.proxy

    tune_params(params, action)

    if action == "widget":
        show_widget(params)
    else:
        res, msg = do_action(action, params)
        process_result(res, action, msg, params)
        exit(res)


if __name__ == "__main__":
    main(sys.argv[1:])

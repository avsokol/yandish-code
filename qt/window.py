import os
from PySide2 import QtCore, QtGui
from PySide2.QtCore import Qt, SIGNAL, SignalInstance
from PySide2.QtGui import *
from PySide2.QtWidgets import QDialog, QMainWindow, QMenu, QApplication, QFileDialog, QTreeWidgetItem
from lib.decorators.action_wait_cursor import ActionWaitCursor
from lib.decorators.wait_cursor import WaitCursor
from .wlayout import UiMainWindow
from lib import actions
from .about import UiDialog
from .trayIcon import SystemTrayIcon
from lib.opts import AppOptions
from yandish import get_default_params, tune_params
from .runWiz import YaWizard
import threading


class About(QDialog, UiDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setup_ui(self)
        self.show()


class Window(QMainWindow, UiMainWindow):

    _removeItems = []
    _threads = []

    _geometry = None

    _prg = None
    _config = None
    _rootdir = None
    _auth = None
    _exclude_dirs = None
    _proxy = None

    _service_err = 0

    addChildSignal = SignalInstance()

    def __init__(self, params, parent=None):

        self.params_init(params)

        QMainWindow.__init__(self, parent)

        self.setup_ui(self)

        self.set_signals()
        self.tIcon = SystemTrayIcon(self)

        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.tree_context_menu)

        self.uTimer = QtCore.QTimer()
        # QtCore.QObject.connect(self.uTimer, SIGNAL("timeout()"), self.refresh_status)
        self.uTimer.timeout.connect(self.refresh_status)

        # is_running, message = actions.is_daemon_running(self._prg)
        # if is_running:
        self.start_timer()

    def tree_context_menu(self, position):
        item = self.treeWidget.itemAt(position)
        if item is None:
            return

        item_prop = self.get_item_properties(item)
        if not item_prop["checkable"]:
            return

        expand_pict = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/expand.xpm")
        collapse_pict = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/collapse.xpm")

        check_pict = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/check.xpm")
        uncheck_pict = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/uncheck.xpm")

        expand_icon = QtGui.QIcon(expand_pict)
        collapse_icon = QtGui.QIcon(collapse_pict)
        check_icon = QtGui.QIcon(check_pict)
        uncheck_icon = QtGui.QIcon(uncheck_pict)

        menu = QMenu()

        if item.childCount():
            expand = menu.addAction(self.tr("Expand"))
            collapse = menu.addAction(self.tr("Collapse"))
            expand.setIcon(expand_icon)
            collapse.setIcon(collapse_icon)
            menu.addSeparator()

            if item.isExpanded():
                expand.setEnabled(False)
                collapse.setEnabled(True)
                QtCore.QObject.connect(collapse, SIGNAL("triggered()"), lambda: item.setExpanded(False))

            else:
                expand.setEnabled(True)
                collapse.setEnabled(False)
                QtCore.QObject.connect(expand, SIGNAL("triggered()"), lambda: item.setExpanded(True))

        check = menu.addAction(self.tr("Check"))
        uncheck = menu.addAction(self.tr("UnCheck"))

        check.setIcon(check_icon)
        uncheck.setIcon(uncheck_icon)

        if item_prop["state"] == Qt.Checked:
            check.setEnabled(False)
            uncheck.setEnabled(True)
            QtCore.QObject.connect(uncheck, SIGNAL("triggered()"), lambda: item.setCheckState(0, Qt.Unchecked))

        else:
            check.setEnabled(True)
            uncheck.setEnabled(False)
            QtCore.QObject.connect(check, SIGNAL("triggered()"), lambda: item.setCheckState(0, Qt.Checked))

        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))

    def params_init(self, params):
        self._prg = params["prg"]
        self._config = params["config"]
        self._rootdir = params["rootdir"]
        self._auth = params["auth"]
        self._exclude_dirs = params["exclude-dirs"]
        self._proxy = params["proxy"]

    def get_params(self):
        return {"prg": self._prg,
                "config": self._config,
                "auth": self._auth,
                "exclude-dirs": self._exclude_dirs,
                "rootdir": self._rootdir}

    def start_timer(self):
        if self.refreshTimeout.value() > 0 and not self.is_timer_active():
            self.uTimer.start(self.refreshTimeout.value() * 1000)

        if self.refreshTimeout.value() == 0 and self.is_timer_active():
            self.uTimer.stop()

    def stop_timer(self):
        self.uTimer.stop()

    def is_timer_active(self):
        return self.uTimer.isActive()

    def restart_timer(self):
        if self.is_timer_active():
            self.stop_timer()

        self.start_timer()

    def closeEvent(self, event):
        self.hide()
        event.ignore()

    def event(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange and self.isMinimized():
            app_opts = AppOptions()
            hide_on_minimize = int(app_opts.get_param("HideOnMinimize"))
            if hide_on_minimize:
                self.hide()

            return True
        else:
            return super(Window, self).event(event)

    @staticmethod
    def screen_geometry():
        g = QApplication.desktop().screenGeometry()
        return g.width(), g.height()

    def hide(self):
        self._geometry = self.saveGeometry()
        super(Window, self).hide()

    def show(self):
        if self._geometry is None:
            screen_x, screen_y = self.screen_geometry()
            w = self.width()
            h = self.height()
            x = int((screen_x-w)/2)
            y = int((screen_y-w)/2)
            self.setGeometry(QtCore.QRect(x, y, w, h))
        else:
            self.restoreGeometry(self._geometry)

        super(Window, self).show()

    def update_tray_menu_state(self):
        self.tIcon.update_tray_menu_state()

    def fill_options(self):
        self.yandex_exec.setText(self._prg)
        self.yandex_exec.setEnabled(False)
        self.yandex_cfg.setText(self._config)
        self.yandex_cfg.setReadOnly(True)
        self.yandex_root.setText(self._rootdir)
        self.yandex_root.setReadOnly(True)
        self.yandex_auth.setText(self._auth)
        self.yandex_auth.setReadOnly(True)

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

        app_opts = AppOptions()
        hide_on_minimize = int(app_opts.get_param("HideOnMinimize"))
        start_minimized = int(app_opts.get_param("StartMinimized"))
        start_service_at_start = int(app_opts.get_param("startServiceAtStart"))
        refresh_period = int(app_opts.get_param("autorefresh"))
        self.startHidden.setChecked(start_minimized)
        self.hideOnMinimize.setChecked(hide_on_minimize)
        self.startServiceAtStart.setChecked(start_service_at_start)
        self.refreshTimeout.setProperty("value", refresh_period)

    def reload_options(self):
        self.fill_options()

        self.refresh_tree(0, 1)

        root = self.treeWidget.invisibleRootItem()
        self.check_children(root)
        for path in self._exclude_dirs:
            self.uncheck_path(path, 0)

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

    def save_yandex_options(self):
        self.get_proxy_cfg()

        yandex_cfg = self.yandex_cfg.text()
        yandex_root = self.yandex_root.text()
        yandex_auth = self.yandex_auth.text()
        yandex_proxy = self._proxy

        self._exclude_dirs = self.get_exclude_dirs_from_tree()
        dirs = ",".join(self._exclude_dirs)

        params = {"auth": yandex_auth, "dir": yandex_root, "exclude-dirs": dirs, "proxy": yandex_proxy}
        actions.save_params_in_cfg_file(params, self._config)

    def save_app_options(self):
        app_opts = AppOptions()
        if self.startHidden.isChecked():
            start_minimized = "1"
        else:
            start_minimized = "0"

        if self.hideOnMinimize.isChecked():
            hide_on_minimize = "1"
        else:
            hide_on_minimize = "0"

        if self.startServiceAtStart.isChecked():
            start_service_at_start = "1"
        else:
            start_service_at_start = "0"

        refresh_period = str(self.refreshTimeout.value())

        yandex_cfg = self.yandex_cfg.text()

        def_params = get_default_params("widget")

        yandexcfg = yandex_cfg

        app_opts.set_param("HideOnMinimize", hide_on_minimize)
        app_opts.set_param("StartMinimized", start_minimized)
        app_opts.set_param("autorefresh", refresh_period)
        app_opts.set_param("startServiceAtStart", start_service_at_start)
        app_opts.set_param("yandex-cfg", yandexcfg)
        app_opts.save_params_to_rc_file()

    def save_options(self):
        self.save_yandex_options()
        self.save_app_options()

    def choose_root_dir(self):
        dirname = QFileDialog.getExistingDirectory(
            self,
            "Select Directory to be the root for Yandex Disk",
            self.yandex_root.text()
        )
        if dirname != "":
            self._rootdir = str(dirname)
            self.yandex_root.setText(dirname)
            self.refresh_tree(1, 1)

    def choose_auth_file(self):
        filename = QFileDialog.getOpenFileName(self, "Select Yandex Auth File", os.environ["HOME"])
        if filename[0] != "":
            self._auth = str(filename)
            self.yandex_auth.setText(filename)

    def choose_cfg_file(self):
        filename = QFileDialog.getSaveFileName(self, "Select Yandex Configuration File", os.environ["HOME"])
        if filename[0] != "":
            self._config = str(filename)
            self.yandex_cfg.setText(filename)

            self.save_options()

    @staticmethod
    def get_path_from_item(item):
        path = []

        text = str(item.text(0))
        path.insert(0, text)

        while item.parent() is not None:
            text = str(item.parent().text(0))
            path.insert(0, text)
            item = item.parent()

        path = "/".join(path)
        return path

    def add_item(self, path, properties):
        item = self.find_path_item(path)
        if item is None:
            item = self.create_child(path)

        if item is not None:
            self.set_item_properties(item, properties)

    def modify_item(self, path, properties):
        item = self.find_path_item(path)
        if item is not None:
            modify_state = 0
            if properties['checkable'] == 0:
                modify_state = 1

            self.set_item_properties(item, properties, modify_state=modify_state)
            if properties["checkable"] == 0:
                for i in range(item.childCount()):
                    child = item.child(i)
                    item.removeChild(child)

    def remove_item(self, path):
        item = self.find_path_item(path)
        if item is None:
            if path in self._removeItems:
                self._removeItems.remove(path)
        else:
            parent = item.parent()
            if parent is None:
                parent = self.treeWidget.invisibleRootItem()

            parent.removeChild(item)
            if path in self._removeItems:
                self._removeItems.remove(path)
            if path in self._exclude_dirs:
                self._exclude_dirs.remove(path)

    def check_and_rm_unused_tree_item(self, parent_item=""):
        if not isinstance(parent_item, QTreeWidgetItem):
            parent_item = self.treeWidget.invisibleRootItem()

        for i in range(parent_item.childCount()):
            child = parent_item.child(i)
            try:
                path = self.get_path_from_item(child)

            except:
                continue

            path = os.path.join(self._rootdir, path)

            if self.is_child_to_be_removed(path):
                path = path.lstrip(self._rootdir)
                if path not in self._removeItems:
                    self._removeItems.append(path)
                    # self.emit(SIGNAL("removeChild"), path)

            else:
                self.check_and_rm_unused_tree_item(child)

    @staticmethod
    def get_item_properties(item):
        properties = {
            "itemText": [str(item.text(0)), str(item.text(1))],
            "foreground": item.foreground(0),
            "checkable": 1,
            "state": item.checkState(0)
        }

        if item.flags() & QtCore.Qt.ItemIsUserCheckable:
            properties["checkable"] = 1
        else:
            properties["checkable"] = 0

        return properties

    def get_path_properties(self, path):
        exists = 0
        is_link = 0
        target = ""
        state = Qt.Checked

        if os.path.isdir(path):
            exists = 1
        if os.path.islink(path):
            is_link = 1
            target = os.readlink(path)
            if os.path.exists(target):
                exists = 1
            else:
                exists = 0

        if path.lstrip(self._rootdir) in self._exclude_dirs:
            state = Qt.Unchecked

        return exists, is_link, target, state

    def prepare_item_properties(self, path, text, exists, is_link, target, state):
        properties = {
            "itemText": [text, ""],
            "foreground": Qt.black,
            "checkable": 1,
            "state": state
        }

        while path != "":
            if path in self._exclude_dirs:
                properties["state"] = Qt.Unchecked
                break
            path = os.path.dirname(path)

        text1 = ""
        if is_link:
            text1 = " -> " + target
        properties["itemText"] = [text, text1]

        if is_link == 1 and exists == 0:
            properties["foreground"] = Qt.red
            properties["checkable"] = 0

        return properties

    @staticmethod
    def set_item_properties(child, properties, modify_state=1):
        child.setText(0, properties["itemText"][0])
        child.setText(1, properties["itemText"][1])
        child.setForeground(0, properties["foreground"])
        child.setForeground(1, properties["foreground"])
        child.setToolTip(0, properties["itemText"][0])
        child.setToolTip(1, properties["itemText"][1])

        if modify_state:
            child.setCheckState(0, properties["state"])

        if properties["checkable"]:
            folder_icon = QtGui.QIcon()
            folder_icon.addPixmap(
                QtGui.QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/folder_closed.png")),
                QtGui.QIcon.Normal,
                QtGui.QIcon.Off
            )
            folder_icon.addPixmap(
                QtGui.QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/folder.png")),
                QtGui.QIcon.Normal,
                QtGui.QIcon.On
            )
            child.setIcon(0, folder_icon)
            child.setFlags(child.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable)
        else:
            err_icon = QtGui.QIcon()
            err_icon.addPixmap(
                QtGui.QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/folder_error.png")),
                QtGui.QIcon.Normal,
                QtGui.QIcon.Off
            )
            child.setIcon(0, err_icon)
            child.setFlags(child.flags() ^ Qt.ItemIsUserCheckable ^ Qt.ItemIsSelectable)

    def is_child_exist(self, path):
        child = self.find_path_item(path)

        if child is None:
            return 0
        else:
            return 1

    @staticmethod
    def is_child_to_be_removed(path):
        try:
            os.lstat(path)
            exists = 1

        except:
            exists = 0

        if exists == 0 or (exists == 1 and os.path.isdir(path) and os.path.exists(path) == 0):
            return 1

        else:
            return 0

    def is_child_to_be_modified(self, path, properties):
        child = self.find_path_item(path)
        if child is None:
            return 0

        item_prop = self.get_item_properties(child)

        for key in properties.keys():
            if key == "itemText":
                if properties[key][0] != item_prop[key][0] or \
                                properties[key][1] != item_prop[key][1]:
                    return 1
            else:
                if properties[key] != item_prop[key]:
                    return 1

        return 0

    def create_child(self, path):
        updir = os.path.dirname(path)

        if updir == "":
            parent_item = "root"

        else:
            parent_item = self.find_path_item(updir)

        if not isinstance(parent_item, QTreeWidgetItem):
            child = QTreeWidgetItem(self.treeWidget)
            self.treeWidget.itemBelow(child)

        elif parent_item is None:
            child = None

        else:
            child = QTreeWidgetItem(parent_item)
            parent_item.addChild(child)

        return child

    def add_dir_as_tree_item(self, parent_dir="", startup=0):
        if parent_dir == "":
            parent_dir = self._rootdir

        c = threading.currentThread()

        if c not in self._threads:
            self._threads.append(c)

        if os.path.exists(parent_dir):
            dirs = os.listdir(parent_dir)

            if len(dirs):
                for d in sorted(dirs):
                    path = os.path.join(parent_dir, d)

                    if os.path.isfile(path) == 0 and d != ".sync":
                        lpath = path.lstrip(self._rootdir)
                        exists, is_link, target, state = self.get_path_properties(path)
                        properties = self.prepare_item_properties(lpath, d, exists, is_link, target, state)

                        if self.is_child_exist(lpath) == 0:
                            if startup:
                                self.add_item(lpath, properties)
                            else:
                                self.add_item(lpath, properties)
                                # self.emit(SIGNAL("addChild"), lpath, properties)
                        elif self.is_child_to_be_modified(lpath, properties):
                            self.modify_item(lpath, properties)
                            # self.emit(SIGNAL("modifyChild"), lpath, properties)

                        self.add_dir_as_tree_item(path, startup)

        if c in self._threads:
            self._threads.remove(c)

    def find_unchecked_items_among_children(self, items, parent_item, column=0):
        if not isinstance(parent_item, QTreeWidgetItem):
            parent_item = self.treeWidget.invisibleRootItem()

        for i in range(parent_item.childCount()):
            if parent_item.child(i).checkState(0) == 0:
                items.append(parent_item.child(i))
            else:
                self.find_unchecked_items_among_children(items, parent_item.child(i), column)
        return items

    def find_item_among_children(self, parent_item, text_to_find, column=0):
        if not isinstance(parent_item, QTreeWidgetItem):
            parent_item = self.treeWidget.invisibleRootItem()

        for i in range(parent_item.childCount()):
            if text_to_find == parent_item.child(i).text(column):
                return parent_item.child(i)

    def find_path_item(self, path_to_find, column=0):
        path = path_to_find.split("/")

        index = None
        for i in path:
            try:
                index = self.find_item_among_children(index, i, column)
            except:
                return None

        return index

    def change_check_state_for_path(self, path_to_find, state, column=0):
        item = self.find_path_item(path_to_find, column)
        if item is not None:
            item.setCheckState(column, state)

    def check_path(self, path_to_find, column=0):
        self.change_check_state_for_path(path_to_find, Qt.Checked, column=column)

    def uncheck_path(self, path_to_find, column=0):
        self.change_check_state_for_path(path_to_find, Qt.Unchecked, column=column)

    def check_children(self, item):
        for i in range(item.childCount()):
            if item.child(i).flags() & QtCore.Qt.ItemIsUserCheckable:
                item.child(i).setCheckState(0, Qt.Checked)
                if item.child(i).childCount() > 0:
                    self.check_children(item.child(i))
        
    def check_parent(self, item):
        if item.parent() is not None:
            item.parent().setCheckState(0, Qt.Checked)
            self.check_parent(item.parent())

    def handle_item_checked(self, item):
        self.check_children(item)
        self.check_parent(item)

    def handle_item_unchecked(self, item):
        for i in range(item.childCount()):
            item.child(i).setCheckState(0, Qt.Unchecked)
            if item.child(i).childCount() > 0:
                self.handle_item_unchecked(item.child(i))

    def handle_item_changed(self, item):
        self.treeWidget.blockSignals(True)
        if item.checkState(0) == QtCore.Qt.Checked:
            self.handle_item_checked(item)
        elif item.checkState(0) == QtCore.Qt.Unchecked:
            self.handle_item_unchecked(item)
        self.treeWidget.blockSignals(False)

    def get_exclude_dirs_from_tree(self):
        paths = []
        items = []
        items = self.find_unchecked_items_among_children(items, "")
        for item in items:
            path = self.get_path_from_item(item)
            paths.append(path)

        return paths

    def save_tree_exclude_dirs(self):
        self._exclude_dirs = self.get_exclude_dirs_from_tree()
        actions.save_exclude_dirs(self._exclude_dirs, self._config)

    def refresh_tree(self, force=0, clear=0):
        if not os.path.exists(self._rootdir):
            try:
                os.mkdir(self._rootdir)

            except:
                return

        if not self.isHidden() or force == 1:

            # for thread in self._threads:
            #     thread._Thread__stop()

            if clear:
                self.treeWidget.clear()

            # self.connect(self, SIGNAL("addChild"), self.add_item)
            # self.connect(self, SIGNAL("modifyChild"), self.modify_item)
            ## self.connect(self, SIGNAL("removeChild"), self.remove_item)

            thread_add = threading.Thread(target=self.add_dir_as_tree_item)
            thread_add.daemon = True
            thread_add.start()

            thread_rm = threading.Thread(target=self.check_and_rm_unused_tree_item)
            thread_rm.daemon = True
            thread_rm.start()
            thread_rm.join()

            for path in self._removeItems:
                self.remove_item(path.lstrip(self._rootdir))

    def init_app(self):
        self.fill_options()
        if self.startServiceAtStart.isChecked():
            self.add_dir_as_tree_item("", 1)
            self.act_service("start")
        else:
            self.refresh_status(1)

        if self._service_err == 3:
            self.run_wizard()

        else:
            self.treeWidget.expandToDepth(False)
            self.treeWidget.itemChanged.connect(self.handle_item_changed)
            self.update_action_buttons()

            app_opts = AppOptions()
            start_minimized = int(app_opts.get_param("StartMinimized"))

            if start_minimized == 0:
                self.show()

            self.update_tray_menu_state()
            self.refresh_status()

    @ActionWaitCursor()
    def act_service(self, action):
        if action == "start":
            self.save_tree_exclude_dirs()

        params = self.get_params()
        res, msg = actions.do_action(action, params)

        self._service_err = res

        cur_text = self.textEdit.toPlainText()
        new_text = actions.process_result(res, action, msg, params, 0)

        if new_text != cur_text:
            self.textEdit.clear()
            self.textEdit.append(new_text)
            self.tIcon.update_tool_tip(new_text)

            y_status = actions.get_status_from_msg(new_text)
            self.tIcon.setIcon(y_status)

    def refresh_status(self, force=0, clear=0):
        self.stop_timer()

        for thread in self._threads:
            thread._shutdown()
            # thread._Thread__stop()

        self.act_service("status")
        self.refresh_tree(force, clear)

        self.start_timer()

    def handle_spin_change(self):
        self.refresh_status()
        self.restart_timer()

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

    # @WaitCursor()
    @staticmethod
    def show_about():
        about = About()
        about.exec_()

    def update_action_buttons(self):
        is_running, message = actions.is_daemon_running(self._prg)
        if is_running:
            self.set_button_in_state("start", "disabled")
            self.set_action_in_state("start", "disabled")
            self.set_button_in_state("stop", "enabled")
            self.set_action_in_state("stop", "enabled")
        else:
            self.set_button_in_state("stop", "disabled")
            self.set_action_in_state("stop", "disabled")
            self.set_button_in_state("start", "enabled")
            self.set_action_in_state("start", "enabled")

    def set_button_in_state(self, button, state):
        if button == "start":
            btn = self.btnStart

        elif button == "stop":
            btn = self.btnStop

        elif button == "status":
            return

        else:
            raise Exception("Unknown button '%s'" % button)

        if state == "disabled":
            btn.setEnabled(False)

        elif state == "enabled":
            btn.setEnabled(True)

        else:
            pass

    def set_action_in_state(self, action, state):
        if action == "start":
            act = self.actionStart

        elif action == "stop":
            act = self.actionStop

        elif action == "status":
            act = self.actionStatus

        else:
            raise Exception("Unknown action '%s'" % action)

        if state == "disabled":
            act.setEnabled(False)

        elif state == "enabled":
            act.setEnabled(True)

        else:
            pass

    def run_wizard(self):
        self.hide()

        params = dict()
        params["prg"] = self._prg
        params["config"] = self._config
        params["rootdir"] = self._rootdir
        params["auth"] = self._auth
        params["exclude-dirs"] = ""
        params["proxy"] = self._proxy

        ya_wiz = YaWizard(params)

        ya_wiz.setWindowModality(Qt.ApplicationModal)
        ya_wiz.show()
        # ya_wiz.button(ya_wiz.NextButton).setEnabled(False)

        wiz_result = ya_wiz.exec_()

        self.show()

        if wiz_result == 0:
            return

        params["prg"] = ""
        params["config"] = ""
        params["rootdir"] = ""
        params["auth"] = ""
        params["exclude-dirs"] = ""
        params["proxy"] = ""

        tune_params(params, "widget")
        self.params_init(params)
        self.reload_options()

    def set_signals(self):
        QtCore.QObject.connect(self.btnExit, SIGNAL("clicked()"), QApplication.quit)

        QtCore.QObject.connect(self.btnStart, SIGNAL("clicked()"), lambda: self.act_service("start"))
        QtCore.QObject.connect(self.btnStop, SIGNAL("clicked()"), lambda: self.act_service("stop"))
        QtCore.QObject.connect(self.btnStatus, SIGNAL("clicked()"), self.refresh_status)

        QtCore.QObject.connect(self.actionStart, SIGNAL("triggered()"), lambda: self.act_service("start"))
        QtCore.QObject.connect(self.actionStop, SIGNAL("triggered()"), lambda: self.act_service("stop"))
        QtCore.QObject.connect(self.actionStatus, SIGNAL("triggered()"), self.refresh_status)

        QtCore.QObject.connect(self.actionSetup_Wizard, SIGNAL("triggered()"), self.run_wizard)

        QtCore.QObject.connect(self.actionHide, SIGNAL("triggered()"), self.hide)
        QtCore.QObject.connect(self.actionExit, SIGNAL("triggered()"), QApplication.quit)

        QtCore.QObject.connect(self.actionReloadCfg, SIGNAL("triggered()"), self.reload_options)
        QtCore.QObject.connect(self.actionSaveCfg, SIGNAL("triggered()"), self.save_options)

        QtCore.QObject.connect(self.ch_yandex_root, SIGNAL("clicked()"), self.choose_root_dir)
        QtCore.QObject.connect(self.ch_yandex_auth, SIGNAL("clicked()"), self.choose_auth_file)
        QtCore.QObject.connect(self.ch_yandex_cfg, SIGNAL("clicked()"), self.choose_cfg_file)

        QtCore.QObject.connect(self.actionAbout, SIGNAL("triggered()"), self.show_about)

        QtCore.QObject.connect(self.refreshTimeout, SIGNAL("editingFinished()"), self.handle_spin_change)

        QtCore.QObject.connect(self.proxyNone, SIGNAL("clicked()"), self.proxy_disable)
        QtCore.QObject.connect(self.proxyAuto, SIGNAL("clicked()"), self.proxy_disable)
        QtCore.QObject.connect(self.proxyManual, SIGNAL("clicked()"), self.proxy_enable)

        QtCore.QObject.connect(self.srvPasswordReq, SIGNAL("clicked()"), self.toggle_proxy_auth)
        QtCore.QObject.connect(self.proxyType, SIGNAL("currentIndexChanged(QString)"), self.toggle_proxy_auth_req)

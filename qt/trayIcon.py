import os
from PySide6.QtCore import QObject, SIGNAL, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QApplication


class SystemTrayIcon(QSystemTrayIcon):

    _parent = None

    __icon = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/yandex-disk.xpm")
    __iconActive = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/yandex-disk_active.xpm")
    __iconPaused = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../ico/yandex-disk_paused.xpm")

    def setParent(self, parent):
        self._parent = parent

    def get_parent(self):
        return self._parent

    def __init__(self, parent=None):

        self.setParent(parent)

        QSystemTrayIcon.__init__(self, parent)

        if QSystemTrayIcon.isSystemTrayAvailable():
            self.trayIcon = QSystemTrayIcon()
            self.setIcon()
            menu = QMenu(parent)
            self.showAction = menu.addAction("Show")
            self.hideAction = menu.addAction("Hide")
            menu.addSeparator()
            exit_action = menu.addAction("Exit")
            QObject.connect(self.showAction, SIGNAL("triggered()"), self.toggle_window)
            QObject.connect(self.hideAction, SIGNAL("triggered()"), self.toggle_window)
            QObject.connect(exit_action, SIGNAL("triggered()"), QApplication.quit)

            self.update_tool_tip("Yandex Disk")
            self.trayIcon.activated.connect(self.on_tray_icon_activated)
            self.trayIcon.setContextMenu(menu)
            self.trayIcon.show()

            self.disambiguateTimer = QTimer(self)
            self.disambiguateTimer.setSingleShot(True)
            self.disambiguateTimer.timeout.connect(self.disambiguate_timer_timeout)

            self.update_tray_menu_state()

    def setIcon(self, status="Unknown"):
        if status in [u"index", u"sync", u"busy", u"синхронизация", u"обработка данных"]:
            icon = QIcon(self.__iconActive)
        elif status in [u"paused", u"остановлен", u"демон не запущен"]:
            icon = QIcon(self.__iconPaused)
        else:
            icon = QIcon(self.__icon)

        self.trayIcon.setIcon(icon)

    def update_tray_menu_state(self):
        parent = self.get_parent()
        if parent.isVisible():
            self.showAction.setEnabled(False)
            self.hideAction.setEnabled(True)
        elif parent.isHidden():
            self.showAction.setEnabled(True)
            self.hideAction.setEnabled(False)

    def update_tool_tip(self, msg):
        self.trayIcon.setToolTip(msg)

    def on_tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            # self.disambiguateTimer.start(QtGui.qApp.doubleClickInterval())
            self.disambiguateTimer.start(0)
        elif reason == QSystemTrayIcon.DoubleClick:
            self.disambiguateTimer.stop()
            # self.toggle_window()

    def disambiguate_timer_timeout(self):
        self.toggle_window()

    def toggle_window(self):
        parent = self.get_parent()
        if parent.isVisible():
            parent.hide()

        elif parent.isHidden():
            parent.show()
            parent.showNormal()

        self.update_tray_menu_state()

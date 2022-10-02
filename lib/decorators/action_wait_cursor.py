from PySide6.QtGui import QCursor, Qt
from PySide6.QtWidgets import QApplication


class ActionWaitCursor(object):

    def __init__(self):
        pass

    def __call__(self, target_func):
        def func_wrapper(cls, action):
            QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
            cls.set_button_in_state(action, "disabled")

            QApplication.processEvents()
            QApplication.processEvents()

            target_func(cls, action)

            cls.set_button_in_state(action, "enabled")
            QApplication.restoreOverrideCursor()
            cls.update_action_buttons()

        return func_wrapper

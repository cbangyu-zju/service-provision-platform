from PyQt5 import QtCore, QtGui, QtWidgets


class ConfigButton(QtWidgets.QPushButton):

    def __init__(self, widget, config_model):
        super(ConfigButton, self).__init__(widget)
        self._model = config_model
        self._set_green = "QPushButton {background-color: green; color: white;}"
        self._set_red = "QPushButton {background-color: #e5863b; color: white;}"

    def on_click(self):
        status = self.check()
        self.set(not status)
        self.refresh()

    def check(self):
        return self._model.check()

    def set(self, status):
        self._model.set(status)
        self.refresh()

    def refresh(self):
        status = self.check()
        if status:
            self._set_to_green()
        else:
            self._set_to_red()

    def _refresh(self, status):
        if status:
            self._set_to_green()
        else:
            self._set_to_red()

    def _set_to_green(self):
        self.setStyleSheet(self._set_green)

    def _set_to_red(self):
        self.setStyleSheet(self._set_red)


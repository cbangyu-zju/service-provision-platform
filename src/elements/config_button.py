from PyQt5 import QtCore, QtGui, QtWidgets


class ConfigButton(QtWidgets.QPushButton):

    def __init__(self, widget, config_model):
        super(ConfigButton, self).__init__(widget)
        self._model = config_model
        self._set_palette = QtGui.QPalette(QtGui.QColor(112, 144, 79))
        self._unset_palette = QtGui.QPalette(QtGui.QColor(202, 120, 49))

    def action(self):
        status = self.check()
        self.set(not status)
        self._refresh(status)

    def check(self):
        return self._model.check()

    def set(self, status):
        self._model.set(status)
        self._refresh(status)

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
        self.setPalette(self._set_palette)

    def _set_to_red(self):
        self.setPalette(self._unset_palette)


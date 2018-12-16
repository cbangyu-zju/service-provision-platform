from PyQt5 import QtCore, QtGui, QtWidgets


class FunctionnTreeView(QtWidgets.QTreeWidget):

    def __init__(self, parent_widget):
        super(FunctionnTreeView, self).__init__(parent_widget)

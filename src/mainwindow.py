# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/view/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import system_configuration
from elements import function_treeview


class Ui_MainWindow(object):

    _tree_map = {
        '基础配置': [],
        '应用服务': [],
        '中间件': [],
        '数据库': [],
        '网络设置': []
    }

    def setupUi(self, MainWindow):
        MainWindow.setPalette(QtGui.QPalette(QtGui.QColor(122, 122, 122)))
        MainWindow.setObjectName("")
        MainWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.systemConfigDlg = system_configuration.SystemConfigDlg()
        self.systemConfigDlg.setupUi(self.centralwidget)

        self.treeView = function_treeview.FunctionTreeWidget(self.centralwidget)
        self.treeView.setPalette(QtGui.QPalette(QtGui.QColor(40, 40, 40)))
        self.treeView.setGeometry(QtCore.QRect(0, 80, 150, 550))
        self.treeView.setObjectName("treeView")
        self.treeView.setHeaderLabel("")
        self.addItems()

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 900, 86))
        self.label.setPixmap(QtGui.QPixmap("./src/res/images/Logo.jpeg"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 80))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", ""))

    def addItems(self):
        for key, value in self._tree_map.items():
            qparent = QtWidgets.QTreeWidgetItem(self.treeView)
            qparent.setText(0, key)
            if len(value) > 0:
                for v in value:
                    item = QtWidgets.QTreeWidgetItem(qparent)
                    item.setText(0, v)

        self.treeView.itemClicked['QTreeWidgetItem*', 'int'].connect(self._on_click_tree)

    def _on_click_tree(self, item, column):
        selectd_item = self.treeView.selectedItems()[0]
        item_text = selectd_item.text(0)
        if item_text == '基础配置':
            self.systemConfigDlg.showUi()
        else:
            self.systemConfigDlg.hideUi()





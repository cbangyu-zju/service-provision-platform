# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/view/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import system_configuration


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setPalette(QtGui.QPalette(QtGui.QColor(40, 40, 40)))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setPalette(QtGui.QPalette(QtGui.QColor(40, 40, 40)))
        self.treeView.setGeometry(QtCore.QRect(0, 80, 150, 550))
        self.treeView.setObjectName("treeView")

        self.systemConfigDlg = system_configuration.SystemConfigDlg()
        self.systemConfigDlg.setupUi(self.centralwidget)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 50, 50))
        qpic = QtGui.QPicture()
        qpic.load("./res/images/Logo.jpeg")
        self.label.setPicture(qpic)

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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))



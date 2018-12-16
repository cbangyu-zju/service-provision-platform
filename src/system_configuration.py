# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/view/system_configuration.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from elements import config_button
from basic_config import forbidden_root_remote_login, forbidden_useless_service
from basic_config import password_complexity, password_period
from basic_config import operation_timeout, login_failed_time_limit, unlawful_lock_limit
from basic_config import enable_log, design_audit_regulation, audit_file_authority, protection_audit_log
from basic_config import config_umask, config_bash_history, config_history_timestamp
from basic_config import forbidden_keyboard_close_command, forbidden_mobile_device
from basic_config import open_ssh_upgrade


class SystemConfigDlg(object):
    _system = 'REDHAT'
    _version = "16.01"
    _button_weight = 160
    _button_hight = 50
    _button_interval_h = 8
    _button_interval_w = 10
    _left_interval = 10
    _head_interval = 50
    _button_list = []

    def setupUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setObjectName("Form")
        Form.resize(750, 550)
        Form.setWindowTitle(_translate("Form", "Form"))

        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(170, 80, 700, 500))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setStyleSheet(
        """
            QTabBar::tab:selected {
                background: gray;
                color: white;
            }
            QTabBar::tab {
                background: #404040;
                color: white;
                width: 200px;
                height: 30px;
                border-top-left-radius: 2px;
                border-top-right-radius: 3px;
                margin-right: 2px;
            }
            QTabWidget::pane {
                background: gray;
            }
        """)

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("一键扫描")
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "一键扫描"))
        self.tab.addAction(self._check_all())


        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("一键配置")
        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "一键设置"))
        self.tab_2.addAction(self._set_all())

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("一键还原")
        self.tabWidget.addTab(self.tab_3, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "一键还原"))
        self.tab_3.addAction(self._unset_all())

        self.tabWidget.currentChanged.connect(self._on_tab_change)

        # l1
        self.button_11= config_button.ConfigButton(
            self.tabWidget, forbidden_root_remote_login.ForbiddenRootRemoteLogin(self._system, self._version))
        self.button_11.setGeometry(QtCore.QRect(
            self._left_interval,
            self._head_interval,
            self._button_weight, self._button_hight))
        self.button_11.setObjectName("button_11")
        self.button_11.setText(_translate("Form", "限制root账户远程登陆"))
        self._button_list.append(self.button_11)

        self.button_12 = config_button.ConfigButton(
            self.tabWidget, forbidden_useless_service.ForbiddenUselessService(self._system, self._version))
        self.button_12.setGeometry(QtCore.QRect(
            self._left_interval+self._button_weight+self._button_interval_w,
            self._head_interval, self._button_weight, self._button_hight))
        self.button_12.setObjectName("button_12")
        self.button_12.setText(_translate("Form", "禁用不需要的服务"))
        self._button_list.append(self.button_12)

        # l2
        self.button_21 = config_button.ConfigButton(
            self.tabWidget, password_complexity.PasswordComplexity(self._system, self._version))
        self.button_21.setGeometry(QtCore.QRect(
            self._left_interval,
            self._head_interval+self._button_hight+self._button_interval_h,
            self._button_weight, self._button_hight))
        self.button_21.setObjectName("button_21")
        self.button_21.setText(_translate("Form", "密码复杂度"))
        self._button_list.append(self.button_21)

        self.button_22 = config_button.ConfigButton(
            self.tabWidget, password_period.PasswordPeriod(self._system, self._version))
        self.button_22.setGeometry(QtCore.QRect(
            self._left_interval+self._button_weight+self._button_interval_w,
            self._head_interval+self._button_hight+self._button_interval_h,
            self._button_weight, self._button_hight))
        self.button_22.setObjectName("button_22")
        self.button_22.setText(_translate("Form", "口令周期"))
        self._button_list.append(self.button_22)

        # l3
        self.button_31 = config_button.ConfigButton(
            self.tabWidget, operation_timeout.OperationTimeout(self._system, self._version))
        self.button_31.setGeometry(QtCore.QRect(
            self._left_interval,
            self._head_interval+2*(self._button_hight+self._button_interval_h),
            self._button_weight, self._button_hight))
        self.button_31.setObjectName("button_31")
        self.button_31.setText(_translate("Form", "操作超时锁定"))
        self._button_list.append(self.button_31)

        self.button_32 = config_button.ConfigButton(
            self.tabWidget, login_failed_time_limit.LoginFaidedTimeLimit(self._system, self._version))
        self.button_32.setGeometry(QtCore.QRect(
            self._left_interval+self._button_weight+self._button_interval_w,
            self._head_interval+2*(self._button_hight+self._button_interval_h),
            self._button_weight, self._button_hight))
        self.button_32.setObjectName("button_32")
        self.button_32.setText(_translate("Form", "登陆失败次数"))
        self._button_list.append(self.button_32)

        self.button_33 = config_button.ConfigButton(
            self.tabWidget, unlawful_lock_limit.UnlawfulLockLimit(self._system, self._version))
        self.button_33.setGeometry(QtCore.QRect(
            self._left_interval+2*(self._button_weight+self._button_interval_w),
            self._head_interval+2*(self._button_hight+self._button_interval_h),
            self._button_weight, self._button_hight))
        self.button_33.setObjectName("button_33")
        self.button_33.setText(_translate("Form", "非法登陆锁定"))
        self._button_list.append(self.button_33)

        # l4
        self.button_41 = config_button.ConfigButton(
            self.tabWidget, enable_log.EnableLog(self._system, self._version))
        self.button_41.setGeometry(QtCore.QRect(
            self._left_interval,
            self._head_interval+3*(self._button_hight+self._button_interval_h),
            self._button_weight, self._button_hight))
        self.button_41.setObjectName("button_41")
        self.button_41.setText(_translate("Form", "启用日志"))
        self._button_list.append(self.button_41)

        self.button_42 = config_button.ConfigButton(
            self.tabWidget, design_audit_regulation.DesignAuditRegulation(self._system, self._version))
        self.button_42.setGeometry(QtCore.QRect(
            self._left_interval+1*(self._button_weight+self._button_interval_w),
            self._head_interval+3*(self._button_hight+self._button_interval_h),
            self._button_weight, self._button_hight))
        self.button_42.setObjectName("button_42")
        self.button_42.setText(_translate("Form", "设计审计内容"))
        self._button_list.append(self.button_42)

        self.button_43 = config_button.ConfigButton(
            self.tabWidget, audit_file_authority.AuditFileAuthority(self._system, self._version))
        self.button_43.setGeometry(QtCore.QRect(
            self._left_interval+2*(self._button_weight+self._button_interval_w),
            self._head_interval+3*(self._button_hight+self._button_interval_h),
            self._button_weight, self._button_hight))
        self.button_43.setObjectName("button_43")
        self.button_43.setText(_translate("Form", "审核文件权限"))
        self._button_list.append(self.button_43)

        self.button_44 = config_button.ConfigButton(
            self.tabWidget, protection_audit_log.ProtectionAuditLog(self._system, self._version))
        self.button_44.setGeometry(QtCore.QRect(
            self._left_interval+3*(self._button_weight+self._button_interval_w),
            self._head_interval+3*(self._button_hight+self._button_interval_h),
            self._button_weight, self._button_hight))
        self.button_44.setObjectName("button_44")
        self.button_44.setText(_translate("Form", "保护审计记录"))
        self._button_list.append(self.button_44)

        # l5
        self.button_51 = config_button.ConfigButton(
            self.tabWidget, config_umask.ConfigUmask(self._system, self._version))
        self.button_51.setGeometry(QtCore.QRect(
            self._left_interval+0*(self._button_weight+self._button_interval_w),
            self._head_interval+4*(self._button_hight+self._button_interval_h),
            self._button_weight, self._button_hight))
        self.button_51.setObjectName("button_51")
        self.button_51.setText(_translate("Form", "设置umask值"))
        self._button_list.append(self.button_51)

        self.button_52 = config_button.ConfigButton(
            self.tabWidget, config_bash_history.ConfigBashHistory(self._system, self._version))
        self.button_52.setGeometry(QtCore.QRect(
            self._left_interval+1*(self._button_weight+self._button_interval_w),
            self._head_interval+4*(self._button_hight+self._button_interval_h),
            self._button_weight, self._button_hight))
        self.button_52.setObjectName("button_52")
        self.button_52.setText(_translate("Form", "设置Bash历史命令"))
        self._button_list.append(self.button_52)

        self.button_53 = config_button.ConfigButton(
            self.tabWidget, config_history_timestamp.ConfigHistoryTimestamp(self._system, self._version))
        self.button_53.setGeometry(QtCore.QRect(
            self._left_interval+2*(self._button_weight+self._button_interval_w),
            self._head_interval+4*(self._button_hight+self._button_interval_h),
            self._button_weight, self._button_hight))
        self.button_53.setObjectName("button_53")
        self.button_53.setText(_translate("Form", "history时间戳"))
        self._button_list.append(self.button_53)

        # l6
        self.button_61 = config_button.ConfigButton(
            self.tabWidget, forbidden_keyboard_close_command.ForbiddenKeyboardCloseCommand(self._system, self._version))
        self.button_61.setGeometry(QtCore.QRect(
            self._left_interval+0*(self._button_weight+self._button_interval_w),
            self._head_interval+5*(self._button_hight+self._button_interval_h),
            self._button_weight, self._button_hight))
        self.button_61.setObjectName("button_61")
        self.button_61.setText(_translate("Form", "禁止键盘关闭命令"))
        self._button_list.append(self.button_61)

        self.button_62 = config_button.ConfigButton(
            self.tabWidget, forbidden_mobile_device.ForbiddenMobileDevice(self._system, self._version))
        self.button_62.setGeometry(QtCore.QRect(
            self._left_interval+1*(self._button_weight+self._button_interval_w),
            self._head_interval+5*(self._button_hight+self._button_interval_h),
            self._button_weight, self._button_hight))
        self.button_62.setObjectName("button_62")
        self.button_62.setText(_translate("Form", "禁用移动设备"))
        self._button_list.append(self.button_62)

        # l7
        self.button_71 = config_button.ConfigButton(
            self.tabWidget, open_ssh_upgrade.OpenSSHUpgrade(self._system, self._version))
        self.button_71.setGeometry(QtCore.QRect(
            self._left_interval+0*(self._button_weight+self._button_interval_w),
            self._head_interval+6*(self._button_hight+self._button_interval_h),
            self._button_weight, self._button_hight))
        self.button_71.setObjectName("button_71")
        self.button_71.setText(_translate("Form", "Openssh升级"))
        self._button_list.append(self.button_71)

        QtCore.QMetaObject.connectSlotsByName(Form)

        for button in self._button_list:
            button.refresh()
            button.clicked.connect(button.on_click)

    def hideUi(self):
        self.tabWidget.setVisible(False)

    def showUi(self):
        self.tabWidget.setVisible(True)

    def _on_tab_change(self, i):
        if i == 0:
            self._check_all()
            print(i)
        elif i == 1:
            self._set_all()
        elif i == 2:
            self._unset_all()

    def _check_all(self):
        for button in self._button_list:
            button.refresh()
            button.setEnabled(True)

    def _set_all(self):
        for button in self._button_list:
            button.set(True)
            button.setEnabled(False)

    def _unset_all(self):
        for button in self._button_list:
            button.set(False)
            button.setEnabled(False)

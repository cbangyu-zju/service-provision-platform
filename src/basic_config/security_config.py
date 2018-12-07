

class SecurityConfig(object):

    def __init__(self, system, version):
        self._system = system
        self._version = version

    # 取消root账户远程登录
    def forbidden_root_remote_login(self):
        pass

    # 禁止不需要的服务
    def forbidden_useless_service(self):
        pass

    # 密码复杂度
    def password_complexity(self):
        pass

    # 口令周期
    def login_period(self):
        pass

    # 操作超时锁定
    def operation_timeout(self):
        pass

    # 登陆失败次数
    def login_failed_time_limit(self):
        pass

    # 非法登陆锁定
    def unlawful_lock_limit(self):
        pass

    # 启用日志
    def enable_log(self):
        pass

    # 设计审计内容
    def design_audit_regulation(self):
        pass

    # 审核文件权限
    def audit_file_authority(self):
        pass

    # 保护审计记录
    def protection_audit_log(self):
        pass

    # 设置umask值
    def config_umask(self):
        pass

    # 设置Bash历史命令
    def config_bash_history(self):
        pass

    # history 时间戳
    def config_history_timestamp(self):
        pass

    # 禁止键盘关闭命令
    def forbidden_keyboard_close_commend(self):
        pass

    # 禁用移动设备
    def forbidden_mobile_device(self):
        pass

    # Openssh 升级
    def open_ssh_upgrade(self):
        pass

from . import base


class PasswordPeriod(base.Base):

    def __init__(self, system, version):
        super(PasswordPeriod, self).__init__(system, version)
        self._first_status = self.check()
        self._status = self._first_status

    def check(self):
        cmd = "ps -ef|grep syslogd"
        stdout, err = self._run_command(cmd)
        if stdout.find(b"/usr/sbin/rsyslogd") >= 0:
            self._status = True
        else:
            self._status = False
        return self._status

    def set(self, status):
        if status == self._status:
            return
        if status:
            self._set()
        else:
            self._unset()

    def _set(self):
        cmd = "service rsyslog start && chkconfig rsyslog on"
        self._run_command(cmd)
        return self.check()

    def _unset(self):
        cmd = "chkconfig rsyslog off && service rsyslog stop"
        self._run_command(cmd)
        return not self.check()

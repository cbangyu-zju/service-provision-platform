from . import base


class ProtectionAuditLog(base.Base):

    def __init__(self, system, version):
        super(ProtectionAuditLog, self).__init__(system, version)
        self._op_file = "/etc/rsyslog.conf"
        self._first_status = self.check()
        self._status = self._first_status

    def check(self):
        cmd = "ls -la {op_file}".format(op_file=self._op_file)
        stdout, err = self._run_command(cmd)
        if stdout.find(b"-r--------.") >= 0:
            self._status = True
        else:
            self._status = False
        return self._status

    def set(self, status):
        if status == self._status:
            return
        if status:
            return self._set()
        else:
            return self._unset()

    def _set(self):
        cmd = "chmod 400 /etc/rsyslog.conf && service rsyslog restart"
        self._run_command(cmd)
        return self.check()

    def _unset(self):
        cmd = "chmod 644 /etc/rsyslog.conf && service rsyslog restart"
        self._run_command(cmd)
        return not self.check()

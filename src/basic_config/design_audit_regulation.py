from . import base


class DesignAuditRegulation(base.Base):
    _op_file = "/etc/rsyslog.conf"
    _regulation_find = [
        "*.info;mail.none;authpriv.none;cron.none[[:space:]].*/var/log/messages",
        "authpriv.*[[:space:]].*/var/log/secure",
        "*.err[[:space:]].*/var/log/errors",
        "kern.warning;authpriv.none[[:space:]].*/var/log/warn",
        "*.emerg[[:space:]].*/var/log/emerg.log",
        "local7.*[[:space:]].*/var/log/boot.log"
    ]
    _regulation_set = [
        "*.info;mail.none;authpriv.none;cron.none /var/log/messages",
        "authpriv.* /var/log/secure",
        "*.err /var/log/errors",
        "kern.warning;authpriv.none /var/log/warn",
        "*.emerg /var/log/emerg.log",
        "local7.* /var/log/boot.log"
    ]
    
    def __init__(self, system, version):
        super(DesignAuditRegulation, self).__init__(system, version)

    def check(self):
        ready_count = 0
        for reg in self._regulation_find:
            cmd = "grep '^{reg}' '{op_file}'".format(reg=reg, op_file=self._op_file)
            stdout, err = self._run_command(cmd)
            if stdout.find(bytes(reg[0:4], encoding="utf8")) >= 0:
                ready_count += 1
        return ready_count == len(self._regulation_find)

    def set(self, status):
        cmd = "chmod 600 {op_file}".format(op_file=self._op_file)
        self._run_command(cmd)
        if status == self._status:
            return
        if status:
            self._set()
        else:
            self._unset()

    def _set(self):
        for reg in self._regulation_set:
            prefix_reg = reg.split(" ")[0]
            cmd = "grep '^{reg}' '{op_file}'".format(reg=prefix_reg, op_file=self._op_file)
            stdout, err = self._run_command(cmd)
            if stdout.find(bytes(prefix_reg[0:4], encoding="utf8")) >= 0:
                cmd = "sed -i  '/^{prefix_reg}.*'/d '{op_file}' && echo '{reg}'>> '{op_file}'".format(
                    prefix_reg=prefix_reg, reg=reg, op_file=self._op_file)
            else:
                cmd = "echo '{reg}' >> {op_file}".format(reg=reg, op_file=self._op_file)
            self._run_command(cmd)
        return self.check()

    def _unset(self):
        for reg in self._regulation_set:
            cmd = "grep '^{reg}' '{op_file}'".format(reg=reg, op_file=self._op_file)
            stdout, err = self._run_command(cmd)
            if stdout.find(bytes(reg[0:4], encoding="utf8")) >= 0:
                cmd = "sed -i '/^{reg}.*'/d '{op_file}'".format(reg=reg.replace("/", "\/"), op_file=self._op_file)
                self._run_command(cmd)
        return not self.check()

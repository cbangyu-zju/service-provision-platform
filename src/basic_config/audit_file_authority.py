from . import base


class AuditFileAuthority(base.Base):

    def __init__(self, system, version):
        super(AuditFileAuthority, self).__init__(system, version)

    def check(self):
        file_auth_map = {
            "/etc/rsyslog.conf": b"-r--------",
            "/var/log/messages": b"-rw-------",
            "/var/log/wtmp": b"-rw-------",
            "/var/run/utmp": b"-rw-------",
            "/etc/shadow": b"-r--------",
            "/etc/group": b"-rw-r--r--"
        }
        ready_count = 0
        for key, value in file_auth_map.items():
            cmd = "ls -la '{op_file}'".format(op_file=key)
            stdout, err = self._run_command(cmd)
            if stdout.find(value) >= 0:
                ready_count += 1
        return ready_count == len(file_auth_map)

    def set(self, status):
        if status == self._status:
            return
        if status:
            return self._set()
        else:
            return self._unset()

    def _set(self):
        cmd = "chmod 400 /etc/rsyslog.conf && chmod 600 /var/log/messages && chmod 600 /var/log/wtmp && chmod 600 /var/run/utmp && chmod 400 /etc/shadow && chmod 644 /etc/group && chkconfig rsyslog on"
        self._run_command(cmd)
        return self.check()

    def _unset(self):
        cmd = "chmod 644 /etc/rsyslog.conf && chmod 600 /var/log/messages && chmod 664 /var/log/wtmp && chmod 664 /var/run/utmp && chmod 400 /etc/shadow && chmod 644 /etc/group"
        self._run_command(cmd)
        return not self.check()

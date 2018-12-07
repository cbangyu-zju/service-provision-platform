from . import base


class PasswordPeriod(base.Base):

    def __init__(self, system, version):
        super(PasswordPeriod, self).__init__(system, version)
        self._op_file = "/etc/pam.d/system-auth"
        self._status = self.check()

    def check(self):
        cmd = "grep '^auth[[:space:]]required[[:space:]]pam_tally2.so[[:space:]]deny=5[[:space:]]unlock_time=600' " \
              " '{op_file}' "
        cmd = cmd.format(op_file=self._op_file)
        stdout, err = self._run_command(cmd)
        if stdout.find(b"auth") >= 0:
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
        if not self.check():
            cmd = "echo 'auth required pam_tally2.so deny=5 unlock_time=600' >> '{op_file}'"
            cmd = cmd.format(op_file=self._op_file)
            self._run_command(cmd)
        return self.check()

    def _unset(self):
        if self.check():
            cmd = "sed -i '/^auth.*required.*pam_tally2.so.*deny=5.*unlock_time=600/d' '{op_file}'".format(
                op_file=self._op_file)
            self._run_command(cmd)
        return not self.check()

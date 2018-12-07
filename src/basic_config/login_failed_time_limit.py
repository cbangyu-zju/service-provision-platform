from . import base


class LoginFaidedTimeLimit(base.Base):

    def __init__(self, system, version):
        super(LoginFaidedTimeLimit, self).__init__(system, version)
        self._op_file = "/etc/pam.d/system-auth"
        self._status = self.check()

    def check(self):
        cmd = "grep '^account[[:space:]]required[[:space:]]pam_tally2.so[[:space:]]deny=5[[:space:]]reset' " \
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
            cmd = "echo 'account required pam_tally2.so deny=5 reset' >> '{op_file}'"
            cmd = cmd.format(op_file=self._op_file)
            self._run_command(cmd)
        return self.check()

    def _unset(self):
        if self.check():
            cmd = "sed -i '/^account.*required.*pam_tally2.so.*deny=5.*reset/d' '{op_file}'".format(
                op_file=self._op_file)
            self._run_command(cmd)
        return not self.check()

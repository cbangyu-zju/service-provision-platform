from . import base


class ConfigUmask(base.Base):

    def __init__(self, system, version):
        super(ConfigUmask, self).__init__(system, version)
        self._op_file = "/etc/profile"
        self._status = self.check()

    def check(self):
        cmd = "grep '^umask[[:space:]]022' '{op_file}' "
        cmd = cmd.format(op_file=self._op_file)
        stdout, err = self._run_command(cmd)
        if stdout.find(b"umask") >= 0:
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
            cmd = "echo 'umask 022' >> '{op_file}'"
            cmd = cmd.format(op_file=self._op_file)
            self._run_command(cmd)
        return self.check()

    def _unset(self):
        if self.check():
            cmd = "sed -i '/^umask 022/d' '{op_file}'".format(
                op_file=self._op_file)
            self._run_command(cmd)
        return not self.check()

from . import base


class ForbiddenMobileDevice(base.Base):
    _op_file = "/etc/security/console.perms"

    def __init__(self, system, version):
        super(ForbiddenMobileDevice, self).__init__(system, version)

    def check(self):
        cmd = "grep '^#<console' '{op_file}'".format(op_file=self._op_file)
        stdout, err = self._run_command(cmd)
        if stdout.find(b"#<console") >= 0:
            self._status = True
        else:
            self._status = False
        return self._status

    def set(self, status):
        if status == self.check():
            return
        if status:
            self._set()
        else:
            self._unset()

    def _set(self):
        cmd = "sed -i 's/^<console/#<console/g' '{op_file}'".format(op_file=self._op_file)
        self._run_command(cmd)
        return self.check()

    def _unset(self):
        cmd = "sed -i 's/^#<console/<console/g' '{op_file}'".format(op_file=self._op_file)
        self._run_command(cmd)
        return not self.check()

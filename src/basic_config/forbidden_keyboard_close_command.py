from . import base


class ForbiddenKeyboardCloseCommand(base.Base):
    _op_file = "/etc/init/control-alt-delete.conf"

    def __init__(self, system, version):
        super(ForbiddenKeyboardCloseCommand, self).__init__(system, version)

    def check(self):
        cmd = "ls {op_file}".format(op_file=self._op_file)
        stdout, err = self._run_command(cmd)
        if stdout.find(bytes(self._op_file, encoding='utf8')) >= 0:
            self._status = False
        else:
            self._status = True
        return self._status

    def set(self, status):
        if status == self.check():
            return
        if status:
            self._set()
        else:
            self._unset()

    def _set(self):
        cmd = "mv {origin} {end}".format(origin=self._op_file, end=self._op_file+".bak")
        self._run_command(cmd)
        return self.check()

    def _unset(self):
        cmd = "mv {origin} {end}".format(origin=self._op_file+".bak", end=self._op_file)
        self._run_command(cmd)
        return not self.check()

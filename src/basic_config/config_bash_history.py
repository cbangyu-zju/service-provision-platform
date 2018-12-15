from . import base


class ConfigBashHistory(base.Base):
    _op_file = "/etc/profile"
    _regulation = [
        "HISTSIZE=5",
        "HISTFILESIZE=5"
    ]

    def __init__(self, system, version):
        super(ConfigBashHistory, self).__init__(system, version)

    def check(self):
        ready_count = 0
        for reg in self._regulation:
            cmd = "grep '^{reg}' {op_file}".format(reg=reg, op_file=self._op_file)
            stdout, err = self._run_command(cmd)
            if stdout.find(bytes(reg, encoding="utf8")) >= 0:
                ready_count += 1
        return ready_count == len(self._regulation)

    def set(self, status):
        if status == self._status:
            return
        if status:
            return self._set()
        else:
            return self._unset()

    def _set(self):
        for reg in self._regulation:
            prefix_reg = reg.split("=")[0]
            cmd = "grep '^{prefix_reg}' {op_file}".format(prefix_reg=prefix_reg, op_file=self._op_file)
            stdout, err = self._run_command(cmd)
            if stdout.find(bytes(prefix_reg, encoding="utf8")) >= 0:
                cmd = "sed -i 's/^{prefix_reg}.*/{reg}/g' '{op_file}'".format(
                    prefix_reg=prefix_reg, reg=reg, op_file=self._op_file)
            else:
                cmd = "echo '{reg}' >> '{op_file}'".format(reg=reg, op_file=self._op_file)
            self._run_command(cmd)
        return self.check()

    def _unset(self):
        for reg in self._regulation:
            cmd = "grep '^{reg}' {op_file}".format(reg=reg, op_file=self._op_file)
            stdout, err = self._run_command(cmd)
            if stdout.find(bytes(reg, encoding="utf8")) >= 0:
                cmd = "sed -i '/^{reg}/d' '{op_file}'".format(
                    prefix_reg=reg, reg=reg, op_file=self._op_file)
            self._run_command(cmd)
        return not self.check()

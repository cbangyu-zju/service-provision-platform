from . import base


class PasswordPeriod(base.Base):

    def __init__(self, system, version):
        super(PasswordPeriod, self).__init__(system, version)
        self._op_file = "/etc/login.defs"
        self._status = self.check()
        self._prepare()

    def check(self):
        cmd = "grep '^PASS_MAX_DAYS[[:space:]]99999' '{op_file}' " \
              "&& grep '^PASS_MIN_DAYS[[:space:]]0' '{op_file}' " \
              "&& grep '^PASS_MIN_LEN[[:space:]]5' '{op_file}' " \
              "&& grep '^PASS_WARN_AGE[[:space:]]7' '{op_file}' "
        cmd = cmd.format(op_file=self._op_file)
        stdout, err = self._run_command(cmd)
        if stdout.find(b"PASS_MAX_DAYS") >= 0 and stdout.find(b"PASS_MIN_DAYS") >= 0 and \
                stdout.find(b"PASS_MIN_LEN") >= 0  and stdout.find(b"PASS_WARN_AGE") >= 0:
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

    def _prepare(self):
        prepare_cmd = "cp '{origin}' '{end}'".format(origin=self._op_file, end=self._op_file+"_tmp")
        self._run_command(prepare_cmd)

    def _set(self):
        cmd = "sed -i 's/^PASS_MAX_DAYS.*/PASS_MAX_DAYS\t99999/g' '{op_file}'" \
              "&& sed -i 's/^PASS_MIN_DAYS.*/PASS_MIN_DAYS\t0/g' '{op_file}'" \
              "&& sed -i 's/^PASS_MIN_LEN.*/PASS_MIN_LEN\t5/g' '{op_file}'" \
              "&& sed -i 's/^PASS_WARN_AGE.*/PASS_WARN_AGE\t7/g' '{op_file}'"
        cmd = cmd.format(op_file=self._op_file)
        self._run_command(cmd)
        return self.check()

    def _unset(self):
        prepare_cmd = "cp '{origin}' '{end}'".format(origin=self._op_file+"_tmp", end=self._op_file)
        self._run_command(prepare_cmd)
        return not self.check()

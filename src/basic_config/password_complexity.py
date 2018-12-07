from . import base


class PasswordComplexity(base.Base):

    def __init__(self, system, version):
        super(PasswordComplexity, self).__init__(system, version)
        self._op_file = "/etc/pam.d/system-auth"
        self._status = self.check()
        self._prepare()

    def check(self):
        cmd = "grep 'password\trequisite\tpam_cracklib.so\tretry=5\tdifok=3\tminlen=8\tucredit=-2\tlcredit=-1\t" \
              "dcredit=-4\tocredit=-1\tdictpath=/usr/share/cracklib/pw_dict' '{op_file}'"
        cmd = cmd.format(op_file=self._op_file)
        stdout, err = self._run_command(cmd)
        if stdout.find(b"password\trequisite\tpam_cracklib.so\tretry=5\tdifok=3\tminlen=8\tucredit=-2\t") >= 0:
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
            return not self._set()

    def _prepare(self):
        prepare_cmd = "cp '{origin}' '{end}'".format(origin=self._op_file, end=self._op_file+"_tmp")
        self._run_command(prepare_cmd)

    def _set(self):
        end = 'password\trequisite\tpam_cracklib.so\tretry=5\tdifok=3\tminlen=8\tucredit=-2\tlcredit=-1\t' \
              'dcredit=-4\tocredit=-1\tdictpath=/usr/share/cracklib/pw_dict'
        cmd = "sed -i 's/^password.*requisite.*/{end}/g' '{op_file}'".format(end=end, op_file=self._op_file)
        self._run_command(cmd)
        return self.check()

    def _unset(self):
        prepare_cmd = "cp '{origin}' '{end}'".format(origin=self._op_file+"_tmp", end=self._op_file)
        self._run_command(prepare_cmd)
        return self.check()

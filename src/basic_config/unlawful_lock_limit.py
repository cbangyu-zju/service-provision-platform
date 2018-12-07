from . import base


class UnlawfulLockLimit(base.Base):

    def __init__(self, system, version):
        super(UnlawfulLockLimit, self).__init__(system, version)
        self._op_file = "/etc/pam.d/system-auth"
        self._status = self.check()

    def check(self):
        cmd = "grep '^password[[:space:]]requisite[[:space:]]pam[[:space:]]cracklib.so[[:space:]]retry=5[[:space:]]" \
              "difok=3[[:space:]]minlen=8[[:space:]]ucredit=-2[[:space:]]lcredit=-1[[:space:]]dcredit=-4[[:space:]]" \
              "ocredit=-1[[:space:]]dictpath=/usr/share/cracklib/pw_dict' " \
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
            cmd = "echo 'password requisite pam_cracklib.so retry=5  difok=3 minlen=8 ucredit=-2 lcredit=-1 \
             dcredit=-4 ocredit=-1 dictpath=/usr/share/cracklib/pw_dict' >> '{op_file}'"
            cmd = cmd.format(op_file=self._op_file)
            self._run_command(cmd)
        return self.check()

    def _unset(self):
        if self.check():
            cmd = "sed -i '/^password.*requisite.*pam_cracklib.so.*retry=5.*difok=3.*minlen=8.*ucredit=-2.*" \
                  "lcredit=-1.*dcredit=-4.*ocredit=-1.*dictpath=/usr/share/cracklib/pw_dict'/d' '{op_file}'"\
                .format(op_file=self._op_file)
            self._run_command(cmd)
        return not self.check()

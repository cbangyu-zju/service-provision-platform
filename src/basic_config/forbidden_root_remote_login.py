from . import base


class ForbiddenRootRemoteLogin(base.Base):
    _op_file = "/etc/ssh/sshd_config"

    def __init__(self, system, version):
        super(ForbiddenRootRemoteLogin, self).__init__(system, version)

    def check(self):
        cmd = "grep '^PermitRootLogin yes' '{origin}'".format(origin=self._op_file)
        stdout, err = self._run_command(cmd)
        if stdout.find(b"PermitRootLogin yes") < 0:
            self._status = True
        else:
            self._status = False
        return self._status

    def set(self, status):
        if status == self._status:
            return
        if status:
            return self._set(status)
        else:
            return not self._set(status)

    def _set(self, status):
        cmd = "sed -i 's/PermitRootLogin {origin}/PermitRootLogin {end}/g' '{op_file}' && sed -i 's/#PermitRootLogin {end}/PermitRootLogin {end}/' '{op_file}'"
        origin = "yes"
        end = "no"
        if not status:
            origin = "no"
            end = "yes"
        cmd = cmd.format(origin=origin, end=end, op_file=self._op_file)
        self._run_command(cmd)
        return self.check()

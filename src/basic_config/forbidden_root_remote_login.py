from . import base


class ForbiddenRootRemoteLogin(base.Base):

    _set_command_line = {
        "ubuntu": "",
        "centos": "cp /etc/ssh/sshd_config ./sshd_config \
            && sed -i 's/PermitRootLogin yes/PermitRootLogin no/' '/etc/ssh/sshd_config' \
            && sed -i 's/#PermitRootLogin no/PermitRootLogin no/' '/etc/ssh/sshd"
    }
    _restore_command_line = {
        "ubuntu": "",
        "centos": "mv './sshd_config' '/etc/ssh/sshd_config'"
    }

    def __init__(self, system, version):
        super(ForbiddenRootRemoteLogin, self).__init__(system, version)
        self._status = self.check()
        self._prepare()

    def check(self):
        cmd = "grep '^PermitRootLogin no' '/etc/ssh/sshd_config'"
        stdout, err = self._run_command(cmd)
        if stdout.find("PermitRootLogin no") >= 0:
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

    def _prepare(self):
        prepare_cmd = "cp '/etc/ssh/sshd_config' './sshd_config'"
        self._run_command(prepare_cmd)

    def _set(self, status):
        cmd = "sed -i 's/PermitRootLogin {origin}/PermitRootLogin {end}/g' '/etc/ssh/sshd_config' \
            && sed -i 's/#PermitRootLogin {end}/PermitRootLogin {end}/' '/etc/ssh/sshd_config'"
        origin = "yes"
        end = "no"
        if not status:
            origin = "no"
            end = "yes"
        cmd = cmd.format(origin=origin, end=end)
        self._run_command(cmd)
        return self.check()


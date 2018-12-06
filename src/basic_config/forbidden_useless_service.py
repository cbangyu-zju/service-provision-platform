from . import base


class ForbiddenUselessService(base.Base):
    _devices = ["bluetooth", "rlogin", "rwho", "sh", "rexec"]

    def __init__(self, system, version):
        super(ForbiddenUselessService, self).__init__(system, version)
        self._status = self.check()

    def check(self):
        ready_count = 0
        for device in self._devices:
            ready_count += self._check(device)
        if ready_count < len(self._devices):
            self._status = False
        else:
            self._status = True
        return self._status

    def set(self, status):
        if status == self._status:
            return True
        ready_count = 0
        for device in self._devices:
            ready_count += self._set(device, status)
        if ready_count < len(self._devices):
            return False
        else:
            return True

    def _check(self, device):
        cmd = "chkconfig --list {device}".format(device=device)
        stdout, err = self._run_command(cmd.split())
        if stdout.find(b"3:off") > 0 and stdout.find(b"5:off") > 0:
            return 1
        else:
            return 0

    def _set(self, device, status):
        cmd = "chkconfig --level 35 {device} {status}"
        set_status = "off"
        if not status:
            set_status = "on"
        cmd = cmd.format(device=device, status=set_status)
        stdout, err = self._run_command(cmd.split())
        if not err:
            return 1
        else:
            return 0

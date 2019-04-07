import logging
import subprocess


class Base(object):
    _op_file = ""

    def __init__(self, system, version):
        self._logger= logging.getLogger(__name__)
        self._system = system
        self._version = version
        self._status = self.check()

    def check(self):
        pass

    def set(self, status):
        pass

    def _run_command(self, command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        stdout, err = process.communicate()
        return stdout, err

    def clear(self):
        pass

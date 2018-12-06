import logging
import subprocess


class Base(object):

    def __init__(self, system, version):
        self._logger= logging.getLogger(__name__)
        self._system = system
        self._version = version

    def check(self):
        pass

    def set(self, status):
        pass

    def _run_command(self, command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        return process.communicate()

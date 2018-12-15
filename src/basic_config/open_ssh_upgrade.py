from . import base


class OpenSSHUpgrade(base.Base):
    _op_file = "openssh-7.5p1"

    def __init__(self, system, version):
        super(OpenSSHUpgrade, self).__init__(system, version)

    def check(self):
        cmd = "ssh -V"
        stdout, err = self._run_command(cmd)
        if stdout.find(b"OpenSSH_7.5p1") >= 0:
            self._status = True
        else:
            self._status = False
        return self._status

    def set(self, status):
        if status == self._status:
            return
        if status:
            self._set()

    def _set(self):
        cmd = "cp -r '{op_file}' '/tmp/{op_file}' && cd /tmp/{op_file} && " \
              "./configure --prefix=/usr --sysconfdir=/etc/ssh --with-pam --with-zlib --with-md5-passwords &&" \
              "cp -r /etc/ssh /etc/ssh_bak_2018 &&" \
              "mv /etc/init.d/sshd /etc/init.d/sshd_bak_2018 &&" \
              "mv /usr/sbin/sshd /usr/sbin/sshd_bak_2018 &&" \
              "cp /usr/bin/ssh /usr/bin/ssh_bak_2018 &&" \
              "mv /etc/ssh/sshd_config /etc/ssh/sshd_config2018 &&" \
              "mv /etc/ssh/ssh_config  /etc/ssh/ssh_config2018 &&" \
              "mv /etc/ssh/moduli /etc/ssh/moduli2018 &&" \
              "make && make install &&" \
              "cp /tmp/openssh-7.5p1/contrib/redhat/sshd.init /etc/init.d/sshd &&" \
              "chmod +x /etc/init.d/sshd &&" \
              "chkconfig --add sshd &&" \
              "chkconfig sshd on &&" \
              "cp /usr/openssh-7.5p1/sshd /usr/local/sbin/sshd &&" \
              "echo 'X11Forwarding yes' >> /etc/ssh/sshd_config &&" \
              "service sshd restart"
        self._run_command(cmd)
        return self.check()


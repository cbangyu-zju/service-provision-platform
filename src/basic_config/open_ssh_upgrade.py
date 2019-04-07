from . import base


class OpenSSHUpgrade(base.Base):
    _op_file = "./openssh-7.5p1"

    def __init__(self, system, version):
        super(OpenSSHUpgrade, self).__init__(system, version)

    def check(self):
        cmd = "ssh -V"
        stdout, err = self._run_command(cmd)
        if stdout.find(b"OpenSSH_7.5") >= 0:
            self._status = True
        else:
            self._status = False
        self._logger.warning("stdout: %s, err: %s, self._status: %s", stdout, err, self._status)
        return self._status

    def set(self, status):
        if status == self._status:
            return
        if status:
            self._set()

    def _set(self):
        cmd = "rm -rf /tmp/openssh && rm -rf /etc/ssh_bak_2018 && rm -rf /usr/bin/ssh_bak_2018 && rm -rf && touch /etc/init.d/sshd && touch /etc/ssh/sshd_config && cp -r '{op_file}' '/tmp/openssh' && cd /tmp/openssh && yum install -y pam* && ./configure --prefix=/usr --sysconfdir=/etc/ssh --with-pam --with-zlib --with-md5-passwords && cp -r /etc/ssh /etc/ssh_bak_2018 && mv /etc/init.d/sshd /etc/init.d/sshd_bak_2018 && cp /usr/bin/ssh /usr/bin/ssh_bak_2018 && cp /etc/ssh/sshd_config /etc/ssh/sshd_config2018 && mv /etc/ssh/ssh_config  /etc/ssh/ssh_config2018 && mv /etc/ssh/moduli /etc/ssh/moduli2018 && make && make install && cp /tmp/openssh/contrib/redhat/sshd.init /etc/init.d/sshd && chmod +x /etc/init.d/sshd && chkconfig --add sshd && chkconfig sshd on && cp /tmp/openssh/sshd /usr/local/sbin/sshd && echo 'X11Forwarding yes' >> /etc/ssh/sshd_config && service sshd restart".format(op_file=self._op_file)
        self._run_command(cmd)
        return self.check()


# redhat 6 换源

1. 卸载,yum rpm -aq|grep yum|xargs rpm -e --nodeps

2. 下载rpm包, wget http://mirrors.163.com/centos/6/os/i386/Packages/python-iniparse-0.3.1-2.1.el6.noarch.rpm

wget http://mirrors.163.com/centos/6/os/i386/Packages/python-iniparse-0.3.1-2.1.el6.noarch.rpm

wget http://mirrors.163.com/centos/6/os/i386/Packages/yum-plugin-fastestmirror-1.1.30-41.el6.noarch.rpm

wget http://mirrors.163.com/centos/6/os/i386/Packages/yum-metadata-parser-1.1.2-16.el6.i686.rpm

3.安装rpm包,rpm -ivh python-iniparse-0.3.1-2.1.el6.noarch.rpm &rpm -ivh yum-*

4.删除所有yum源,rm /etc/yum.repos.d/*

5.重新下载yum源,wget http://mirrors.163.com/.help/CentOS6-Base-163.repo

6.替换掉releasever,:%s/$releasever/6/g

7.yum clean all&yum makecache

8.yum update -y

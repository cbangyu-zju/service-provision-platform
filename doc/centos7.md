## centos7 换源
```bash
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
cd /etc/yum.repos.d/
wget http://mirrors.163.com/.help/CentOS7-Base-163.repo
yum makecache
yum -y update
```


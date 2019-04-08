#!/bin/bash

rm -rf /etc/yum.repos.d/CentOS7*
cd /etc/yum.repos.d/
wget http://mirrors.163.com/.help/CentOS7-Base-163.repo
yum makecache
yum -y update

echo "正在安装相关组件"
yum install -y openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel gcc-c++ gcc openssl-devel

echo "下载安装包"
wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz

echo "正在解压安装包"
tar -xf Python-3.6.5.tgz -C /root/  && cd /root/Python-3.6.5/

echo "添加ssl支持"
cat >> /root/Python-3.6.5/Modules/Setup.dist <<"EOF"
_socket socketmodule.c

SSL=/usr/local/ssl
_ssl _ssl.c \
-DUSE_SSL -I$(SSL)/include -I$(SSL)/include/openssl \
-L$(SSL)/lib -lssl -lcrypto
EOF

echo "正在编译安装Python"
./configure --prefix=/usr/local/python --enable-shared && make && make install
cd /root

echo "删除安装包"
rm -rf /root/Python-3.6.5.tgz && rm -rf /root/Python-3.6.5

echo "正在添加环境变量"
echo "export PATH=/usr/local/python/bin:$PATH">> ~/.bash_profile
source ~/.bash_profile

echo "安装完成,请执行python3进行测试"

echo "/usr/local/python/lib" > /etc/ld.so.conf.d/python3.6.conf
ldconfig
ldd /usr/local/python/bin/python3

pyvenv venv
source venv/bin/activate
pip install PyQt5 -i https://pypi.douban.com/simple
pip install pyinstaller -i https://pypi.douban.com/simple

## redhat 6 安装pyqt5

```bash
# 1 增加 epel 源
yum install epel-release -y

# 2 安装qt5

yum install qt5-qtquickcontrols qt5-qtdeclarative-devel qt5-qtdeclarative -y

# 3. 安装编译环境
yum install gcc gcc-c++ python-devel -y

# 4. 下载sip-4.18
wget https://jaist.dl.sourceforge.net/project/pyqt/sip/sip-4.18/sip-4.18.tar.gz

# 5. 编译sip-4。18
tar xzvf sip-4.18.tar.gz
cd sip-4.18
python configure.py
make && make install

# 6. 下载pyqt5.7
wget https://jaist.dl.sourceforge.net/project/pyqt/PyQt5/PyQt-5.7/PyQt5_gpl-5.7.tar.gz

# 7. 安装pyqt5.7
tar xzvf PyQt5_gpl-5.7.tar.gz
cd PyQt5_gpl-5.7
python configure --qmake=/usr/bin/qmake-qt5
make all && make install

```
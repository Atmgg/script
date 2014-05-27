#!/bin/bash
cd ~

mkdir -p ~/bin
echo "export PATH=\$PATH:~/bin">>~/.bashrc
echo -n "mkdir ~/bin succeed."

# install curl,elinks,git and subversion
sudo apt-get install curl elinks git subversion g++ 

# this two tools are used to gen configure files
sudo apt-get install autoconf libtool

echo "export EDITOR=/usr/bin/vim" >> ~/.bashrc

# install blade
git clone https://github.com/chen3feng/typhoon-blade.git
./typhoon-blade/install
sudo apt-get install scons
echo "alias bb=\"blade build\"">> ~/.bashrc

# install pip
current_dir=$(cd $(dirname $0) && pwd)
cd /tmp
curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py
sudo apt-get install python-dev
sudo python get-pip.py 
cd $current_dir

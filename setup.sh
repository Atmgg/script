#!/bin/sh

#add fcitx ppa
sudo add-apt-repository ppa:fcitx-team/nightly
#Ìí¼Ócaffeine ppa
ppa:caffeine-developers/ppa

#add ubuntu-tweak ppa
sudo apt-add-repository ppa:tualatrix/ppa

#add virtualbox ppa
sudo add-apt-repository ppa:debfx/virtualbox

#add claws-mail ppa
sudo add-apt-repository ppa:claws-mail/ppa
apt-get update

#install fonts
cd ~/fonts/consolas/
sudo chmod 644 Consolas.ttf
sudo mkfontscale
sudo mkfontdir
sudo fc-cache -fv

sudo bash -c "echo LANG='en_US.UTF-8' > /etc/default/locale"
sudo bash -c "echo LANGUAGE='en_US:en' >> /etc/default/locale"
#change locale to chinese
#sudo bash -c "echo LANG='zh_CN.UTF-8' > /etc/default/locale"
#sudo bash -c "echo LANGUAGE='zh_CN:zh' >> /etc/default/locale"

#install gnome
sudo apt-get install gnome-panel
gdmflexiserver

#install gvim
sudo apt-get install vim-gnome 
echo "alias gvim='gvim -f'" >> ~/.bashrc 
source ~/.bashrc

#install fcitx ime
sudo apt-get install fcitx-sogoupinyin
#im-switch this command is to set default ime in the X system
im-switch -s fcitx

#set system variable EDITOR
echo export EDITOR=/usr/bin/vim >> ~/.bashrc
source ~/.bashrc

#change gnome¡¯s text editor from edit to gvim
sudo sed -i "s/gedit.desktop/gvim.desktop/g" /etc/gnome/defaults.list 

#install caffeine
sudo apt-get install caffeine

#install chrome
wget -O ~/Downloads/google-chrome-i386.deb https://dl.google.com/linux/direct/google-chrome-stable_current_i386.deb

sudo apt-get install libxss1
sudo dpkg -i ~/Downloads/google-chrome-i386.deb
echo "alias chrome='/opt/google/chrome/google-chrome>/dev/null 2>&1'" >> ~/.bashrc
source ~/.bashrc

#install nutstore
wget -O  ~/Downloads/nautilus_nutstore_i386.deb https://jianguoyun.com/static/exe/installer/ubuntu/nautilus_nutstore_i386.deb
sudo apt-get install openjdk-6-jre-headless 
sudo dpkg -i ~/Downloads/nautilus_nutstore_i386.deb

#cancel nutstore¡¯s deamon process
mv /home/wangjingji/.config/autostart/nutstore-daemon.desktop ~/Cloud_Folder/nutstore-daemon.desktop

#install virtualbox
wget -O  ~/Downloads/virtualbox-4.3.deb http://download.virtualbox.org/virtualbox/4.3.0/virtualbox-4.3_4.3.0-89960~Ubuntu~precise_i386.deb
sudo dpkg -i virtualbox-4.3.deb

#install matlab
sudo mkdir /mnt/matlab
sudo mount ~/Downloads/matlab_unix_2009b.iso /mnt/matlab -o loop
sudo mkdir /opt/matlab2009b
sudo chmod o+x /opt/matlab2009b/
cd /mnt/matlab
./install
sudo umount /mnt/matlab/
sudo rmdir /mnt/matlab/
bash -c "echo alias matlab='/opt/matlab2009b/bin/matlab>/dev/null 2>&1'>>~/.bashrc"

#install goldendict
sudo apt-get install goldendict

#install alipay plug-in
wget -O ~/Downloads/aliedit.tar.gz  https://download.alipay.com/alipaysc/linux/aliedit/1.0.3.20/aliedit.tar.gz
cd ~/Downloads/
tar -zxvf ~/Downloads/aliedit.tar.gz 
./aliedit.sh

#install ubuntu-tweak
sudo apt-get install ubuntu-tweak 

#install wine-QQ
cd ~/Downloads/
sudo dpkg -i WineQQ2012-20121221-Longene.deb

#install claws-mail
sudo apt-get install claws-mail

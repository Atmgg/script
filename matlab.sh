#!/bin/sh

cd /opt/matlab2009b/sys/java/jre/glnx86/jre/lib/fonts/
sudo mkdir fallback
cd fallback
sudo ln -s /usr/share/fonts/truetype/wqy/wqy-zenhei.ttc ./wqy-zenhei.ttc
sudo mkfontscale
cd ..
#�����ɵ�fonts.scale��ӵ�fonts.dir��

cat fallback/fonts.scale >> fonts.dir

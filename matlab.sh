#!/bin/sh

cd /opt/matlab2009b/sys/java/jre/glnx86/jre/lib/fonts/
sudo mkdir fallback
cd fallback
sudo ln -s /usr/share/fonts/truetype/wqy/wqy-zenhei.ttc ./wqy-zenhei.ttc
sudo mkfontscale
cd ..
#将生成的fonts.scale添加到fonts.dir中

cat fallback/fonts.scale >> fonts.dir

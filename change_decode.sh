#!/bin/sh


# filename=`basename $var1`; filepath=`dirname $var1`
# read -p "请输入你的转换文件路径+文件名: " filename

filepath=`pwd`

if   [ $# != 1 ]
then
     echo "Usage:change_decode filename1"
else
     echo "Your input is: "$1
fi 

filename=$1
destiname=$filename"_ch"
iconv -f gb2312 -t utf-8 $filename >$destiname



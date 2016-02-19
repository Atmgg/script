# /bin/sh

if [ $# != 1 ]; then
    echo invalid arg num
    exit
fi

echo $1 | sed -e "s/>//g" -e "s/</\\\x/g" -e "s/^/'/g" -e "s/$/'\\n/g" | xargs echo -e

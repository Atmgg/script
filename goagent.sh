#!/bin/sh

cd /usr/local/bin/goagent/local
python proxy.py>/dev/null 2>&1 &

#!/bin/bash
#SPDX-FileCopyrightText:2025 Ikki Chikaraishi
#SPDX-Licence-Identifier:BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える.

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep '2025-01-01: 元日'
if [ $? = 0 ]; then
    echo 1/1 OK
else
    echo 1/1 NG
    res=1
fi

cat /tmp/mypkg.log | grep '2025-01-03'
if [ $? = 0 ]; then
    echo 1/3 OK
else
    echo 1/3 NG
    res=1
fi

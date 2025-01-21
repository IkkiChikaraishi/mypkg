#!/bin/bash
#SPDX-FileCopyrightText:2025 Ikki Chikaraishi
#SPDX-Licence-Identifier:BSD-3-Clause

res=0

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える.

sudo apt -y install python3-pip
pip install psutil

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg memory_listen.launch.py &> /tmp/mypkg_test.log

totalmem=`free -b | awk 'NR==2 {print substr($2,1)}'`

cat /tmp/mypkg_test.log

grep $totalmem /tmp/mypkg_test.log
if [ $? = 0 ]; then
    echo TotalMemoryOK
else
    echo TotalMemoryNG
    res=1
fi

if grep -E 'Free_Memory: [0-9]+' /tmp/mypkg_test.log; then
    echo FreeMemoryOK
else
    echo FreeMemoryNG
    res=1
fi

if grep -E 'Used_memory: [0-9]+' /tmp/mypkg_test.log; then
    echo UsedMemoryOK
else
    echo UsedMemoryNG
    res=1
fi

exit $res

#!/bin/bash

sp_pid=`ps -ef | grep main2.py | grep -v grep | awk '{print $2}'`
if [ -z "$sp_pid" ];
then
    echo "[ not find main2.py pid ]"
else
    echo "find result: $sp_pid "
    kill -9 $sp_pid
fi

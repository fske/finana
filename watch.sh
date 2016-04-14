#! /bin/bash

while [ 1 ]
do
  procID=`pgrep python`
  if [ "${procID}" == "" ];then
    echo $procID
    ~/finana/start.sh
  fi
  usleep 1000
done &

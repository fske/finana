#! /bin/bash

while [ 1 ]
do
  procID=`pgrep python`
  if [ "${procID}" == "" ];then
    date >> sys.log
    ~/finana/start.sh >> sys.log
  fi
  usleep 1000
done &

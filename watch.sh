#! /bin/bash

while [ 1 ]
do
  procID=`pgrep python`
  if [ "${procID}" == "" ];then
    date >> sys.log
    nohup python ~/finana/get_precious_metal_price.py >> ~/finana/gpmp.log 2>>~/finana/sys.log &
  fi
  usleep 1000
done &

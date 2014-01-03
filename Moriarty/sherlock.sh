#!/bin/sh

sleep 100  #deauth duration

MPID=$(ps aux | grep -v grep | grep "sh ./Moriarity" | awk '{print $2}')
PYPID=$(ps aux | grep -v grep | grep "/usr/bin/python /root/Moriarity/death.py" | awk '{print $2}')
APID=$(ps aux | grep -v grep | grep "aireplay" | awk '{print $2}')

#Kill Must happen in proper order

kill -15 $APID  #deauth kill
kill -15 $PYPID #death kill
kill -15 $MPID  #Moriarity Kill
killall ngrep   #kill zombies

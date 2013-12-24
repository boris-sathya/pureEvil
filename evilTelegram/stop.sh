#!/bin/sh

PID=$(ps aux | grep -v grep | grep "/usr/bin/python /root/deauth" | awk '{print $2}')
APID=$(ps aux | grep -v grep | grep "aireplay" | awk '{print $2}')

kill -15 $PID
kill -15 $APID

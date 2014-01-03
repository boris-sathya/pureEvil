#!/bin/sh

#Kill arpsoof process, we no longer need this
#Need processor juice for deauth

PID=$(ps aux | grep -v grep | grep "arpspoof" | awk '{print $2}')

kill -15 $PID

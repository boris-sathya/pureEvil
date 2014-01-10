Moriarty
==========

Description
-----------

As you guessed, the name is inspired from **Sherlock Holmes**. Like the criminal mastermind, this
shell scriptic version of Moriarity is evil and cunning.

Moriarty, disconnects a target from a wireless LAN when they visit a target website. Yes, Moriarty is
your one stop solution to prevent your roomate from watching pr0n.

Techical Description
-------------------

1. ARP Spoof the router and intercept traffic intended for victim
2. Pass the traffic to the awesome ngrep, which would detect if a packet is from our target host website
3. If a match is found, ngrep signals a python wrapper code (death.py) via netcat
4. Stop arpspoofing(arpspoofkill.sh), need CPU juice for the deauth attack
5. Launch Sherlock.sh which would give 100 seconds for death.py to deauth the victim
6. After 100 seconds, Sherlock.sh would kill all the evil process created by Moriarity and exit

Requirements
-----------
* Fully tested on BackTrack 5
* Alfa AWUS036H or similar network card
* As long as you have a working monitor mode card, any linux platform would suffice

How To
--------
```
Put wireless card on Monitor mode
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 1024
sh ./Moriarty.sh
```
Yeah, as simple as that. Make sure to change file paths according to your location.

Credits
--------
Many thanks to [Niranjan](http://people.epfl.ch/niranjan.thanikachalam) for the **evil** idea.
Dedicated to BBC Sherlock Holmes Season 3 :)

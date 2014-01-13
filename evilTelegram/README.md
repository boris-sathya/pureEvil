Telegram
========
Telegram is the latest `whatsapp killer` messaging service. It exposes a RPC
API. It also has libraries written in a couple of languages. Not to mention,
their iOS client beats whatsapp by a mile.

evilTelegram
========

evilTelegram is a way of arming Telegram. The motivation is to resuse telegram client's source to do something more on receiving a particular text message. In this project, I'm triggering a Deauthentication attack on a (WPA2-PSK) WLAN on receiving a message. 

Telegram's code has been slightly modified to run respective scripts depending upon message recieved or sent.

Requirements
============
1) A Linux machine
2) Alfa card or anything other wireless card that can be put in Monitor mode (Promiscous)
![Alfa Card](http://oneeyeddog.files.wordpress.com/2011/07/alfa-awuso36h1.jpg)
3) Appropriate Drivers Installed

How To Install
========
```
Telegram:
0)Source Code: https://github.com/vysheng/tg/
1)Download Telegram Source Code from the link above.
2)Replace interface.c on the Telegram's source with interface.c from this repo
3)Compile - Follow Readme Telegram's repo (0) 
```
```
Aireplay:
0)Start a monitoring interface on mon0
1)Place all the .py and .sh scripts in appropriate directories (as in code or change the path in code)
```
How to Use:
===========
```
1)Start telegram ./telegram
2)Deauth attack starts on either sending or Receiving the 'GO' keyword
```
Go Codes:
==========
```
1) Launch Deauth -> mayday
2) Stop Deauth -> Billa
``` 

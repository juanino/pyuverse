#!/usr/bin/python
import sys
import rrdtool
import ConfigParser


# read the config file
# default location is /etc/pyuverse
Config = ConfigParser.ConfigParser()
try:
   open("/etc/pyuverse.conf")
except IOError as e:
   print 'Cannot open file or you need to copy pyuverse.conf to /etc'
   sys.exit()
Config.read("/etc/pyuverse.conf")

# set variables
UverseRouterUrl = Config.get("general","UverseRouterUrl")
rrdFile = Config.get("general","rrdFile")
try:
    open(rrdFile)
    print 'Opened rrdfile ' + rrdFile
except IOError as e:
    print 'rrd file ' + rrdFile + ' cannot be opened'

ret = rrdtool.graph("x.png", "--start", "-15m", "--vertical-label=Bytes/s",
 "DEF:inoctets=" + rrdFile + ":input:AVERAGE",
 "DEF:outoctets=" + rrdFile + ":output:AVERAGE",
 "CDEF:inbits=inoctets,8,*",
 "CDEF:outbits=outoctets,8,*",
 "PRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf %Sbps",
 "PRINT:inbits:MAX: %6.2lf %Sbps",)

print ret

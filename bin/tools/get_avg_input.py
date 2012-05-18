#!/usr/bin/python
import sys
import rrdtool
import ConfigParser
import pprint

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
 "PRINT:inbits:AVERAGE:%6.2lf %Sbps",
 "PRINT:outbits:AVERAGE:%6.2lf %Sbps",)

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(ret)

downstream = ret[2][0]
upstream = ret[2][1]
print "Downstream:" + downstream
print "Upstream:" + upstream
downstream = downstream.split(None, 1)
upstream = upstream.split(None, 1)

downstream = downstream[0]
upstream = upstream[0]

print "Printing json to stats.json"
f = open('stats.json', 'w')
json =  '''
{
 "version":"1.0.0",
 "title":"inid stats",
 "datastreams" : [
    {"id":"transmit", "current_value":"''' + upstream + '''"},
    {"id":"receive", "current_value":"''' + downstream + '''"}
  ]
}
'''

f.write(json)

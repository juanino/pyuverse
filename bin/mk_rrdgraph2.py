#!/usr/bin/python
import sys
import rrdtool
import datetime
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("/home/juanino/github/pyuverse/etc/pyuverse.conf")
rrdFile = Config.get("general","rrdFile")
print rrdFile


def make_mbits_graph():
    now = datetime.datetime.now()
    humantime = now.strftime("%Y-%m-%d %H:%M")
    title = "--title=24 hour inid traffic " + humantime
    print "rrd file is " + rrdFile
    ret = rrdtool.graph("net.png", "--start", "-1d", "--vertical-label=Bits/s", 
     title,
     "DEF:inoctets=" + rrdFile + ":input:AVERAGE",
     "DEF:outoctets=" + rrdFile + ":output:AVERAGE",
     "CDEF:inbits=inoctets,8,*",
     "CDEF:outbits=outoctets,8,*",
     "AREA:inbits#00FF00:In traffic",
     "LINE1:outbits#0000FF:Out traffic\\r",
     "COMMENT:\\n",
     "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf %Sbps",
     "GPRINT:inbits:MAX:Max In traffic\: %6.2lf %Sbps\\r",
     "GPRINT:outbits:AVERAGE:Avg Out traffic\: %6.2lf %Sbps",
     "GPRINT:outbits:MAX:Max Out traffic\: %6.2lf %Sbps\\r")
    print "saving to /var/www/net.png"
    print ret

def make_mbits_graph_1hr():
    now = datetime.datetime.now()
    humantime = now.strftime("%Y-%m-%d %H:%M")
    title = "--title=1 hour inid traffic " + humantime
    ret = rrdtool.graph("net1hr.png", "--start", "-1h", "--vertical-label=Bits/s",
     title,
     "DEF:inoctets=" + rrdFile + ":input:AVERAGE",
     "DEF:outoctets=" + rrdFile  + ":output:AVERAGE",
     "CDEF:inbits=inoctets,8,*",
     "CDEF:outbits=outoctets,8,*",
     "AREA:inbits#00FF00:In traffic",
     "LINE1:outbits#0000FF:Out traffic\\r",
     "COMMENT:\\n",
     "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf %Sbps",
     "GPRINT:inbits:MAX:Max In traffic\: %6.2lf %Sbps\\r",
     "GPRINT:outbits:AVERAGE:Avg Out traffic\: %6.2lf %Sbps",
     "GPRINT:outbits:MAX:Max Out traffic\: %6.2lf %Sbps\\r")
    print "saving to /var/www/net1hr.png"
    print ret

def mk_mbits_graph_1hr_upload():
    now = datetime.datetime.now()
    humantime = now.strftime("%Y-%m-%d %H:%M")
    title = "--title=1 hour inid traffic " + humantime
    ret = rrdtool.graph("net1hr_upload.png", "--start", "-1h", "--vertical-label=Bits/s",
     title,
     "DEF:outoctets=" + rrdFile + ":output:AVERAGE",
     "CDEF:outbits=outoctets,8,*",
     "LINE1:outbits#0000FF:Out traffic\\r",
     "COMMENT:\\n",
     "GPRINT:outbits:AVERAGE:Avg Out traffic\: %6.2lf %Sbps",
     "GPRINT:outbits:MAX:Max Out traffic\: %6.2lf %Sbps\\r")
    print "saving to /var/www/net1hr_upload.png"
    print ret

#!/usr/bin/python
import sys
import rrdtool
import datetime

def make_mbits_graph():
    now = datetime.datetime.now()
    humantime = now.strftime("%Y-%m-%d %H:%M")
    title = "--title=24 hour inid traffic " + humantime
    ret = rrdtool.graph("/var/www/net.png", "--start", "-1d", "--vertical-label=Bits/s", 
     title,
     "DEF:inoctets=/var/www/net.rrd:input:AVERAGE",
     "DEF:outoctets=/var/www/net.rrd:output:AVERAGE",
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
    ret = rrdtool.graph("/var/www/net1hr.png", "--start", "-1h", "--vertical-label=Bits/s",
     title,
     "DEF:inoctets=/var/www/net.rrd:input:AVERAGE",
     "DEF:outoctets=/var/www/net.rrd:output:AVERAGE",
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
    ret = rrdtool.graph("/var/www/net1hr_upload.png", "--start", "-1h", "--vertical-label=Bits/s",
     title,
     "DEF:outoctets=/var/www/net.rrd:output:AVERAGE",
     "CDEF:outbits=outoctets,8,*",
     "LINE1:outbits#0000FF:Out traffic\\r",
     "COMMENT:\\n",
     "GPRINT:outbits:AVERAGE:Avg Out traffic\: %6.2lf %Sbps",
     "GPRINT:outbits:MAX:Max Out traffic\: %6.2lf %Sbps\\r")
    print "saving to /var/www/net1hr_upload.png"
    print ret

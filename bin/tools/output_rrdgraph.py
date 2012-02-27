#!/usr/bin/python
import sys
import rrdtool
 
ret = rrdtool.graph("x.png", "--start", "-1d", "--vertical-label=Bytes/s",
 "DEF:outoctets=/tmp/net.rrd:output:AVERAGE",
 "LINE1:outoctets#0000FF:Out traffic\\r",
 "CDEF:outbits=outoctets,8,*",
 "COMMENT:\\n",
 "GPRINT:outbits:AVERAGE:Avg Out traffic\: %6.2lf %Sbps",
 "COMMENT: ",
 "GPRINT:outbits:MAX:Max Out traffic\: %6.2lf %Sbps\\r")

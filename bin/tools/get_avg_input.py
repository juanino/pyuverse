#!/usr/bin/python
import sys
import rrdtool
 
ret = rrdtool.graph("x.png", "--start", "-15m", "--vertical-label=Bytes/s",
 "DEF:inoctets=/var/www/net.rrd:input:AVERAGE",
 "DEF:outoctets=/var/www/net.rrd:output:AVERAGE",
 "CDEF:inbits=inoctets,8,*",
 "CDEF:outbits=outoctets,8,*",
 "PRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf %Sbps",
 "PRINT:inbits:MAX: %6.2lf %Sbps",)

print ret

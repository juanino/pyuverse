#!/usr/bin/python

# no longer needed
# this is now handled by pyuverselib

import sys
import rrdtool

ret = rrdtool.create("net.rrd", "--step", "300", "--start", '0',
 "DS:input:COUNTER:600:U:U",
 "DS:output:COUNTER:600:U:U",
 "RRA:AVERAGE:0.5:1:600",
 "RRA:AVERAGE:0.5:6:700",
 "RRA:AVERAGE:0.5:24:775",
 "RRA:AVERAGE:0.5:288:797",
 "RRA:MAX:0.5:1:600",
 "RRA:MAX:0.5:6:700",
 "RRA:MAX:0.5:24:775",
 "RRA:MAX:0.5:444:797")
 
if ret:
 print rrdtool.error()

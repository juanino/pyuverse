#!/usr/bin/python
import sys
import time
import rrdtool
 
total_input_traffic = 0
total_output_traffic = 0
 
while 1:
 total_input_traffic =  1
 total_output_traffic = 2
 ret = rrdtool.update('net.rrd','N:' + `total_input_traffic` + ':' + `total_output_traffic`);
 if ret:
     print rrdtool.error()
 else:
     print "good"
 time.sleep(300)

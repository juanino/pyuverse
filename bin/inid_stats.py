#!/usr/bin/python
# Author: Jerry Uanino (https://github.com/juanino/)
# Purpose: fetch stats from my inid
#          so I know when TV streams are too high
#          and HD will go in the crapper

# http://192.168.1.254/xslt?PAGE=C_1_0

from BeautifulSoup import BeautifulSoup
import urllib
import sys
import time
import rrdtool
import ConfigParser
from subprocess import call
from mk_rrdgraph2 import make_mbits_graph 
from mk_rrdgraph2 import make_mbits_graph_1hr
from mk_rrdgraph2 import mk_mbits_graph_1hr_upload
from pyuverselib import rrdCreateNew

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
    print 'creating new rrdfile ' + rrdFile
    rrdCreateNew()

trafficTotalTable = Config.getint("tableinfo","trafficTotalTable")
trafficTotalTransmitRow = Config.getint("tableinfo","trafficTotalTransmitRow")
trafficTotalReceiveRow = Config.getint("tableinfo","trafficTotalReceiveRow")
trafficTotalTransmitColumn = Config.getint("tableinfo","trafficTotalTransmitColumn")
trafficTotalReceiveColumn = Config.getint("tableinfo","trafficTotalReceiveColumn")

while True:

    f = urllib.urlopen(UverseRouterUrl)
    s = f.read()

    html = s
    soup = BeautifulSoup(''.join(html))

    lines = []
    tables = soup.findAll('table')
    rows = tables[trafficTotalTable].findAll('tr')
    transmitcols = rows[trafficTotalTransmitRow].findAll('td')
    receivecols = rows[trafficTotalReceiveRow].findAll('td')
    transmit = transmitcols[trafficTotalTransmitColumn].find(text=True)
    receive = receivecols[trafficTotalReceiveColumn].find(text=True)
    
    print transmit
    print receive
    
    updatestring = "N:" + str(receive) + ":" + str(transmit)
    print "Going to update with " + updatestring
    returncode = rrdtool.update(rrdFile,updatestring)
    print returncode

    make_mbits_graph()
    make_mbits_graph_1hr()
    mk_mbits_graph_1hr_upload()
    print "Sleeping...."
    time.sleep(300)

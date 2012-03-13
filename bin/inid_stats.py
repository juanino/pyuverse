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

# read the config file
Config = ConfigParser.ConfigParser()
Config.read("/home/juanino/github/pyuverse/etc/pyuverse.conf")

# set variables
UverseRouterUrl = Config.get("general","UverseRouterUrl")
rrdFile = Config.get("general","rrdFile")
totalTrafficTransmit = Config.getint("general","totalTrafficTransmit")
totalTrafficReceive = Config.getint("general","totalTrafficReceive")

while True:

    f = urllib.urlopen(UverseRouterUrl)
    s = f.read()

    html = s
    soup = BeautifulSoup(''.join(html))

    lines = []
    tables = soup.findAll('table')
    rows = tables[3].findAll('tr')
    transmitcolumns = rows[1].findAll('td')
    receivecolumns = rows[2].findAll('td')
    transmit = transmitcolumns
    print receivecolumns

    transmit = lines[totalTrafficTransmit] 
    receive = lines[totalTrafficReceive]
    shellcmd = "rrdtool update " + rrdFile + " N:" + receive + ":" + transmit

    return_code = call(shellcmd, shell=True)
    if return_code:
        print "return code is"  
        print return_code
    else:
        print "Good update. ----------->" + shellcmd
    make_mbits_graph()
    make_mbits_graph_1hr()
    mk_mbits_graph_1hr_upload()
    print "Sleeping...."
    time.sleep(300)

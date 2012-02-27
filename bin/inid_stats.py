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
from subprocess import call
from mk_rrdgraph2 import make_mbits_graph 
from mk_rrdgraph2 import make_mbits_graph_1hr
from mk_rrdgraph2 import mk_mbits_graph_1hr_upload


while True:

    f = urllib.urlopen("http://192.168.1.254/xslt?PAGE=C_1_0")
    s = f.read()

    html = s
    soup = BeautifulSoup(''.join(html))

    lines = []
    tables = soup.findAll('table')
    for table in tables:
        rows = table.findAll('tr')
        for tr in rows:
            cols = tr.findAll('td')
            for td in cols:
                column_data =  td.find(text=True)
                lines.append( column_data )

    transmit = lines[143] # (this will vary by device type)
    receive = lines[148] # (this will vary by device type)
    shellcmd = "rrdtool update /var/www/net.rrd N:" + receive + ":" + transmit

    return_code = call(shellcmd, shell=True)
    if return_code:
        print "return code is"  
        print return_code
    else:
        print "Good update. ----------->" + shellcmd
    print "Sleeping...."
    make_mbits_graph()
    make_mbits_graph_1hr()
    mk_mbits_graph_1hr_upload()
    time.sleep(300)

#!/bin/bash

# modify with your install location

INSTALLROOT=/root/appliance/pyuverse/bin/
if [ -x ${INSTALLROOT}/inid_stats.py ] ; then
    echo starting up ${INSTALLROOT}/inid_stats.py
else
    echo Could not find ${INSTALLROOT}/inid_stats.py
    echo please check the value of INSTALLROOT in start_daemon.sh
fi

daemon ${INSTALLROOT}/inid_stats.py --stdout /var/log/inid_stats.log --stderr /var/log/inid_stats.log --output /var/log/inid_stats.log
beep -f 2000 -r 4


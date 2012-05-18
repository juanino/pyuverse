#!/bin/bash
# purpose: extract mb/sec up and downstream
#          and send to cosm to graph

./get_avg_input.py
APIKEY=`cat /etc/pyuverse.conf |grep apikey | awk -F: {'print $2'}`
FEEDURL=`cat /etc/pyuverse.conf | grep feedurl | sed 's/feedurl://g'`

# do the update
curl --request PUT \
     --data-binary @stats.json \
     --header "X-ApiKey: ${APIKEY}" \
     --verbose \
     ${FEEDURL}

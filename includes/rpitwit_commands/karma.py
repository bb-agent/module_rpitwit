#!/usr/bin/python

import sys
import os
import time

from SOAPpy import SOAPProxy

url = 'http://localhost/BlackBulb/wsdl/BlackBulb.php?wsdl'

namespace = 'urn:BlackBulb'
server = SOAPProxy(url, namespace)

args=sys.argv[1:]

if len(args) > 0:
	if args[0] == "start":
		print server.moduleAction('s_karma','start')
		msg = "Karma Enabled"
	else:
		print server.moduleAction('s_karma','stop')
		msg = "Karma Disabled"

	mod_logs = "/usr/share/BlackBulb/logs/rpitwit.log"
	os.system("echo '" + time.strftime("%Y-%m-%d %X") + " - "+msg+"' >> " + mod_logs)
	os.system("twitter --oauth /usr/share/BlackBulb/conf/rpitwit_twitter_oauth set '" + msg + " (" + time.strftime("%Y-%m-%d %X") + ")'")

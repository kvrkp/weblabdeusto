#!/usr/bin/env python
#-*-*- encoding: utf-8 -*-*-
#
# Copyright (C) 2005-2009 University of Deusto
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#
# This software consists of contributions made by many individuals, 
# listed below:
#
# Author: Luis Rodríguez <4lurodri@rigel.deusto.es>
#         Jaime Irurzun <jaime.irurzun@gmail.com>
# 

import xmlrpclib
import base64

host = "http://localhost:12345"

print "Trying to establish connection (port 12345)... ",
conn = xmlrpclib.Server(host)
print "done."

try:
    print "test_me('hello!')... -> ",
    print conn.Util.test_me('hello')
    
    print "is_up_and_running()... -> ",
    print conn.Util.is_up_and_running()
    
    print "start_experiment()... -> ",
    print conn.Util.start_experiment()
    
    print "send_command('switch 2 on')... -> ",
    print conn.Util.send_command('switch 2 on')
    
    print "send_file('loooong file', 'info')... -> ",
    print conn.Util.send_file(base64.encodestring("looooong file"), 'info')
    
    print "dispose()... -> ",
    print conn.Util.dispose()
    
except xmlrpclib.Fault, faultobj:
    print "Error de Servidor : ", faultobj.faultCode
    print ">>> %s <<<" % faultobj.faultString

except:
    print "Error de Cliente: '%s/%s'" % (sys.exc_type, sys.exc_value)

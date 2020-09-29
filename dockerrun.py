#!/usr/bin/python3
print('content-type:text/html')
print()

import subprocess as sp
import cgi
osname=cgi.FieldStorage().getvalue('x')
image=cgi.FieldStorage().getvalue('i')

cmd = 'docker run -d -it --name {0} {1}'.format(osname,image)
output = sp.getstatusoutput('sudo {0}'.format(cmd))

error_code= output[0]
error= output[1]

if(error_code==0):
 print('docker launched with OS name : {0}'.format(osname))
else:
 print(error)

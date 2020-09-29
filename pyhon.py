#!/usr/bin/python3
import cgi
import subprocess as sp
print("content-type:text/html")
print()

cmd=cgi.FieldStorage().getvalue("x")

if(("DATE" in cmd) or ("date" in cmd) or ("Date" in cmd) ):
  out=sp.getoutput('date \'+Todays date is : %m %d %Y\' ')
elif(("Cal" in cmd) or ("cal" in cmd) or ("calender" in cmd) or ("Calender" in cmd)):
  out=sp.getoutput('cal')
elif(("Time" in cmd) or ("time" in cmd) or ("TIME" in cmd)):
  out=sp.getoutput('date \'+Time is : %T\' ')

print(out)

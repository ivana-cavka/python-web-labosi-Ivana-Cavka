#!C:\Python310\python.exe

#pokrenit apache u xampp-u (control panel xampp)
#u C\xampp\cgi-bin dodat folder
#dodat python path (doma je #!C:\Python310\python.exe)
#u browseru otvorit http://localhost/cgi-bin/HTML_forme_CGI_skripte/test2.py (port 80 default)

import cgi
import os

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello Word - First CGI Program</title>')
print ('</head>')
print ('<body>')
print ('<h2>Hello Word! This is my first CGI program</h2>')
print ('</body>')
print ('</html>')

print  (os.environ)
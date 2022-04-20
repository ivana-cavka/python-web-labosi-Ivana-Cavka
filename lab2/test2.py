#!C:\ProgramData\Anaconda3\python.exe

import cgi
import os
import cgitb
cgitb.enable(display=0, logdir="")

print  ("""
<!DOCTYPE html>
<html>
<body>
<h2>Unesite podatke:</h2>
<form action="test3.py" method="post">
<table style="padding: 1px; border: 1px solid black;">
<tr>
  <td style="padding: 1px; border: 1px solid black;">Ime:</td>
  <td style="padding: 1px; border: 1px solid black;"><input type="text" name="ime" value=""></td>
</tr>
<tr>
  <td style="padding: 1px; border: 1px solid black;">Lozinka:</td>
  <td style="padding: 1px; border: 1px solid black;"><input type="password" name="lozinka" value=""></td>
</tr>
<tr>
  <td style="padding: 1px; border: 1px solid black;">Ponovi lozinku:</td>
  <td style="padding: 1px; border: 1px solid black;"><input type="password" name="opet_lozinka" value=""></td>
</tr>
<tr>
  <td style="padding: 1px; border: 1px solid black;"><input type="submit" value="Next"></td>
  <td style="padding: 1px; border: 1px solid black;"></td>
</tr>
</table>
</form> 

</body>
</html>
""")

flag = True
while flag:
  params = cgi.FieldStorage() 
#print (params)
#print (os.environ['REQUEST_METHOD'])
  print ("<br>")
  if params.getvalue("lozinka") == params.getvalue("opet_lozinka"):
      print ("lozinka tocna")
      flag = False
  else:
      print("lozinka netocna, pokusajte opet")
#if os.environ['REQUEST_METHOD'].upper() == 'POST':
#    print (params.getvalue("ime"))
#else:
#    print(params.getvalue("lastname"))

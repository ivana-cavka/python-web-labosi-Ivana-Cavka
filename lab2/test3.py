#!C:\Python310\python.exe

import cgi
from types import NoneType
params = cgi.FieldStorage()

#print("parametri iz skripte koja se submit-ala na test3.py: ")
#print (params.getvalue("ime"))

print ("""
<!DOCTYPE html>
<html>
<body>
""")
if params.getvalue('ime') == None:
  print("upisite ime")
  print(''' <br>
      <a href="test2.py">Pokusaj opet</a>
      ''')
elif params.getvalue('lozinka') == None:
  print("upisite lozinku")
  print(''' <br>
      <a href="test2.py">Pokusaj opet</a>
      ''')
elif params.getvalue('opet_lozinka') == None:
  print("upisite ime")
  print(''' <br>
      <a href="test2.py">Pokusaj opet</a>
      ''')
else:
    print ("<br>")
    if params.getvalue("lozinka") == params.getvalue("opet_lozinka"):
      print ('''
              <form action="test4.py" method="post">
              <table style="padding: 1px; border: 1px solid black;">
              <tr>
                <td style="padding: 1px; border: 1px solid black;">Status:</td>
                <td style="padding: 1px; border: 1px solid black;">
                  <label for="redovan">Redovan: </label>
                  <input type="radio" id="redovan" name="status" value="redovan">
                  <label for="izvanredan">Izvanredan: </label>
                  <input type="radio" id="izvanredan" name="status" value="izvanredan">
                </td>
              </tr>
              <tr>
                <td style="padding: 1px; border: 1px solid black;">E-mail:</td>
                <td style="padding: 1px; border: 1px solid black;"><input type="email" style="width: 76%;" name="email" value=""></td>
              </tr>
              <tr>
                <td style="padding: 1px; border: 1px solid black;">Smjer:</td>
                <td style="padding: 1px; border: 1px solid black;">
                  <select id="smjer" name="smjer" style="width: 80%;">
                    <option value="Baze podataka">Baze podataka</option>
                    <option value="Programiranje">Programiranje</option>
                    <option value="Racunalne mreze">Racunalne mreze</option>
                    <option value="Sigurnost racunala">Sigurnost racunala</option>
                  </select>
                </td>
              </tr>
              <tr>
                <td style="padding: 1px; border: 1px solid black;">Zavrsni:</td>
                <td style="padding: 1px; border: 1px solid black;"><input type="checkbox" name="zavrsni" value="da"></td>
              </tr>
              <tr>
                <td style="padding: 1px; border: 1px solid black;"><input type="submit" value="Next"></td>
                <td style="padding: 1px; border: 1px solid black;"></td>
              </tr>
              </table>
                <br><br>''')
      print ('<input type="hidden" name="ime" value="' + params.getvalue('ime') + '">')
      print ('''
              </form>''')
    else:
      print("lozinka netocna, pokusajte opet")
      print(''' <br>
      <a href="test2.py">Pokusaj opet</a>
      ''')
print('''</body>
         </html>''')
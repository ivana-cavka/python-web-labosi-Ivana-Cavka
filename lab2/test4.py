#!C:\Python310\python.exe

import cgi
params = cgi.FieldStorage()
if params.getvalue('zavrsni') == 'da':
  zavrsni = 'Da'
else:
  zavrsni = 'Ne'
print ("""
<!DOCTYPE html>
<html>
<body>
""")
if params.getvalue('status') == None:
  print("odaberite status")
  print(''' <br>
      <a href="test3.py">Pokusaj opet</a>
      ''')
elif params.getvalue('email') == None:
  print("upisite email")
  print(''' <br>
      <a href="test3.py">Pokusaj opet</a>
      ''')
elif params.getvalue('smjer') == None:
  print("odaberite smjer")
  print(''' <br>
      <a href="test3.py">Pokusaj opet</a>
      ''')
else:
  print ('''
<!DOCTYPE html>
<html>
<body>
<form action="test5.py" method="post">
<table style="padding: 1px; border: 1px solid black;">
<tr>
  <td style="padding: 1px; border: 1px solid black;">Napomene:</td>
  <td style="padding: 1px; border: 1px solid black;">
    <textarea rows = "5" cols = "18" name = "napomena">Prelazak na izvanredni studij...</textarea>
  </td>
</tr>
<tr>
  <td style="padding: 1px; border: 1px solid black;"><input type="submit" value="Next"></td>
  <td style="padding: 1px; border: 1px solid black;"></td>
</tr>
</table>
''')
  print ('<input type="hidden" name="ime" value="' + params.getvalue("ime") + '">')
  print ('<input type="hidden" name="status_redovan" value="''' + params.getvalue("status") + '">')
  print ('<input type="hidden" name="email" value="''' + params.getvalue("email") + '">')
  print ('<input type="hidden" name="smjer" value="' + params.getvalue("smjer") + '">')
  print ('<input type="hidden" name="zavrsni" value="' + zavrsni + '">')
  print ('''
    </form>
    </body>
    </html>''')
#print (params.getvalue("smjer_studija"))
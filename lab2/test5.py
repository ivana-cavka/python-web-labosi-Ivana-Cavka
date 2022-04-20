#!C:\Python310\python.exe

import cgi
params = cgi.FieldStorage()
if params.getvalue('napomena') == "Prelazak na izvanredni studij...":
  napomena = " "
else:
  napomena = params.getvalue("napomena")

print ('''
<!DOCTYPE html>
<html>
<body>
<table style="padding: 1px; border: 1px solid black;">
<tr>
  <td style="padding: 1px; border: 1px solid black;" colspan="2"><b>Uneseni podaci:</b></td>
  <td></td>
</tr>
<tr>
  <td style="padding: 1px; border: 1px solid black;">Ime:</td>
  <td style="padding: 1px; border: 1px solid black;">''' + params.getvalue("ime") + '''</td>
</tr>
<tr>
  <td style="padding: 1px; border: 1px solid black;">E-mail:</td>
  <td style="padding: 1px; border: 1px solid black;">''' + params.getvalue("email") + '''</td>
</tr>
<tr>
  <td style="padding: 1px; border: 1px solid black;">Status:</td>
  <td style="padding: 1px; border: 1px solid black;">''' + params.getvalue("status_redovan") + '''</td>
</tr>
<tr>
  <td style="padding: 1px; border: 1px solid black;">Smjer:</td>
  <td style="padding: 1px; border: 1px solid black;">''' + params.getvalue("smjer") + '''</td>
</tr>
<tr>
  <td style="padding: 1px; border: 1px solid black;">Zavrsni rad:</td>
  <td style="padding: 1px; border: 1px solid black;">''' + params.getvalue("zavrsni") + '''</td>
</tr>
<tr>
  <td style="padding: 1px; border: 1px solid black;">Napomene:</td>
  <td style="padding: 1px; border: 1px solid black;">''' + napomena + '''</td>
</tr>
</table>
<a href="test2.py">Na pocetak</a>
''')
print ('''
</body>
</html>''')



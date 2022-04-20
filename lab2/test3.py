#!C:\ProgramData\Anaconda3\python.exe

import cgi
params = cgi.FieldStorage()
#first_name = params.getvalue("firstname")

print ('''
<!DOCTYPE html>
<html>
<body>
<form action="test4.py" method="post">
<table style="padding: 1px; border: 1px solid black;">
<tr>
  <td style="padding: 1px; border: 1px solid black;">Status:</td>
  <td style="padding: 1px; border: 1px solid black;">
    <label for="redovan">Redovan: </label>
    <input type="radio" id="redovan" name="status_redovan" value="red">
    <label for="izvanredan">Izvanredan: </label>
    <input type="radio" id="izvanredan" name="status_izvanredan" value="izv">
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
      <option value="baze">Baze podataka</option>
      <option value="prog">Programiranje</option>
      <option value="mreze">Racunalne mreže</option>
    </select>
  </td>
</tr>
<tr>
  <td style="padding: 1px; border: 1px solid black;">Zavrsni:</td>
  <td style="padding: 1px; border: 1px solid black;"><input type="checkbox" name="zavrsni" value=""></td>
</tr>
<tr>
  <td style="padding: 1px; border: 1px solid black;"><input type="submit" value="Next"></td>
  <td style="padding: 1px; border: 1px solid black;"></td>
</tr>
</table>
  <select name="smjer_studija">
    <option value="programiranje">programiranje</option>
    <option value="baze_podataka">baze podataka</option>
    <option value="mreze">mreze</option>
    <option value="informacijski_sustavi">informacijski sustavi</option>
  </select>
  <br><br>''')
print ('<input type="hidden" name="ime" value="' + params.getvalue("firstname") + '">')
print ('''
<br>
<input type="submit" value="submit">
</form>

</body>
</html>''')
print("Ovako se zovu post parametri iz skripte koja se submit-ala na test3.py: ")
print (params.getvalue("firstname"))
print ('<br>')
print("Parametri pod ovim imenom ne postoje: ")
print (params.getvalue("ime"))

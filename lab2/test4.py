#!C:\ProgramData\Anaconda3\python.exe

import cgi
params = cgi.FieldStorage()

print ('''
<!DOCTYPE html>
<html>
<body>

<h2>Program studija</h2>
 <form action="test5.py" method="post">
  <input type="radio" name="studij" value="izvanredni" checked> izvanredni studij<br>
  <input type="radio" name="studij" value="redovni"> redovni studij<br>
  <br><br>)''')
print ('<input type="hidden" name="ime" value="''' + params.getvalue("ime") + '">')
print ('<input type="hidden" name="smjer_studija" value="' + params.getvalue("smjer_studija") + '">')
print ('''<input type="submit" value="dalje">
</form>
</body>
</html>''')
print (params.getvalue("smjer_studija"))
print ('<br>')
print (params.getvalue("ime")) 

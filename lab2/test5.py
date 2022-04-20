#!C:\ProgramData\Anaconda3\python.exe

import cgi
params = cgi.FieldStorage()

print ('''
<!DOCTYPE html>
<html>
<body>

<h2>Oznaciti upisane ects-ove:</h2>

<form action="upisni_list.py">
<input type="checkbox" name="zavrsni" value="zavrsni">Zavrsni rad
<br>
<input type="checkbox" name="praksa" value="praksa">Praksa''')
print ('<input type="hidden" name="smjer" value="' + params.getvalue("smjer_studija") + '">')
print ('<input type="hidden" name="ime" value="' + params.getvalue("ime") + '">' )
print ('''<br><br>
<input type="submit">
</form> 

</body>
</html>''')



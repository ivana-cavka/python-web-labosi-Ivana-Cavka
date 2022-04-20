#!C:\ProgramData\Anaconda3\python.exe

import cgi
form_data = cgi.FieldStorage()

print('')
print (form_data.getvalue('ime'))
print (form_data.getvalue('smjer'))


#!C:\Users\ivana\AppData\Local\Programs\Python\Python310\python.exe
from queue import Empty
from http import cookies
#from types import NoneType
import base
import cgi
import subjects
import os

def list_others():
    year = params.getvalue('year')
    for key in subjects.year_names:
        if(str(subjects.year_names[key]) != year):
            base.print_table(str(subjects.year_names[key]))

params = cgi.FieldStorage()
year = params.getvalue('year')
cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies_object = cookies.SimpleCookie(cookies_string)
for key in subjects.subjects:
        value = params.getvalue(key)
        if (value is not None):
            cookie = cookies.SimpleCookie()
            cookie[key] = value
            print(cookie.output())
base.start_html()
base.display_header()
if (os.environ["REQUEST_METHOD"].upper() == "POST"): 
    if params.getvalue('year') is None:
        base.display_upisni_list()
    else:
        year = params.getvalue('year')
        base.print_table(year)
base.end_html()
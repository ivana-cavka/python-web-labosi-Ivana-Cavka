#!C:\Users\ivana\AppData\Local\Programs\Python\Python310\python.exe
from queue import Empty
from turtle import onclick
from types import NoneType
import base
import cgi
import subjects
import os
import index

params = cgi.FieldStorage()

base.start_html()
if (os.environ["REQUEST_METHOD"].upper() == "POST"): #klik na botun godine, bez list all
    year = params.getvalue('year')
    index.print_table(year)
    index.display_list_all_option()
else: #list all 
    for key in subjects.year_names:
        index.print_table(subjects.year_names[key])
        print('<br>')
base.end_html()
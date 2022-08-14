#!python.exe
from asyncio.windows_events import NULL
from queue import Empty
from http import cookies
#from types import NoneType
import base
import cgi
import subjects
import os
import db
import session

def start_html():
    print("""
    <!DOCTYPE html>
    <html>
    <head></head>
    <body>
     """)

def end_html():
    print("""</body>
    </html>
    """)

def display_header():
    for key in subjects.year_names:
        print('''
        <form action="index.py" method="post">
            <input type="submit" name="year" value="''' + str(subjects.year_names[key]) + '''" >
        ''')
    print('''
            <input type="submit" name="upisni_list" value="Upisni list" onclick="''')
    print('''">
        ''')
    print('''<br><br>''')

def display_upisni_list():
    session_id = session.get_or_create_session_id()
    _, session_data = db.get_session(session_id) 
    print(""" 
    <table style="padding: 1px; border: 1px solid black;">
    <tr>
        <td style="padding: 1px; border: 1px solid black;">Predmet</td>
        <td style="padding: 1px; border: 1px solid black;">Status</td>
        <td style="padding: 1px; border: 1px solid black;">Ects</td>
    </tr>
    """)
    for key in subjects.subjects:
        if key in session_data:
            choice = subjects.status_names[session_data[key]]
        else: 
            choice = "Not selected"
        print('''
                    <tr>
                        <td style="padding: 1px; border: 1px solid black;">'''
                        + str(subjects.subjects[key]['name']) +
                        '''</td>
                        <td style="padding: 1px; border: 1px solid black;">'''
                        + str(choice) +
                        '''</td>
                        <td style="padding: 1px; border: 1px solid black;">'''
                        + str(subjects.subjects[key]['ects']) +
                        '''</td>
                    </tr>
                    ''')
    print(""" 
    <table>""")

def print_table(year):
    print(""" 
    <table style="padding: 1px; border: 1px solid black;">
    <tr>
        <td style="padding: 1px; border: 1px solid black;">"""
            + str(year) +
        """</td>
        <td style="padding: 1px; border: 1px solid black;">Ects
        </td>
        <td style="padding: 1px; border: 1px solid black;">Status
        </td>
    </tr>
    """)
    for key in subjects.subjects:
        if(subjects.subjects[key]['year'] == subjects.year_ids[year]):
            print('''
                    <tr>
                        <td style="padding: 1px; border: 1px solid black;">'''
                        + str(subjects.subjects[key]['name']) +
                        '''</td>
                        <td style="padding: 1px; border: 1px solid black;">'''
                        + str(subjects.subjects[key]['ects']) +
                        '''</td>
                        <td style="padding: 1px; border: 1px solid black;">
                        ''')
            print_status(key)
            print('''
                        </td>
                    </tr>
                    ''')
    print(""" 
    <table>""")
    display_list_all_option()

def display_list_all_option():
    print('''
        <a href="index.py" name="link">List all</a>
    </form>''')

def print_status(subject):
    for key in subjects.status_names:
        value = set_status(subject)
        print('''<input type="radio" id="status" name="''' + str(subject) +
                        '''" value="''' + str(key) + '''"''')
        if(value == key):
            print(''' checked''') 
        print('''>
                <label for="status">''' + str(subjects.status_names[key]) +'''</label>
            ''')

def set_status(subject):
    session_id = session.get_or_create_session_id()
    _, session_data = db.get_session(session_id) 
    if subject in session_data:
        value = session_data[subject]
    else:
        value = 'not'
    return value
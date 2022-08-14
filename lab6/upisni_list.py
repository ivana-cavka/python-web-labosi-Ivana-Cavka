#!python.exe
import cgi
import db
import os
from session import get_or_create_session_id
import user
import json
from http import cookies
import base

def get_user_id(session_id):
    mydb = db.get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT user_id FROM sessions WHERE session_id=" + str(session_id))
    myresult = cursor.fetchone()
    user_id = myresult[0] if myresult[0] else None
    return user_id

def is_student(user_id):
    mydb = db.get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT uloga FROM users WHERE id=" + str(user_id))
    myresult = cursor.fetchone()
    is_student = True if myresult[0] == "student" else False
    return is_student

def create_upisni_list(student_id):
    query = "INSERT INTO upisni_list (id_studenta) VALUES (%s)"
    values = (student_id,)
    mydb = db.get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid 

def get_upisni_list(upisni_list_id):
    mydb = db.get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM upisni_list WHERE id=" + str(upisni_list_id))
    myresult = cursor.fetchone()
    return myresult

def get_or_create_upisni_list():
    session_id = get_or_create_session_id()
    user_id = get_user_id(session_id)
    if is_student(user_id):
        mydb = db.get_DB_connection()
        cursor = mydb.cursor()
        cursor.execute("SELECT id FROM sessions WHERE student_id=" + str(user_id))
        myresult = cursor.fetchone()
        upisni_list_id = myresult[0] if myresult[0] else None
    else:
        upisni_list_id=None
    if upisni_list_id is None:
        upisni_list_id = create_upisni_list(user_id)
    return upisni_list_id

def add_to_upisni_list(params):
    upisni_list_id = get_or_create_upisni_list()
    _, session_data = db.get_session(upisni_list_id) 
    for article_id in params.keys():
        session_data[article_id]=params[article_id].value
    db.update_session(upisni_list_id, session_data)
    return session_data

#main
params = cgi.FieldStorage()
base.start_html()
add_to_upisni_list(params)
base.end_html()
from typing import Iterable
from typing import Dict
from typing import DefaultDict
import db
import os
from http import cookies
import json
import subjects

def get_or_create_session_id():
    http_cookies_str = os.environ.get('HTTP_COOKIE', '')
    get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
    session_id = get_all_cookies_object.get("session_id").value if get_all_cookies_object.get("session_id") else None
    if session_id is None:
        session_id = db.create_session()
        cookies_object = cookies.SimpleCookie()
        cookies_object["session_id"] = session_id
        print(cookies_object.output()) #upisivanje cookie-a u header
    return session_id

def add_to_session(params):
    session_id = get_or_create_session_id()
    _, session_data = db.get_session(session_id) 
    for article_id in params.keys():
        session_data[article_id]=params[article_id].value
    db.update_session(session_id, session_data)
    return session_data

def remove_from_session(params):
    session_id = get_or_create_session_id()
    _, data = db.get_session(session_id)
    for article_id in params.keys():
        data[article_id] = data.get(article_id)
        if data.get(article_id) < 1:
            data.pop(article_id, "")
    db.update_session(session_id, data)

def destroy_session(session_id):
    mydb = db.get_DB_connection()
    cursor = mydb.cursor()
    query = 'DELETE FROM sessions WHERE session_id= (%s)'
    values = (session_id, )
    cursor.execute(query, values)
    mydb.commit()
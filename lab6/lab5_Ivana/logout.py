#!python.exe
import cgi
import user
import os
import base
from http import cookies
import session

#Unistiti sesiju (izbrisati sesiju iz baze i ukloniti cookie session_id iz preglednika) i preusmjeriti korsnika na stranicu za prijavu.

#main
http_cookies_str = os.environ.get('HTTP_COOKIE', '')
get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
session_id = get_all_cookies_object.get("session_id").value
session.destroy_session(session_id)
cookies_object = cookies.SimpleCookie()
cookies_object["session_id"] = ""
cookies_object["session_id"]["expires"] = 'Thu, 01 Jan 1970 00:00:00 GMT'
print (cookies_object.output()) #upisivanje cookie-a u header
base.start_html()
user.display_menu()
base.end_html()
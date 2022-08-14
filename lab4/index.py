#!python.exe
#Svaka od stranica (godina) zadržava status predmeta (radio button ostaje označen prema zadnjem odabiru). 
# Da bi se to omogućilo, pri promijeni stranice, podatke o predmetima spremiti iz post parametara u sesiju u bazi podataka 
# i čitati iz sesije u bazi podataka varijable pri generiranju HTML-a. Skripta predmeti.py sadrži popis predmeta po godinama 
# i druge potrebne podatke i potrebno ju je uključiti sa import. 
# Sve funkcionalnosti moraju raditi i nakon dodavanja/uklanjanja predmeta iz popisa. 
# Kôd podijeliti u funkcije za:
#⦁	Ispis jednog predmeta sa odabirom
#⦁	Ispis predmeta godine
#⦁	Ispis upisnog lista
#⦁	Spremanje odabira iz post parametere u sesiju u bazi podataka
from queue import Empty
from http import cookies
#from types import NoneType
import base
import cgi
import subjects
import os
import db
import session

def list_others():
    year = params.getvalue('year')
    for key in subjects.year_names:
        if(str(subjects.year_names[key]) != year):
            base.print_table(str(subjects.year_names[key]))

params = cgi.FieldStorage()
year = params.getvalue('year')
if (os.environ["REQUEST_METHOD"].upper() == "POST"): 
    data = session.add_to_session(params)
else:
    session.get_or_create_session_id()
base.start_html()
base.display_header()
if (os.environ["REQUEST_METHOD"].upper() == "POST"): 
    if params.getvalue('year') is None:
        base.display_upisni_list()
    else:
        year = params.getvalue('year')
        base.print_table(year)
base.end_html()
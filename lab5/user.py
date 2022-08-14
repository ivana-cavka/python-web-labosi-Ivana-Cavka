import hashlib
import base
import cgi
import subjects
import os
import db
import session
import mysql.connector

# Koristiti gdje je prikladno password_hash() i password_verify(). 
# Prilikom zahtijevanja pocetne stranice, neprijavljene korisnike preusmjeravati na stranicu za prijavu. 
# Podatke o korisniku cuvati u bazi podataka u tablici users. 
# Tablica ce imati cetiri stupca: 
# id (primarni kljuc), 
# ime (varchar 100),  
# email (varchar 100 i postaviti ga na razini baze na unique) 
# te password (binary 64, jer ce sadrzavati hash).  
# Prilikom potvrde identiteta (uspjesne autentikacije) kreirati sesiju u koju ce se spremiti id autenticiranog korisnika. 
# Na vrhu stranice dodati pozdravnu poruku „Hej [ime korisnika]!”. Razdvojite kod na sljedece funkcije i pomocne funkcije:
# register()
# login()
# create_user()
# get_user()
# Rjecnik subjects iz datoteke subjects.py zamijeniti tablicom „subjects” u bazi podataka. 
# Tablica ce imati sljedece stupce: id (int, AI, primarni kljuc), kod (varchar), ime (varchar 100), bodovi (int), godina (int). 
# Rucno popuniti tablicu podacima iz rjecnika. Listu predmeta na stranici dohvatiti iz baze podataka.


def display_menu():
    print('''<form action="index.py" method="post">
            <input type="submit" name="home" value="PREDMETI" style="width:300px"> 
            </form>
            <form action="registration.py" method="post">
            <input type="submit" name="registracija" value="REGISTRACIJA" style="width:300px">
            </form>
            <form action="login.py" method="post">
            <input type="submit" name="login" value="LOGIN" style="width:300px">
            </form>
            <form action="logout.py" method="post">
            <input type="submit" name="odjava" value="ODJAVA" style="width:300px">
            </form>
            <form action="change_passwd.py" method="post">
            <input type="submit" name="promjena lozinke" value="PROMJENA LOZINKE" style="width:300px">
            </form>''')

def create_user(name, email, password):
    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    values = (name, email, password)
    mydb = db.get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid 

def get_user(user_id):
    mydb = db.get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE id=" + str(user_id))
    myresult = cursor.fetchone()
    return myresult[0], myresult[1], myresult[2], myresult[3]

def get_user_passwd_by_name(user_name):
    mydb = db.get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT password FROM users WHERE name='" + str(user_name) + "'")
    myresult = cursor.fetchone()
    return myresult[0] #tuple

def is_user_created_by_name(user_name):
    mydb = db.get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT id FROM users WHERE name='" + str(user_name)+ "'")
    myresult = cursor.fetchone()
    if myresult == None: #check tuple - not subscriptable
        return False
    return True

def hash_password(password):
    psswd = password.encode('utf-8')
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', psswd, salt, 100000)
    return salt + key

def verify_password(login_password, stored_hash):
    psswd = login_password.encode('utf-8')
    salt = stored_hash[:32]
    key = stored_hash[32:]
    new_key = hashlib.pbkdf2_hmac('sha256', psswd, salt, 100000)
    return (key == new_key)

def update_password(user_name, new_password):
    mydb = db.get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute('''
    UPDATE users SET password=%s 
    WHERE name=%s''', (new_password,user_name))  
    mydb.commit()

#!python.exe
import cgi
import os
import user
import base

#Prijavljivanje: Standardna login forma sa imenom i lozinkom
#U slucaju greske u autentikaciji, vratiti korisnika na stranicu sa porukom o greski.
#U slucaju uspjesne autentikacije, prosljediti korisnika na pocetnu stranicu.

def login():
    if (os.environ["REQUEST_METHOD"].upper() == "POST"): 
        if params.getvalue('name') == None or params.getvalue('passwd_1') == None or params.getvalue('passwd_2') == None:
            print("""Molimo popunite sva naznacena polja. Ponovite unos <br><br>""")
            print_login_form()
        elif params.getvalue('passwd_1') != params.getvalue('passwd_2'):
            print("""Upisane lozinke se ne podudaraju. Ponovite unos <br><br>""")
            print_login_form()
        elif not user.is_user_created_by_name(params.getvalue('name')):
            print("""Korisnik nije pronaden. Ponovite unos <br><br>""")
            print_login_form()
        elif not user.verify_password(params.getvalue('passwd_1'), user.get_user_passwd_by_name(params.getvalue('name'))):
            print("""Netocna lozinka. Ponovite unos <br><br>""")
            print_login_form()
        else:
            user.display_menu()
    else:
        print_login_form()

def print_login_form():
    print(""" 
    <form action="login.py" method="post">
    <table style="padding: 1px; border: 1px solid black;">
    <tr>
        <td style="padding: 1px; border: 1px solid black;">Ime:</td>
        <td style="padding: 1px; border: 1px solid black;"><input type="text" name="name" value=""></td>
    </tr>
    <tr>
        <td style="padding: 1px; border: 1px solid black;">Lozinka:</td>
        <td style="padding: 1px; border: 1px solid black;"><input type="password" name="passwd_1" value=""></td>
    </tr>
    <tr>
        <td style="padding: 1px; border: 1px solid black;">Ponovi lozinku:</td>
        <td style="padding: 1px; border: 1px solid black;"><input type="password" name="passwd_2" value=""></td>
    </tr>
    <tr>
        <td style="padding: 1px; border: 1px solid black;" colspan="2" ><input type="submit" value="Prijavi se" style="padding-left:35%; padding-right:35%" ></td>
    </tr>
    <table>
    </form>""")

#main
params = cgi.FieldStorage()
base.start_html()
login()
base.end_html()
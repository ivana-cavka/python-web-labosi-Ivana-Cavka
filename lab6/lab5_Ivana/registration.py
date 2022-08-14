#!python.exe
import cgi
import os
import user
import base

#Registracijska forma sadrži: ime, e-mail, lozinku, ponovljenu lozinku
#potrebno je provjeriti da ime ili e-mail nisu zauzeti i da su lozinke jednake te korisnika 
#u slucaju greske vratiti korisnika na istu stranicu sa opisom greske.
#U slucaju uspjeha prosljediti korisnika na stranicu za prijavu (login)

def register():
    if (os.environ["REQUEST_METHOD"].upper() == "POST"): 
        if params.getvalue('name') == None or params.getvalue('email') == None or params.getvalue('passwd_1') == None or params.getvalue('passwd_2') == None:
            print("""Molimo popunite sva naznacena polja. Ponovite unos <br><br>""")
            print_registration_form()
        elif params.getvalue('passwd_1') != params.getvalue('passwd_2'):
            print("""Upisane lozinke se ne podudaraju. Ponovite unos <br><br>""")
            print_registration_form()
        elif len(str(params.getvalue('name'))) <= 2 :
            print("""Ime mora biti duze od dva znaka. Ponovite unos <br><br>""")
            print_registration_form()
        elif user.is_user_created_by_name(params.getvalue('name')):
            print("""Korisnicko ime vec postoji. Ponovite unos <br><br>""")
            print_registration_form()
        else:
            hashed = user.hash_password(params.getvalue('passwd_1'))
            user.create_user(params.getvalue('name'), params.getvalue('email'), hashed)
            user.display_menu()
    else:
        print_registration_form()

def print_registration_form():
    print(""" 
    <form action="registration.py" method="post">
    <table style="padding: 1px; border: 1px solid black;">
    <tr>
        <td style="padding: 1px; border: 1px solid black;">Ime:</td>
        <td style="padding: 1px; border: 1px solid black;"><input type="text" name="name" value=""></td>
    </tr>
    <tr>
        <td style="padding: 1px; border: 1px solid black;">E-mail:</td>
        <td style="padding: 1px; border: 1px solid black;"><input type="email" name="email" value=""></td>
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
        <td style="padding: 1px; border: 1px solid black;" colspan="2" ><input type="submit" value="Registriraj se" style="padding-left:35%; padding-right:35%" ></td>
    </tr>
    <table>
    </form>""")

#main
params = cgi.FieldStorage()
base.start_html()
register()
base.end_html()
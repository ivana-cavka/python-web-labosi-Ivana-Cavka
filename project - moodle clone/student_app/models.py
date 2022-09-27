import datetime
from xmlrpc.client import DateTime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
#from student_app.validate import validate_student
#import validate

class RolesEnum(models.TextChoices):
    Admin = 'administrator'
    Student = 'student'
    Profesor = 'profesor'
    Nema = 'none'
    #https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-choices-enum-types
    #povratna vrijednost za 'opis' je string zdesna

#tablica korisnici (prosiriti AbstractUser klasu sa atributom za ulogu korisnika ili dodati novu
#tablicu za definiranje uloge)
class CustomUser(AbstractUser):
    pass
    role = models.CharField(max_length=64, choices=RolesEnum.choices, default=RolesEnum.Nema)
    #https://docs.djangoproject.com/en/4.1/topics/auth/customizing/

#- tablica dokumenti - atributi su id (primarni kljuc), naslov dokumenta (varchar), putanja na
#dokument koji je spremljen na serveru (varchar), vrijeme kreiranja dokumenta, kreator (strani kljuckoji profesor je kreirao dokument)
class Document(models.Model):
    title = models.CharField(max_length=256)
    path = models.CharField(max_length=256)
    created = models.DateTimeField()
    creator = models.ForeignKey(CustomUser, on_delete=models.SET_DEFAULT, default='unknown')
    #updated = models.DateTimeField(default=datetime.datetime.now())
   
    def __str__(self):
        return '%s %s %s' %(self.title, self.path, self.created)

#- tablica (medjutablica) student_dokument za definiranje s kojim studentima je dokument
#podijeljen – atributi su id (primarni kljuc), dokument (strani kljuc na model Dokument), student
#(strani kljuc na model Korisnik koji ima ulogu Student). Opcionalno umjesto primarnog kljuca se
#moze koristiti kombinirani kljuc od dva strana kljuca.
class Student_Document(models.Model):
    student_id = models.ForeignKey(CustomUser, limit_choices_to={'role': 'student'}, on_delete=models.CASCADE) #1 korisnik n dokumenata
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE) #n dokumenata 1 korisnik

    def __str__(self):
        return '%s %s' %(self.student_id, self.document_id)

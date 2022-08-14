from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# python manage.py makemigrations - za stvaranje skripte
# python manage.py migrate - za migriranje u bazu
# id je automatski dodan

class Projection(models.Model):
    movie_name = models.CharField(max_length=50, null=True) #blank umisto nulla za forme
    time = models.CharField(max_length=50, null=True)
    room_capacity = models.IntegerField(default=0, null=True)

    #def __str__(self):
        #return '%s, %s, %s' % (self.movie_name, self.time, self.room_capacity)

class Ticket(models.Model):
    seat_number = models.IntegerField(default=0, null=True)
    movie_projection = models.ForeignKey(Projection, on_delete=models.SET_NULL, null=True) # koji se brise?
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '%s' % (self.seat_number)
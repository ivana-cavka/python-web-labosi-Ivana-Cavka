from django.forms import ModelForm
from .models import Projection, Ticket

class ProjectionForm(ModelForm):
    class Meta:
        model = Projection
        fields = ['movie_name', 'time', 'room_capacity']

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['seat_number', 'movie_projection', 'customer']
from lib2to3.pgen2.token import LESS
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Projection, Ticket
from django.contrib.auth.models import User

# Create your views here.
def welcome(request):
    return HttpResponse('<h1>Hi there!</h1>')

# s vracanjem templatea
def welcome_2(request):
    return render(request, "home.html", {"data": {"prvi", "drugi", "treci"}})

# def ticket_input(request):
    # tickets.html
    # punjenje baze priko neke forme?

def projection_input(request):
    p = Projection(movie_name="Doctor Strange", time="16:00", room_capacity=40)
    p.save()
    #za foreign key ic s get i filter
    return HttpResponse('<h1>Done!</h1>')

def ticket_input(request):
    t = Ticket(seat_number=21, movie_projection = Projection.objects.get(pk=1), customer = User.objects.get(pk=2))
    t.save()
    return HttpResponse('<h1>Done!</h1>')

def show_projections(request):
    projections = Projection.objects.all()
    tickets = Ticket.objects.all()
    seats_left = {}
    for proj in projections:
        seats_taken=Ticket.objects.filter(movie_projection_id=Projection.objects.get(id=proj.id)).count()
        seats_left[proj.id] = proj.room_capacity - seats_taken
    print("SEATS LEFT: ",seats_left)
    return render(request, "projections.html", {"projection_data":projections, "seat_data":seats_left})

def get_tickets_by_id(request, id):
    ticket = Ticket.objects.get(pk=id)
    projection = Projection.objects.get(pk=ticket.movie_projection_id)
    return render(request, 'tickets.html', {"ticket_data":ticket, "projection_data":projection})

def ticket_receipt(request, id):
    projection_requested = Projection.objects.get(pk=id)
    num_of_tickets = Ticket.objects.count()
    seats_taken=Ticket.objects.filter(movie_projection_id=Projection.objects.get(id=id)).count()
    seats_left = projection_requested.room_capacity - seats_taken
    if seats_left > 0 :
        ticket_bought = Ticket(seat_number=num_of_tickets + 1, movie_projection = Projection.objects.get(pk=id), customer = User.objects.get(pk=2))
        ticket_bought.save()
        flag = True
    else: 
        flag = False
    return render(request, 'ticket_receipt.html', {"is_bought":flag, "ticket_data":ticket_bought, "projection_data":projection_requested})

def delete_ticket_by_id(request, id):
    Ticket.objects.filter(id=id).delete()
    return redirect('projections')

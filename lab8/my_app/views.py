from lib2to3.pgen2.token import LESS
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import Projection, Ticket
from .forms import ProjectionForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
#def welcome(request):
    #return HttpResponse('<h1>Hi there!</h1>')

# s vracanjem templatea
#def welcome_2(request):
    #return render(request, "home.html", {"data": {"prvi", "drugi", "treci"}})

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
    seats_taken = {}
    for proj in projections:
        seats_taken[proj.id]=Ticket.objects.filter(movie_projection_id=Projection.objects.get(id=proj.id)).count()
        seats_left[proj.id] = proj.room_capacity - seats_taken[proj.id]
    return render(request, "projections.html", {"projection_data":projections, "seats_left":seats_left, "seats_taken":seats_taken})

@login_required
def get_ticket_by_id(request, id):
    ticket = Ticket.objects.get(pk=id)
    projection = Projection.objects.get(pk=ticket.movie_projection_id)
    return render(request, 'tickets.html', {"ticket_data":ticket, "projection_data":projection})

@login_required
def ticket_receipt(request, id):
    user_id = request.user.id
    projection_requested = Projection.objects.get(pk=id)
    num_of_tickets = Ticket.objects.count()
    seats_taken=Ticket.objects.filter(movie_projection_id=Projection.objects.get(id=id)).count()
    seats_left = projection_requested.room_capacity - seats_taken
    if seats_left > 0 :
        ticket_bought = Ticket(seat_number=num_of_tickets + 1, movie_projection = Projection.objects.get(pk=id), customer = User.objects.get(pk=user_id))
        ticket_bought.save()
        flag = True
    else: 
        flag = False
    return render(request, 'ticket_receipt.html', {"is_bought":flag, "ticket_data":ticket_bought, "projection_data":projection_requested})

@login_required
def delete_ticket_by_id(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.delete()
    return redirect('projections')

@staff_member_required
def add_projection(request):
    if request.method == 'GET':
        form = ProjectionForm()
        return render(request, 'add_projection.html', {"form" : form})
    elif request.method == 'POST':
        form = ProjectionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('projections')

@staff_member_required
def delete_projection(request, id):
    projection = Projection.objects.get(id=id)
    projection.delete()
    return redirect('projections')

@staff_member_required
def update_projection(request, id):
    projection = Projection.objects.get(id=id)
    if request.method == 'GET':
        data_to_update = ProjectionForm(instance=projection)
        return render(request, 'update_projection.html', {'form': data_to_update})
    elif request.method == 'POST':
        print(request.POST)
        data_to_update = ProjectionForm(request.POST, instance=projection)
        if data_to_update.is_valid():
            data_to_update.save()
            return redirect('projections')
    else:
        return HttpResponse("Something went wrong!")

def register(request):
    if request.method == 'GET':
        userForm = UserCreationForm()
        return render(request, 'register.html', {'form':userForm})
    elif request.method == 'POST':
        userForm = UserCreationForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            return redirect('login')
        else:
            return redirect('register')
    else:
        return HttpResponseNotAllowed('Not able to save!')

def get_tickets_by_projection(request, id):
    projection = Projection.objects.get(id=id)
    tickets = Ticket.objects.filter(movie_projection=projection)
    for ticket in tickets:
        print(ticket.customer.email)
    return render(request, 'tickets-by-projection.html', {"ticket_data":tickets, "projection_data":projection})

def get_tickets_by_user(request):
    id = request.user.id
    user = User.objects.get(id=id)
    tickets = Ticket.objects.filter(customer=user)
    print("ID: ",id,"  USER: ",user,"  TICKETS ", tickets)
    return render(request, 'tickets-by-user.html', {"ticket_data":tickets, "user_data":user})
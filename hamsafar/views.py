from django.shortcuts import render, redirect
from .models import Trip, User, CompanionRequest
from django.http import HttpResponse
# Create your views here.

def home_list(request):
    userhome = User.objects.all()
    triphome = Trip.objects.all()
    companionrequest = CompanionRequest.objects.all()
    return render(request, 'home_list.html', {'users':userhome, 'trips':triphome, 'companions':companionrequest})

def create_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        image = request.FILES.get('image')
        if username and email and password and image:
            User.objects.create(username = username, email = email, password = password, image = image)
            return redirect('home')
        return render(request, 'create_user_list.html')
    return render(request, 'create_user_list.html')

def create_trip(request):
    if request.method == "POST":
        start = request.POST.get('start_location')
        end = request.POST.get('end_location')
        date = request.POST.get('date')
        seats = request.POST.get('seats_available')
        description = request.POST.get('description')
        if start and end and date and seats and description:
            Trip.objects.create(start_location=start, end_location=end, date=date, seats_available=seats, description=description)
            return redirect('home')
        return render(request, 'create_trip_list.html', {'error': 'hamai malumothoro purra kuned'})
    return render(request, 'create_trip_list.html')


     
def create_companion(request):
    if request.method == "POST":
        start = request.POST.get('start_location')
        end = request.POST.get('end_location')
        date = request.POST.get('date')
        description = request.POST.get('description')
        if start and end and date and description:
            CompanionRequest.objects.create(start_location=start, end_location=end, date=date, description=description)
            return redirect('home')
        return render(request, 'create_companion_list.html', {'error': 'hamai malumothoro purra kuned'})
    return render(request, 'create_companion_list.html')
    
    
def update_user(request, id):
    users = User.objects.filter(id=id).first()
    if not users:
        return HttpResponse("user not found", status=404)
    if request.method == 'POST':
        users.username = request.POST.get('username')
        users.email = request.POST.get('email')
        users.password = request.POST.get('password')
        if request.FILES.get('image'):
            users.image = request.FILES.get('image')
        users.save()
        return redirect('home')
    return render(request, 'update_users.html', {'std': users})
       
def update_trip(request, id):
    trips = Trip.objects.filter(id=id).first()
    if not trips:
        return HttpResponse("trips not found", status=404)
    if request.method == "POST":
        trips.start_location = request.POST.get('start_location')
        trips.end_location = request.POST.get('end_location')
        trips.date = request.POST.get('date')
        trips.seats_available = request.POST.get('seats_available')
        trips.description = request.POST.get('description')
        trips.save()
        return redirect('home')
    return render(request, 'update_trips.html', {'std': trips})


def update_companion(request, id):
    companions = CompanionRequest.objects.filter(id = id).first()
    if not companions:
        return HttpResponse("trips not found", status=404)
    if request.method == "POST":
        companions.start_location = request.POST.get('start_location')
        companions.end_location = request.POST.get('end_location')
        companions.date = request.POST.get('date')
        companions.description = request.POST.get('description')
        companions.save()
        return redirect('home')
    return render(request, 'update_companions.html', {'std': companions})


def delete_user(request, id):
    users = User.objects.filter(id=id).first()
    if not users:
        return HttpResponse('user not found')
    users.delete()
    return redirect('home')

def delete_trip(request, id):
    trips = Trip.objects.filter(id=id).first()
    if not trips:
        return HttpResponse('trip not found')
    trips.delete()
    return redirect('home')

def delete_companion(request, id):
    companions = CompanionRequest.objects.filter(id=id).first()
    if not companions:
        return HttpResponse('companions not found')
    companions.delete()
    return redirect('home')


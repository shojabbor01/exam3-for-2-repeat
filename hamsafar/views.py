from django.shortcuts import render, redirect
from .models import Trip, User, CompanionRequest
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
    
    
    
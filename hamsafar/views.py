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
        create_at = request.POST.get('create_at')
        image = request.FILES.get('image')
        if username and email and password and create_at and image:
            User.objects.create(username = username, email = email, password = password, create_at = create_at, image = image)
            return redirect('home')
        return render(request, 'create_user_list.html')
    return render(request, 'create_user_list.html')


    

        

        
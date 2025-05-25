from django.shortcuts import render, redirect
from .models import Trip, User, CompanionRequest
# Create your views here.

def home_list(request):
    userhome = User.objects.all()
    triphome = Trip.objects.all()
    companionrequest = CompanionRequest.objects.all()
    return render(request, 'home_list.html', {'users':userhome}, {'trips':triphome}, {'companions':companionrequest})
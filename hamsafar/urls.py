from django.urls import path
from .views import home_list, create_trip, create_user

urlpatterns = [
    path('',home_list, name='home'),
    path('create_user/', create_user, name='createuser'),
    path('create_trip/', create_trip, name='createtrip'),
]

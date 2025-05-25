from django.urls import path
from .views import home_list, create_trip, create_user, create_companion, update_user, update_trip, update_companion, delete_companion, delete_user, delete_trip

urlpatterns = [
    path('',home_list, name='home'),
    path('create_user/', create_user, name='createuser'),
    path('create_trip/', create_trip, name='createtrip'),
    path('create_companion/', create_companion, name='createcompanion'),
    path('update_user/<int:id>/', update_user, name='updateuser'),
    path('update_trip/<int:id>/', update_trip, name='updatetrip'),
    path('update_companion/<int:id>/', update_companion, name='updatecompanion'),
    path('delete_companion/<int:id>/', delete_companion, name='deletecompanion'),
    path('delete_trip/<int:id>/', delete_trip, name='deletetrip'),
    path('delete_user/<int:id>/', delete_user, name='deleteuser'),

]

from django.contrib import admin
from .models import Trip, User, CompanionRequest
# Register your models here.

admin.site.register(Trip)
admin.site.register(User)
admin.site.register(CompanionRequest)

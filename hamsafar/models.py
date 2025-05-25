from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='user_photos', blank=True, null=True)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'users'
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
class Trip(models.Model):
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    date = models.DateTimeField()
    seats_available = models.IntegerField() 
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.start_location} → {self.end_location}"
    
    class Meta:
        db_table = 'trips'
        managed = True
        verbose_name = 'Trip'
        verbose_name_plural = 'Trips'
        
class CompanionRequest(models.Model):
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"dar justujui {self.start_location} → {self.end_location}"
    
    class Meta:
        db_table = 'companionrequest'
        managed = True
        verbose_name = 'Companionrequest'
        verbose_name_plural = 'CompanionRequests'

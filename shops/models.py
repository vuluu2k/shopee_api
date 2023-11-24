from django.db import models
from uuid import uuid4
from users.models import User
# Create your models here.

class Shop(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    name = models.TextField()
    thumbnail = models.ImageField(upload_to='uploads/images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

class Follower(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

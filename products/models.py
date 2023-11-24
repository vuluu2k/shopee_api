from django.db import models
from uuid import uuid4
from users.models import User

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4)
    thumbnails = models.TextField()
    price = models.FloatField(default=0)
    quantity_sold = models.IntegerField(default=0)
    attribute = models.JSONField()
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Variation(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4)
    thumbnail = models.TextField()
    price = models.FloatField(default=0)
    remain_quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Feedback(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    star = models.IntegerField(default=5)
    like = models.IntegerField(default=0)
    attachment = models.TextField(default="")
    message = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
from django.contrib import admin

# Register your models here.
from .models import Shop, Follower

admin.site.register(Shop)
admin.site.register(Follower)

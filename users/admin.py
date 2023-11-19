from django.contrib import admin
from .models import Profile, BankAccount, CreditCard
# Register your models here.

admin.site.register(Profile)
admin.site.register(BankAccount)
admin.site.register(CreditCard)
from django.contrib import admin
from .models import User, BankCard, CreditCard
# Register your models here.

admin.site.register(User)
admin.site.register(BankCard)
admin.site.register(CreditCard)
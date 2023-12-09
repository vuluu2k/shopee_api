from django.contrib import admin

# Register your models here.

from .models import Product, Variation, Feedback, Order, OrderDetail

admin.site.register(Product)
admin.site.register(Variation)
admin.site.register(Feedback)
admin.site.register(Order)
admin.site.register(OrderDetail)
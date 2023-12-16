from django.db import models
from users.models import User
from products.models import Product


class UserActivity(models.Model):
    ACTIVITY_TYPES = [
        ('search', 'Search'),
        ('product_click', 'Product Click'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    query = models.JSONField(max_length=255, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
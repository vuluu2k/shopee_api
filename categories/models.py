from django.db import models

# Create your models here.

class Main_category(models.Model):
    name = models.TextField(primary_key=True, default="")
    image = models.TextField(default="")

    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default="")
    parent = models.ForeignKey('self', on_delete=models.CASCADE,\
                                null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name
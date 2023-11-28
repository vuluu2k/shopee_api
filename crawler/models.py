from django.db import models
from uuid import uuid4

# Create your models here.


class Crawler(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.url

class Version(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    crawler = models.ForeignKey(Crawler, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.crawler.url + ' - ' + str(self.id) + ' - ' + str(self.created_at)
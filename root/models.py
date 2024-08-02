from django.db import models
from django.contrib.auth.models import User

class Services(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField(default="Test")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("created_at",)

# Create your models here.

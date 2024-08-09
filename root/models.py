from django.db import models
from django.contrib.auth.models import User

class Special_services(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField(default="description special services")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("created_at",)



class Services(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField(default="description services")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("created_at",)



class Attributes(models.Model):
    name = models.TextField(default="content attribute")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("created_at",)



class Pricings(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField(default="description pricing")
    fee = models.FloatField(default=3)
    attributes = models.ManyToManyField(Attributes)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("created_at",)



class Questions(models.Model):
    question = models.TextField(default="title question?")
    answer = models.TextField(default="answer question")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ("created_at",)



class Skills(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("created_at",)

class Trainer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="trainer",default="default.jpg")
    content = models.TextField(default="description trainer")
    skills = models.ManyToManyField(Skills)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ("created_at",)
# Create your models here.

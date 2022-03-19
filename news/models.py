from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)




class BlogNews(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    topic = models.CharField(max_length=255)
    datecreated = models.DateTimeField(auto_now=True)
    article = models.CharField(max_length=255)

class Complain(models.Model):
    username = models.CharField(max_length=300, null=True)
    topic = models.CharField(max_length=300)
    article = models.CharField(max_length=300)
    datecreated = models.DateTimeField(auto_now=True)
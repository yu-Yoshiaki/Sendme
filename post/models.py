from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=180)
    fruits = models.CharField(max_length=180,null=True)
    team = models.CharField(max_length=180)

from django.db import models

# Create your models here.

class Hello(models.Model):
    first_name = models.CharField(max_length=50)
from django.db import models

# Create your models here.
class Admin(models.Model):
    adminid = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=20)
    name = models.TextField()


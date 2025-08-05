from django.db import models

# Create your models here.
class Admin(models.Model):
    adminid = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=20)
    name = models.TextField()

class Lokasi(models.Model):
    lid = models.AutoField(primary_key=True)
    list_lokasi = models.CharField(max_length=255)

class Elemen1(models.Model):
    e1id = models.AutoField(primary_key=True)
    e1 = models.TextField()

class Elemen2(models.Model):
    e2id = models.AutoField(primary_key=True)
    e2 = models.TextField()

class Elemen3(models.Model):
    e3id = models.AutoField(primary_key=True)
    e3 = models.TextField()

class Elemen4(models.Model):
    e4id = models.AutoField(primary_key=True)
    e4 = models.TextField()
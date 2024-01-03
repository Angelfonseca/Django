from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20)
    curp = models.CharField(max_length=18)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

from django.db import models

class Sensor(models.Model):
    soilhumsens = models.DecimalField(max_digits=10, decimal_places=2)
    humsens = models.DecimalField(max_digits=10, decimal_places=2)
    temp = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Module(models.Model):
    Sensors = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


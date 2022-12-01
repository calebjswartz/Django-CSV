from django.db import models

# Create your models here.
class Biostats(models.Model):
    name = models.CharField(max_length=150)
    sex = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)



    def __str__(self):
        return self.name
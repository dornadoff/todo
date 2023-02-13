from django.db import models

class Todo(models.Model):
    nomi = models.CharField(max_length=100)
    sanasi = models.DateField()
    batafsil = models.CharField(max_length=500)
    holat = models.CharField(max_length=100)

from django.db import models
from django.contrib.auth.models import *

class Todo(models.Model):
    nomi = models.CharField(max_length=100)
    sanasi = models.DateField()
    batafsil = models.CharField(max_length=500)
    holat = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

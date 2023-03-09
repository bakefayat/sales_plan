from django.db import models

# Create your models here.


class Consumers(models.Model):
    name = models.CharField(max_length=150)
    family = models.CharField(max_length=150)
    number_of_members = models.IntegerField()

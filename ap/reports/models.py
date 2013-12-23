from django.db import models

# Create your models here.

class Trainee(models.Model):
    name = models.CharField(verbose_name="full name", max_length=50)
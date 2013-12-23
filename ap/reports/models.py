from django.db import models

# Create your models here.

class TraineeReport(models.Model):
    hc = models.BooleanField(default=False)
    name= models.CharField(verbose_name="Name", max_length=50)
    gender= models.CharField(verbose_name="G", max_length=1)
    term= models.CharField(verbose_name="TM", max_length=1)
    locality= models.CharField(verbose_name="Locality", max_length=50)
    team= models.CharField(verbose_name="Team", max_length=50)
    residence= models.CharField(verbose_name="Residence", max_length=50)
    bed= models.CharField(verbose_name="bed", max_length=50)
    v= models.BooleanField(verbose_name="V", default=False)
    cell= models.CharField(verbose_name="Cell P", max_length=50)
    TA= models.CharField(verbose_name="", max_length=50)


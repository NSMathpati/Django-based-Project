from django.db import models

# Create your models here.

class Inputf(models.Model):
    Name = models.CharField(max_length=200)
    time_log = models.TimeField()


class Reservation(models.Model):
    name = models.CharField("Name",max_length=250)
    contact = models.CharField("Phone Number", max_length=200)
    time = models.TimeField(auto_now=True)
    count = models.IntegerField()
    notes = models.CharField("Note", max_length=650)
    
    def __str__(self) -> str:
        return self.name


class Cuisine(models.Model):
    cusine = models.CharField(max_length=250)
    cusineid = models.IntegerField(primary_key=True,default=None)

    def __str__(self) -> str:
        return self.cusine

class Menu(models.Model):
    name = models.CharField(max_length=250)
    cusineid = models.ForeignKey(Cuisine, on_delete=models.PROTECT, default=None)
    price = models.IntegerField(null=False)
    description = models.CharField(max_length=750)
    
    def __str__(self) -> str:
        return self.name

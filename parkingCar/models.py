
from django.db import models
from django.utils import timezone 
# Create your models here.






#--------------------- Project Parking Car ---------------------


    
class Places(models.Model) :
    PlaceId = models.AutoField(primary_key=True)
    PlaceNumero = models.IntegerField()
    PlaceCodeQr = models.CharField(max_length=500, default="N/A")
    DateCreatePlace = models.DateField()
    DateEdit = models.DateField()
    Reserver = models.BooleanField(default=False)
    MatriculeCar = models.CharField(max_length=500, default="N/A")
    PhotoFileName = models.CharField(max_length=500, default="Anonymous.png")
    Time = models.DateTimeField(default=timezone.now) 
    
    
class History(models.Model):
    Id = models.AutoField(primary_key=True)
    NumeroPlace = models.IntegerField()
    PlaceCodeQr = models.CharField(max_length=500, default="N/A")
    MatriculeCar = models.CharField(max_length=500)
    DateCreate = models.DateField()
    TypeMouvement = models.CharField(max_length=500)
    Time = models.DateTimeField(default=timezone.now) 
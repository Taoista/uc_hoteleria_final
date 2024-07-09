from django.db import models
from eloquent import DatabaseManager
# Create your models here.

class Hoteles(models.Model):
    id_hotel = models.AutoField(db_column='id', primary_key=True) 
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    
    def _str_(self):
        return self.nombre



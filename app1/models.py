from django.db import models
from eloquent import DatabaseManager
# Create your models here.

class Hoteles(models.Model):
    id_hotel = models.AutoField(db_column='id', primary_key=True) 
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    
    def _str_(self):
        return self.nombre


class Habitaciones(models.Model):
    id_habitacion = models.AutoField(db_column='id', primary_key=True) 
    titulo = models.CharField(max_length=100)
    caracteristicas = models.CharField(max_length=500)
    precio = models.IntegerField();

    def _str_(self):
        return self.nombre

class ServiciosExtras(models.Model):
    id_serv_extras = models.AutoField(db_column='id', primary_key=True) 
    titulo = models.CharField(max_length=100)
    precio = models.IntegerField();

    def _str_(self):
        return self.nombre
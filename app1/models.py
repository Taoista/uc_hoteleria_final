from django.db import models
from eloquent import DatabaseManager
# Create your models here.

class Hoteles(models.Model):
    id_hotel = models.AutoField(db_column='id', primary_key=True) 
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    imagen = models.CharField(max_length=100)
    
    def _str_(self):
        return self.nombre


class Habitaciones(models.Model):
    id_habitacion = models.AutoField(db_column='id', primary_key=True) 
    titulo = models.CharField(max_length=100)
    caracteristicas = models.CharField(max_length=500)
    precio = models.IntegerField()
    imagen = models.CharField(max_length=100)


    def _str_(self):
        return self.nombre

class ServiciosExtras(models.Model):
    id_serv_extras = models.AutoField(db_column='id', primary_key=True) 
    titulo = models.CharField(max_length=100)
    precio = models.IntegerField()
    imagen = models.CharField(max_length=100)


class Reservas(models.Model):
    id_reserva = models.AutoField(db_column='id', primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.IntegerField()
    id_hotel = models.ForeignKey(Hoteles,on_delete=models.PROTECT, db_column='id_hotel')
    id_habitacion = models.ForeignKey(Habitaciones,on_delete=models.PROTECT, db_column='id_habitacion')
    f_inicio = models.DateField()
    f_termino = models.DateField()
    cantidad = models.IntegerField()
    total = models.IntegerField(default=0)

class ReservasServiciosExtras(models.Model):
    id_res_serv_extras =  models.AutoField(db_column='id', primary_key=True)
    id_reserva = models.ForeignKey(Reservas,on_delete=models.PROTECT, db_column='id_reserva')
    id_serivicio_extra = models.ForeignKey(ServiciosExtras,on_delete=models.PROTECT, db_column='id_servicio_extra')

class HotelHabitacion(models.Model):
    id_hot_hav = models.AutoField(db_column='id', primary_key=True)
    estado = models.BooleanField(default=False)
    id_hotel = models.ForeignKey(Hoteles,on_delete=models.PROTECT, db_column='id_hotel')
    id_habitacion = models.ForeignKey(Habitaciones,on_delete=models.PROTECT, db_column='id_habitacion')
    
   
    # def _str_(self):
    #     return self.nombre
    def __str__(self):
        return str(self.id_hotel)
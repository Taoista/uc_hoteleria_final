from django.contrib import admin
from .models import Hoteles, Habitaciones, ServiciosExtras

# Register your models here.

@admin.register(Hoteles)
class HotelAdmin(admin.ModelAdmin):
    # ? ver los campos editar los campos en el admin
    fields = ['nombre',
            'direccion']

    # ? verlos en el admin
    list_display = ['nombre', 'direccion']

@admin.register(Habitaciones)
class HabitacionesAdmin(admin.ModelAdmin):
    fields = ['titulo',
            'caracteristicas',
            'precio']

    list_display = ['titulo', 'caracteristicas', 'precio']

@admin.register(ServiciosExtras)
class ServiciosExtrasAdmin(admin.ModelAdmin):
    fields = ['titulo'
            'precio']

    list_display = ['titulo', 'precio']


# admin.site.register(Hoteles)
# admin.site.register(Habitaciones)
# admin.site.register(ServiciosExtras)
# admin.site.register(CantidadTipoHabitacion)
# admin.site.register(Servicios)
# admin.site.register(Habitacion)
# admin.site.register(ServicioExtra)
# admin.site.register(Reserva)
# admin.site.register(CentroEvento)
# admin.site.register(ArriendoEvento)





from django.contrib import admin
from .models import Hoteles, Habitaciones, ServiciosExtras,HotelHabitacion

# Register your models here.

@admin.register(Hoteles)
class HotelAdmin(admin.ModelAdmin):
    # ? ver los campos editar los campos en el admin
    fields = ['nombre',
            'direccion', 'imagen']

    # ? verlos en el admin
    list_display = ['nombre', 'direccion', 'imagen']

@admin.register(Habitaciones)
class HabitacionesAdmin(admin.ModelAdmin):
    fields = ['titulo',
            'caracteristicas',
            'precio', 'imagen']

    list_display = ['titulo', 'caracteristicas', 'precio', 'imagen']

@admin.register(ServiciosExtras)
class ServiciosExtrasAdmin(admin.ModelAdmin):
    fields = ['titulo',
            'precio', 'imagen']

    list_display = ['titulo', 'precio', 'imagen']

@admin.register(HotelHabitacion)
class HotelHabitacionAdmin(admin.ModelAdmin):
    fields = ['estado',
                'id_hotel',
                'id_habitacion'
                ]

    list_display = ['estado','id_hotel','id_habitacion']


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





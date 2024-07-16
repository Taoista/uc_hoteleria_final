from django.shortcuts import render
from django.http import HttpResponse
from .models import Hoteles, ServiciosExtras, HotelHabitacion
import json
import datetime
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def index(request):

    hoteles = Hoteles.objects.all()
    servicios = ServiciosExtras.objects.all()

    current_year = datetime.datetime.now().year

    context = {
        'hoteles': hoteles,
        'servicios': servicios,
        'current_year': current_year
    }

    return render(request, "inventario/index.html", context)

# ? ficha del hotel
def hotel(request, id_hotel):
    hoteles = Hoteles.objects.order_by('?')[:3]
    servicios = ServiciosExtras.objects.all()

    hotel_habitaciones = HotelHabitacion.objects.filter(id_hotel=id_hotel, estado=True).select_related('id_habitacion')

    data = Hoteles.objects.filter(id_hotel=id_hotel)

    titulo = data[0].nombre.upper()
    direccion = data[0].direccion


    context = {
        'id_hotel': id_hotel,
        'hoteles': hoteles,
        'servicios': servicios,
        'hotel_habitaciones': hotel_habitaciones,
        'titulo': titulo,
        'direccion':direccion
    }
    return render(request, "inventario/hotel.html", context)


def contacto(request):
    return render(request, "inventario/contacto.html")


def editar(request):
    context = {}
    return render(request, "editar/editar.html")

def crear(request):
    return render(request, "crear/crear.html")


def eliminar(request):
    return render(request, "eliminar/eliminar.html")
    


# def otros(request):
#     return render(request, "administrar/administrar.html")

# def ver(request):

#     hoteles = Hoteles.objects.prefetch_related('tipohabitacion_set', 'servicios_set').all()

#     context = {
#         'hoteles':hoteles
#     }

#     return render(request, "administrar/ver.html", context)

# def create(request):

#     tipo_habitacion = TipoHabitacion.objects.all()
#     servicios = Servicios.objects.all()

#     tipo_habitacion_json = json.dumps(list(tipo_habitacion.values()))

#     context = {
#         'tipo_habitacion': tipo_habitacion,
#         'servicios': servicios,  # Pasa tipo_habitaciones al contexto
#         'tipo_habitacion_json': tipo_habitacion_json
#     }

#     return render(request,"administrar/create.html", context)
from django.shortcuts import render
from django.http import HttpResponse
from .models import Hoteles
import json
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def index(request):

    hoteles = Hoteles.objects.all()


    context = {
        'hoteles': hoteles,
    }
    
    return render(request, "inventario/index.html", context)


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
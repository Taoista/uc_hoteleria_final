from django.shortcuts import render, redirect  # Para renderizar vistas y redirigir
from django.http import HttpResponse, QueryDict  # Para manejar respuestas HTTP y trabajar con QueryDict
from .models import Hoteles, ServiciosExtras, HotelHabitacion, Habitaciones, Reservas  # Modelos de tu aplicación
import json  # Para manejar datos en formato JSON
from datetime import date, datetime  # Para trabajar con fechas y horas
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
# ? controlador de fecha desde JS
def parse_date(date_str):
    # Dividir la cadena de entrada por '-'
    parts = date_str.split('-')
    
    # Extraer el día, mes y año
    day = int(parts[0])
    month = int(parts[1])
    year = int(parts[2])
    
    # Retornar la lista en el formato deseado
    return [year, month, day]


def index(request):

    hoteles = Hoteles.objects.all()
    servicios = ServiciosExtras.objects.all()

    current_year = date.today().year

    context = {
        'hoteles': hoteles,
        'servicios': servicios,
        'current_year': current_year
    }

    return render(request, "inventario/index.html", context)

# ? ficha del hotel
def hotel(request, id_hotel):
    # ? elementos de 3 para mostrar random
    hoteles = Hoteles.objects.order_by('?')[:3]
    # ? servicios para mostrar
    servicios = ServiciosExtras.objects.all()

    #? habitaciones para mostrar segun id ingresado
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
    
def reservar(request):
    id_hotel = request.POST.get('id_hotel')
    id_habitacion = request.POST.get('id_habitacion')
    f_inicio = request.POST.get('f_inicio')
    f_termino = request.POST.get('f_termino')
    cantidad = request.POST.get('cantidad')

    hotel = Hoteles.objects.filter(id_hotel=id_hotel)
    habitacion = Habitaciones.objects.filter(id_habitacion=id_habitacion)
    
    imagen_habitacion = habitacion[0].imagen
    nombre_hotel = hotel[0].nombre.upper()
    nombre_habitacion = habitacion[0].titulo.upper()

    precio = habitacion[0].precio

    context = {
        'id_hotel': id_hotel,
        'id_habitacion': id_habitacion,
        'f_inicio' :f_inicio,
        'f_termino': f_termino, 
        'cantidad': cantidad,
        'imagen_habitacion': imagen_habitacion,
        'nombre_hotel': nombre_hotel,
        'nombre_habitacion': nombre_habitacion,
        'precio': precio
    }


    return render(request, "inventario/reservation.html", context)

def checkout(request):
    id_hotel = request.POST.get('id_hotel')
    id_habitacion = request.POST.get('id_habitacion')
    f_inicio = request.POST.get('f_inicio')
    f_termino = request.POST.get('f_termino')
    cantidad = request.POST.get('cantidad')

    hotel = Hoteles.objects.filter(id_hotel=id_hotel)
    habitacion = Habitaciones.objects.filter(id_habitacion=id_habitacion)

    imagen_habitacion = habitacion[0].imagen
    nombre_hotel = hotel[0].nombre.upper()
    nombre_habitacion = habitacion[0].titulo.upper()

    precio = habitacion[0].precio

    context = {
        'id_hotel': id_hotel,
        'id_habitacion': id_habitacion,
        'f_inicio' :f_inicio,
        'f_termino': f_termino, 
        'cantidad': cantidad,
        'imagen_habitacion': imagen_habitacion,
        'nombre_hotel': nombre_hotel,
        'nombre_habitacion': nombre_habitacion,
        'precio': precio
    }


    return render(request, "inventario/checkout.html", context)


def create_reservacion(request):
    if request.method == 'POST':
        id_hotel = request.POST.get('id_hotel')
        id_habitacion = request.POST.get('id_habitacion')
        f_inicio = request.POST.get('f_inicio')
        f_termino = request.POST.get('f_termino')
        cantidad = request.POST.get('cantidad')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        
        # ?
        nueva_reserva = Reservas(
            nombre=nombre.lower(),
            apellido=apellido.lower(),
            email=correo.lower(),
            telefono=telefono,  # Asegúrate de que el número de teléfono sea un número entero
            id_hotel=Hoteles.objects.get(pk=id_hotel),  # Asegúrate de obtener la instancia de Hoteles correcta
            id_habitacion=Habitaciones.objects.get(pk=id_habitacion),  # Asegúrate de obtener la instancia de Habitaciones correcta
            f_inicio=date(parse_date(f_inicio)[0], parse_date(f_inicio)[1], parse_date(f_inicio)[2]),  # Fecha de inicio
            f_termino=date(parse_date(f_termino)[0], parse_date(f_termino)[1], parse_date(f_termino)[2]),  # Fecha de término
            cantidad=cantidad  # Cantidad de huéspedes
        )
        # Guardar la reserva en la base de datos
        nueva_reserva.save()
        # ? borrar los datos post

        id_registro = nueva_reserva.id_reserva
    
        fecha_actual =  datetime.now().strftime("%d-%m-%Y")

        hotel = Hoteles.objects.filter(id_hotel=id_hotel)
        habitacion = Habitaciones.objects.filter(id_habitacion=id_habitacion)

        imagen_habitacion = habitacion[0].imagen
        nombre_hotel = hotel[0].nombre.upper()
        nombre_habitacion = habitacion[0].titulo.upper()

        precio = habitacion[0].precio
        # ? limpio los datos post
        request.POST = QueryDict()


        context = {
            'id_hotel': id_hotel,
            'id_habitacion': id_habitacion,
            'f_inicio' :f_inicio,
            'f_termino': f_termino, 
            'cantidad': cantidad,
            'nombre': nombre,
            'apellido': apellido,
            'correo': correo,
            'telefono': telefono,
            'id_registro': id_registro,
            'fecha_actual': fecha_actual,
            'imagen_habitacion': imagen_habitacion,
            'nombre_hotel': nombre_hotel,
            'nombre_habitacion': nombre_habitacion,
            'precio': precio
        }


        # return render(request, "inventario/reservacion-success.html", context)
        return redirect('success_reserva', id_reserva=id_registro)
    else:
        return render(request, "inventario/index.html")


def success_reserva(request, id_reserva):

    reservas  = Reservas.objects.select_related('id_habitacion', 'id_hotel').filter(id_reserva=id_reserva).first()

    habitacion = reservas.id_habitacion
    hotel = reservas.id_hotel

    nombre = reservas.nombre
    apellido = reservas.apellido
    email = reservas.email
    telefono = reservas.telefono
    f_inicio = reservas.f_inicio
    f_termino = reservas.f_termino
    cantidad = reservas.cantidad,
    precio = habitacion.precio
    imagen_habitacion = habitacion.imagen
    nombre_habitacion = habitacion.titulo
    nombre_hotel = hotel.nombre
    # cantidad = reservas[0].cantidad

    fecha_actual =  datetime.now().strftime("%d-%m-%Y")



    context = {
        'nombre' : nombre,
        'apellido' : apellido,
        'correo' : email,
        'telefono' : telefono,
        'f_inicio' : f_inicio,
        'f_termino' : f_termino,
        'id_registro' :id_reserva,
        'fecha_actual' : fecha_actual,
        'cantidad' : cantidad,
        'precio': precio,
        'imagen_habitacion': imagen_habitacion,
        'nombre_habitacion': nombre_habitacion,
        'nombre_hotel': nombre_hotel

        
    }

    return render(request, "inventario/reservacion-success.html", context)

def contacto():
    return HttpResponse("soy el contacto")


def login_intranet(request):

    return render(request, "intranet/login_intranet.html")


def intranet(request):

    reservas  = Reservas.objects.select_related('id_habitacion', 'id_hotel')

    
    context = {
        'reservas' : reservas,
    }

    return render(request, "intranet/intranet.html", context)
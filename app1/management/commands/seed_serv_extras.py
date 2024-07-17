from django.core.management.base import BaseCommand
from app1.models import ServiciosExtras

class Command(BaseCommand):
    help = 'Crea 5 registros de servicios extras'

    def handle(self, *args, **kwargs):
        # Crear una lista de datos para los hoteles
        servicios_datos = [
            {'titulo': 'piscina','precio':5000, 'imagen' : 'assets/images/services-2.jpg'},
            {'titulo': 'gimnasio','precio':7000, 'imagen' : 'assets/images/services-2.jpg'},
            {'titulo': 'jacuzzi','precio':8000, 'imagen' : 'assets/images/services-2.jpg'},
        ]
        
        # Iterar sobre los datos y crear registros en la base de datos
        for data in servicios_datos:
            ServiciosExtras.objects.create(**data)
        
        self.stdout.write(self.style.SUCCESS('5 registros creados servicios extras'))


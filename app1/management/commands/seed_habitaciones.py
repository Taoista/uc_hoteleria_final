from django.core.management.base import BaseCommand
from app1.models import Habitaciones

class Command(BaseCommand):
    help = 'Crea 5 registros de habitaciones'

    def handle(self, *args, **kwargs):
        # Crear una lista de datos para los hoteles
        habitaciones_data = [
            {'titulo': 'habitacion 1', 'caracteristicas':'carac 1', 'precio':5000, 'imagen': 'assets/images/room-1.jpg'},
            {'titulo': 'habitacion 2', 'caracteristicas':'carac 2', 'precio':7000, 'imagen': 'assets/images/room-1.jpg'},
            {'titulo': 'habitacion 3', 'caracteristicas':'carac 3, carac 2', 'precio':8500, 'imagen': 'assets/images/room-1.jpg'},
           
        ]
        
        # Iterar sobre los datos y crear registros en la base de datos
        for data in habitaciones_data:
            Habitaciones.objects.create(**data)
        
        self.stdout.write(self.style.SUCCESS('5 registros creados'))


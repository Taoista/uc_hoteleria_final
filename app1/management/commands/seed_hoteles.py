from django.core.management.base import BaseCommand
from app1.models import Hoteles  # Asegúrate de importar tu modelo desde el archivo correcto

class Command(BaseCommand):
    help = 'Crea 5 registros de hoteles en la base de datos'

    def handle(self, *args, **kwargs):
        # Crear una lista de datos para los hoteles
        hoteles_data = [
            {'nombre': 'Hotel Santiago', 'direccion': 'Calle Falsa 123', 'imagen':'https://i.ibb.co/wJ8ZddN/f1.jpg'},
            {'nombre': 'Hotel Vina del mar', 'direccion': 'Avenida Siempre Viva 742', 'imagen':'https://i.ibb.co/B2r8Drm/hotel1.jpg'},
            # {'nombre': 'Hotel Europa', 'direccion': 'Gran Vía 15', 'imagen':'https://i.ibb.co/wJ8ZddN/f1.jpg'},
            # {'nombre': 'Hotel Sol', 'direccion': 'Avenida del Sol 10', 'imagen':'assets/images/hotel_1.jpg'},
            # {'nombre': 'Hotel Mar', 'direccion': 'Playa del Carmen 25', 'imagen':'assets/images/hotel_1.jpg'},
        ]
        
        # Iterar sobre los datos y crear registros en la base de datos
        for data in hoteles_data:
            Hoteles.objects.create(**data)
        
        self.stdout.write(self.style.SUCCESS('5 registros de hoteles se han creado exitosamente.'))


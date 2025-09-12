from django.core.management.base import BaseCommand
from faker import Faker
import random
from workshop.models import Cliente, Vehiculo, Servicio, OrdenReparacion

faker = Faker()

class Command(BaseCommand):
    help = "Seed workshop data"

    def handle(self, *args, **kwargs):
        # Crear clientes y vehículos
        for _ in range(5):
            cliente = Cliente.objects.create(
                nombre=faker.first_name(),
                apellido=faker.last_name(),
                telefono=faker.phone_number(),
                email=faker.email()
            )
            Vehiculo.objects.create(
                patente=faker.license_plate(),
                marca=faker.company(),
                modelo=faker.word(),
                anio=random.randint(2000, 2023),
                cliente=cliente
            )

        # Crear servicios
        servicios = [
            Servicio.objects.get_or_create(nombre="Cambio aceite", precio=20000)[0],
            Servicio.objects.get_or_create(nombre="Frenos", precio=45000)[0],
            Servicio.objects.get_or_create(nombre="Scanner", precio=15000)[0],
        ]
        # Crear ordenes
        for vehiculo in Vehiculo.objects.all():
            orden = OrdenReparacion.objects.create(
                vehiculo=vehiculo,
                estado=random.choice(["ingresado", "en_progreso", "finalizado"])
            )
            orden.servicios.add(random.choice(servicios))
            orden.calcular_monto_total()

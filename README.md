
Proyecto Django para gestionar clientes, vehículos, servicios y órdenes de reparación en un taller automotriz.

[![Python](https://img.shields.io/badge/Python-3.13+-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0+-green)](https://www.djangoproject.com/)
[![Faker](https://img.shields.io/badge/Faker-28.0+-yellow)](https://faker.readthedocs.io/)


## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/Dylan-af/Taller_automotriz.git
cd taller_automotriz

    Crear entorno virtual:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

    Instalar dependencias:

pip install -r requirements.txt

    Aplicar migraciones:

python manage.py makemigrations
python manage.py migrate

Generar datos de prueba
Manual (shell)

python manage.py shell

Luego copia los comandos de shell_tests.txt para crear:

    2 clientes (cada uno con un vehículo)

    3 servicios

    2 órdenes de reparación

Automático (Faker)

python manage.py seed_workshop

Esto generará datos aleatorios coherentes para clientes, vehículos, servicios y órdenes.
Consultas ORM 

# Vehículos de un cliente
Cliente.objects.get(nombre="Juan").vehiculos.all()

# Órdenes de un vehículo
Vehiculo.objects.get(patente="ABC123").ordenes.all()

# Servicios asociados a una orden
OrdenReparacion.objects.get(id=1).servicios.all()

# Órdenes en progreso
OrdenReparacion.objects.filter(estado="en_progreso")

# Órdenes sin fecha_salida
OrdenReparacion.objects.filter(fecha_salida__isnull=True)

Notas finales

.gitignore asegura que no se suban archivos temporales ni la base de datos local.

    shell_tests.txt contiene evidencia de la creación de registros y consultas ORM.

    Proyecto reproducible en cualquier máquina con Python 3.13+ y Django 5+.

from django.db import models

# Create your models here.

class Cliente (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Vehiculo (models.Model):
    patente = models.CharField(max_length=100, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.PositiveIntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="vehiculos")
    
    def __str__(self):
        return f"{self.patente} - {self.marca} {self.modelo} {self.anio}"

class Servicio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class OrdenReparacion(models.Model):
    ESTADOS = [
        ('ingresado', 'Ingresado'),
        ('en_progreso', 'En Progreso'),
        ('finalizado', 'Finalizado'),
    ]

    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name="ordenes")
    servicios = models.ManyToManyField(Servicio, related_name="ordenes")
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='ingresado')
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calcular_monto_total(self):
        total = sum(servicio.precio for servicio in self.servicios.all())
        self.monto_total = total
        self.save()

    def __str__(self):
        return f"Orden #{self.id} - {self.vehiculo.patente} ({self.estado})"

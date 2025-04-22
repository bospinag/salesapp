from django.db import models

from django.db import models

class Order(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    direccion_raw = models.TextField()
    direccion_formateada = models.TextField(blank=True)
    pago_en_casa = models.BooleanField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"# Create your models here.

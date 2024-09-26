from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombres= models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    numero_identificacion=models.CharField(max_length=15)
    numero_contacto=models.CharField(max_length=15)
    direccion=models.CharField(max_length=50)

    def __str__(self):

        return self.nombres
    

class Productos(models.Model):
    nombre=models.CharField(max_length=50)
    unidades=models.IntegerField()

    def __str__(self):
        return {self.nombre},{self.unidades}


class Ventas(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta de {self.cantidad} x {self.producto.nombre} a {self.cliente.nombre} el {self.fecha_venta} por {self.total}"
   
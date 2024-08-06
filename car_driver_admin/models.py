from django.db import models

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    year = models.IntegerField()

class Chofer(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField()
    vehiculo = models.OneToOneField('Vehiculo', on_delete=models.CASCADE, related_name='chofer')

class Registro_Contabilidad(models.Model):
    fecha_compra = models.DateField()
    valor = models.FloatField()
    vehiculo = models.OneToOneField('Vehiculo', on_delete=models.CASCADE, related_name='reg_cont')



















# # PSQL
# CREATE TABLE myapp_person (
#     "id" serial NOT NULL PRIMARY KEY,
#     "first_name" varchar(30) NOT NULL,
#     "last_name" varchar(30) NOT NULL
# );

# # python
# from django.db import models

# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
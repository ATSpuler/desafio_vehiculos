from models import *
from django.core.exceptions import ValidationError

def crear_vehiculo(patente, marca, modelo, year):
    if len(patente)!= 6:
        raise ValidationError("Patente debe tener 6 caracteres")
    if len(marca) > 20 or len(modelo) > 20:
        raise ValidationError("Marca y modelo deben tener max 20 caracteres")
    if not isinstance(year, int):
        raise ValidationError("Año debe ser un entero")

    vehiculo = Vehiculo(patente=patente, marca=marca, modelo=modelo, year=year)
    vehiculo.save()
    return vehiculo


def crear_chofer(rut, nombre, apellido, activo=False, creacion_registro=None, vehiculo_id=None):
    if len(rut)!= 9:
        raise ValidationError("Rut debe tener 9 caracteres")
    if len(nombre) > 50 or len(apellido) > 50:
        raise ValidationError("Nombre y apellido deben tener max 50 caracteres")
    if not isinstance(activo, bool):
        raise ValidationError("Activo debe ser un booleano")
    if creacion_registro and not isinstance(creacion_registro, date):
        raise ValidationError("Creacion registro debe ser una fecha")
    if vehiculo_id and (len(vehiculo_id)!= 6 or not Vehiculo.objects.filter(patente=vehiculo_id).exists()):
        raise ValidationError("Vehiculo id debe ser un string de 6 caracteres y existir en la base de datos")

    chofer = Chofer(rut=rut, nombre=nombre, apellido=apellido, activo=activo, creacion_registro=creacion_registro)
    if vehiculo_id:
        chofer.vehiculo = Vehiculo.objects.get(patente=vehiculo_id)
    chofer.save()
    return chofer


def crear_registro_contable(fecha_compra, valor, vehiculo_id):
    if not isinstance(fecha_compra, date):
        raise ValidationError("Fecha de compra debe ser una fecha")
    if not isinstance(valor, (int, float)):
        raise ValidationError("Valor debe ser un número")
    if len(vehiculo_id)!= 6 or not Vehiculo.objects.filter(patente=vehiculo_id).exists():
        raise ValidationError("Vehiculo id debe ser un string de 6 caracteres y existir en la base de datos")

    reg_cont = RegCont(fecha_compra=fecha_compra, valor=valor, vehiculo_id=vehiculo_id)
    reg_cont.vehiculo = Vehiculo.objects.get(patente=vehiculo_id)
    reg_cont.save()
    return reg_cont


def deshabilitar_chofer(rut):
    if len(rut)!= 9:
        raise ValidationError("Rut debe tener 9 caracteres")
    try:
        chofer = Chofer.objects.get(rut=rut)
    except Chofer.DoesNotExist:
        raise ValidationError("Chofer no encontrado")

    chofer.activo = False
    chofer.save()
    return chofer

def deshabilitar_vehiculo(patente):
    if len(patente)!= 6:
        raise ValidationError("Patente debe tener 6 caracteres")
    try:
        vehiculo = Vehiculo.objects.get(patente=patente)
    except Vehiculo.DoesNotExist:
        raise ValidationError("Vehiculo no encontrado")

    # Override the save method to raise an exception
    def save(self, *args, **kwargs):
        raise ValidationError("Vehiculo deshabilitado")

    vehiculo.save = save.__get__(vehiculo, type(vehiculo))
    return vehiculo

def habilitar_chofer(rut):
    if len(rut)!= 9:
        raise ValidationError("Rut debe tener 9 caracteres")
    try:
        chofer = Chofer.objects.get(rut=rut)
    except Chofer.DoesNotExist:
        raise ValidationError("Chofer no encontrado")

    chofer.activo = True
    chofer.save()
    return chofer


def habilitar_vehiculo(patente):
    if len(patente)!= 6:
        raise ValidationError("Patente debe tener 6 caracteres")
    try:
        vehiculo = Vehiculo.objects.get(patente=patente)
    except Vehiculo.DoesNotExist:
        raise ValidationError("Vehiculo no encontrado")

    vehiculo.activo = True
    vehiculo.save()
    return vehiculo



def obtener_vehiculo(patente):
    if len(patente)!= 6:
        raise ValidationError("Patente debe tener 6 caracteres")
    try:
        vehiculo = Vehiculo.objects.get(patente=patente)
    except Vehiculo.DoesNotExist:
        raise ValidationError("Vehiculo no encontrado")

    return vehiculo

# def obtener_vehiculo(patente):
#     if len(patente)!= 6:
#         raise ValidationError("Patente debe tener 6 caracteres")
#     try:
#         return Vehiculo.objects.get(patente=patente)
#     except Vehiculo.DoesNotExist:
#         return None

def obtener_chofer(rut):
    if len(rut)!= 9:
        raise ValidationError("Rut debe tener 9 caracteres")
    try:
        chofer = Chofer.objects.get(rut=rut)
    except Chofer.DoesNotExist:
        raise ValidationError("Chofer no encontrado")

    return chofer

# def obtener_chofer(rut):
#     if len(rut)!= 9:
#         raise ValidationError("Rut debe tener 9 caracteres")
#     try:
#         return Chofer.objects.get(rut=rut)
#     except Chofer.DoesNotExist:
#         return None


def asignar_chofer_a_vehiculo(rut, patente):
    if len(rut)!= 9:
        raise ValidationError("Rut debe tener 9 caracteres")
    if len(patente)!= 6:
        raise ValidationError("Patente debe tener 6 caracteres")
    try:
        chofer = Chofer.objects.get(rut=rut)
    except Chofer.DoesNotExist:
        raise ValidationError("Chofer no encontrado")
    try:
        vehiculo = Vehiculo.objects.get(patente=patente)
    except Vehiculo.DoesNotExist:
        raise ValidationError("Vehiculo no encontrado")

    chofer.vehiculo = vehiculo
    chofer.save()
    return chofer

# def asignar_chofer_a_vehiculo(rut, patente):
#     if len(rut)!= 9:
#         raise ValidationError("Rut debe tener 9 caracteres")
#     if len(patente)!= 6:
#         raise ValidationError("Patente debe tener 6 caracteres")
#     try:
#         chofer = Chofer.objects.get(rut=rut)
#     except Chofer.DoesNotExist:
#         return None
#     try:
#         vehiculo = Vehiculo.objects.get(patente=patente)
#     except Vehiculo.DoesNotExist:
#         return None

#     chofer.vehiculo = vehiculo
#     chofer.save()
#     return chofer

def imprimir_datos_vehiculos():
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        print(f"Patente: {vehiculo.patente}")
        print(f"Marca: {vehiculo.marca}")
        print(f"Modelo: {vehiculo.modelo}")
        print(f"Año: {vehiculo.year}")
        print("------------------------")
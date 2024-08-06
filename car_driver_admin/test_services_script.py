from models import *
from services import *

# Create vehiculos
print("Creating vehiculos...")
vehiculo1 = crear_vehiculo("ABC123", "Toyota", "Corolla", 2015)
vehiculo2 = crear_vehiculo("DEF456", "Honda", "Civic", 2018)

# Create choferes
print("Creating choferes...")
chofer1 = crear_chofer("12345678-9", "Juan", "Perez", True)
chofer2 = crear_chofer("98765432-1", "Maria", "Gonzalez", True)

# Asignar chofer a vehiculo
print("Asignando chofer a vehiculo...")
asignar_chofer_a_vehiculo("12345678-9", "ABC123")

# Imprimir datos vehiculos
print("Imprimiendo datos vehiculos...")
imprimir_datos_vehiculos()

# Obtener vehiculo
print("Obteniendo vehiculo...")
vehiculo = obtener_vehiculo("ABC123")
print(vehiculo)

# Obtener chofer
print("Obteniendo chofer...")
chofer = obtener_chofer("12345678-9")
print(chofer)

# Deshabilitar chofer
print("Deshabilitando chofer...")
deshabilitar_chofer("12345678-9")

# Habilitar chofer
print("Habilitando chofer...")
habilitar_chofer("12345678-9")

# Deshabilitar vehiculo
print("Deshabilitando vehiculo...")
deshabilitar_vehiculo("ABC123")

# Habilitar vehiculo
print("Habilitando vehiculo...")
habilitar_vehiculo("ABC123")

# Crear registro contable
print("Creando registro contable...")
registro_contable = crear_registro_contable("2022-01-01", 1000.0, "ABC123")
CREATE TABLE Vehiculo_tb (
  patente CHAR(6) PRIMARY KEY,
  marca CHAR(20) NOT NULL,
  modelo CHAR(20) NOT NULL,
  year INT NOT NULL
);

CREATE TABLE Chofer_tb (
  rut CHAR(10) PRIMARY KEY,
  nombre CHAR(50) NOT NULL,
  apellido CHAR(50) NOT NULL,
  activo BOOLEAN DEFAULT FALSE,
  creacion_registro DATE,
  vehiculo_id CHAR(6) UNIQUE,
  FOREIGN KEY (vehiculo_id) REFERENCES Vehiculo_tb(patente)
);

CREATE TABLE Registro_Contabilidad_tb (
  id INTEGER PRIMARY KEY,
  fecha_compra DATE NOT NULL,
  valor FLOAT NOT NULL,
  vehiculo_id CHAR(6) NOT NULL UNIQUE,
  FOREIGN KEY (vehiculo_id) REFERENCES Vehiculo_tb(patente)
);


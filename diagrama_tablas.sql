Vehiculo_tb

PK	patente char(6)
	marca char(20) not null
	modelo char(20) not null
	year int not null


Chofer_tb

PK	rut char(9)
	nombre char(50) not null
	apellido char(50) not null
	activo bool default False
	creacion_registro date	

FK	vehiculo_id char(6) unique

 

Reg_Cont_tb

PK	id integer autonumic
	fecha_compra date not null
	valor float not null

FK	vehiculo_id char(6) not null unique
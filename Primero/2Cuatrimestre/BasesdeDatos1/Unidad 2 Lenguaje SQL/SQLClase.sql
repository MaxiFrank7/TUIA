CREATE DATABASE P2_EJ1

USE P2_EJ1

CREATE TABLE EMPLEADO
(Legajo VARCHAR(10),
 Nombre VARCHAR(80),
 Domicilio VARCHAR(100),
 Telefono VARCHAR(15),
 Sector VARCHAR(40),
 Sueldo MONEY

 CONSTRAINT PK_Legajo PRIMARY KEY (Legajo), -- Clave primaria 
 CONSTRAINT UK_Telefono UNIQUE (Telefono), -- Clave unica


);

CREATE TABLE SERVICIO_TECNICO(






);
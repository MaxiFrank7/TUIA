CREATE DATABASE empresa_basica;
USE empresa_basica

 CREATE TABLE DIRECTOR (
  directorid int IDENTITY PRIMARY KEY NOT NULL,
  dni int NOT NULL, 
  nombre varchar(30),
  apellido1 varchar(30),
  apellido2 varchar(30),
  direccion varchar(50),
  fecha_designacion date,
  sueldo int
);

INSERT INTO DIRECTOR VALUES (33193456, 'Romina','Alvarez','Provenzano', 'Tratado del Pilar 4356','1981-06-19', 300000),
                            (31282582, 'Federico','Alloati','', 'Estivariz 987','1981-06-19',300000),
                            (30830001, 'Lucia', 'Alika','Montez', 'Suipacha 578','1981-06-19', 300000);

  CREATE TABLE DPTO (
  dptoid int IDENTITY PRIMARY KEY  NOT NULL, 
  nombre varchar(30),
  directorid int,
  FOREIGN KEY (directorid) REFERENCES DIRECTOR(directorid)
);

INSERT INTO DPTO VALUES ('Sede Central',1),
                        ('Administracion', 2),
                        ('Investigacion', 3);

CREATE TABLE PROYECTO (
  proyectoid int IDENTITY PRIMARY KEY NOT NULL,
  nombre varchar(30),
  dptoid int,
  FOREIGN KEY (dptoid) REFERENCES DPTO(dptoid)
);


INSERT INTO PROYECTO VALUES ('ProductoX', 3),
                            ('ProductoY', 3),
                            ('ProductoZ',3 ),
                            ('Computacion', 2),
                            ('Reorganizacion', 2),
                            ('Comunicaciones',2);

SELECT * FROM PROYECTO

  CREATE TABLE EMPLEADO (
  empleadoid int IDENTITY PRIMARY KEY NOT NULL,
  dni int NOT NULL,
  nombre varchar(30),
  apellido1 varchar(30),
  apellido2 varchar(30),
  fechanac date,
  direccion varchar(50),
  sueldo int,
  dptoid int,
  FOREIGN KEY (dptoid) REFERENCES DPTO(dptoid)
);

INSERT INTO EMPLEADO VALUES (333445555,'Jose', 'Perez','','1965-09-01', 'Eloy 198', 200000, 1),
                            (388665555, 'Alberto', 'Campos', 'Sastre', '1995-12-08', 'Avda. Ramos 9098',200000, 2),
                            (333445555,'Aurora', 'Oliva', 'Avezuela', '1982-07-31', 'Antonio Savedra 632', 200000, 3),
                            (333445555,'Fernanda', 'Ojeda', '', '1962-09-15', 'Portillo 1234', 150000, 3),
                            (350094421, 'Eduardo', 'Ochoa', 'Paredes', '1937-11-10', 'Las Peñas 1934', 200000, 1),
                            (318665555, 'Juana', 'Sainz', 'Oreja', '1941-06-20', 'Cerquillo 67', 200000, 2),
                            (357654321, 'Luis', 'Pajares', 'Morera', '1969-03-29', 'Av. Enebros 90',  250000, 1),
                            (397654321, 'Alicia', 'Jimenez', 'Celaya', '1968-05-12', 'Gran Via 3800',  200000, 3);

CREATE TABLE PROYECTO_EMPLEADO (
  PRIMARY KEY (empleadoid, proyectoid),
  empleadoid int,
  proyectoid int ,
  rol varchar(30),
  horas float,
  FOREIGN KEY (empleadoid) REFERENCES EMPLEADO(empleadoid),
  FOREIGN KEY (proyectoid) REFERENCES PROYECTO(proyectoid)
);

INSERT INTO PROYECTO_EMPLEADO VALUES (2,1,'colaborador',5.5),
                                     (8,1,'organizador',6),
                                     (2,2,'organizador',3),
                                     (2,4,'instructor',2.5),
                                     (6,5,'colaborador',2);

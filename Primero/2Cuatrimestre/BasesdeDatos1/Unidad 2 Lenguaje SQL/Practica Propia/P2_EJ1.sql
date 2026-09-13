CREATE DATABASE PRACTICA2
GO

USE P2_EJ1
GO

CREATE TABLE EMPLEADO 
(Legajo VARCHAR(20), 
Nombre VARCHAR(80),
Domicilio VARCHAR(100),
Telefono VARCHAR(20),
Sector VARCHAR(80),
Sueldo MONEY
);
GO

CREATE TABLE SERVICIO_TECNICO
(serviciotecnicoid INT IDENTITY(1,1),
nombre VARCHAR(80) NOT NULL,
telefono VARCHAR(20),
direccion VARCHAR(100) NOT NULL
CONSTRAINT PK_SERVICIO_TECNICO_id PRIMARY KEY (serviciotecnicoid), -- Clave primaria 
);
GO

ALTER TABLE EMPLEADO ALTER COLUMN Legajo VARCHAR(20) NOT NULL
ALTER TABLE EMPLEADO ALTER COLUMN Nombre VARCHAR(80) NOT NULL
ALTER TABLE EMPLEADO ALTER COLUMN Domicilio VARCHAR(100) NOT NULL
GO
ALTER TABLE EMPLEADO ADD CONSTRAINT PK_EMPLEADO_Legajo PRIMARY KEY(Legajo)
GO

INSERT INTO EMPLEADO (Legajo, Nombre, Domicilio, Telefono, Sector, Sueldo) VALUES
('B9912', 'Pablo Ramirez', '3 de Febrero 992', '341660354', 'Produccion', 250000)
GO

SELECT * FROM EMPLEADO;
GO

INSERT INTO EMPLEADO (Legajo, Nombre, Domicilio, Telefono, Sector, Sueldo) VALUES
('E8123', 'Mariana Sosa', 'Estanislao Lopez 2987', '341665987', 'Administracion', 260000)
INSERT INTO EMPLEADO (Legajo, Nombre, Domicilio, Telefono, Sector, Sueldo) VALUES
('A9400', 'Carlos Aguierre', 'Santa Fe 3456', '341660431', 'Administracion', 230000)
GO

INSERT INTO SERVICIO_TECNICO (nombre, telefono, direccion) VALUES
('Electrolux SA', '341220956', 'Del cairo 3400'),
('Martinez maquinarias SRL', '0800345761', 'Riobamba 4567'),
('Fast Reparaciones S.A.', '341665789', 'Pellegrini 4578')
GO

SELECT * FROM SERVICIO_TECNICO;
GO


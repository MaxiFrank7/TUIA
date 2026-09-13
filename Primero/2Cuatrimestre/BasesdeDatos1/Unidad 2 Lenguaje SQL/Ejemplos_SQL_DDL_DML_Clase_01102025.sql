-- ======== Lenguaje DDL (Data Definition Language) ===================================

/*==================== Bases de datos ============================================================*/
-- Creamos una base de datos
---DROP DATABASE UNRBD1C12025;
--T-SQL Transact SQL
IF NOT EXISTS (SELECT 1 FROM sys.databases WHERE name = 'UNRBD1C12025') -- Va a crear la base solo si no existe
CREATE DATABASE UNRBD1C12025;

USE UNRBD1C12025
GO
-- Creacion de la base de datos Especificando Datafiles y ubicacion
CREATE DATABASE UNRBD1C12025
ON 
(
    NAME = UNRBD1C12025,                   -- Nombre l�gico del archivo de datos
    FILENAME = 'M:\DBA\Bases\UNRBD1C12025.mdf',   -- Ruta f�sica completa del archivo de datos
    SIZE = 10MB,                                -- Tama�o inicial
    MAXSIZE = 100MB,                            -- Tama�o m�ximo
    FILEGROWTH = 5MB                            -- Incremento al crecer
)
LOG ON
(
    NAME = MiBaseDatos_Log,                     -- Nombre l�gico del archivo de log
    FILENAME = 'M:\DBA\Bases\UNRBD1C12025.ldf', -- Ruta f�sica completa del log
    SIZE = 5MB,
    MAXSIZE = 50MB,
    FILEGROWTH = 1MB
);


/*==================== Tablas ============================================================*/
-- Creamos una tabla llamada Alumnos
/* Para crear una tabla es: 
   Comando CREATE TABLE [Nombre de la tabla] (Atributos + tipos de datos separados por comas)*/
use UNRBD1C12025
CREATE TABLE Alumnos
(IdAlumno INT IDENTITY(1,1),
 Nombre VARCHAR(80),
 Direccion VARCHAR(100),
 Correo VARCHAR(100),
 FechaNac DATE
);
CREATE TABLE Prueba.Alumnos -- Esquema.tabla
(IdAlumno INT IDENTITY(1,1),
 Nombre VARCHAR(80),
 Direccion VARCHAR(100),
 Correo VARCHAR(100),
 FechaNac DATE
);

CREATE TABLE BBDD.dbo.Alumnos -- Base.Esquema.Tabla (en este caso en otra base que se llama BBDD)
(IdAlumno INT IDENTITY(1,1),
 Nombre VARCHAR(80),
 Direccion VARCHAR(100),
 Correo VARCHAR(100),
 FechaNac DATE
);


-- Modificamos la tabla Alumnos y le agregamos un nuevo atributo
ALTER TABLE Alumnos ADD Legajo VARCHAR(30);

-- Modificamos la tabla Alumnos y le cambiamos el tipo de dato a un atributo
ALTER TABLE Alumnos ALTER COLUMN Direccion VARCHAR(150); 
-- Esta operacion es muy costosa(dependiendo del tipo de dato a cambiar) y generar� Bloqueos en la tabla
-- si la tabla tiene muchos registros!!!!! 		 

-- Eliminamos la tabla Alumnos
DROP TABLE Alumnos;

/*==================== Restricciones ============================================================*/
-- Vamos a crear la tabla Alumnos2 con todos los ejemplos de Restricciones:
CREATE TABLE Alumnos2
(    
    IdAlumno INT IDENTITY(1,1) PRIMARY KEY, -- Clave primaria    
    Nombre VARCHAR(80) NOT NULL,  -- Obligatorio    
    Direccion VARCHAR(100),  -- Sin Restriccion, pude ser null (por defecto)
    Correo VARCHAR(100) UNIQUE,  -- El correo debe ser unico
    FechaNac DATE CHECK (FechaNac <= GETDATE()), -- No se puede ingresar una fecha mayor a la fecha actual
    Pais VARCHAR(50) DEFAULT 'Argentina', -- Si no especifica dato, guarda Argentina como default
	IdCiudad INT CONSTRAINT FK_CIUDADES FOREIGN KEY (IdCiudad) REFERENCES Ciudades(IdCiudad),-- Clave Foranea a la tabla ciudades
	legajo VARCHAR(30) UNIQUE -- El Legajo debe ser unico
);

-- Ejemplo de FK (Foreign Key) con la tabla Ciudades, la creamos antes de crear la tabla alumnos
-- que estar� relacionada por IdCiudad

CREATE TABLE Ciudades
(IdCiudad INT IDENTITY (1,1) PRIMARY KEY,
 Ciudad VARCHAR(80)
 )

-- Creamos la tabla Alumnos3 pero con los nombres de los indices customizados en los nombres
CREATE TABLE Alumnos3
(    
    IdAlumno INT IDENTITY(1,1), 
    Nombre VARCHAR(80) NOT NULL,  
    Direccion VARCHAR(100),  -- Sin Restriccion, pude ser null (por defecto)
    Correo VARCHAR(100) NOT NULL,  
    FechaNac DATE, 
    Pais VARCHAR(50), 
	IdCiudad INT NOT NULL, 
	legajo VARCHAR(30) NOT NULL,
	CONSTRAINT PK_Alumnos3_IdAlumno PRIMARY KEY (IdAlumno), -- Clave primaria 
	CONSTRAINT UK_Alumnos3_Correo UNIQUE (Correo), -- Clave unica
	CONSTRAINT CHK_Alumnos3_FechaNac CHECK (FechaNac <= GETDATE()),-- No se puede ingresar una fecha mayor a la fecha actual
	--CONSTRAINT DEF_Alumnos3_Pais DEFAULT 'Argentina' FOR Pais, -- Si no especifica dato, guarda Argentina como default (da error)
	CONSTRAINT UK_Alumnos3_Legajo UNIQUE (legajo), -- Clave unica
	CONSTRAINT FK_Alumnos3_Ciudades FOREIGN KEY (IdCiudad) REFERENCES Ciudades(IdCiudad) --Clave Foranea a tabla ciudades
);
ALTER TABLE Alumnos3 ADD CONSTRAINT DEF_Alumnos3_Pais DEFAULT 'Argentina' FOR Pais;


 -- ============ INDICES ===========================================
 -- Creamos un nuevo indice UNICO (Clave Alternativa) en la tabla Alumnos sobre el atributo legajo
CREATE UNIQUE INDEX IDXU_Alumnos_Legajo ON Alumnos(Legajo);

-- Creamos un nuevo indice NO UNICO en la tabla Alumnos sobre el Atributo FechaNac
CREATE INDEX IDXU_Alumnos_FechaNac ON Alumnos(FechaNac);
 
 CREATE UNIQUE NONCLUSTERED INDEX IXU_Ciudades_Ciudad ON Ciudades (Ciudad); -- Creamos un indice unico sobre el atributo Ciudad

 DROP INDEX IXU_Ciudades_Ciudad ON Ciudades;  -- Eliminamos el indice



/* ========== LENGUAJE DML (DATA MANIPULATION LANGUAGE) ===========*/

-- =========== SELECT ================================================
-- Vamos a obtener algunos datos de una tabla llamada clientes
--Consultas simples sobre la base de datos NORTHWIND
USE [Northwind]
GO
SELECT * FROM Customers; -- Todos los atributos(columnas) de la tabla Customres

SELECT CustomerID,contactName,Address,postalcode from Customers -- Algunos Atributos de la tabla Customers (Proyeccion)
ORDER BY ContactName desc;

SELECT * FROM Products;
SELECT * FROM [Order Details];

SELECT OrderId,ProductID,UnitPrice,Quantity, UnitPrice * Quantity as TotalRenglon
FROM [Order Details];

SELECT OrderId,ProductID,UnitPrice,Quantity, 'Total x Renglon: ' + UnitPrice * Quantity as TotalRenglon
FROM [Order Details]; -- Esta consulta da error porque estamos concatenando un string ('Total x Renglon: ') con
-- un tipo de dato que no es string (UnitPrice) que es del tipo de dato Money

SELECT OrderId,ProductID,UnitPrice,Quantity, 'Total x Renglon: ' + CAST((UnitPrice * Quantity)as VARCHAR) as TotalRenglon
FROM [Order Details]; -- Con la funcion CAST podemos realizar la consulta

-- Distinct
SELECT Country FROM Customers -- Los paises de cada cliente (se repiten por cada cliente al que corresponde su pais)
ORDER BY Country;

SELECT DISTINCT Country FROM Customers -- El DISTINCT elimina registros repetidos del atributo Country
ORDER BY Country;

SELECT CustomerID, CompanyName,Address,City -- Algunos atributos de la tabla Clientes
FROM Customers;

-- Consultas "Calificadas", poseen clausula where para filtros

SELECT CustomerID, CompanyName,Address,City,region -- Todos los Clientes de Londres
FROM Customers 
WHERE City = 'London'

SELECT OrderId,ProductID,UnitPrice,Quantity, UnitPrice * Quantity as TotalRenglon
FROM [Order Details]
WHERE UnitPrice * Quantity > 100 -- Solo los renglones totales que sean mayores a 100
AND Quantity > 20 -- Solo los renglones que tengan mas de 20 unidades

-- Orden de sintaxis(no de ejecucion) de un SELECT SIMPLE (sin Joins ni agrupamiento)
/*1)*/SELECT CustomerID, CompanyName,Address,Country,Region
/*2)*/FROM Customers
/*3)*/WHERE Country = 'London' 
/*4)*/AND Region is null 
/*5)*/ORDER BY CustomerID
	  
	  
SELECT Id_Factura_Detalle,IdProducto,PrecioSinImporte,Cantidad,PrecioSinImporte * Cantidad as PrecioCalculado
FROM FacturaDetalle
WHERE PrecioSinImporte * cantidad > 50


-- ======================== INSERT ===========================================
-- Vamos a insertar datos en las tablas Alumnos(sin restricciones) y Alumnos3 
-- Insert en tabla Alumnos sin Restricciones 

TRUNCATE TABLE Alumnos; -- Dejo la tabla vacia, mas rapido y performante que un Delete que se ve mas abajo OJO!!! NO HAY VUELTA ATRAS!!!
TRUNCATE TABLE Alumnos3;

--Insertamos algunos registros en la tabla Alumnos
INSERT INTO Alumnos (Nombre, Direccion, Correo, FechaNac) VALUES
('Juan Perez', 'Calle Falsa 123', 'juan.perez@example.com', '1990-05-15');

INSERT INTO Alumnos (Nombre, Direccion, Correo, FechaNac) VALUES
('Mar�a Gomez', 'Av. Libertad 456', 'maria.gomez@example.com', '1992-08-22');

INSERT INTO Alumnos (Nombre, Direccion, Correo, FechaNac) VALUES
('Carlos Ramirez', 'Calle Mayor 789', 'carlos.ramirez@example.com', '1988-12-03');

INSERT INTO Alumnos (Nombre, Direccion, Correo, FechaNac) VALUES
('Luc�a Fernandez', 'Boulevard Central 321', 'lucia.fernandez@example.com', '1995-03-30');

INSERT INTO Alumnos (Nombre, Direccion, Correo, FechaNac) VALUES
('Mateo Sanchez', 'Calle del Sol 555', 'mateo.sanchez@example.com', '1991-11-11');

INSERT INTO Alumnos (Nombre, Direccion, Correo, FechaNac) VALUES
('Mateo Sanchez', 'Rivadavia 3554', 'msanchez4@example.com', '1994-12-10');

-- Insertamos algunos registros en la tabla ciudades 
-- Si no insertamos estos registros, cuando queremos insertar en Alumnos3 dar� error de integridad referencial, porque si ingresamos un IdCiudad
-- no existe en la tabla Ciudades (Padre)

INSERT INTO Ciudades (Ciudad) VALUES ('Rosario')
INSERT INTO Ciudades (Ciudad) VALUES ('Buenos Aires')
INSERT INTO Ciudades (Ciudad) VALUES ('Bahia Blanca')

-- Insertamos en Alumnos3 con Restricciones

INSERT INTO Alumnos3 (Nombre, Direccion, Correo, FechaNac, Pais, IdCiudad, legajo)
VALUES ('Juan Perez', 'Calle Falsa 123', 'juan.perez@example.com', '1990-05-15', DEFAULT, 1, 'LEG001'); -- Violacion de registro duplicado (LEG001), ya existe 
-- un Alumno con ese legajo

INSERT INTO Alumnos3 (Nombre, Direccion, Correo, FechaNac, Pais, IdCiudad, legajo)
VALUES (null, 'Av. Libertad 456', 'maria.gomez@example.com', '1992-08-22', DEFAULT, 1, 'LEG002'); -- Error, el nombre no puede ser nulo

INSERT INTO Alumnos3 (Nombre, Direccion, Correo, FechaNac, Pais, IdCiudad, legajo)
VALUES ('Carlos Ramirez', 'Calle Mayor 789', 'juan.perez@example.com', '1988-12-03', DEFAULT, 1, 'LEG003'); -- Registro duplicado (Correo) que tiene indice
																											-- UNIQUe		
INSERT INTO Alumnos3 (Nombre, Direccion, Correo, FechaNac, Pais, IdCiudad, legajo)
VALUES ('Lucia Fernandez', 'Boulevard Central 321', 'lucia.fernandez@example.com', '2050-12-21', DEFAULT, 1, 'LEG004');-- Fecha mayor a la actual, habiamos
-- creado una constrain check para que no se ingres una fecha mayor a la actual																													   	

INSERT INTO Alumnos3 (Nombre, Direccion, Correo, FechaNac, Pais, IdCiudad, legajo)
VALUES ('Mateo Sanchez', 'Calle del Sol 555', 'mateo.sanchez1@example.com', '1991-11-11', DEFAULT, 999, 'LEG045'); -- Error de FK, no existe el IdCiudad 999
-- en la tabla Ciudades (Padre)

-- Inserts validos
INSERT INTO Alumnos3 (Nombre, Direccion, Correo, FechaNac, Pais, IdCiudad, legajo)
VALUES ('Juan Perez', 'Calle Falsa 123', 'juan.perez@example.com', '1990-05-15', DEFAULT, 1, 'LEG001');

INSERT INTO Alumnos3 (Nombre, Direccion, Correo, FechaNac, Pais, IdCiudad, legajo)
VALUES ('Mar�a Gomez', 'Av. Libertad 456', 'maria.gomez@example.com', '1992-08-22', DEFAULT, 2, 'LEG002');

INSERT INTO Alumnos3 (Nombre, Direccion, Correo, FechaNac, Pais, IdCiudad, legajo)
VALUES ('Carlos Ramirez', 'Calle Mayor 789', 'carlos.ramirez@example.com', '1988-12-03', DEFAULT, 3, 'LEG003');

INSERT INTO Alumnos3(Nombre, Direccion, Correo, FechaNac, Pais, IdCiudad, legajo)
VALUES ('Lucia Fernandez', 'Boulevard Central 321', 'lucia.fernandez@example.com', '1995-03-30', DEFAULT, 2, 'LEG004');

INSERT INTO Alumnos3 (Nombre, Direccion, Correo, FechaNac, Pais, IdCiudad, legajo)
VALUES ('Mateo Sanchez', 'Calle del Sol 555', 'mateo.sanchez@example.com', '1991-11-11', DEFAULT, 1, 'LEG005');

INSERT INTO Alumnos3 (Nombre, Direccion, Correo, FechaNac, Pais, IdCiudad, legajo)
VALUES ('Mateo Sanchez', 'Mitre 4588', 'msanchez4@example.com', '1993-02-14', DEFAULT, 1, 'LEG012');


-- ============================== UPDATE ==============================================================
-- Vamos a modificar datos de algunos registros
--Modificamos el Legajo del Alumno 

SELECT * FROM alumnos3

UPDATE Alumnos3 SET legajo = 'LEG014' 
WHERE legajo = 'LEG012';

-- Modificamos la direccion del alumno Mateo Sanchez

UPDATE Alumnos3 SET Direccion='Calle del Sol 555' 
--WHERE Nombre = 'Mateo Sanchez' -- Que va a pasar ac�? -- Modificariamos la direccion de todos los alumnos que se llaman Mateo Sanchez!!
where DIRECCION = 'Calle del Sol 554'; 

UPDATE Alumnos3 SET Direccion='Calle del Sol 555' 
WHERE Nombre = 'Mateo Sanchez' 
AND DIRECCION = 'Calle del Sol 554'; 

UPDATE Alumnos3 SET Direccion = 'Anchorena 990', Pais = 'Brasil', Legajo='LEG008'
WHERE Nombre = 'Lucia Fernandez';

SELECT * FROM ALUMNOS3 WHERE Nombre = 'Lucia Fernandez'; -- Verificamos los cambios

UPDATE Alumnos3 SET Pais = 'Nueva zelanda'; -- Que pasa aca??? Modificariamos TODOS LOS REGISTROS DE LA TABLA!!!!!
-- LO IMPORTANTE DEL WHERE


-- ============================== DELETE ===============================================================
-- Vamos a eliminar algunos registros de las tablas de Alumnos

SELECT * FROM Alumnos3 order by Nombre;

--- Eliminamos un registro
DELETE FROM Alumnos3 WHERE IdAlumno=2;

--- Eliminar el registro del Alumno Mateo Sanchez (que deberiamos hacer ante este pedido???)
DELETE FROM Alumnos3 WHERE Nombre = 'Mateo Sanchez';-- Si hay mas de 1 alumno Mateo Sanchez elimiriamos todos

DELETE FROM ALUMNOS3 -- Sin WHERE eliminariamos TODOS LOS REGISTROS DE LA TABLA!!

DELETE Ciudades WHERE Ciudad = 'Rosario'; -- Que pasa aca???? 
--Si la tabla hija (Alumnos3) tiene Alumnos que son de la Ciudad de Rosario dara Error por FK

/******************************************************************************************************************************
*              UPDATES Y DELETES SIEMPRE SIEMPRE SIEMPRE SIEMPRE CON WHERE !!!!!!!!!! (Salvo que se necesite borrar todo)     *
*******************************************************************************************************************************/
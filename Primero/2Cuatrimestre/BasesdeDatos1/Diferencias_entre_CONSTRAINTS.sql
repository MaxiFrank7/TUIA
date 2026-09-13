CREATE DATABASE pruebas
GO

USE pruebas 

-- Primero, creamos la tabla de soporte que ambas versiones necesitarán
CREATE TABLE Ciudades (
    IdCiudad INT IDENTITY(1,1) PRIMARY KEY,
    Ciudad VARCHAR(80) NOT NULL
);
GO -- Separa los lotes de ejecución

-- ------------------------------------------------------------------
-- VERSION 1: CONSTRAINTS "EN LÍNEA" (NOMBRES AUTOMÁTICOS)
-- ------------------------------------------------------------------
-- Aquí, las restricciones se definen junto a la columna.
-- Es más rápido de escribir pero menos organizado.
PRINT 'Creando la tabla Alumnos_En_Linea...';

CREATE TABLE Alumnos_En_Linea (
    IdAlumno INT IDENTITY(1,1) PRIMARY KEY,
    Nombre VARCHAR(80) NOT NULL,
    Correo VARCHAR(100) NOT NULL UNIQUE,
    FechaNac DATE CHECK (FechaNac <= GETDATE()),
    Pais VARCHAR(50) DEFAULT 'Argentina',
    legajo VARCHAR(30) NOT NULL UNIQUE,
    IdCiudad INT NOT NULL FOREIGN KEY REFERENCES Ciudades(IdCiudad)
);
GO

-- ------------------------------------------------------------------
-- VERSION 2: CONSTRAINTS NOMBRADAS Y SEPARADAS (MEJOR PRÁCTICA)
-- ------------------------------------------------------------------
-- Aquí, las restricciones se definen en un bloque separado al final.
-- Les damos nombres claros y descriptivos.
PRINT 'Creando la tabla Alumnos_Nombrados...';

CREATE TABLE Alumnos_Nombrados (
    IdAlumno INT IDENTITY(1,1),
    Nombre VARCHAR(80) NOT NULL,
    Correo VARCHAR(100) NOT NULL,
    FechaNac DATE,
    Pais VARCHAR(50),
    legajo VARCHAR(30) NOT NULL,
    IdCiudad INT NOT NULL,

    -- Bloque dedicado a las restricciones con nombres personalizados
    CONSTRAINT PK_Alumnos_Nombrados PRIMARY KEY (IdAlumno),
    CONSTRAINT UQ_Alumnos_Nombrados_Correo UNIQUE (Correo),
    CONSTRAINT UQ_Alumnos_Nombrados_Legajo UNIQUE (legajo),
    CONSTRAINT CK_Alumnos_Nombrados_FechaNac CHECK (FechaNac <= GETDATE()),
    --CONSTRAINT DF_Alumnos_Nombrados_Pais DEFAULT 'Argentina' FOR Pais,
    CONSTRAINT FK_Alumnos_Nombrados_Ciudades FOREIGN KEY (IdCiudad) REFERENCES Ciudades(IdCiudad)
);
GO

PRINT 'Tablas creadas exitosamente.';
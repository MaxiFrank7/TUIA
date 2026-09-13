-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2024-11-27 13:11:14.959

-- tables
-- Table: Ciudad
CREATE TABLE Ciudad (
    ID_Ciudad int  NOT NULL,
    Ciudad varchar(50)  NOT NULL,
    CONSTRAINT UK_Ciudad UNIQUE (Ciudad),
    CONSTRAINT PK_Ciudad PRIMARY KEY  (ID_Ciudad)
);

-- Table: Club
CREATE TABLE Club (
    ID_Club int  NOT NULL,
    NombreClub varchar(50)  NOT NULL,
    Direccion varchar(50)  NOT NULL,
    ID_Ciudad int  NOT NULL,
    Presidente varchar(50)  NOT NULL,
    Socios int  NOT NULL DEFAULT 0,
    CONSTRAINT UK_Club UNIQUE (NombreClub),
    CONSTRAINT PK_Club PRIMARY KEY  (ID_Club)
);

-- Table: DirectorTecnico
CREATE TABLE DirectorTecnico (
    ID_DirectorTecnico int  NOT NULL,
    Nombre varchar(50)  NOT NULL,
    Apellido varchar(50)  NOT NULL,
    DNI varchar(20)  NOT NULL,
    FechaNacimiento date  NOT NULL,
    Email varchar(50)  NOT NULL,
    Telefono int  NOT NULL,
    ID_Club int  NULL,
    CONSTRAINT UK_DirectorTecnico_DNI UNIQUE (DNI),
    CONSTRAINT UK_DirectorTecnico_Club UNIQUE (ID_Club),
    CONSTRAINT PK_DirectorTecnico PRIMARY KEY  (ID_DirectorTecnico)
);

-- Table: Historial
CREATE TABLE Historial (
    ID_Historial int  NOT NULL,
    ID_Club int  NOT NULL,
    ID_Jugador int  NOT NULL,
    FechaInicio date  NOT NULL,
    FechaFin date  NULL,
    Partidos int  NOT NULL DEFAULT 0,
    GolesMarcados int  NOT NULL DEFAULT 0,
    GolesRecibidos int  NOT NULL DEFAULT 0,
    Titulos int  NOT NULL DEFAULT 0,
    CONSTRAINT UK_Historial UNIQUE (ID_Club, ID_Jugador, FechaInicio),
    CONSTRAINT PK_Historial PRIMARY KEY  (ID_Historial)
);

-- Table: Jugador
CREATE TABLE Jugador (
    ID_Jugador int  NOT NULL,
    Nombre varchar(50)  NOT NULL,
    Apellido varchar(50)  NOT NULL,
    Telefono varchar(20)  NOT NULL,
    FechaNacimiento date  NOT NULL,
    ID_Ciudad int  NOT NULL,
    CONSTRAINT Jugador_pk PRIMARY KEY  (ID_Jugador)
);

-- Table: Posicion
CREATE TABLE Posicion (
    ID_Posicion tinyint  NOT NULL,
    Posicion varchar(20)  NOT NULL,
    CONSTRAINT UK_Posicion UNIQUE (Posicion),
    CONSTRAINT PK_Posicion PRIMARY KEY  (ID_Posicion)
);

-- Table: PosicionJugador
CREATE TABLE PosicionJugador (
    ID_Jugador int  NOT NULL,
    ID_Posicion tinyint  NOT NULL,
    CONSTRAINT PK_PosicionJugador PRIMARY KEY  (ID_Jugador,ID_Posicion)
);

-- foreign keys
-- Reference: Club_Ciudad (table: Club)
ALTER TABLE Club ADD CONSTRAINT Club_Ciudad
    FOREIGN KEY (ID_Ciudad)
    REFERENCES Ciudad (ID_Ciudad);

-- Reference: DirectorTecnico_Club (table: DirectorTecnico)
ALTER TABLE DirectorTecnico ADD CONSTRAINT DirectorTecnico_Club
    FOREIGN KEY (ID_Club)
    REFERENCES Club (ID_Club);

-- Reference: Historial_Club (table: Historial)
ALTER TABLE Historial ADD CONSTRAINT Historial_Club
    FOREIGN KEY (ID_Club)
    REFERENCES Club (ID_Club);

-- Reference: Historial_Jugador (table: Historial)
ALTER TABLE Historial ADD CONSTRAINT Historial_Jugador
    FOREIGN KEY (ID_Jugador)
    REFERENCES Jugador (ID_Jugador);

-- Reference: Jugador_Ciudad (table: Jugador)
ALTER TABLE Jugador ADD CONSTRAINT Jugador_Ciudad
    FOREIGN KEY (ID_Ciudad)
    REFERENCES Ciudad (ID_Ciudad);

-- Reference: PosicionJugador_Jugador (table: PosicionJugador)
ALTER TABLE PosicionJugador ADD CONSTRAINT PosicionJugador_Jugador
    FOREIGN KEY (ID_Jugador)
    REFERENCES Jugador (ID_Jugador);

-- Reference: PosicionJugador_Posicion (table: PosicionJugador)
ALTER TABLE PosicionJugador ADD CONSTRAINT PosicionJugador_Posicion
    FOREIGN KEY (ID_Posicion)
    REFERENCES Posicion (ID_Posicion);

-- End of file.


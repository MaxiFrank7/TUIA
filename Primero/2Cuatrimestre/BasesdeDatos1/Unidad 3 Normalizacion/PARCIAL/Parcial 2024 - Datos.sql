INSERT INTO Ciudad (ID_Ciudad, Ciudad) VALUES
(1, 'Buenos Aires'),
(2, 'Rosario'),
(3, 'La Plata');

INSERT INTO Club (ID_Club, NombreClub, Direccion, ID_Ciudad, Presidente, Socios) VALUES
(1, 'Boca Juniors', 'Av. Del Libertador 600', 1, 'Jorge Amor Ameal', 200000),
(2, 'River Plate', 'Av. Pres. Figueroa Alcorta 7597', 1, 'Jorge Brito', 200000),
(3, 'Rosario Central', 'Calle 9 de Julio 510', 2, 'Gonzalo Belloso', 65000),
(4, 'Estudiantes de La Plata', 'Calle 1 777', 3, 'Juan Sebastián Verón', 30000);

INSERT INTO DirectorTecnico (ID_DirectorTecnico, Nombre, Apellido, DNI, FechaNacimiento, Email, Telefono, ID_Club) VALUES
(1, 'Sebastián', 'Bataglia', '12345678A', '1980-10-21', 'sebastian@bocajuniors.com.ar', 1123456789, 1),
(2, 'Marcelo', 'Gallardo', '23456789B', '1976-06-18', 'marcelo@riverplate.com.ar', 1123456790, 2),
(3, 'Dario', 'Holan', '34567890C', '1975-04-30', 'dario@rosariocentral.com.ar', 1123456791, 3),
(4, 'Ricardo', 'Zielinski', '45678901D', '1963-02-14', 'ricardo@estudiantes.com.ar', 1123456792, 4);

INSERT INTO Jugador (ID_Jugador, Nombre, Apellido, Telefono, FechaNacimiento, ID_Ciudad) VALUES
(1, 'Cristian', 'Medina', '1122334455', '2001-08-23', 1),
(2, 'Pablo', 'Aimar', '2233445566', '1979-11-03', 1),
(3, 'Hernán', 'López', '3344556677', '1988-09-15', 2),
(4, 'Marcelo', 'Negri', '4455667788', '1994-03-22', 3);

INSERT INTO Posicion (ID_Posicion, Posicion) VALUES
(1, 'Delantero'),
(2, 'Centrocampista'),
(3, 'Defensa'),
(4, 'Arquero');

INSERT INTO PosicionJugador (ID_Jugador, ID_Posicion) VALUES
(1, 2),  -- Cristian Medina como Centrocampista
(2, 1),  -- Pablo Aimar como Delantero
(3, 3),  -- Hernán López como Defensa
(4, 3);  -- Marcelo Negri como Defensa


INSERT INTO Historial (ID_Historial, ID_Club, ID_Jugador, FechaInicio, FechaFin, Partidos, GolesMarcados, GolesRecibidos, Titulos) VALUES
(1, 1, 1, '2020-01-01', NULL, 50, 10, 0, 1),
(2, 2, 2, '2001-01-01', '2006-06-30', 100, 30, 0, 2),
(3, 3, 3, '2015-01-01', NULL, 80, 25, 0, 0),
(4, 4, 4, '2019-01-01', NULL, 40, 5, 0, 0),
(5, 3, 2, '2010-01-01', '2020-06-30', 300, 80, 0, 1);

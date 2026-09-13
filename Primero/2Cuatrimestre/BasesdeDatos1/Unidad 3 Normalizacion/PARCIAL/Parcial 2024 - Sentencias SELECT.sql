--1) 
SELECT j.Nombre, j.Apellido, c.NombreClub, h.GolesMarcados
FROM Jugador j
	JOIN Historial h ON h.ID_Jugador = j.ID_Jugador
	JOIN Club c ON c.ID_Club = h.ID_Club
WHERE h.FechaFin IS NULL
AND h.GolesMarcados >= 10;
--
--2) 
SELECT SUM(h.GolesMarcados) AS TotalGolesMarcados
FROM Jugador j
	JOIN Historial h ON h.ID_Jugador = j.ID_Jugador
WHERE j.Apellido = 'Negri'
AND j.Nombre = 'Marcelo'
--
--3 -ID)
SELECT h.ID_Club, SUM(h.GolesMarcados) AS TotalGolesMarcados
FROM Historial h
GROUP BY h.ID_Club
--HAVING SUM(h.GolesMarcados) >= 20
ORDER BY TotalGolesMarcados DESC;
--
--3 -Nombre)
SELECT c.NombreClub, SUM(h.GolesMarcados) AS TotalGolesMarcados
FROM Historial h
	JOIN Club c ON c.ID_Club = h.ID_Club
GROUP BY c.NombreClub
--HAVING SUM(h.GolesMarcados) >= 20
ORDER BY TotalGolesMarcados DESC;
--

USE empresa_basica2;
--apartado a
SELECT nombre, apellido1 + ' ' + apellido2 AS Apellido, dni
FROM DIRECTOR
WHERE dni=33193456;

--apartado b
/*SELECT dptoid AS NRO_DEPTO, COUNT(*) AS CANTIDAD_PROYECTOS
FROM PROYECTO
WHERE dptoid=3
GROUP BY dptoid;*/

SELECT COUNT(*) AS Cantidad_Proyectos
FROM PROYECTO
WHERE dptoid = (SELECT dptoid FROM DPTO WHERE nombre='Investigacion');

--apartado c
/*SELECT TOP 1 DNI
FROM EMPLEADO
WHERE dptoid=1
ORDER BY sueldo DESC;*/

SELECT TOP 1 DNI
FROM EMPLEADO
WHERE dptoid = (SELECT dptoid FROM DPTO WHERE nombre='Sede Central')
ORDER BY sueldo DESC;

--apartado d
/*SELECT AVG(sueldo) AS sueldo_promedio
FROM EMPLEADO
WHERE dptoid=1;*/

SELECT AVG(sueldo) AS sueldo_promedio
FROM EMPLEADO
WHERE dptoid = (SELECT dptoid FROM DPTO WHERE nombre='Sede Central')

--apartado e
SELECT * FROM PROYECTO_EMPLEADO
SELECT * FROM PROYECTO

/*SELECT E.nombre, E.apellido1 + ' ' + E.apellido2 AS Apellido
FROM EMPLEADO AS E
INNER JOIN PROYECTO_EMPLEADO AS PE ON E.empleadoid=PE.empleadoid
WHERE PE.horas>3 AND PE.proyectoid=1;*/

--SELECT *
SELECT COUNT(empleadoid) AS Cantidad_Empleados
FROM PROYECTO_EMPLEADO AS PE
INNER JOIN PROYECTO AS P ON PE.proyectoid=P.proyectoid
INNER JOIN DPTO AS D ON P.dptoid=D.dptoid
WHERE PE.horas>=3 AND P.nombre='ProductoX' AND D.nombre='Investigacion';


--apartado f
SELECT *
FROM EMPLEADO
WHERE fechanac BETWEEN '1960-01-01' AND '1980-12-31';

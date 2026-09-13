USE TP_BBDDI_FRANK_WINTER
GO
/*a. Mostrar información de los reclamos. Se desea saber la fecha de cada uno,
el código del árbol asociado al reclamo, la cantidad de días que se tardó en
asignar la tarea y la cantidad de días que se tardó en resolver el mismo. Sino tiene tarea asignada o no fue resuelto calcular los días hasta la fechaactual.*/
CREATE VIEW v_InfoReclamos AS
	SELECT R.Fecha, A.Codigo, 
		DATEDIFF(DAY, R.Fecha, ISNULL(T.FechaRealizado, GETDATE())) AS [Tiempo de Resolucion], 
		DATEDIFF(DAY, R.Fecha, ISNULL(R.FechaAsignacionTarea, GETDATE())) AS [Tiempo de Asignacion]
	FROM Reclamos R
	JOIN Arbol A ON A.idArbol=R.idArbol
	JOIN Tarea T ON T.idtarea=R.idTarea
GO
SELECT * FROM v_InfoReclamos;
SELECT * FROM v_InfoReclamos WHERE [Tiempo de Asignacion] > 10;
/*b. Resumen de tareas ya realizadas según su tipo. Se desea saber la fecha de
la primer y última tarea de cada tipo y la cantidad de tareas realizadas*/
CREATE VIEW v_TareasRealizadas AS
	SELECT TT.Descripcion, 
		MIN(T.FechaRealizado) AS [Primera Fecha Realizada], 
		MAX(T.FechaRealizado) AS [Ultima Fecha Realizada], 
		COUNT(*) AS [Cantidad Tareas]
	FROM Tarea T
	JOIN TipoTarea TT ON T.idTipoTarea=TT.idTipoTarea
	WHERE T.FechaRealizado<=GETDATE()
	GROUP BY TT.Descripcion
GO
SELECT * FROM v_TareasRealizadas;
SELECT * FROM v_TareasRealizadas WHERE [Cantidad Tareas] > 2;
GO

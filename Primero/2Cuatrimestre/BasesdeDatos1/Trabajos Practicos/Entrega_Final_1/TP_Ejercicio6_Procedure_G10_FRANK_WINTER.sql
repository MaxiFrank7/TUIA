USE TP_BBDDI_FRANK_WINTER
GO
/*6. Escriba un procedimiento almacenado para identificar si existen tareas no realizadas
dado un árbol en particular y un tipo de tareas. El procedimiento debe devolver:
a. Como parámetro de salida, la fecha de la próxima tarea del tipo indicado a
realizarse sobre el árbol, si existiera.
b. Debe retornar (como valor de retorno) la cantidad de tareas pendientes de
realizar para el tipo de tarea y árbol proporcionados.
Incluya dos ejemplos de ejecución del procedimiento (encontrando y no encontrandotareas) y muestre los valores devueltos en cada caso.*/

CREATE OR ALTER PROCEDURE sp_AnalizarTareasArbol
	@idArbol INT,
	@idTipoTarea INT,
	@FechaProxima DATE OUTPUT
AS
BEGIN
	--punto a
	SELECT TOP 1 @FechaProxima=T.FechaEstimada
	FROM TareaArbol TA
	JOIN Tarea T ON T.idTarea=TA.idTarea
	WHERE TA.idArbol=@idArbol 
		  AND T.idTipoTarea=@idTipoTarea 
		  AND T.FechaRealizado IS NULL 
		  AND T.FechaEstimada>=GETDATE()
	ORDER BY T.FechaEstimada ASC;
	--punto b
	DECLARE @CantidadPendientes INT;
	SELECT @CantidadPendientes = COUNT(T.idTarea)
    FROM TareaArbol TA
    INNER JOIN Tarea T ON TA.idTarea = T.idTarea
    WHERE TA.idArbol = @idArbol 
      AND T.idTipoTarea = @idTipoTarea
      AND T.FechaRealizado IS NULL;
	RETURN @CantidadPendientes;
END
GO

--Caso 1 encontrando tareas
DECLARE @FechaSalida DATE;      -- Variable para atrapar el OUTPUT
DECLARE @CantidadTareas INT;   -- Variable para atrapar el RETURN

EXEC @CantidadTareas = sp_AnalizarTareasArbol 
    @idArbol = 11,                
    @idTipoTarea = 1,             
    @FechaProxima = @FechaSalida OUTPUT;

-- Mostrar resultados
SELECT 
    'Caso Encontrado' AS Escenario,
    @FechaSalida AS [Fecha Próxima Tarea],
    @CantidadTareas AS [Tareas Pendientes];
GO

--Caso 2 No encontradoDECLARE @FechaSalida2 DATE;
DECLARE @CantidadRetorno2 INT;

-- Ejecución
EXEC @CantidadRetorno2 = sp_AnalizarTareasArbol 
    @idArbol = 1,                -- ID de un árbol sin tareas o inexistente
    @idTipoTarea = 1,
    @FechaProxima = @FechaSalida2 OUTPUT;

-- Mostrar resultados
SELECT 
    'Caso NO Encontrado' AS Escenario,
    @FechaSalida2 AS [Fecha Próxima Tarea], -- Debería ser NULL
    @CantidadRetorno2 AS [Cantidad Pendientes]; -- Debería ser 0
GO
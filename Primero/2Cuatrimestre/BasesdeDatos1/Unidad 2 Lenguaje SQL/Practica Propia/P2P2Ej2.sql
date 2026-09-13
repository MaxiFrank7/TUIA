USE ordenes2
--b. Seleccionar el cliente (número y nombre) asociado al pedido con clave 2 (PED2).
SELECT numero, nombre
FROM cliente
WHERE pedido_clave='PED2';
--c. Seleccionar todos los tipos de movimiento cuya descripción sea nula o vacía.
SELECT * 
FROM tipo_movimiento 
WHERE descripcion IS NULL OR descripcion='';
--a. Seleccionar todos los clientes (número y nombre) con estado igual a 10 o 20, ordenados alfabéticamente por nombre en forma creciente.
SELECT numero, nombre 
FROM cliente 
WHERE estado=10 OR estado=20 
ORDER BY nombre ASC;
--d. Determinar cuántos tipos de movimiento con descripción no nula existen.
SELECT COUNT(*)
FROM tipo_movimiento
WHERE descripcion IS NOT NULL;
--e. Seleccionar todos los productos (número y nombre) de color blanco cuyo precio este en el intervalo [20, 50].
SELECT numero, nombre 
FROM producto 
WHERE color = 'blanco' AND precio BETWEEN 20 AND 50;
--f. Seleccionar todos los clientes (número y nombre) que tienen al menos una orden.
SELECT numero, nombre
FROM cliente
WHERE EXISTS (SELECT * FROM orden 
              WHERE cliente_numero = cliente.numero);
--g. Seleccionar la lista de todos los clientes (número y nombre) que tienen al menos una orden, considerando que los clientes no deben repetirse, 
--independientemente de cuantas ordenes asociadas tenga.
SELECT DISTINCT numero, nombre
FROM cliente c
INNER JOIN orden o ON c.numero=o.cliente_numero
--h. Para cada cliente con al menos una cuenta, determinar el saldo promedio de aquellas asociadas a él.
--SELECT cliente_numero, AVG(saldo) AS Saldo_promedio FROM cuenta GROUP BY cliente_numero
SELECT c.nombre, c.numero, AVG(cu.saldo) AS Saldo_Promedio
FROM cliente c
INNER JOIN cuenta cu ON c.numero=cu.cliente_numero
GROUP BY c.nombre, c.numero;
--i. Para cada producto (número y nombre), determinar cuántas ordenes asociadas tiene
--SELECT producto_numero, COUNT(*) AS CANT_ORDENES FROM orden GROUP BY producto_numero
SELECT p.numero, p.nombre, COUNT(*) AS CANT_ORDENES 
FROM producto p
INNER JOIN orden o ON p.numero=o.producto_numero
GROUP BY p.numero, p.nombre;
--j. Seleccionar los productos (número y nombre) y la cantidad de ?ordenes asociadas, solo para aquellos que tengas más de 2
SELECT p.numero, p.nombre, COUNT(*) AS CANT_ORDENES 
FROM producto p
INNER JOIN orden o ON p.numero=o.producto_numero
GROUP BY p.numero, p.nombre
HAVING COUNT(*)>2;

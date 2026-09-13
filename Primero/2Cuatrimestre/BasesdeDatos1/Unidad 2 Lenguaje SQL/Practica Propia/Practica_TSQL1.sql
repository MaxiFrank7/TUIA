USE northwind;

--Consultas:
--1. Se necesita obtener un listado de todos los pedidos con el nombre del cliente (nombre de la empresa)
SELECT Cu.CompanyName, O.OrderID
FROM Orders O
INNER JOIN Customers Cu ON O.CustomerID=Cu.CustomerID;
--2. Se necesita saber la cantidad de pedidos que realizó cada cliente(ordenados por nombre de la empresa)
SELECT Cu.CompanyName, COUNT(O.OrderID) AS Cant_Pedidos
FROM Orders O
INNER JOIN Customers Cu ON O.CustomerID=Cu.CustomerID
GROUP BY Cu.CompanyName
ORDER BY Cu.CompanyName;
--3. Calcular el total y promedio de ventas por empleado
SELECT E.FirstName + ' ' + E.LastName AS Nombre_Completo, E.EmployeeID, SUM(OD.Quantity * OD.UnitPrice) AS TOTAL_VENTAS, AVG(OD.Quantity * OD.UnitPrice) AS PROM_VENTAS
FROM Employees E
INNER JOIN Orders O ON E.EmployeeID=O.EmployeeID
INNER JOIN [Order Details] OD ON O.OrderID=OD.OrderID
GROUP BY E.FirstName, E.LastName, E.EmployeeID;
--4. Mostrar los productos con ventas totales mayores a $10.000
SELECT P.ProductName AS Nombre, P.ProductID, SUM(OD.Quantity * OD.UnitPrice) AS TOTAL_VENTAS
FROM Products P
INNER JOIN [Order Details] OD ON P.ProductID=OD.ProductID
GROUP BY P.ProductName, P.ProductID	
HAVING SUM(OD.Quantity * OD.UnitPrice)>10000;
--5. Obtener el primer y ultimo pedido de cada cliente
SELECT Cu.CompanyName AS NombreEmpresa, MIN(O.OrderID) AS PrimerPedido, MAX(O.OrderID) AS UltimoPedido
FROM Customers Cu
INNER JOIN Orders O ON Cu.CustomerID=O.CustomerID
GROUP BY Cu.CompanyName
ORDER BY Cu.CompanyName;
--6. Mostrar un listado de los clientes que realizaron más de 20 pedidos
SELECT Cu.CustomerID, Cu.CompanyName AS NombreEmpresa, COUNT(O.OrderID) AS CantPedidos
FROM Customers Cu
INNER JOIN Orders O ON O.CustomerID=Cu.CustomerID
GROUP BY Cu.CompanyName, Cu.CustomerID
HAVING COUNT(O.OrderID)>20;
--7. Obtener el promedio de cantidad pedida por producto y categoría
SELECT Ca.CategoryName, P.ProductName, AVG(OD.Quantity) AS PromCantidad
FROM Products P
INNER JOIN Categories Ca ON P.CategoryID=Ca.CategoryID
INNER JOIN [Order Details] OD ON P.ProductID=OD.ProductID
GROUP BY Ca.CategoryName, P.ProductName
ORDER BY PromCantidad DESC;
--8. Obtener las ventas totales por país de envío
SELECT O.ShipCountry, SUM(OD.UnitPrice * OD.Quantity) AS VentasTotales
FROM Orders O
INNER JOIN [Order Details] AS OD ON O.OrderID = OD.OrderID
GROUP BY O.ShipCountry
ORDER BY VentasTotales DESC;
--9. Obtener el Promedio de precios de productos por categoría
SELECT Ca.CategoryName, AVG(P.UnitPrice) PromPrecio_x_Categoria
FROM Products P
INNER JOIN Categories Ca ON Ca.CategoryID=P.CategoryID
GROUP BY Ca.CategoryName
ORDER BY PromPrecio_x_Categoria DESC;
--10. Listado de clientes con pedidos enviados a más de un país
SELECT Cu.CompanyName AS Compania, O.ShipCountry AS PaisEnvio, COUNT(O.OrderID) As Pedidos
FROM Orders O
INNER JOIN Customers Cu ON Cu.CustomerID=O.CustomerID
GROUP BY Cu.CompanyName, O.ShipCountry
HAVING COUNT(O.OrderID)>1
ORDER BY Compania;

------------------------Ejercicio 2-----------------------------------------
--1. Obtener un reporte que informe cuanto vendió cada empleado a cada cliente, mostrar solo las ventas que superen los $15.000 (se deben unir las 
--tablas de clientes, empleados y pedidos)
SELECT E.EmployeeID, E.FirstName + ' ' + E.LastName AS Empleado, Cu.CompanyName AS Cliente, SUM(OD.UnitPrice * OD.Quantity) AS Venta 
FROM Employees E
INNER JOIN Orders O ON O.EmployeeID=E.EmployeeID
INNER JOIN Customers Cu ON Cu.CustomerID=O.CustomerID
INNER JOIN [Order Details] OD ON OD.OrderID=O.OrderID
GROUP BY  E.EmployeeID, E.FirstName, E.LastName, Cu.CompanyName
HAVING SUM(OD.UnitPrice * OD.Quantity)>15000
ORDER BY Venta DESC;
--2. Obtener las ventas mensuales por categoría de producto:
--a. Unir categorías, productos, pedidos y detalles
--b. Agrupar por año y por mes
--c. Calcular el total vendido y el promedio mensual
SELECT Ca.CategoryName AS Categoria,  YEAR(O.OrderDate) AS Anio, MONTH(O.OrderDate) AS Mes, SUM(OD.UnitPrice * OD.Quantity) AS TotalVentas, AVG(OD.UnitPrice * OD.Quantity) AS PromedioVenta
FROM Products P
INNER JOIN Categories Ca ON Ca.CategoryID=P.CategoryID
INNER JOIN [Order Details] OD ON OD.ProductID=P.ProductID
INNER JOIN Orders O ON OD.OrderID=O.OrderID
GROUP BY YEAR(O.OrderDate), MONTH(O.OrderDate), Ca.CategoryName
ORDER BY YEAR(O.OrderDate), MONTH(O.OrderDate);
--3. Obtener del resultado de la ultima consulta, solo las ventas del año 1998
SELECT Ca.CategoryName AS Categoria,  YEAR(O.OrderDate) AS Anio, MONTH(O.OrderDate) AS Mes, SUM(OD.UnitPrice * OD.Quantity) AS TotalVentas, AVG(OD.UnitPrice * OD.Quantity) AS PromedioVenta
FROM Products P
INNER JOIN Categories Ca ON Ca.CategoryID=P.CategoryID
INNER JOIN [Order Details] OD ON OD.ProductID=P.ProductID
INNER JOIN Orders O ON OD.OrderID=O.OrderID
WHERE YEAR(O.OrderDate)=1998
GROUP BY YEAR(O.OrderDate), MONTH(O.OrderDate), Ca.CategoryName
ORDER BY YEAR(O.OrderDate), MONTH(O.OrderDate);
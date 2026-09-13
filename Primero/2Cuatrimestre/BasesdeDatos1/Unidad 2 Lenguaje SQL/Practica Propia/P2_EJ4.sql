CREATE DATABASE P2_EJ4
GO
USE P2_EJ4;

CREATE TABLE Producto (
nroProd VARCHAR(4) NOT NULL,
nombreProd VARCHAR(20) NOT NULL,
color VARCHAR(10) NOT NULL,
precio DECIMAL(10,2) NOT NULL,
CONSTRAINT PK_Producto_nroProd PRIMARY KEY (nroProd),
CONSTRAINT CHK_Producto_color CHECK (color IN ('Rosa', 'Verde', 'Azul', 'Violeta', 'Negro', 'Blanco'))
);

INSERT INTO Producto (nroProd, nombreProd, color, precio) VALUES
('1234','Auricular', 'Azul', 1000.20);

INSERT INTO Producto (nroProd, nombreProd, color, precio) VALUES
('123','Teclado', 'Violeta', 2000.20);

SELECT * FROM Producto;
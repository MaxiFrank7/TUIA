from arepl_dump import dump
"""
Ejercicio 1: Gestión de Inventario de una Tienda
Este ejercicio se enfoca en la composición de objetos y la gestión del estado interno, similar a los ejercicios de Carrera y Automovil.

Consigna:
Define dos clases: Producto y Stock.

La clase Producto debe contener los siguientes atributos de instancia:
    codigo (string)
    nombre (string)
    precio (float)

La clase Stock representará el inventario de la tienda y se compondrá de objetos Producto. Deberá tener:

Un atributo de instancia productos, que será un diccionario para almacenar los productos y su cantidad. La clave será el código del producto y el valor será un diccionario con "producto" (el objeto Producto) 
y "cantidad" (un entero).

La clase Stock deberá implementar los siguientes métodos de instancia:
    * agregar_producto(producto: Producto, cantidad: int): Agrega un nuevo producto al stock. Si el producto ya existe (mismo código), simplemente actualiza su cantidad sumando el nuevo valor.
    * buscar_producto(codigo: str): Devuelve el objeto Producto correspondiente a un código. Si no lo encuentra, debe retornar None.
    * vender_producto(codigo: str, cantidad: int): Reduce la cantidad de un producto en el stock. Debe verificar si hay suficiente cantidad para vender. 
Si no hay suficiente, debe imprimir un mensaje de error y no realizar la venta.
    * valor_total_inventario(): Calcula y devuelve el valor total del inventario, multiplicando el precio de cada producto por su cantidad en stock y sumando los resultados."""

class Producto:
    def __init__(self, codigo:str, nombre:str, precio:float )->None:
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
    def __str__(self)->str:
        return f'El producto {self.nombre} de codigo: {self.codigo} y vale $: {self.precio}'

class Stock:
    def __init__(self)->None:
        # {'codigo_producto': {'producto': <objeto Producto>, 'cantidad': <int>}}
        self.productos:dict[str,dict[Producto,int]]={}

    
    def agregar_producto(self, producto:Producto, cantidad:int)->None:
        if producto.codigo in self.productos:
             self.productos[producto.codigo]["cantidad"]+=cantidad
        else:
            self.productos[producto.codigo]={"producto":producto, "cantidad":cantidad} #se crea la entrada
    
    def buscar_producto(self, codigo:str)->Producto|None:
        if codigo in self.productos:
            return self.productos[codigo]["producto"]
        return None
    
    def vender_producto(self, codigo:str, cantidad:int)->None:
        if codigo not in self.productos:
            print(f'El codigo {codigo} no pertenece a ningun producto en stock')
            return
        
        if cantidad<=self.productos[codigo]["cantidad"]:
            self.productos[codigo]["cantidad"]-=cantidad
            print(f"Venta exitosa. Stock restante de {codigo}: {self.productos[codigo]['cantidad']}")
            return
        print(f"No hay cantidad disponible para de {codigo} para vender. Stock actual ({self.productos[codigo]['cantidad']})")
        return
    
    def valor_total_inventario(self)->float:
        total=0.0
        for producto in self.productos.values():
            total+=producto["producto"].precio*producto["cantidad"]
        return total

    def __str__(self) -> str:
        """Devuelve una representación en string del inventario completo."""
        if not self.productos:
            return "El inventario está vacío."
        
        # Se construye un encabezado para el reporte.
        reporte = "--- Reporte de Inventario ---\n"
        reporte += f"{'Código':<8} | {'Producto':<25} | {'Cantidad':<10} | {'Subtotal':>15}\n"
        reporte += "-" * 70 + "\n"
        
        # Se itera sobre los productos para agregar cada línea al reporte.
        for item in self.productos.values():
            subtotal = item["producto"].precio * item["cantidad"]  
            reporte += f"{item["producto"].codigo:<8} | {item["producto"].nombre:<25} | {item["cantidad"]:<10} | ${subtotal:14,.2f}\n"
            
        # Se agrega el valor total al final.
        reporte += "-" * 70 + "\n"
        reporte += f"Valor total del inventario: ${self.valor_total_inventario():,.2f}\n"
        
        return reporte
    
# Creamos productos
print("### Solución Ejercicio 1 ###\n")
celular = Producto("CEL-01", "Smartphone Modelo X", 45000.0)
tablet = Producto("TAB-05", "Tablet Modelo Y", 68000.0)
 # Creamos el stock y agregamos productos
mi_stock = Stock()
mi_stock.agregar_producto(celular, 10)
mi_stock.agregar_producto(tablet, 5)
mi_stock.agregar_producto(celular, 5) # Agregamos más del mismo producto

 # Verificamos el valor total
print(f"Valor total del inventario: ${mi_stock.valor_total_inventario()}")
#Valor total del inventario: $1015000.0

 # Realizamos una venta
mi_stock.vender_producto("CEL-01", 8)
mi_stock.vender_producto("TAB-05", 6) # Intento de venta fallido
#No hay suficiente stock para vender 6 unidades del producto TAB-05.

 # Verificamos el nuevo valor del inventario
print(f"Nuevo valor del inventario: ${mi_stock.valor_total_inventario()}")
#Nuevo valor del inventario: $655000.0

print(mi_stock)

"""Ejercicio 3: Jerarquía de Vehículos
Este ejercicio está diseñado para practicar la herencia y la sobrescritura de métodos (override), siguiendo la línea de los ejercicios de Animales y Jugador.

Consigna:
Crea una jerarquía de clases para modelar diferentes tipos de vehículos.

Clase Padre Vehiculo:
    Atributos de instancia: marca (string) y velocidad_maxima (int).
    Un método __str__ que devuelva una descripción básica del vehículo.
    Un método acelerar() que imprima un mensaje genérico como "El vehículo está acelerando.".

Clase Hija Coche (hereda de Vehiculo):
    Un atributo de instancia adicional: tipo_combustible (string, ej: "Gasolina", "Eléctrico").
    Sobrescribe el constructor __init__ para incluir el nuevo atributo. Usa super() para llamar al constructor de la clase padre.
    Sobrescribe el método acelerar() para que imprima "El coche está acelerando en la carretera.".

Clase Hija Bicicleta (hereda de Vehiculo):
    Un atributo de instancia adicional: tipo_terreno (string, ej: "Montaña", "Urbana").
    Sobrescribe el constructor __init__ para incluir el nuevo atributo. Usa super().
    Sobrescribe el método acelerar() para que imprima "La bicicleta gana velocidad pedaleando.".
    Un método propio llamado pedalear() que imprima "Pedaleando con esfuerzo."."""

class Vehiculo:
    def __init__(self, marca:str, velocidad_maxima:int)->None:
        self.marca=marca
        self.velocidad_maxima=velocidad_maxima
    def __str__(self)->str:
        return f'El vehiculo es un {self.marca} y su velocidad maxima son los {self.velocidad_maxima} km/h'
    def acelerar(self)->None:
        print(f'El vehiculo esta acelerando')

class Coche(Vehiculo):
    def __init__(self, marca:str, velocidad_maxima:int, tipo_combustible:str)->None:
        super().__init__(marca, velocidad_maxima)
        self.tipo_combustible=tipo_combustible
    def acelerar(self)->None:
        print(f'El coche esta acelerando en la carretera')

class Bicicleta(Vehiculo):
    def __init__(self, marca:str, velocidad_maxima:int, tipo_terreno:str)->None:
        super().__init__(marca, velocidad_maxima)
        self.tipo_terreno=tipo_terreno
    def acelerar(self)->None:
        print(f'La bicicleta gana velocidad pedaleando.')
    def pedalear(self)->None:
        print(f'Pedaleando con esfuerzo.')

# --- Ejemplo de uso ---
print("\n### Solución Ejercicio 3 ###\n")
mi_coche = Coche("Toyota", 180, "Gasolina")
mi_bici = Bicicleta("Trek", 35, "Montaña")

print(mi_coche)
print(mi_bici)

mi_coche.acelerar()
mi_bici.acelerar()
mi_bici.pedalear()
print("-" * 20)

"""Ejercicio 4: Gestión de una Playlist Musical (Composición)
Este ejercicio es similar al de Stock y Producto. Deberás crear una clase para representar una canción y otra para representar una playlist que contendrá una colección de canciones.

Consigna:
Define dos clases: Cancion y Playlist.

La clase Cancion debe tener los siguientes atributos de instancia:
    titulo (string)
    artista (string)
    duracion (int, en segundos)

La clase Playlist se compondrá de objetos Cancion y deberá tener:
    Un atributo de instancia nombre (string).
    Un atributo de instancia canciones, que será una lista para almacenar los objetos Cancion.

La clase Playlist deberá implementar los siguientes métodos de instancia:
    agregar_cancion(cancion: Cancion): Añade una canción al final de la playlist.
    eliminar_cancion(titulo: str): Busca una canción por su título y la elimina de la playlist. Si no la encuentra, no debe hacer nada.
    duracion_total(): Calcula y devuelve la duración total de la playlist en segundos (la suma de la duración de todas sus canciones).
    __str__(): Devuelve una representación en texto de la playlist, mostrando su nombre y la lista de canciones que contiene, junto con la duración total en formato "minutos:segundos"."""

class Cancion:
    def __init__(self, titulo:str, artista:str, duracion:int)->None:
        self.titulo=titulo
        self.artista=artista
        self.duracion=duracion
    def __str__(self)->str:
        minutos=self.duracion//60
        segundos=self.duracion%60
        return f'La cancion se llama {self.titulo} de {self.artista} y dura ({minutos}:{segundos:02}).'
class Playlist:
    def __init__(self, nombre:str)->None:
        self.nombre=nombre
        self.canciones:list[Cancion]=[]
    def agregar_cancion(self, cancion:Cancion)->None:
        if cancion not in self.canciones:
            self.canciones.append(cancion)
    def eliminar_cancion(self, titulo:str)->None:
        lista=[cancion for cancion in self.canciones if cancion.titulo != titulo]
        self.canciones=lista   
    def eliminar_cancion(self, titulo:str)->None:
        for cancion in self.canciones:
            if titulo == cancion.titulo:
                self.canciones.remove(cancion)
                return
        return
    def duracion_total(self)->int:
        total=0
        for cancion in self.canciones:
            total+=cancion.duracion
        return total
    def __str__(self)->str:
        if not self.canciones:
            return f'PLAYLIST: {self.nombre} esta vacia'
        
        resultado=f"----------------PLAYLIST: {self.nombre}----------------\n"
        for cancion in self.canciones:
            resultado+=f"Cancion: {cancion.titulo:<18} | Artista: {cancion.artista:<12} | Duracion: {cancion.duracion//60}:{cancion.duracion%60:02} |\n"
        resultado+="-"*60+"\n"
        resultado+=f"Duracion total lista: {self.duracion_total()//60}:{self.duracion_total()%60:02}\n"
        return resultado

# --- Ejemplo de uso ---
print("\n### Solución Ejercicio 4 ###\n")
cancion1 = Cancion("Bohemian Rhapsody", "Queen", 355)
cancion2 = Cancion("Stairway to Heaven", "Led Zeppelin", 482)
cancion3 = Cancion("Hotel California", "Eagles", 391)

mi_playlist = Playlist("Clásicos del Rock")
mi_playlist.agregar_cancion(cancion1)
mi_playlist.agregar_cancion(cancion2)
mi_playlist.agregar_cancion(cancion3)

print(mi_playlist)

print("\n--- Después de eliminar una canción ---\n")
mi_playlist.eliminar_cancion("Stairway to Heaven")
print(mi_playlist)

"""Ejercicio 5: Jerarquía de Figuras Geométricas (Herencia)
Este ejercicio se enfoca en la herencia y el polimorfismo, similar al de Vehiculo. Crearás una clase base FiguraGeometrica y clases hijas que hereden de ella y proporcionen implementaciones específicas para calcular el área y el perímetro.

Consigna:
Crea una jerarquía de clases para modelar figuras geométricas.

Clase Padre FiguraGeometrica:
    Atributo de instancia: color (string).
    Un método __str__ que devuelva una descripción indicando que es una "Figura de color [color]".
    Dos métodos area() y perimetro(). En esta clase base, ambos métodos simplemente deben pass o retornar 0, ya que una figura genérica no tiene una fórmula para calcularlos.

Clase Hija Rectangulo (hereda de FiguraGeometrica):
    Atributos de instancia adicionales: base (float) y altura (float).
    Sobrescribe el constructor __init__ para incluir los nuevos atributos, utilizando super() para el color.
    Sobrescribe los métodos area() y perimetro() para que calculen y devuelvan los valores correctos para un rectángulo.
    Área: base * altura
    Perímetro: 2 * (base + altura)

Clase Hija Circulo (hereda de FiguraGeometrica):
    Atributo de instancia adicional: radio (float).
    Sobrescribe el constructor __init__ para incluir el nuevo atributo, utilizando super().
    Sobrescribe los métodos area() y perimetro(). Necesitarás importar el módulo math para usar math.pi.
    Área: π * radio²
    Perímetro (circunferencia): 2 * π * radio"""

class FiguraGeometrica:
    def __init__(self, color:str)->None:
        self.color=color
    def __str__(self) -> str:
        return f'Figura de color {self.color}'
    def area(self)->None:
        pass
    def perimetro(self)->None:
        pass
class Rectangulo(FiguraGeometrica):
    def __init__(self, color:str, base:float, altura:float)->None:
        super().__init__(color)
        self.base=base
        self.altura=altura
    def area(self)->float:
        return self.base*self.altura
    def perimetro(self)->float:
        return (self.base+self.altura)*2
    def __str__(self)->str:
        return f'La figura es un Rectangulo de color {self.color} de base {self.base} y altura {self.altura}'
class Circulo(FiguraGeometrica):
    def __init__(self, color:str, radio:float)->None:
        super().__init__(color)
        self.radio=radio
    def area(self)->float:
        return 3.14*(self.radio**2)
    def perimetro(self)->float:
        return 2*3.14*(self.radio)
    def __str__(self)->str:
        return f'La figura es un circulo de color {self.color} de radio {self.radio}'

# --- Ejemplo de uso ---
print("\n### Solución Ejercicio 5 ###\n")
mi_rectangulo = Rectangulo("Azul", 10, 5)
mi_circulo = Circulo("Rojo", 7)

# Probamos el rectángulo
print(mi_rectangulo)
print(f"Área del rectángulo: {mi_rectangulo.area()}")
print(f"Perímetro del rectángulo: {mi_rectangulo.perimetro()}")

print("-" * 30)

# Probamos el círculo
print(mi_circulo)
print(f"Área del círculo: {mi_circulo.area():.2f}")
print(f"Perímetro del círculo: {mi_circulo.perimetro():.2f}")

"""Ejercicio 6: Sistema de Gestión de una Biblioteca (Composición)
Este ejercicio es similar al de Playlist y Stock. Deberás modelar un Libro y una Biblioteca que gestiona una colección de libros.

Consigna:
Define dos clases: Libro y Biblioteca.
    La clase Libro debe tener los siguientes atributos de instancia:
    titulo (string)
    autor (string)
    isbn (string, un identificador único como "978-3-16-148410-0")
    prestado (booleano, se inicializa en False)

La clase Biblioteca se compondrá de objetos Libro y deberá tener:
    Un atributo de instancia catalogo, que será un diccionario. La clave será el isbn del libro y el valor será el objeto Libro.
    La clase Biblioteca deberá implementar los siguientes métodos de instancia:
    agregar_libro(libro: Libro): Añade un libro al catálogo. Si ya existe un libro con el mismo ISBN, no debe hacer nada.
    prestar_libro(isbn: str): Busca un libro por su ISBN. Si el libro existe y no está prestado, cambia su estado a prestado=True y devuelve True. 
Si el libro no existe o ya está prestado, devuelve False.
    devolver_libro(isbn: str): Busca un libro por su ISBN. Si el libro existe y está prestado, cambia su estado a prestado=False y devuelve True. En cualquier otro caso, devuelve False.
    __str__(): Devuelve una representación en texto del catálogo de la biblioteca, mostrando el título, autor y estado ("Disponible" o "Prestado") de cada libro."""

class Libro:
    def __init__(self, titulo:str, autor:str, isbn:str, prestado:bool=False)->None:
        self.titulo=titulo
        self.autor=autor
        self.isbn=isbn
        self.prestado=prestado
    def __str__(self)->str:
        return f'El libro {self.titulo} de {self.autor}. ISBN: {self.isbn}. Estado: {self.prestado}'
class Biblioteca:
    def __init__(self)->None:
        self.catalogo:dict[str,Libro]={}
    def agregar_libro(self, libro:Libro)->None:
        if libro.isbn not in self.catalogo:
            self.catalogo[libro.isbn]=libro
    def prestar_libro(self, isbn:str)->bool:
        if isbn in self.catalogo and self.catalogo[isbn].prestado is False:
            self.catalogo[isbn].prestado=True
            return True
        else:
            return False
    def devolver_libro(self, isbn:str)->bool:
        if isbn in self.catalogo and self.catalogo[isbn].prestado is True:
            self.catalogo[isbn].prestado=False
            return True
        return False
    def __str__(self)->str:
        if not self.catalogo:
            return f'No hay libros en el catalogo'
        
        resultado="------- Catalogo de la biblioteca -------\n"
        resultado+= f"{'Titulo':<25} | {'Autor':<25} | {'ISBN':<15} | {'Estado':<10} |\n"
        for libro in self.catalogo.values():
            if libro.prestado is True:
                estado= "Prestado"
            else:
                estado="Disponible"
            resultado+= f'{libro.titulo:<25} | {libro.autor:<25} | {libro.isbn:<15} | {estado:<10} |\n'
        return resultado



# --- Ejemplo de uso ---
print("\n### Solución Ejercicio 6 ###\n")
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-0307350434")
libro2 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", "978-0618640157")

mi_biblioteca = Biblioteca()
mi_biblioteca.agregar_libro(libro1)
mi_biblioteca.agregar_libro(libro2)

mi_biblioteca.prestar_libro("978-0307350434")

print(mi_biblioteca)

mi_biblioteca.devolver_libro("978-0307350434")

print("\n--- Después de la devolución ---\n")
print(mi_biblioteca)
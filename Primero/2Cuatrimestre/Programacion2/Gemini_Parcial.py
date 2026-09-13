"""Ejercicio 1: Recursión y Potencia
Implemente una función recursiva llamada potencia_rec que reciba como parámetros dos números enteros, una base b y un exponente n (con n >= 0), 
y que calcule b^n. Para su implementación, considere las siguientes propiedades matemáticas:
    b^n=1 si n=0
    b^n=(b^n/2)^2 si n es par
    b^n=b*b^(n-1) si n es impar
Escriba, además, una función iterativa potencia_it que resuelva el mismo problema."""
def potencia_rec(b:int, n:int)->int:
    if n==0:
        return 1
    if n%2!=0:
        return b*potencia_rec(b,n-1)
    else:
        return b*potencia_rec(b,n//2)
print(potencia_rec(2,3))
print(potencia_rec(2,2))

def potencia_it(b:int, n:int)->int:
    resultado=1
    for _ in range(n):
        resultado*=b
    return resultado
print(potencia_it(2,3))
print(potencia_it(2,2))

"""1. Cálculo de Productoria
Implemente una función recursiva llamada productoria_rec que reciba como parámetro una lista de números enteros y devuelva el producto de todos sus elementos. Si la lista está vacía, debe devolver 1.

Escriba, además, una función iterativa productoria_it que sea equivalente.

Justificación de diseño: Este ejercicio evalúa la capacidad de traducir un concepto matemático simple a dos paradigmas de programación distintos, 
un desafío similar al de contar_ocurrencias en los parciales originales. La lógica se deriva directamente del concepto de caso base y caso recursivo explicado en los apuntes de recursión."""
def productoria_rec(lista:list[int])->int:
    if not lista:
        return 1
    return lista[0]*productoria_rec(lista[1:])
print(productoria_rec([1,2,3,4]))
print(productoria_rec([]))

def productoria_it(lista:list[int])->int:
    if not lista:
        return 1
    total=1
    for num in lista:
        total*=num
    return total
print(productoria_it([1,2,3,4]))
print(productoria_it([]))

"""Ejercicio 2: Complejidad Temporal
Analice el siguiente algoritmo y determine su orden de complejidad temporal (notación O grande). Explique detalladamente el razonamiento utilizado 
para llegar a esa conclusión, contando las operaciones más relevantes que realiza la función."""

def procesar_datos1(matriz: list[list[int]]) -> int:
    """
    Procesa una matriz cuadrada (n x n).
    """
    n = len(matriz)                 #1
    suma_total = 0                       #1
    # Bucle 1
    for i in range(n):                   #n
        print(f"Procesando fila {i}")    #1
        suma_total += matriz[i][i]       #2 --->Total=3n=O(n)
    # Bucle 2
    for i in range(n):                   #n
        for j in range(i, n):            #n-i
            print(f"Analizando elemento ({i}, {j})") #1
            suma_total += matriz[i][j] * 2          #3--->Total bucle= n*n-i*(4)=n*(4n-4i)=4n2-4ni
    return suma_total                   #1
#Complejidad O(n2)

"""2. Análisis de Complejidad Temporal
Indique el orden de complejidad temporal del siguiente algoritmo. Explique lo más detalladamente posible cómo obtiene esa complejidad, 
basándose en el análisis de sus bucles y operaciones."""
def procesar_datos2(datos: list[int]) -> int:
    n = len(datos)                  #1
    total = 0                            #1
    # Bucle 1
    for i in range(n):                  #n
        for j in range(n):              #n
            total += datos[i] * datos[j] #1 ---> Total bucle: n*n*1=n2 O(n2)
    # Bucle 2
    for k in range(n):                  #n
        print(f"Procesando elemento {k}") #1 ---> Total bucle=n O(n)
    # Bucle 3
    for _ in range(10):                 #10
        total -= 1                      #1 ---> Total bucle=10
    return total                        #1
#Complejidad O(n2), la mas importante la del bucle1

"""Ejercicio 6: Sistema de Gestión de una Biblioteca (Composición)
Este ejercicio es similar al de Playlist y Stock. Deberás modelar un Libro y una Biblioteca que gestiona una colección de libros.

Consigna:
Define dos clases: Libro y Biblioteca.

La clase Libro debe tener los siguientes atributos de instancia:
    * titulo (string)
    * autor (string)
    * isbn (string, un identificador único como "978-3-16-148410-0")
    * prestado (booleano, se inicializa en False)

La clase Biblioteca se compondrá de objetos Libro y deberá tener:
    Un atributo de instancia catalogo, que será un diccionario. La clave será el isbn del libro y el valor será el objeto Libro.

La clase Biblioteca deberá implementar los siguientes métodos de instancia:
    * agregar_libro(libro: Libro): Añade un libro al catálogo. Si ya existe un libro con el mismo ISBN, no debe hacer nada.
    * prestar_libro(isbn: str): Busca un libro por su ISBN. Si el libro existe y no está prestado, cambia su estado a prestado=True 
y devuelve True. Si el libro no existe o ya está prestado, devuelve False.
    * devolver_libro(isbn: str): Busca un libro por su ISBN. Si el libro existe y está prestado, cambia su estado a prestado=False 
y devuelve True. En cualquier otro caso, devuelve False.
    * __str__(): Devuelve una representación en texto del catálogo de la biblioteca, mostrando el título, autor y estado ("Disponible" o "Prestado") de cada libro."""

class Libro:
    def __init__(self, titulo:str, autor:str, isbn:str,)->None:
        self.isbn=isbn
        self.titulo=titulo
        self.autor=autor
        self.prestado=False #por defecto
    def __str__(self)->str:
        if self.prestado is True:
            estado="Prestado"
        else:
            estado="Disponible"
        return f'Libro: {self.titulo} de {self.autor} codigo: {self.isbn} y su estado es {estado}'

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
        return False
    
    def devolver_libro(self, isbn:str)->bool:
        if isbn in self.catalogo and self.catalogo[isbn].prestado is True:
            self.catalogo[isbn].prestado=False
            return True
        return False
    
    def __str__(self)->str:
        if not self.catalogo:
            return f'No hay libros disponibles en el catalogo\n'
        resultado=" | Catalogo de libros disponibles\n"
        resultado+=f' | {'ISBN':<15} | {'Titulo':<25} | {'Autor':<25} | {'Estado':<15} | \n'
        for libro in self.catalogo.values():
            if libro.prestado is True:
                estado='Prestado'
            else:
                estado='Disponible'
            resultado+=f' | {libro.isbn:<15} | {libro.titulo:<25} | {libro.autor:<25} | {estado:<15} | \n'
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

print("\n--- Después de la devolución ---")
print(mi_biblioteca)

    
"""Ejercicio 1: Suma de Dígitos
Implemente una función recursiva llamada sumar_digitos_rec que reciba como parámetro un número entero no negativo 
y devuelva la suma de sus dígitos. Por ejemplo, sumar_digitos_rec(123) debería devolver 6 (porque 1+2+3=6).

Escriba, además, una función iterativa sumar_digitos_it que resuelva el mismo problema.
Ayuda: Para la versión recursiva, piense en un caso base (un número de un solo dígito) y en cómo reducir el problema 
en cada llamada (por ejemplo, utilizando el cociente // y el resto % de la división por 10)."""

def sumar_digitos_rec(n:int)->int:
    if 0<=n<10:
        return n
    return sumar_digitos_rec(n//10)+(n%10)
def sumar_digitos_it(n:int)->int:
    suma=0
    while n>0:
        suma+=n%10
        n=n//10
    return suma
numero = 9524
print(f"Recursivo: La suma de los dígitos de {numero} es {sumar_digitos_rec(numero)}") # Resultado: 20
print(f"Iterativo: La suma de los dígitos de {numero} es {sumar_digitos_it(numero)}")   # Resultado: 20

"""Ejercicio 2: Complejidad Temporal
Indique el orden de complejidad temporal (notación O grande) del siguiente algoritmo. Explique detalladamente su razonamiento, 
identificando las operaciones más significativas y cómo su número escala con el tamaño de la entrada n"""

def algoritmo_misterioso(n: int) -> None:
    """
    Realiza una serie de operaciones basadas en el entero n.
    """
    # Bucle 1
    for i in range(n):                  #n
        # Bucle interno con un número fijo de iteraciones
        for j in range(10):             #10
            print(f"Procesando ({i}, {j})") #1 --->Total bucle:n*10=O(n)
    # Bucle 2
    for k in range(n):                  #n
        print(f"Paso final {k}")        #1  --->Total bucle:n O(n)
 #Total O(n)

"""Ejercicio 3: Sistema de Carrito de Compras
Implemente un sistema simple de carrito de compras utilizando programación orientada a objetos. Para ello, deberá implementar las clases que se especifican a continuación.

1. Implementación de la clase Producto:
Implemente una clase Producto con los siguientes atributos de instancia:
    id_producto (str): el código de identificación único del producto.
    nombre (str): el nombre del producto.
    precio (float): el precio unitario del producto.

La clase debe incluir:
    Un método constructor __init__ para inicializar todos los atributos.
    Un método __str__ que devuelva una representación en cadena del producto (por ejemplo: "ID: P001, Nombre: Teclado, Precio: $50.0").

2. Implementación de la clase CarritoDeCompras:
Implemente una clase CarritoDeCompras para gestionar una colección de productos. Tendrá el siguiente atributo:
    items (dict[str, int]): un diccionario donde la clave es el id_producto y el valor es la cantidad de ese producto en el carrito.

Esta clase debe tener los siguientes métodos:
    * __init__(): Crea un carrito de compras vacío.
    * agregar_item(producto: Producto, cantidad: int): Recibe un objeto de tipo Producto y una cantidad. Si el producto ya está en el carrito, 
incrementa su cantidad. Si no está, lo agrega al diccionario items. No devuelve nada.
    * eliminar_item(id_producto: str): Recibe el ID de un producto y lo elimina completamente del carrito. 
Si el producto no existe en el carrito, no debe hacer nada.
    * calcular_total() -> float: Recorre los items del carrito y, utilizando la información de una lista de productos disponibles que recibe como parámetro, calcula y devuelve 
el precio total de la compra. Este método deberá recibir como parámetro un diccionario de productos disponibles (clave: id_producto, valor: objeto Producto) para poder consultar sus precios.
    * mostrar_carrito(): Muestra por pantalla de forma clara todos los productos en el carrito, incluyendo nombre, cantidad y precio unitario. Similar al método calcular_total,
necesitará recibir el diccionario de productos disponibles como parámetro."""
class Producto:
    def __init__(self, id_producto:str, nombre:str, precio:float)->None:
        self.id_producto=id_producto
        self.nombre=nombre
        self.precio=precio
    def __str__(self)->str:
        return f'ID: {self.id_producto} | Producto: {self.nombre} | Precio: $ {self.precio} '
class CarritoDeCompras:
    def __init__(self)->None:
        self.items:dict[str,int]={}

    def agregar_item(self, producto:Producto, cantidad:int)->None:
        if producto.id_producto in self.items:
            self.items[producto.id_producto]+=cantidad
        else:
            self.items[producto.id_producto]=cantidad
    def eliminar_items(self, id_producto:str)->None:
        if id_producto in self.items:
            self.items.pop(id_producto)

    def calcular_total(self, productos_disponibles:dict[str,Producto])->float:
        total=0.0
        for id, cantidad in self.items.items():
            if id in productos_disponibles:
                total+=cantidad*productos_disponibles[id].precio
        return total
    
    def mostrar_carrito(self, productos_disponibles:dict[str,Producto])->None:
        if not self.items:
            print(f'Carrito esta vacio\n')
            return
        
        print(f'\n| Listado de productos en el carrito:')
        print(f'| {'ID':<4} | {'Producto':<20} |  {'Precio':<5} | {'cantidad':<8} | {'Precio Total':<10} | ')
        # Recorremos solo los items que están EN EL CARRITO
        for id, cantidad in self.items.items():
            if id in productos_disponibles:
                producto=productos_disponibles[id]
                print(f'| {id:<4} | {producto.nombre:<20} | $ {producto.precio:<5} | {self.items[id]:<8} | $ {producto.precio*cantidad:<10} | ') 
        print(f'| Total carrito: $ {self.calcular_total(productos_disponibles)}\n')

# Catálogo de productos disponibles en la tienda
catalogo_tienda = {
    "P001": Producto("P001", "Teclado Mecánico", 55.00),
    "P002": Producto("P002", "Mouse Gamer", 25.50),
    "P003": Producto("P003", "Monitor 24 pulgadas", 150.00)
}

# Crear un carrito de compras
mi_carrito = CarritoDeCompras()

# Agregar items
mi_carrito.agregar_item(catalogo_tienda["P001"], 1)
mi_carrito.agregar_item(catalogo_tienda["P002"], 2)
mi_carrito.agregar_item(catalogo_tienda["P001"], 3) # Agrega otra unidad del mismo producto

# Mostrar contenido y total
mi_carrito.mostrar_carrito(catalogo_tienda)
total_compra = mi_carrito.calcular_total(catalogo_tienda)
print(f"Total a pagar: ${total_compra:.2f}")

# Eliminar un item
mi_carrito.eliminar_items("P002")
mi_carrito.mostrar_carrito(catalogo_tienda)
total_compra = mi_carrito.calcular_total(catalogo_tienda)
print(f"Nuevo total a pagar: ${total_compra:.2f}")

"""Ejercicio 1: Búsqueda del Máximo Elemento
Implemente una función recursiva llamada encontrar_maximo_rec que reciba como parámetro una lista de números enteros y devuelva el número más grande de la lista.
 Puede asumir que la lista no estará vacía.

Escriba, además, una función iterativa encontrar_maximo_it que resuelva el mismo problema."""

def encontrar_maximo_rec(lista:list[int])->int:
    if len(lista)==1:
        return lista[0]
    if lista[0]> encontrar_maximo_rec(lista[1:]):
        return lista[0]
    else:
        return encontrar_maximo_rec(lista[1:])

def encontrar_maximo_it(lista:list[int])->int:
    max=lista[0]
    for num in lista[1:]:
        if num>max:
            max=num
    return max
numeros = [12, 45, 8, 99, 23, 56]
print(f"Recursivo: El máximo es {encontrar_maximo_rec(numeros)}") # Resultado: 99
print(f"Iterativo: El máximo es {encontrar_maximo_it(numeros)}")   # Resultado: 99

"""Ejercicio 2: Complejidad Temporal
Determine el orden de complejidad temporal (notación O grande) del siguiente algoritmo. Justifique su respuesta explicando detalladamente cómo la 
cantidad de operaciones escala en función del tamaño de la lista de entrada, n"""

def calculo_complejo(lista: list[int]) -> int:
    """
    Realiza un cálculo sobre una lista de enteros.
    """
    n = len(lista)  #1
    resultado = 0        #1
    for i in range(n):   #n
        for j in range(i, n): #n-i  si i=0->n i=1 -> n-1  i=2 -> n-2 
            # Esta operación se considera de tiempo constante O(1)
            resultado += lista[i] * lista[j] #O(1)--> Total bucle es n*(n+1)/2=n2/2+n/2
    return resultado #1
#Total= 1+1+n2/2+n/2+1=3+n2/2+n/2->O(n2)

"""Ejercicio 3: Sistema de Pedidos de un Restaurante
Implemente un sistema de gestión de pedidos para un restaurante utilizando programación orientada a objetos. Para ello, deberá implementar las clases que se especifican a continuación.

1. Implementación de la clase Plato:
Implemente una clase Plato con los siguientes atributos de instancia:
    id_plato (str): el código de identificación único del plato.
    nombre (str): el nombre del plato.
    precio (float): el precio del plato.

La clase debe incluir:
    Un método constructor __init__ para inicializar todos los atributos.
    Un método __str__ que devuelva una representación en cadena del plato (ej: "ID: C01, Nombre: Milanesa con Papas, Precio: $3500.00").

2. Implementación de la clase Pedido:
Implemente una clase Pedido que gestione la comanda de una mesa. Tendrá los siguientes atributos:
    numero_mesa (int): el número de la mesa que realiza el pedido.
    items (dict[str, int]): un diccionario donde la clave es el id_plato y el valor es la cantidad solicitada de dicho plato.

Esta clase debe tener los siguientes métodos:

    __init__(numero_mesa: int): Crea un pedido para una mesa específica, con una lista de ítems vacía.
    agregar_plato(plato: Plato, cantidad: int): Agrega una cantidad de un plato al pedido. Si el plato ya fue pedido, simplemente incrementa la cantidad.
    calcular_total(menu_disponible: dict[str, Plato]) -> float: Recibe como parámetro el menú del restaurante (un diccionario de objetos Plato) 
y calcula el costo total del pedido.
    mostrar_pedido(menu_disponible: dict[str, Plato]): Recibe el menú del restaurante y muestra por pantalla un detalle del pedido, 
incluyendo el nombre de cada plato, la cantidad pedida, el precio unitario y el subtotal por ítem, finalizando con el total general."""

class Plato:
    def __init__(self, id_plato:str, nombre:str, precio:float)->None:
        self.id_plato=id_plato
        self.nombre=nombre
        self.precio=precio
    def __str__(self)->str:
        return f'| ID: {self.id_plato:<4} | Plato: {self.nombre:<15} | Precio: $ {self.precio:<6} |'

class Pedido:
    def __init__(self, numero_mesa:int)->None:
        self.items:dict[str,int]={}
        self.numero_mesa=numero_mesa

    def agregar_plato(self, plato:Plato, cantidad:int)->None:
        if plato.id_plato not in self.items:
            self.items[plato.id_plato]=cantidad
        else:
            self.items[plato.id_plato]+=cantidad
    
    def calcular_total(self, menu_disponible:dict[str,Plato])->float:
        total=0.0
        for id, cantidad in self.items.items():
            if id in menu_disponible:
                total+=cantidad*menu_disponible[id].precio
        return total
    
    def mostrar_pedido(self, menu_disponible:dict[str, Plato])->None:
        if not self.items:
            print(f'No hay pedidos para la mesa {self.numero_mesa}')
        
        print(f'\n| Detalle Pedido para la mesa {self.numero_mesa}: ')
        print(f'| {'Plato':<25} | {'Cantidad':<8} | {'Precio':<6} | {'Subtotal':<8} |')
        for id, cantidad in self.items.items():
            if id in menu_disponible:
                plato=menu_disponible[id]
                print(f'| {plato.nombre:<25} | {cantidad:<8} | {plato.precio:<6} | {cantidad*plato.precio:<8} |')
        print(f'| Total de la mesa {self.numero_mesa}: $ {self.calcular_total(menu_disponible)}')
# Menú del restaurante
menu = {
    "C01": Plato("C01", "Milanesa con Papas", 3500.00),
    "B01": Plato("B01", "Agua sin gas", 800.00),
    "P01": Plato("P01", "Flan con dulce de leche", 1500.00)}
# Crear un pedido para la mesa 5
pedido_mesa_5 = Pedido(5)
# Agregar platos
pedido_mesa_5.agregar_plato(menu["C01"], 2) # Dos milanesas
pedido_mesa_5.agregar_plato(menu["B01"], 3) # Tres aguas
pedido_mesa_5.agregar_plato(menu["P01"], 1) # Un flan
# Mostrar el detalle del pedido
pedido_mesa_5.mostrar_pedido(menu)
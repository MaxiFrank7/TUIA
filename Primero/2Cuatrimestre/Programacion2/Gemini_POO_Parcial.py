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
print("#"*60)
print("##### Solución Ejercicio Libros #####\n")
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
print("#"*60)
print("##### Solución Ejercicio carrito #####")
mi_carrito.mostrar_carrito(catalogo_tienda)
total_compra = mi_carrito.calcular_total(catalogo_tienda)
print(f"Total a pagar: ${total_compra:.2f}")

# Eliminar un item
mi_carrito.eliminar_items("P002")
print("\n--- Después de la devolución P002 ---")
mi_carrito.mostrar_carrito(catalogo_tienda)
total_compra = mi_carrito.calcular_total(catalogo_tienda)
print(f"Nuevo total a pagar: ${total_compra:.2f}")

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
print('\n'+'#'*60)
print("##### Solución Ejercicio platos #####")
pedido_mesa_5.mostrar_pedido(menu) 

"""Ejercicio 3: Sistema de Gestión de Tareas
Implemente un sistema simple para gestionar una lista de tareas (To-Do list) utilizando programación orientada a objetos. Para ello, deberá implementar las clases que se especifican a continuación.

1. Implementación de la clase Tarea:
Implemente una clase Tarea con los siguientes atributos de instancia:
    id_tarea (int): un número de identificación único para la tarea.
    descripcion (str): el texto que describe la tarea.
    completada (bool): un estado que indica si la tarea ha sido completada (True) o está pendiente (False).

La clase debe incluir:
    Un método constructor __init__ para inicializar todos los atributos. Por defecto, una nueva tarea debe estar en estado pendiente (completada = False).
    Un método __str__ que devuelva una representación en cadena de la tarea, indicando su estado. Por ejemplo: "[X] ID 1: Comprar leche" si está completada, 
o "[ ] ID 1: Comprar leche" si está pendiente.
    Un método marcar_como_completada() que cambie el estado de la tarea a True.

2. Implementación de la clase GestionTareas:
Implemente una clase GestionTareas que administre una colección de tareas. Tendrá los siguientes atributos:
    tareas (dict[int, Tarea]): un diccionario donde la clave es el id_tarea y el valor es el objeto Tarea correspondiente.
    siguiente_id (int): un contador para asignar automáticamente un ID único a cada nueva tarea.

Esta clase debe tener los siguientes métodos:
    __init__(): Crea un gestor con una lista de tareas vacía y el siguiente_id inicializado en 1.
    agregar_tarea(descripcion: str): Recibe una descripción, crea una nueva Tarea con un ID único (usando y luego incrementando siguiente_id), 
y la agrega al diccionario de tareas.
    completar_tarea(id_tarea: int) -> bool: Recibe el ID de una tarea y, si existe, la marca como completada utilizando el método de la clase Tarea. 
Devuelve True si la tarea se encontró y se marcó; False en caso contrario.
    eliminar_tarea(id_tarea: int) -> bool: Recibe el ID de una tarea y la elimina del diccionario. Devuelve True si la tarea existía y fue eliminada; 
False si no se encontró.
    mostrar_tareas_pendientes(): Muestra por pantalla todas las tareas que aún no han sido completadas."""

class Tarea:
    def __init__(self, id_tarea:int, descripcion:str, completada:bool=False)->None:
        self.id_tarea=id_tarea
        self.descripcion=descripcion
        self.completada=completada
    def __str__(self)->str:
        if self.completada is True:
            estado="X"
        else:
            estado=""
        return f'[{estado}] ID {self.id_tarea}: {self.descripcion}'
    def marcar_como_completada(self)->None:
        self.completada=True

class GestionTareas:
    def __init__(self)->None:
        self.tareas:dict[int,Tarea]={}
        self.siguiente_id=1
    def agregar_tarea(self, descripcion:str)->None:
        nueva_tarea=Tarea(self.siguiente_id, descripcion)
        self.tareas[self.siguiente_id]=nueva_tarea
        print(f'Se agrego la tarea: {descripcion} con ID: {self.siguiente_id}.')
        self.siguiente_id+=1
    def completar_tarea(self, id_tarea:int)->bool:
        if id_tarea in self.tareas:
            self.tareas[id_tarea].marcar_como_completada()
            return True
        return False
    def eliminar_tarea(self, id_tarea:int)->bool:
        if id_tarea in self.tareas:
            self.tareas.pop(id_tarea)
            return True
        print(f'El {id_tarea} no corresponde a ninguna tarea')
        return False
    def mostrar_tareas_pendientes(self)->None:
        if not self.tareas:
            print(f'No hay tareas pendientes')
            return
        print(f'\n| Listado de tareas pendientes: ')
        tarea_pendientes=[]
        for tarea in self.tareas.values():
            if tarea.completada is False:
                #print(f'| {tarea.id_tarea:<4} | {tarea.descripcion:<20} |')
                #print(tarea)
                tarea_pendientes.append(tarea)
        for tarea in tarea_pendientes:
            print(tarea)
        print(f'| Fin listado de tareas pendientes ---------- ')

# Crear un gestor de tareas
mi_lista = GestionTareas()

# Agregar tareas
print('\n'+'#'*60)
print(f'##### Ejercicio de Tareas #####\n')
mi_lista.agregar_tarea("Comprar pan")
mi_lista.agregar_tarea("Estudiar para el parcial de Programación II")
mi_lista.agregar_tarea("Hacer ejercicio")
# Mostrar tareas pendientes
mi_lista.mostrar_tareas_pendientes()
# Completar una tarea
mi_lista.completar_tarea(1)
# Eliminar una tarea
mi_lista.eliminar_tarea(3)
# Mostrar tareas pendientes de nuevo
mi_lista.mostrar_tareas_pendientes()

"""Ejercicio 3: Sistema de Cuentas Bancarias
Implemente un sistema simple para la gestión de cuentas bancarias utilizando programación orientada a objetos. Para ello, deberá implementar las clases que se especifican a continuación.

1. Implementación de la clase Cuenta:
Implemente una clase Cuenta con los siguientes atributos de instancia:
    numero_cuenta (str): el número de identificación único de la cuenta.
    titular (str): el nombre del titular de la cuenta.
    saldo (float): el dinero disponible en la cuenta.

La clase debe incluir:
    Un método constructor __init__ que inicialice todos los atributos. El saldo inicial debe ser un parámetro.
    Un método __str__ que devuelva una representación en cadena de la cuenta (ej: "Cuenta N° 12345 | Titular: Juan Perez | Saldo: $50000.00").
    Un método depositar(monto: float) que recibe un monto y lo suma al saldo.
    Un método retirar(monto: float) -> bool que resta un monto del saldo solo si hay fondos suficientes. Devuelve True si la operación fue exitosa y False en caso contrario.

2. Implementación de la clase Banco:
Implemente una clase Banco que administre una colección de cuentas. Tendrá el siguiente atributo:
    cuentas (dict[str, Cuenta]): un diccionario donde la clave es el numero_cuenta y el valor es el objeto Cuenta correspondiente.

Esta clase debe tener los siguientes métodos:
    __init__(): Crea un banco sin cuentas.
    crear_cuenta(cuenta: Cuenta): Recibe un objeto de tipo Cuenta y lo agrega al diccionario de cuentas, siempre y cuando no exista ya una cuenta con ese número.
    consultar_saldo(numero_cuenta: str): Recibe el número de una cuenta y, si existe, muestra su información por pantalla. Si no existe, informa el error.
    realizar_deposito(numero_cuenta: str, monto: float): Recibe un número de cuenta y un monto, y realiza el depósito en la cuenta 
correspondiente si esta existe.
    realizar_retiro(numero_cuenta: str, monto: float): Recibe un número de cuenta y un monto, e intenta realizar el retiro de la cuenta
correspondiente si esta existe. Informa si la operación fue exitosa o si no hubo fondos suficientes."""

class Cuenta:
    def __init__(self, numero_cuenta:str, titular:str, saldo:float)->None:
        self.numero_cuenta=numero_cuenta
        self.titular=titular
        self.saldo=saldo
    def __str__(self)->str:
        return f'Cuenta N° {self.numero_cuenta} | Titular: {self.titular} | Saldo: ${self.saldo}'
    def depositar(self, monto:float)->None:
        self.saldo+=monto
        print(f'Se depositaron ${monto} en la cuenta {self.numero_cuenta}')
    def retirar(self, monto:float)->bool:
        if self.saldo>=monto:
            self.saldo-=monto
            print(f'Se retiraron ${monto} en la cuenta {self.numero_cuenta}')
            return True
        print(f'Error al retirar, no hay saldo suficiente ({self.saldo}) en la cuenta {self.numero_cuenta}')
        return False
class Banco:
    def __init__(self)->None:
        self.cuentas:dict[str,Cuenta]={}
    def crear_cuenta(self, cuenta:Cuenta)->None:
        if cuenta.numero_cuenta not in self.cuentas:
            self.cuentas[cuenta.numero_cuenta]=cuenta
            
    def consultar_saldo(self, numero_cuenta:str)->None:
        if numero_cuenta in self.cuentas:
            print(self.cuentas[numero_cuenta])
            return
        else:
            print(f'El numero {numero_cuenta} no pertenece a una cuenta del banco')
            return
        
    def realizar_deposito(self, numero_cuenta:str, monto:float)->None:
        if numero_cuenta in self.cuentas:
            self.cuentas[numero_cuenta].depositar(monto)
            return
        else:
            print(f'El numero {numero_cuenta} no pertenece a una cuenta del banco')
            return
        
    def realizar_retiro(self, numero_cuenta:str, monto:float)->None:
        if numero_cuenta in self.cuentas:
            self.cuentas[numero_cuenta].retirar(monto)
            return
        else:
            print(f'El numero {numero_cuenta} no pertenece a una cuenta del banco')
            return

# Crear un banco
mi_banco = Banco()

# Crear instancias de Cuenta y agregarlas al banco
print('\n'+'#'*60)
print(f'##### Ejercicio de Banco #####')
cuenta1 = Cuenta("123-456", "Ana Lopez", 50000.0)
cuenta2 = Cuenta("789-012", "Carlos Gomez", 10000.0)
mi_banco.crear_cuenta(cuenta1)
mi_banco.crear_cuenta(cuenta2)

# Realizar operaciones
print("\n--- Operaciones ---")
mi_banco.consultar_saldo("123-456")
mi_banco.consultar_saldo("789-012")
mi_banco.realizar_deposito("123-456", 5000.0)
mi_banco.realizar_retiro("789-012", 12000.0) # Debería fallar
mi_banco.realizar_retiro("789-012", 8000.0)  # Debería ser exitoso
print("\n--- Luego de operaciones ---")
mi_banco.consultar_saldo("123-456")
mi_banco.consultar_saldo("789-012")

"""Ejercicio 3: Sistema de Inventario
Implemente un sistema simple para la gestión del inventario de una tienda utilizando programación orientada a objetos. Para ello, deberá implementar las clases que se especifican a continuación.

1. Implementación de la clase Producto: Implemente una clase Producto con los siguientes atributos de instancia:
    id_producto (str): el código de identificación único del producto.
    nombre (str): el nombre del producto.
    precio (float): el precio unitario del producto.
    stock (int): la cantidad de unidades disponibles del producto.

La clase debe incluir:
    Un método constructor __init__ para inicializar todos los atributos.
    Un método __str__ que devuelva una representación en cadena del producto, incluyendo su stock (ej: "ID: A001 | Nombre: Teclado | Precio: $50.00 | Stock: 15 unidades").

2. Implementación de la clase Inventario: Implemente una clase Inventario que administre la colección de productos de la tienda. Tendrá el siguiente atributo:
    productos (dict[str, Producto]): un diccionario donde la clave es el id_producto y el valor es el objeto Producto correspondiente.

Esta clase debe tener los siguientes métodos:
    __init__(): Crea un inventario vacío.
    agregar_producto(producto: Producto): Agrega un objeto de tipo Producto al inventario. Si ya existe un producto con el mismo ID, no debe hacer nada.
    vender_producto(id_producto: str, cantidad: int) -> bool: Resta la cantidad especificada del stock del producto. Solo debe realizar la venta si el producto existe 
y hay stock suficiente. Devuelve True si la venta fue exitosa y False en caso contrario.
    reponer_stock(id_producto: str, cantidad: int): Suma la cantidad especificada al stock del producto. Solo debe reponer si el producto existe.
    mostrar_inventario(): Muestra por pantalla la información de todos los productos en el inventario."""

class Producto:
    def __init__(self, id_producto:str, nombre:str, precio:float, stock:int)->None:
        self.id_producto=id_producto
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
    def __str__(self)->str:
        return f'ID: {self.id_producto} | Nombre: {self.nombre} | Precio: ${self.precio} | Stock: {self.stock} unidades'
class Inventario:
    def __init__(self)->None:
        self.productos:dict[str, Producto]={}
    def agregar_producto(self, producto: Producto)->None:
        if producto.id_producto not in self.productos:
            self.productos[producto.id_producto]=producto
    def vender_producto(self, id_producto:str, cantidad:int)->bool:
        if id_producto in self.productos and cantidad<=self.productos[id_producto].stock:
            self.productos[id_producto].stock-=cantidad
            print(f'Se vendieron {cantidad} unidades de {self.productos[id_producto].nombre}')
            return True
        print(f'No se pudieron vender {cantidad}, no hay unidades ({self.productos[id_producto].stock})')
        return False
    def reponer_stock(self, id_producto:str, cantidad:int)->None:
        if id_producto in self.productos:
            self.productos[id_producto].stock+=cantidad
            print(f'Se añadio {cantidad} unidades de {self.productos[id_producto].nombre}')
        else:
            print(f'No se encontro producto en stock')
    def mostrar_inventario(self)->None:
        if not self.productos:
            print(f'Inventario vacio')
        print(f'| Listado de productos en inventario: ')
        for producto in self.productos.values():
            print(producto)
        print(f'Fin de listado de inventario----------------')

# Crear un inventario
mi_tienda = Inventario()
print('\n'+'#'*60)
print(f'##### Ejercicio de Inventario #####')
# Crear y agregar productos
prod1 = Producto("A001", "Mouse inalámbrico", 1500.0, 20)
prod2 = Producto("A002", "Monitor LED 22''", 45000.0, 10)
mi_tienda.agregar_producto(prod1)
mi_tienda.agregar_producto(prod2)
# Mostrar inventario
mi_tienda.mostrar_inventario()
# Realizar operaciones
print("\n--- Realizando Operaciones ---")
mi_tienda.vender_producto("A001", 5)
mi_tienda.vender_producto("A002", 12)  # Debería fallar
mi_tienda.reponer_stock("A002", 5)
# Mostrar inventario final
mi_tienda.mostrar_inventario()

""" Ejercicio 3: Sistema de Calificaciones de Alumnos
Implemente un sistema para gestionar las calificaciones de alumnos en diferentes materias, utilizando programación orientada a objetos.

Implementación de la clase Alumno: Implemente una clase Alumno con los siguientes atributos de instancia:
    legajo (str): el número de legajo único del alumno.
    nombre (str): el nombre completo del alumno.
    calificaciones (dict[str, float]): un diccionario donde la clave es el nombre de una materia (ej: "Programación II") y el valor es la calificación obtenida (de 0 a 10).

La clase debe incluir:
    Un método constructor init para inicializar el legajo y el nombre. El diccionario de calificaciones debe iniciarse vacío.
    Un método str que devuelva una representación del alumno (ej: "Legajo: 123/25 | Nombre: Ana Sosa").
    Un método agregar_calificacion(materia: str, nota: float) que añade una nueva calificación al diccionario.
    Un método calcular_promedio() -> float que devuelve el promedio de todas las calificaciones del alumno. Si no tiene calificaciones, debe devolver 0.0.

Implementación de la clase RegistroAcademico: Implemente una clase RegistroAcademico que administre una colección de alumnos. Tendrá el siguiente atributo:

alumnos (dict[str, Alumno]): un diccionario donde la clave es el legajo del alumno y el valor es el objeto Alumno correspondiente.

Esta clase debe tener los siguientes métodos:
    init(): Crea un registro académico vacío.
    matricular_alumno(alumno: Alumno): Agrega un objeto de tipo Alumno al registro.
    cargar_nota(legajo_alumno: str, materia: str, nota: float): Asigna una nota en una materia a un alumno específico, 
identificado por su legajo. Debe verificar que el alumno exista en el registro.
    obtener_promedio_general() -> float: Calcula y devuelve el promedio de los promedios de todos los alumnos matriculados.
    mostrar_registro(): Muestra por pantalla la información de todos los alumnos matriculados y su promedio individua"""

class Alumno:
    def __init__(self, legajo:str, nombre:str)->None:
        self.legajo=legajo
        self.nombre=nombre
        self.califaciones:dict[str,float]={}
    def __str__(self)->str:
        return f'Legajo: {self.legajo} | Nombre: {self.nombre}'
    def agregar_califaciones(self, materia:str, nota:float)->None:
        if materia not in self.califaciones:
            self.califaciones[materia]=nota
    def calcular_promedio(self)->float:
        #if not self.calificaciones:
        #   return 0.0
        cont=0
        suma=0
        for nota in self.califaciones.values():
            suma+=nota
            cont+=1
        if cont==0:
            return 0.0
        return suma/cont
    
class RegistroAcademico:
    def __init__(self)->None:
        self.alumnos:dict[str,Alumno]={}
    def matricular_alumno(self, alumno:Alumno)->None:
        if alumno.legajo not in self.alumnos:
            self.alumnos[alumno.legajo]=alumno
    def cargar_nota(self, legajo_alumno:str, materia:str, nota:float)->None:
        if legajo_alumno not in self.alumnos:
            print(f'El alumno de {legajo_alumno} no bla bla')
        else:
            self.alumnos[legajo_alumno].agregar_califaciones(materia, nota)
            print(f'Se cargo {nota} en {materia} para {legajo_alumno}')
    def obtener_promedio_general(self)->float:
        if not self.alumnos:
            return 0.0
        suma=0
        cont=0
        for alumno in self.alumnos.values():
            suma+=alumno.calcular_promedio()
            cont+=1
        return suma/cont
    def mostrar_registro(self)->None:
        if not self.alumnos:
            print(f'No hay alumnos registrados')
            return
        for alumno in self.alumnos.values():
            promedio_alumno=alumno.calcular_promedio()
            print(f'{alumno} | Promedio: {promedio_alumno}')



print('\n'+'#'*60)
print(f'##### Ejercicio de Materias #####')
# Crear un registro académico
registro = RegistroAcademico()

# Crear y matricular alumnos
alumno1 = Alumno("110-24", "Laura Paez")
alumno2 = Alumno("112-24", "Marcos Diaz")
registro.matricular_alumno(alumno1)
registro.matricular_alumno(alumno2)

# Cargar notas
registro.cargar_nota("110-24", "Programación II", 8.5)
registro.cargar_nota("110-24", "Bases de Datos", 7.0)
registro.cargar_nota("112-24", "Programación II", 9.0)

# Mostrar el registro
registro.mostrar_registro()

# Obtener promedio general
promedio_curso = registro.obtener_promedio_general()
print(f"\nPromedio general del curso: {promedio_curso:.2f}")


"""Ejercicio 3: Sistema de Cursos y Estudiantes
Implemente un sistema para gestionar la inscripción de estudiantes en cursos, utilizando programación orientada a objetos.

1. Implementación de la clase Estudiante: Implemente una clase Estudiante con los siguientes atributos de instancia:
    legajo (str): el número de legajo único del estudiante.
    nombre (str): el nombre completo del estudiante.

La clase debe incluir:
    Un método constructor __init__ para inicializar todos los atributos.
    Un método __str__ que devuelva una representación del estudiante (ej: "Legajo: 150/25 | Estudiante: Martin Castro").

2. Implementación de la clase Curso: Implemente una clase Curso que administre la información de un curso y sus estudiantes inscriptos. Tendrá los siguientes atributos:

    codigo_curso (str): el código de identificación único del curso.
    nombre_curso (str): el nombre de la materia.
    cupo_maximo (int): la cantidad máxima de estudiantes permitidos.
    inscriptos (list[Estudiante]): una lista que contiene los objetos de tipo Estudiante inscriptos en el curso.

Esta clase debe tener los siguientes métodos:

    __init__(): Crea un curso con su código, nombre y cupo. La lista de inscriptos debe iniciarse vacía.
    inscribir_estudiante(estudiante: Estudiante) -> bool: Agrega un objeto de tipo Estudiante a la lista inscriptos solo si el cupo máximo no ha sido alcanzado. 
Devuelve True si la inscripción fue exitosa y False en caso contrario.
    desinscribir_estudiante(legajo_estudiante: str) -> bool: Elimina un estudiante de la lista de inscriptos, buscándolo por su legajo. 
Devuelve True si el estudiante fue encontrado y eliminado, y False si no estaba inscripto.
    mostrar_inscriptos(): Muestra por pantalla la información de todos los estudiantes inscriptos en el curso."""

class Estudiante:
    def __init__(self, legajo:str, nombre:str)->None:
        self.legajo=legajo
        self.nombre=nombre
    def __str__(self)->str:
        return f'Legajo: {self.legajo} | Estudiante: {self.nombre}'
class Curso:
    def __init__(self, codigo_curso:str, nombre_curso:str, cupo_maximo:int)->None:
        self.codigo_curso=codigo_curso
        self.nombre_curso=nombre_curso
        self.cupo_maximo=cupo_maximo      
        self.inscriptos:list[Estudiante]=[]
    def inscribir_estudiante(self, estudiante:Estudiante)->bool:
        if self.cupo_maximo>0:
            self.inscriptos.append(estudiante)
            print(f'El estudiante {estudiante.nombre} de {estudiante.legajo} fue inscripto')
            return True
        print(f'No hay mas cupos disponibles')
        return False
    def desinscribir_estudiante(self, legajo_estudiante:str)->bool:
        for alumno in self.inscriptos:
            if legajo_estudiante == alumno.legajo:
                self.inscriptos.remove(alumno)
                print(f'Se desinscribio el alumno {alumno.nombre}')
                return True
        print(f"Error: No se encontró al estudiante con legajo {legajo_estudiante}.")
        return False
    def mostrar_inscriptos(self)->None:
        if not self.inscriptos:
            print(f'Lista de inscriptos vacia')
            return
        print(f'\nLista de inscriptos al {self.nombre_curso}')
        for alumno in self.inscriptos:
            print(alumno)

# Crear estudiantes
print('\n'+'#'*60)
print(f'##### Ejercicio de Alumnos #####\n') 
est1 = Estudiante("150-25", "Martin Castro")
est2 = Estudiante("151-25", "Sofia Rodriguez")
est3 = Estudiante("152-25", "Lucas Fernandez")

# Crear un curso
curso_prog2 = Curso("P2-2025", "Programación II", 2)

# Inscribir estudiantes
curso_prog2.inscribir_estudiante(est1)
curso_prog2.inscribir_estudiante(est2)
curso_prog2.inscribir_estudiante(est3) # Debería fallar por falta de cupo

# Mostrar inscriptos
curso_prog2.mostrar_inscriptos()

# Desinscribir un estudiante
curso_prog2.desinscribir_estudiante("150-25")

# Mostrar inscriptos de nuevo
curso_prog2.mostrar_inscriptos()
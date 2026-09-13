from typing import Any
#Ejercicio 1
"""Defina una clase Pila que implemente el TAD Pila utilizando listas de Python."""
class Pila:
    def __init__(self)->None:
        """Crea la pila vacia"""
        self.items=[]
    def push(self, elemento:Any)->None:
        """Apila elemento sobre la lista"""
        self.items.append(elemento)
    def pop(self)->Any:
        """Desapila el ultimo elemento y lo devuelve"""
        if self.isEmpty():
            print(f'Pila vacia')
            return
        return self.items.pop()
    def isEmpty(self)->bool:
        if len(self.items)==0:
            return True
        return False
#Ejercicio 2
"""Defina una clase PilaEnlazada que implemente el TAD Pila utilizando una estructura enlazada"""
class Nodo:
    def __init__(self, dato:Any=None, prox=None)->None:
        self.dato=dato
        self.prox=prox
    def __str__(self):
        return str(self.dato)
class PilaEnlazada:
    def __init__(self)->None:
        """Crea pila vacia"""
        self.cima=None #cima es el elemento de mas arriba de la pila
        self.len=0
    def isEmpty(self)->bool:
        if self.len==0:
            return True
        return False
    def push(self, item:Any)->None:
        """Apila elemento a la pila"""
        nuevo=Nodo(item)
        nuevo.prox=self.cima
        self.cima=nuevo
        self.len+=1
    def pop(self)->Any:
        """Desapila el ultimo elemento y lo devuelve"""
        if self.isEmpty():
            print(f'Pila vacia')
            return
        dato=self.cima.dato
        self.cima=self.cima.prox
        self.len-=1
        return dato
#Ejercicio 4
"""Escriba una función balanceado que reciba una expresión matemática (en forma de string) y devuelve
True si los paréntesis (), corchetes [] y llaves {} están correctamente balanceados, False en caso
contrario
balanceado('(x+y)/2')
True
balanceado('[8*4(x+y)]+{2/5}')
True
balanceado('(x+y]/2')
False
balanceado('1+)2(+3')
False"""
class Pila:
    def __init__(self)->None:
        """Crea la pila vacia"""
        self.items=[]
    def push(self, elemento:Any)->None:
        """Apila elemento sobre la lista"""
        self.items.append(elemento)
    def pop(self)->Any:
        """Desapila el ultimo elemento y lo devuelve"""
        if self.isEmpty():
            print(f'Pila vacia')
            return
        return self.items.pop()
    def isEmpty(self)->bool:
        if len(self.items)==0:
            return True
        return False
    def balanceado(self, expresion:str)->bool:
        p=Pila()
        pares={'(':')', '[':']', '{':'}'}
        for caracter in expresion:
            if caracter in '{([':
                p.push(caracter)
            elif caracter in '})]':
                if p.isEmpty(): #caso de cierre sin apertura
                    return False
                tope=p.pop()
                if tope != pares[caracter]: #caso que cierre incorrecto
                    return False
        return p.isEmpty() #devuelve True si se abrieron y cerraron correctamente

#Ejercicio 5
"""Defina una clase Cola que implemente el TAD Cola utilizando listas de Python"""
class Cola:
    def __init__(self)->None:
        self.items=[]
    def insert(self, x:Any)->None:
        self.items.append(x)
    def remove(self)->Any:
        if self.isEmpty():
            print('Cola vacia')
            return
        return self.items.pop(0)
    def isEmpty(self)->bool:
        return len(self.items)==0
#Ejercicio 6
"""Defina una clase ColaEnlazada que implemente el TAD Cola utilizando una estructura enlazada"""
class Nodo:
    def __init__(self, dato: Any = None, prox=None):
        self.dato = dato
        self.prox = prox

class ColaEnlazada:
    def __init__(self)->None:
        self.length=0
        self.head=None
        self.last=None
    def isEmpty(self)->bool:
        return self.length==0
    def insert(self, x:Any)->None:
        nuevo=Nodo(x)
        nuevo.prox=None
        if self.length==0:
            self.head=self.last=nuevo
        else:
            last=self.last
            last.prox=nuevo #el prox del anterior ultimo es el nuevo nodo
            self.last=nuevo #engancha al nodo nuevo al final
        self.length+=1
    def remove(self)->Any:
        if self.isEmpty():
            print('Cola vacia')
            return
        dato=self.head.dato
        self.head=self.head.prox
        self.length-=1
        if self.length==0:
            self.last=None
        return dato
#Ejercicio 7
"""Cola Generalizada.
Hace un montón de años había una viejísma sucursal del correo que tenía un cartel que decía “No se recibirán más de 5 cartas por persona”. 
Es decir, la gente entregaba sus cartas (hasta la cantidad permitida) y luego tenía que volver a hacer la cola si tenía más cartas para despachar.
Modelar una cola de correo generalizada, donde en la inicialización se indica la cantidad (no necesariamente 5) de cartas que se reciben por persona."""
class Cliente:
    def __init__(self, nombre: str, cant_cartas: int = 1) -> None:
        self.nombre = nombre
        self.cant_cartas = cant_cartas

class ColaGeneralizada:
    def __init__(self, limite:int=5)->None:
        self.cola=ColaEnlazada()
        self.limite=limite
    def isEmpty(self)->bool:
        return self.cola.isEmpty()
    def push(self, cliente:Cliente)->None:
        self.cola.insert(cliente)
    def remove(self)->Any:
        if self.isEmpty():
            print('Cola vacia')
            return
        cliente=self.cola.remove()
        if self.limite>=cliente.cant_cartas:
            despachadas = cliente.cant_cartas
            print(f"Atendido cliente {cliente.nombre}, despachadas {despachadas} cartas")
        else:
            despachadas = self.limite
            cliente.cant_cartas-=self.limite
            print(f"Atendido cliente {cliente.nombre}, despachadas {despachadas} cartas")
            self.cola.insert(cliente)
#Ejercicio Adicionales
#Ejercicio 7
"""Dado un Stack de números, reordenarlos para que estén abajo los impares y arriba los pares, pero que
entre números del mismo tipo preserven el orden.
Ayuda: utilizar dos Stacks auxiliares de números pares e impares respectivamente."""
def reordenar_pila(pila:Pila)->Pila:
        pares=Pila()
        impares=Pila()
        while not pila.isEmpty():
            numero=pila.pop()
            if numero%2==0:
                pares.push(numero) #los ordena en el orden inverso por LIFO
            else:
                impares.push(numero) #los ordena en el orden inverso por LIFO
        while not impares.isEmpty():
            pila.push(impares.pop()) #los pongo abajo y quedan en el orden original
        while not pares.isEmpty():
            pila.push(pares.pop()) #los pongo arriba de los impares en la pila original
        return pila
#Ejercicio 8
"""Una implementación alternativa del TAD Cola puede implementarse internamente utilizando dos Stacks de la siguiente manera:
• Inserta por uno de los stacks.
• Remueve por el otro stack.
• Cuando queremos remover de stack vacío, primero volcamos el stack de inserción en este y seguimos normalmente.
Definir una clase FastQueue que realice esta implementación del TAD Cola.
Escribir código cliente para verificar qué tanto FastQueue como Queue se comportan efectivamente como Colas.
Ayuda: puede serle útil implementar un método extra _volcar."""
class FastQueue:
    def __init__(self)->None:
        self.inserta=Pila()
        self.remueve=Pila()
    def isEmpty(self)->bool:
        return self.inserta.isEmpty() and self.remueve.isEmpty()
    def insert(self,x:Any)->None:
        self.inserta.push(x)

    def volcar(self)->None:
        while not self.inserta.isEmpty():
            self.remueve.push(self.inserta.pop()) 
    
    def remove(self)->Any:
        if self.remueve.isEmpty():
            self.volcar() #la vuelca al reves, el ultimo de la pila es el primero de la "fastqueue" y el primero es el ultimo(que es el primero en salir FIFO)
        if self.remueve.isEmpty():
           print("La cola está vacía")
           return None
        return self.remueve.pop() #remueve el ultimo de la "fastqueue" que era el primero que entro a la pila

#Ejercicio 9
"""Escribir una clase TorreDeControl que modele el trabajo de una torre de control de un aeropuerto con
una pista de aterrizaje. Los aviones que están esperando para aterrizar tienen prioridad sobre los que
están esperando para despegar. La clase debe funcionar conforme al siguiente ejemplo:"""
class TorreDeControl:
    def __init__(self)->None:
        """Inicia colas vacias para arribos y partidas"""
        self.arribos=ColaEnlazada()
        self.partidas=ColaEnlazada()
    def nuevo_arribo(self, vuelo:str)->None:
        """Agrega vuelo a la cola de arribos"""
        self.arribos.insert(vuelo)
    def nueva_partida(self, vuelo:str)->None:
        """Agrega vuelo a la cola de partidas"""
        self.partidas.insert(vuelo)
    def ver_estado(self)->None:
        """Muestra estado de vuelos"""
        if not self.arribos.isEmpty():
            print('Hay vuelos esperando para aterrizar.')
        if not self.partidas.isEmpty():
            print('Hay vuelos esperando para despegar.')
    def asignar_pista(self)->None:
        if not self.arribos.isEmpty():
            vuelo=self.arribos.remove()
            print(f'{vuelo} aterrizó con éxito.')
        elif not self.partidas.isEmpty():
            vuelo=self.partidas.remove()
            print(f'{vuelo} despegó con éxito.')
        else:
            print('No hay vuelos en espera.')

#Ejercicio 10
"""Escribir las clases Impresora y Oficina que permita modelar el funcionamiento de un conjunto de
impresoras conectadas en red.
Una impresora:
• Tiene un nombre, y una capacidad máxima de tinta.
• Permite encolar un documento para imprimir (recibiendo el nombre del documento).
• Permite imprimir el documento que está al frente de la cola.
– Si no hay documentos encolados, se muestra un mensaje informándolo.
– Si no hay tinta suficiente, se muestra un mensaje informándolo.
– En caso contrario, se muestra el nombre del documento, y se gasta 1 unidad de tinta.
• Permite cargar el cartucho de tinta
Una oficina:
• Permite agregar una impresora
• Permite obtener una impresora por nombre.
• Permite quitar una impresora por nombre.
• Permite obtener la impresora que tenga menos documentos encolados.
Para facilitar el ejercicio, supondremos que todos los documentos a imprimir consumen la misma
cantidad de tinta, es decir la cantidad de tinta la representaremos como un número entero y cada
documento impreso la disminuye en uno. Al inicializar una impresora, esta siempre tiene la tinta al
máximo."""
class Impresora:
    def __init__(self,nombre:str, tinta_max:int)->None:
        self.nombre=nombre
        self.capacidad_maxima=tinta_max
        self.tinta_actual=tinta_max
        self.cola=ColaEnlazada()
    def encolar(self, documento:str)->None:
        """Agrega un documento a la cola de impresión."""
        self.cola.insert(documento)
    def imprimir(self)->None:
        """Imprime el primer documento de la cola."""
        if self.cola.isEmpty():
            print('No hay nada en la cola')
            return
        if self.tinta_actual<1:
            print('No tengo tinta :(')
            return
        documento=self.cola.remove()
        print(f'{documento} impreso')
        self.tinta_actual-=1
    def cargar_tinta(self)->None:
        """Recarga la tinta al máximo."""
        self.tinta_actual=self.capacidad_maxima

class Oficina:
    def __init__(self)->None:
        self.impresoras={}
    def agregar_impresora(self, impresora:Impresora)->None:
        """Agrega una impresora a la oficina."""
        self.impresoras[impresora.nombre]=impresora
    def impresora(self, nombre:str)->Impresora:
        """Obtiene una impresora por su nombre."""
        return self.impresoras[nombre]
    def quitar_impresora(self, nombre:str)->None:
        """Quita una impresora de la oficina."""
        if nombre in self.impresoras:
            self.impresoras.pop(nombre)
    def obtener_impresora_libre(self)->Impresora|None:
        """Devuelve la impresora con menos documentos en cola."""
        if not self.impresoras:
            return None
        impresora_libre=None
        minimo=10000000000000
        for impresora in self.impresoras.values():
            if impresora.cola.length<minimo:
                impresora_libre=impresora
                minimo=impresora.cola.length
        return impresora_libre

#Ejercicio 11
"""En la parada del colectivo 133 pueden ocurrir dos eventos diferentes:
• Llega una persona.
• Llega un colectivo con n asientos libres, y se suben al mismo todas las personas que están
esperando, en orden de llegada, hasta que no quedan asientos libres. Asumimos que no pueden
viajar personas de pie.
Cada evento se representa con una tupla que incluye:
• El instante de tiempo (cantidad de segundos desde el inicio del día).
• El tipo de evento, que puede ser p (persona) o c (colectivo).
• En el caso de un evento de tipo c hay un tercer elemento que es la cantidad de asientos libres.
Escribir una función que recibe una lista de eventos, ordenados cronológicamente, y devuelva el promedio
de tiempo de espera de los pasajeros en la parada.
Ejemplo:
promedio_espera([(35,'p'), (43,'p'), (80,'c',1), (98,'p'), (142,'c',2)])
62.6667 # calculado como (45 + 99 + 44) / 3
"""
def 


#Ejercicio 3
"""Defina una clase PilaConMaximo que implemente las operaciones de Pila (push(item) y pop()) y el
método obtener_maximo() que devuelva el elemento máximo de la Pila, sin sacarlo de la misma y que funcione en tiempo constante.
Ayuda: usar dos pilas, una para guardar los elementos y otra para guardar los máximos."""
class PilaConMaximo:
    def __init__(self)->None:
        """Inicia las dos pilas vacias, una para guardar elementos, otra para guardar maximos"""
        self.elementos=[]
        self.maximos=[]
    def isEmpty(self)->bool:
        return len(self.elementos)==0
    def push(self, elemento:Any)->None:
        """Apila elemento a la pila"""
        self.elementos.append(elemento) #agrega elemento a la lista de elementos
        if not self.maximos or elemento>=self.maximos[-1]: #si la lista de maximos esta vacia o si el elemento es mayor al maximo actual lo agrega
            self.maximos.append(elemento)
    def pop(self)->Any:
        if self.isEmpty():
            print(f'Pila vacia')
            return
        sacar=self.elementos.pop()
        if sacar==self.maximos[-1]: #si el elemento a remover coincide con el maximo, se lo saca
            self.maximos.pop()
        return sacar

    def obtener_maximo(self)->Any:
        if self.isEmpty():
            return None
        return self.maximos[-1]
        

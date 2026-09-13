def contar_ocurrencias_rec(lista:list, valor:int)->int:
    if not lista:
        return 0
    if lista[0]==valor:
        return 1+contar_ocurrencias_rec(lista[1:], valor)
    return contar_ocurrencias_rec(lista[1:], valor)

print(contar_ocurrencias_rec([],1))

def contar_ocurrencias_it(lista:list, valor)->int:
    cont=0
    for elemento in lista:
        if elemento==valor:
            cont+=1
    return cont

print(contar_ocurrencias_it([1,3,3,3,5,8],3))

"""Ejercicio 3"""
class Evento:
    def __init__(self, codigo_evento:str, nombre:str, fecha:str, hora:str, capacidad:int)->None:
        self.codigo_evento=codigo_evento
        self.nombre=nombre
        self.fecha=fecha
        self.hora=hora
        self.capacidad=capacidad
    def __str__(self)->str:
        return f'Evento: {self.nombre}, codigo: {self.codigo_evento} que se celebrara el {self.fecha} a las {self.hora}. Capacidad maxima para {self.capacidad} personas'
    
class ReservaEvento:
    def __init__(self, dni_cliente:str, nombre_cliente:str, evento:Evento, numero_asistentes:int)->None:
        self.dni_cliente=dni_cliente
        self.nombre_cliente=nombre_cliente
        self.evento=evento
        self.numero_asistentes=numero_asistentes
    def __str__(self)->str:
        return f'Reserva: {self.nombre_cliente}, dni: {self.dni_cliente} reservo el {self.evento} con {self.numero_asistentes} asistentes'
class SistemaEventos:
    def __init__(self)->None:
        self.eventos:dict[str,Evento]={}
        self.reservas:dict[str,list[ReservaEvento]]={}

    def agregar_evento(self, evento:Evento)->None:
        if evento not in self.eventos:
            self.eventos[evento.codigo_evento]=evento
            self.reservas[evento.codigo_evento]=[]


    def eliminar_evento(self, codigo:str)->None:
        for evento in self.eventos.values():
            if evento.codigo_evento==codigo: #esto es como hacer if codigo in self.eventos
                self.eventos.pop(codigo)
        return None
    
    def mostrar_eventos(self)->None:
        if not self.eventos:
            print(f'No hay eventos')
        print(f'Listado de eventos disponibles. \n')
        for evento in self.eventos.values():
            print(f'{evento}\n')

    def devolver_capacidad_restante(self, codigo:str)->int:
        cap_max=self.eventos[codigo].capacidad
        if codigo in self.reservas:
            asistentes=0
            for reserva in self.reservas[codigo]:
                asistentes+=reserva.numero_asistentes
            return cap_max-asistentes
        return cap_max
    
    def crear_reserva(self, dni:str, nombre:str, codigo:str, asistentes:int )->None:
        if codigo in self.eventos:
            cap_restante=self.devolver_capacidad_restante(codigo)
            if asistentes<=cap_restante:
                nueva_reserva=ReservaEvento(dni, nombre, self.eventos[codigo], asistentes)
                self.reservas[codigo].append(nueva_reserva)
    
    def eliminar_reserva(self, dni:str, codigo:str)->None:
        if codigo in self.reservas:
            reserva_conservar=[] #reserva_conservar =[ reserva for reserva in self.reservas[codigo] if dni!= reserva.dni_clierte ]
            for reserva in self.reservas[codigo]: 
                if dni != reserva.dni_cliente :
                    reserva_conservar.append(reserva) 
            self.reservas[codigo]=reserva_conservar

# Ejemplo de uso
sistema = SistemaEventos ()
# Creando eventos
evento1 = Evento (" E001 ", " Concierto de Rock ", " 2023 -10 -20 ", " 19:00 ", 120)
evento2 = Evento (" E002 ", " Teatro Musical ", " 2023 -10 -21 ", " 20:00 ", 90)
sistema . agregar_evento ( evento1 )
sistema . agregar_evento ( evento2 )
# Mostrando eventos
sistema . mostrar_eventos ()
# Creando reservas
sistema . crear_reserva (" 12345678 ", " Juan Perez ", " E001 ", 15)
sistema . crear_reserva (" 87654321 ", " Maria Lopez ", " E002 ", 20)
sistema . crear_reserva (" 87654321 ", " Rober Galati ", " E002 ", 70)
sistema . crear_reserva (" 87654321 ", " asdfadfadfa ", " E002 ", 10)

# Devolviendo capacidad restante
print (" Capacidad restante para el evento E001 :", sistema . devolver_capacidad_restante (" E001 "))
print (" Capacidad restante para el evento E002 :", sistema . devolver_capacidad_restante (" E002 "))

# Eliminando una reserva
sistema . eliminar_reserva (" 12345678 ", " E001 ")
print (" Capacidad restante para el evento E001 POST ELIMINAR:", sistema . devolver_capacidad_restante (" E001 "))

# Mostrando reservas despu és de eliminar
# sistema . mostrar_reservas (" E001 ")
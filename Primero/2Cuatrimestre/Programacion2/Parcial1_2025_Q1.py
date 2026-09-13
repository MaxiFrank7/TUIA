###Ejercicio 1
def contar_ocurrencias_rec(lista:list, n:int)->int:
    if len(lista)==0:
        return 0
    if lista[0]==n:
        return 1+contar_ocurrencias_rec(lista[1:],n)
    else:
        return contar_ocurrencias_rec(lista[1:],n)

l=[1,3,5,9,87,4,5,6,87,2,85,87]
print(contar_ocurrencias_rec(l,1287))
def contar_ocurrencias_it(lista:list, n:int)->int:
    cont=0
    for num in lista:
        if num==n:
            cont+=1
    return cont
l=[1,3,5,9,87,4,5,6,87,2,85,87]
print(contar_ocurrencias_it(l,87))

###Ejercicio 2
def f(n: int) -> None :
    for i in range (n):                 #n asignaciones
        print (f" Elemento {i}")        #1
        for j in range (1, n + 1):      #n * n asignaciones
            print (f"Sub - elemento {j} en la iteración {i}")  #1
    for i in range (3 ,0 , -1):         #3
        print (i)                       #1
    print (" Salimos de la funci ón!")  #1
#Total n*(1+n*(1))+3+1=n+n2+4 ->O(n2)

###Ejercicio 3
class Evento:
    def __init__(self, codigo_evento:str, nombre:str, fecha:str, hora:str, capacidad:int)->None:
        self.codigo_evento=codigo_evento
        self.nombre=nombre
        self.fecha=fecha
        self.hora=hora
        self.capacidad=capacidad
    def __str__(self)->str:
        return f"El evento {str(self.codigo_evento)} es {str(self.nombre)}, sera el {str(self.fecha)} a las {str(self.hora)} y capacidad maxima de {str(self.capacidad)} personas."
    
class ReservaEvento:
    def __init__(self, dni_cliente:str, nombre_cliente:str, evento:'Evento', numero_asistentes:int)->None:
        self.dni_cliente=dni_cliente
        self.nombre_cliente=nombre_cliente
        self.evento=evento
        self.numero_asistentes=numero_asistentes
    def __str__(self)->str:
        return f'{str(self.nombre_cliente)} con DNI: {str(self.dni_cliente)} reservo el evento: {str(self.evento)} y asisten {str(self.numero_asistentes)} personas.'

class SistemaEventos:
    def __init__(self)->None:
        self.eventos:dict[str,Evento]={}
        self.reservas:dict[str,list[ReservaEvento]]={}

    def agregar_evento(self, evento:Evento)->None:
        if evento not in self.eventos:
            self.eventos[evento.codigo_evento]=evento
            self.reservas[evento.codigo_evento]=[]
    
    def eliminar_evento(self, codigo:str)->None:
        if codigo in self.eventos:
            self.eventos.pop(codigo, None)
        if codigo in self.reservas:
            self.reservas.pop(codigo, None)
    
    def mostrar_eventos(self)->None:
        print(f'-------Lista de eventos actuales-------')
        if not self.eventos:
            print(f'No hay eventos actuales')
        for evento in self.eventos.values():
            print(f'{evento}\n')
        print(f'-----------------------------------')

    def devolver_capacidad_restante(self, codigo:str)->int:
        if codigo in self.reservas:
            asistentes=0
            cap_maxima=self.eventos[codigo].capacidad
            for reserva in self.reservas[codigo]:
                asistentes+=reserva.numero_asistentes
            return cap_maxima - asistentes
        return self.eventos[codigo].capacidad
    
    def crear_reserva(self, dni:str, nombre:str, codigo:str, asistentes:int)->None:
        if codigo in self.eventos:
            if asistentes<= self.devolver_capacidad_restante(codigo):
                nueva_reserva=ReservaEvento(dni, nombre, self.eventos[codigo], asistentes)
                self.reservas[codigo].append(nueva_reserva) #no hago el if codigo in self.reservas porque ya esta creada en agregar_evento, ya se que existe
    
    def eliminar_reserva(self, dni:str, codigo:str)->None:
        """Elimina la reserva de un cliente para un evento específico"""
        if codigo in self.reservas:
            reservas_conservar=[]  #reservas_conservar =[reserva for reserva in self.reservas[codigo] if reserva.dni_cliente != dni]
            for reserva in self.reservas[codigo]:
                if reserva.dni_cliente !=dni:
                    reservas_conservar.append(reserva) #agrego la reserva que quiero mantener
            self.reservas[codigo]=reservas_conservar

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
sistema . crear_reserva (" 12345678 ", " Juan Perez ", " E001 ", 4)
sistema . crear_reserva (" 87654321 ", " Maria Lopez ", " E002 ", 3)
# Devolviendo capacidad restante
print (" Capacidad restante para el evento E001 :",
sistema . devolver_capacidad_restante (" E001 "))
# Eliminando una reserva
sistema . eliminar_reserva (" 12345678 ", " E001 ")# Mostrando reservas despu és de eliminar
sistema . eliminar_evento (" E001 ")
sistema . mostrar_eventos ()


"""Ejercicio 1
#Implemente una función recursiva llamada contar_pacientes_rec que recibe como parámetros una lista de pacientes
#(cada paciente es un diccionario con las claves "Nombre","DNI" y "Síntomas") y un síntoma (por ejemplo, "fiebre",
#"dolor de cabeza", etc) y que cuente cuántos pacientes sufren dicho síntoma (tener en cuenta que un paciente puede
#tener varios síntomas, el valor asociado a la clave "Síntomas" es un str con los síntomas separados por ’,’). Escriba,
#además, una función iterativa contar_pacientes_it equivalente"""

def contar_pacinetes_rec(lista:list[dict[str,str]], sintoma:str)->int:
    #caso base
    if len(lista)==0:
        return 0
    if sintoma in lista[0]["Sintomas"]:
        return 1+contar_pacinetes_rec(lista[1:], sintoma)
    else:
        return contar_pacinetes_rec(lista[1:], sintoma)
    
def contar_pacientes_it(lista:list[dict[str,str]], sintoma:str)->int:
    cont=0
    for paciente in lista:
        if sintoma in paciente["Sintomas"]:
            cont+=1
    return cont

def registrar_pacientes(n: int) -> list[dict[str ,str]]:
    lista_pac = []                          #1
    datos = ["Nombre","DNI","Síntomas"]     #1
    for i in range(n):                                 #n
        print(f"Registrando paciente {i + 1}")          #1
        pac = {}                        #1
        for j in range (3):                             #3
            pac[datos[i]] = input(f"Ingrese {datos[i]} para paciente {i + 1}:") #1
            lista_pac.append(pac)
    return lista_pac                                    #1
#Total= 1+1+n*(1+1+3*(1))+1=2+5n+1=3+5n->O(n)

"""Ejercicio 3
Implemente un sistema de gestión de pacientes utilizando programación orientada a objetos. Para ello, implemente
las clases que se especifican a continuación:
1. Implementación de una clase Paciente:
    Implemente una clase Paciente que tenga los siguientes atributos:
        dni (str): el DNI del paciente.
        nombre (str): el nombre del paciente.
        edad (int): la edad del paciente.
        sintomas (str): los sintomas del paciente (asumiendo que se ingresan separados por ’,’).
    La clase debe incluir un método __init__ (con los argumentos que considere necesarios) y __str__ que devuelva
    una representación en cadena del paciente.
2. Implementación de la clase Hospital:
    Implemente una clase Hospital que gestione múltiples pacientes y que tenga los siguientes atributos:
        pacientes (dict[str, Paciente]): un diccionario que almacena los pacientes, donde la clave es el DNI del paciente.
    Esta clase debe tener los siguientes métodos:
        __init__(): Crea un hospital vacío (sin pacientes).
        agregar_paciente: Recibe como parámetro un objeto de tipo Paciente y lo agrega al diccionario pacientes.
        eliminar_paciente: Recibe como parámetro el DNI de un paciente y elimina al paciente correspondiente, si existe.
        mostrar_pacientes: Muestra por pantalla todos los pacientes registrados en el hospital.
        contar_pacientes_con_sintoma: Recibe como parámetro un síntoma y devuelve la cantidad de pacientes que tienen ese síntoma."""

class Paciente:
    def __init__(self, dni:str, nombre:str, edad:int, sintomas:str)->None:
        self.dni=dni
        self.nombre=nombre
        self.edad=edad
        self.sintomas=sintomas
    def __str__(self)->str:
        return f'Paciente {self.nombre} | DNI: {self.dni} | Edad: {self.edad} | Sintomas: {self.sintomas}'
class Hospital:
    def __init__(self)->None:
        self.pacientes:dict[str,Paciente]={}
    def agregar_paciente(self, paciente:Paciente)->None:
        if paciente.dni not in self.pacientes:
            self.pacientes[paciente.dni]=paciente
        else:
            print(f'Paciente con dni: {paciente.dni} ya registrado')
    def eliminar_paciente(self, dni:str)->None:
        if dni in self.pacientes:
            self.pacientes.pop(dni, None)
        return
    def mostrar_pacientes(self)->None:
        if not self.pacientes:
            print(f'Lista de pacientes vacia')
            return
        print(f'Lista de pacientes de Hospital\n')
        print('-'*50+"\n")
        print(f'{"Nombre":<15} | {'DNI':<8} | {'Edad':<3} | {'Sintomas':<20}| \n')
        for paciente in self.pacientes.values():
            print(f'{paciente.nombre:<15} | {paciente.dni:<8} | {paciente.edad:<3} | {paciente.sintomas:<20} |\n')
            #print(paciente) funciona porque ya tiene el str
        print('-'*50+'\n')
    

    def contar_pacientes_con_sintoma(self, sintoma:str)->int:
        cont=0
        for paciente in self.pacientes.values():
            if sintoma in paciente.sintomas:
                cont+=1
        return cont
# Ejemplo de uso
hospital = Hospital ()
# Creando pacientes
paciente1 = Paciente("12345678", "Juan Perez", 30, "fiebre , tos")
paciente2 = Paciente("87654321", "Maria Lopez", 25,"dolor de oidos")
paciente3 = Paciente("36598741", "Goncho Banzas", 30,"fiebre")

hospital.agregar_paciente(paciente1)
hospital.agregar_paciente(paciente2)
hospital.agregar_paciente(paciente3)
# Mostrando pacientes
hospital.mostrar_pacientes ()
# Contando pacientes con fiebre
print("Pacientes con fiebre:", hospital.contar_pacientes_con_sintoma("fiebre"))
# Eliminando un paciente
hospital.eliminar_paciente("12345678")
print(f'Paciente despues de borrar paciente 2')
hospital.mostrar_pacientes ()


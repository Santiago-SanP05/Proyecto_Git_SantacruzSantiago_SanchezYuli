from Busqueda import *
from Ciudades import *

def Menu():
    list = ["1.Para opciones de ciudades","2.Para busqueda avanzada","3.Para salir"]
    while True:
        print("Por favor marca una de las opciones")
        for i in list:
            print(i)
        opc = int(input("->"))
        if opc == 1:
            print("---Accediendo---")
            menuthree()
        elif opc == 2:
            print("---Accediendo---")
            Menutwo()         
        elif opc == len(list):
            print("---Cerrando Programa---")
            print("...Hasta la proxima...")
            break
def menuthree():
    list = ["1.Para registrar","2.Para editar","3.Busqueda por ciudad","4.Para retroceder"]
    while True:
        print("Por favor marca una de las opcciones:")
        for i in list:
            print(i)
        opc = int(input("->"))
        if opc == 1:
            print("---Accediendo---")
            registrar()
        elif opc == 2:
            print("---Accediendo---")
            modificar()
        elif opc == 3:
            print("---Accediendo---")
            busqueda()
        elif opc == len(list):
            print("---Retrocediento---")
            break

def Menutwo():
    list = ["1.Cod-postal","2.Población Estimada","3.Pais de origen","4. Para retroceder"]
    while True:
        print("Por favor seleccione una opción para hacer una busqueda avanzada")
        for i in list:
            print(i)
        opc = int(input("->"))
        if opc == 1:
            print("---Accediendo---")
            BusquedaCod()
        elif opc == 2:
            print("---Accediendo---")
            BusquedaPes()
        elif opc == 3:
            print("---Accediendo---")
            BusquedaOrigenP()
        elif opc == len(list):
            print("----Retrocediendo----")
            break


        
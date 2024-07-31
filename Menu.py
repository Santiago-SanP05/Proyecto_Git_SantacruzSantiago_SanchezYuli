



def Menu():
    list = ["1.para ingresar un usuario nuevo","2.para editar","3.para busqueda avanzada","4.para salir"]
    while True:
        print("por favor marca una de las opcciones")
        for i in list:
            print(i)
        opc = int(input("->"))
        if opc == 1:
            print("---accediendo---")
        elif opc == 2:
            print("---accediendo---")
        elif opc == 3:
            print("---accediendo---")            
        elif opc == len(list):
            print("---Cerrando Programa---")
            print("hasta la proxima...")
            break

def Menutwo():
    list = ["1.Cod-postal","2.poblacio Estimada",".3Pais de origen","Ó si no marca 4 para salir"]
    while True:
        print("por favor selecciones una opccion a hacer Busqueda avanzada")
        for i in list:
            print(i)
        opc == int(input("->"))
        if opc == 1:
            print("---Accediendo---")
        elif opc == 2:
            print("---Accediendo---")
        elif opc == 3:
            print("---Accediendo---")
        elif opc == len(list):
            print("----Retrocediendo----")         

        
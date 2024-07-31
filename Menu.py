



def Menu():
    list = ["1.para ingresar un usuario nuevo","2.para editar","3.para salir"]
    while True:
        print("por favor marca una de las opcciones")
        for i in list:
            print(i)
        opc = int(input("->"))
        if opc == 1:
            print("---accediendo---")
        elif opc == 2:
            print("---accediendo---")
        elif opc == len(list):
            print("---Cerrando Programa---")
            print("hasta la proxima...")
            break


        
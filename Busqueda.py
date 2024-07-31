from datos import *

def BusquedaCod():
    datos = cargar_datos()
    while True:
        print("por favor ingrese su el codigo postal de la ciudad que deseas buscar")
        opc = int(input("->"))
        for i in datos["Ciudades"]:
            cod = datos["Ciudades"][i]["Codigo postal"]
            if opc == cod:
                print("La ciudad que cumple con estas caracteristicas es:")
                print(i)
                print("retrocediendo...")
            else:
                print("No hay una ciudad con este codigo postal")       
        break

def BusquedaPes():
    datos = cargar_datos()
    while True:
        print("por favor ingrese la pobalcion estimada qeu deseas buscar")
        opc = input("->")
        for i in datos["Ciudades"]:
            cod = datos["Ciudades"][i]["Poblacion Estimada"]
            if opc == cod:
                print("La ciudad que cumple con estas caracteristicas es:")
                print(i)
                print("retrocediendo...")
            else:
                print("No hay una ciudad con esta poblacion")       
        break
def BusquedaOrigenP():
    datos = cargar_datos()
    while True:
        print("por favor ingrese la pobalcion estimada qeu deseas buscar")
        opc = input("->")
        for i in datos["Ciudades"]:
            cod = datos["Ciudades"][i]["Pais de origen"]
            if opc == cod:
                print("La ciudad que cumple con estas caracteristicas es:")
                print(i)
                print("retrocediendo...")
            else:
                print("No hay una ciudad con esta poblacion")       
        break


    










BusquedaOrigenP()
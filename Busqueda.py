from datos import *

def BusquedaCod():
    datos = cargar_datos()
    while True:
        print("Por favor ingrese su el codigo postal de la ciudad que deseas buscar")
        opc = int(input("->"))
        for i in datos["Ciudades"]:
            cod = datos["Ciudades"][i]["Codigo postal"]
            if opc == cod:
                print("La ciudad que cumple con estas caracteristicas es:")
                print(i)
                print("Retrocediendo...")
                break
            else:
                print("No hay una ciudad con este codigo postal")       
        break

def BusquedaPes():
    datos = cargar_datos()
    while True:
        print("Por favor ingrese la población estimada que deseas buscar")
        opc = input("->")
        for i in datos["Ciudades"]:
            cod = datos["Ciudades"][i]["Poblacion Estimada"]
            if opc == cod:
                print("La ciudad que cumple con estas caracteristicas es:")
                print(i)
                print("Retrocediendo...")
                break
            else:
                print("No hay una ciudad con esta poblacion")       
        break
def BusquedaOrigenP():
    datos = cargar_datos()
    while True:
        print("Por favor ingrese la población estimada que deseas buscar")
        opc = input("->")
        print("La ciudad o ciudades que cumple con estas caracteristicas son:")
        for i in datos["Ciudades"]:
            cod = datos["Ciudades"][i]["Pais de origen"]
            if opc == cod:
                print("->", i)
        print("---Retrocediendo---")
        break

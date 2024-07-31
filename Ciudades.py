import datos as book

def registrar():
    car= book.cargar_datos()
    dixi={}
    name=input("Ingrese nombre de la ciudad: ")
    if name in car["Ciudades"]:
        print("Esta ciudad ya esta registrada")
    else:
        dixi["Codigo postal"]=int(input("Ingrese codigo postal: "))
        dixi["Poblacion Estimada"]=input("Ingrese población estimada: ")
        dixi["Pais de origen"]=input("Ingrese pais: ")
        car["Ciudades"][name]=dixi
        book.guardar_datos(car)
        print("Ciudad registrada correctamente")

def modificar():
    car= book.cargar_datos()
    dixi={}
    name=input("Ingrese nombre de la ciudad: ")
    if name in car["Ciudades"]:
        print("Por favor ingrese estos datos de nuevo para editar")
        dixi["Codigo postal"]=int(input("Ingrese codigo postal: "))
        dixi["Poblacion Estimada"]=input("Ingrese población estimada: ")
        dixi["Pais de origen"]=input("Ingrese pais: ")
        car["Ciudades"][name]=dixi
        book.guardar_datos(car)
        print("Ciudad modificada correctamente")
    else:
        print("Esta ciudad no esta registrada")

modificar()
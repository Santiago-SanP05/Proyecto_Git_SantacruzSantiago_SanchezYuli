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

def busqueda():
    car= book.cargar_datos()
    name=input("Ingrese nombre de la ciudad: ")
    if name in car["Ciudades"]:
        opc=input("Desea buscar: \n1.Nombre \n2.Poblacion \n3.Pais \n4.Toda la info \nIngrese: ")
        if opc == "1":
            mostrar=car["Ciudades"][name].get("Codigo postal")
            print("El codigo postal de ",name, "es",mostrar)
        elif opc == "2":
            mostrar=car["Ciudades"][name].get("Poblacion Estimada")
            print("La poblacion Estimada de ",name, "es",mostrar)
        elif opc == "3":
            mostrar=car["Ciudades"][name].get("Pais de origen")
            print("El pais de origen de ",name, "es",mostrar)
        elif opc == "4":
            mostrar=car["Ciudades"].get(name)
            print("Esta es toda la informacion de ",name, ":",mostrar)
        else:
            print("Opcion incorrecta")
    else:
        print("Nombre de ciudad ingresado incorrectamente o no existe")

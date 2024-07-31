import json 

ruta= "info.json"

def guardar_datos(datos):
    try:
        with open(ruta, "w") as file:
            json.dump(datos, file, indent=4)
    except Exception as err:
        print("********************************")
        print("ERROR AL GUARDAR DATOS", err)

def cargar_datos():
    try: 
        with open(ruta, "r") as archivito:
            datos= json.load(archivito)
            return datos
    except Exception as err:
        print("********************************")
        print("ERROR AL CARGAR DATOS", err)
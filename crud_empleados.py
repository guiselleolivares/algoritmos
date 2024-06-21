import os
import json
os.system("cls")

URL_EMPLEADOS = 'empleados.json'

# en la evaluacion el profe va a dar la funcion leer archivo json, guardar archivo json tenemos que aprender a implementarlas 
#leer archivo json
def leer_archivo_json(url):
    try:
        with open(url, 'r') as archivo: # leemos el archivo
            return json.load(archivo) # retornamos lo que tenga el archivo
    except:
        return[]
    
def guardar_archivo_json(url, data):
    try:
        with open(url, 'w') as archivo: # leemos el archivo
            json.dump(data, archivo, indent=4)
    except:
        return[]


#crear funcion empleados 
def crear_empleado():
    os.system("cls")
    print("== REGISTRAR EMPLEADOS ==")
    empleados = leer_archivo_json(URL_EMPLEADOS)

    id_empleado = input("ingrese el ID del nuevo empleado >>")
    nombre = input("ingrese el NOMBRE del nuevo empleado  >>")
    apellido = input("ingrese el APELLIDO del nuevo empleado  >>")
    sueldo = int(input("ingrese el SUELDO del nuevo empleado  >>")) # aca hay que validar int
    id_cargo = input("ingrese el ID CARGO del nuevo empleado  >>")

    nuevo_empleado = {
        "id_empleado": id_empleado,
        "nombre": nombre,
        "apellido":apellido,
        "sueldo": sueldo,
        "id_cargo": id_cargo
    }

# agregar un nuevo listado al arrys 
    empleados.append(nuevo_empleado)

    guardar_archivo_json(URL_EMPLEADOS, empleados)


# crear funcion listar empleados     
def listar_empleados():
    os.system("cls")
    print(" == LISTADO DE EMPLEADOS==")

    empleados = leer_archivo_json(URL_EMPLEADOS)
    
    headers = ['id_empleado', 'nombre', 'apellido', 'sueldo', 'id_cargo']
    col_widths = [15,15,15,15,15]
    
    # Imprimir el encabezado
    header_line = ' | '.join(f"{header.capitalize():^{col_widths[i]}}" for i, header in enumerate(headers))
    print(header_line)
    print('-' * len(header_line))
    
    for empleado in empleados:
        row = ' | '.join(f"{str(empleado.get(header, '')):^{col_widths[i]}}" for i, header in enumerate(headers))
        print(row)


# crear funcion actualizar empleados
def actualizar_empleados():
    os.system("cls")
    print("== EDITAR EMPLEADOS ==")
    empleados = leer_archivo_json(URL_EMPLEADOS)

    listar_empleados()
    id_empleado = input("ingrese el ID del empleado que desea EDITAR  >>")


    nombre = input("ingrese el NOMBRE del nuevo empleado  >>")
    apellido = input("ingrese el APELLIDO del nuevo empleado  >>")
    sueldo = int(input("ingrese el SUELDO del nuevo empleado  >>")) # aca se valida el int 
    id_cargo = input("ingrese el ID CARGO del nuevo empleado  >>")

    for empleado in empleados:
        if empleado ['id_empleado'] == id_empleado:
            empleado ['nombre'] = nombre
            empleado ['apellido'] = apellido
            empleado ['sueldo'] = sueldo
            empleado ['id_cargo'] = id_cargo
            break


    guardar_archivo_json(URL_EMPLEADOS, empleados)

# crear funcion eliminar empleados
def eliminar_empleados():
    os.system("cls")
    print("== BORRAR EMPLEADOS ==")
    empleados = leer_archivo_json(URL_EMPLEADOS)


    listar_empleados()
    id_empleado = input("ingrese el ID del empleado que desea ELIMINAR  >>")

    empleados_que_quedan = []

    for empleado in empleados:
        if empleado['id_empleado'] != id_empleado:
            empleados_que_quedan.append(empleado)


    guardar_archivo_json(URL_EMPLEADOS, empleados_que_quedan)



# crear funcion menu_general 
def menu_general():
    os.system("cls")
    print("== EMPLEADOS ==")
    print("1. crear      -CREATE")
    print("2. actualizar -UPDATE")
    print("3. listar     - READ")
    print("4. borrar     - DELETE")
    print("5. salir")

# crear funcion seleccionar_opcion
def seleccionar_opcion(max_value):
    opcion = 0
    while True:
        try:
            opcion = int(input("ingrese una de las opcion  >>"))
        except:
            pass
        if opcion < 1 or opcion > max_value:
            input("opcion invalida, intente nuevamente  >>")
        else:
            return opcion
        
# crear funcion iniciar_programa
def iniciar_programa():
    while True:
        menu_general()
        opcion = seleccionar_opcion(5)
    
        if opcion == 1:
            crear_empleado()
        elif opcion == 2:
            actualizar_empleados()
        elif opcion == 3:
            listar_empleados()
        elif opcion == 4:
            eliminar_empleados()
        elif opcion == 5:
            return
        input()

# en la ultima se pone return porque este mata el ciclo white y returna la funcion y la acaba 


#if __name__ == __"main__": inicia el programa 
# significa que cuando ejecutes este archivo lo primero que se ejecuta es esta funcion
if __name__ == "__main__":
    iniciar_programa()

#---Proyecto smart home---
import os

def crearArchivoUsuarios():#Crea un archivo para usuarios para posteriormente añadir la info
    if not os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "w"):
            pass
        print("\n---¡Archivo de info de usuario creado correctamente!---\n")

    else:
        pass
    print("\n---¡Archivo de info de usuario cargado correctamente!---\n")



def cargarUsuarios():
    usuarios = []
    try:
        with open("usuarios.txt", "r") as file:
            for linea in file:
                nombre, correo, pin, *casas = linea.strip().split(',')
                usuarios.append({"Nombre": nombre, "Correo": correo, "PIN": pin, "Casas":casas})
    except FileNotFoundError:
        pass
    print("Cargar usuarios:", usuarios)
    print("Los usuarios se cargaron CORRECTAMENTE")
    return usuarios
def agregarInfoUsuario():
    print("\n--- Registro de Nuevo Usuario ---")
    usuarios = []

    while True:
        nombre = input("Ingrese su nombre: ")
        correo = input("Ingrese su correo electrónico: ")
        pin = input("Ingrese su PIN: ")

        nuevoUsuario = {"Nombre": nombre, "Correo": correo, "PIN": pin, "Casas": []} #casas es un lista vacía que se iniciliza x esta linea
        usuarios.append(nuevoUsuario)
        print("¡Usuario registrado exitosamente!")

        guardarUsuarios(usuarios)
        break

def guardarUsuarios(usuarios):
    with open("usuarios.txt", "a+") as file: 
        for usuario in usuarios: # cada dicionmario representa un usuario, for diccionario in usuarios
            file.write(f"{usuario['Nombre']},{usuario['Correo']},{usuario['PIN']

def consultarInfoPorPIN():
    pinConsulta = input("Ingrese su PIN para consultar la información: ")
    nombreConsulta = input("Ingrese su nombre para consultar la información: ")
    usuarios = cargarUsuarios()

    for usuario in usuarios:
        if usuario["PIN"] == pinConsulta and nombreConsulta == usuario["Nombre"]:
            imprimirInfoUsuario(usuario) #osea le pasa ese en especifico
            break

        else:
            print("\nCredenciales incorrectos\n")
            break

def imprimirInfoUsuario(usuario):
    print("\nInformación del usuario:")
    print(usuario)        

def agregarHabitacionDispositivos():
    usuarios = cargarUsuarios()
    
    if not usuarios:
        print("No hay usuarios registrados. Registre un usuario primero.")
        return

    usuarioActual = usuarios[-1]  # Obtén el último usuario

    casas = []

    while True:
        casa = []
        casa.append(input("Ingrese el nombre de la casa: "))  # El primer elemento es el nombre de la casa
        habitaciones = []

        while True:
            habitacion = []
            habitacion.append(input("Ingrese el nombre de la habitacion: "))  # El primer elemento es el nombre de la habitacion
            dispositivos = []

            while True:
                dispositivo = []
                dispositivo.append(input("Ingrese el nombre del dispositivo: "))
                dispositivo.append(input("Ingrese el estado del dispositivo (Encendido/Apagado): "))
                dispositivos.append(dispositivo)

                opcionDispositivo = input("¿Desea agregar otro dispositivo a esta habitacion? (1=Si, Otra tecla=No): ")
                if opcionDispositivo != "1":
                    break

            habitacion.append(dispositivos)
            habitaciones.append(habitacion)

            opcionHabitacion = input("¿Desea agregar otra habitación a esta casa? (1=Sí, Otra tecla=No): ")
            if opcionHabitacion != "1":
                break

        casa.append(habitaciones)
        casas.append(casa)

        opcionCasa = input("¿Desea agregar otra casa? (1=Sí, Otra tecla=No): ")
        if opcionCasa != "1":
            break

    usuarioActual["Casas"] = casas  # Asigna la lista de casas al último usuario
    guardarUsuarios(usuarios)
    print("\n---¡Archivo de habitaciones y dispositivos creado correctamente---\n")
    
                                                                  
cargarUsuarios()
while True:
    print("Bienvenido al programa. Seleccione una opcion")
    opcion = str(input("Seleciione una opción:\n1=Registrar usuario \n2=Ver info de usuario y sus dispositivos\nOtra tecla= Salir\nOPCIÓN:"))
    if opcion == "1":
        crearArchivoUsuarios()
        agregarInfoUsuario()
        agregarHabitacionDispositivos()
    elif opcion =="2":
        consultarInfoPorPIN()
    else:
        break

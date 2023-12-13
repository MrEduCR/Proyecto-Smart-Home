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

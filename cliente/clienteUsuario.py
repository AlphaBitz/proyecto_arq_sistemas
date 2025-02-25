# test
import socket, sys, json
from os import system, name
from funcionesGenerales import limpiarPantalla, enviarTransaccion, escucharBus
REGISTRO = "regi9"
LOGIN = "logi9" #Registro de usuarios
BUSCAR = "busc9"

sesion = {"id": None,"usuario":None,"rol":None}
sock = None




def menuIngresar():
    limpiarPantalla()
    menu = """
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║ Proceso cliente para proyecto de Arquitectura de Sistemas             ║
    ╠═══════════════════════════════════════════════════════════════════════╣
    ║ Bienvenido al sistema                                                 ║
    ║ Elige una opción:                                                     ║
    ║ 1) Ingresar                                                           ║
    ║ 2) Registrarse                                                        ║
    ╚═══════════════════════════════════════════════════════════════════════╝
    Opción:"""
    opcionElegida = input(menu)
    if opcionElegida == "1":
        menuLogin()
    elif opcionElegida =="2":
        menuRegistrarse()
    else:
        print("No valido")
        menuLogin()
def menuRegistrarse():
    nombreUsuario = None
    rol = None
    menu = """
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║ Proceso cliente para proyecto de Arquitectura de Sistemas             ║
    ╠═══════════════════════════════════════════════════════════════════════╣
    ║ Registro                                                              ║
    ║ Ingresa tu nombre de usuario                                          ║
    ╚═══════════════════════════════════════════════════════════════════════╝
    Nombre de usuario:"""
    
    limpiarPantalla()
    nombreUsuario = input(menu)
    rol = "1"
    menu2 = f"""
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║ Proceso cliente para proyecto de Arquitectura de Sistemas             ║
    ╠═══════════════════════════════════════════════════════════════════════╣
    ║ Registro                                                              ║
    ║ Confirma tus datos:                                                   ║
    ║ 1) Si                                                                 ║
    ║ 2) No                                                                 ║
    ╚═══════════════════════════════════════════════════════════════════════╝
    Usuario: {nombreUsuario}
    Opción:"""
    limpiarPantalla()
    confirmar = input(menu2)
    if confirmar == "1":
        contenido = {"usuario": nombreUsuario, "rol":rol}
        enviarTransaccion(sock, json.dumps(contenido), REGISTRO )
        serv, mensaje=escucharBus(sock)
        msg =  json.loads(mensaje[2:]) # los 2 primeros caracteres son OK
        print("serv",serv)
        print("msg",msg)
        if serv == REGISTRO:
            if msg["respuesta"]:
                print(msg["respuesta"])
    else:
        menuRegistrarse()
def menuLogin():
    # limpiarPantalla()
    menu = """
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║ Proceso cliente para proyecto de Arquitectura de Sistemas             ║
    ╠═══════════════════════════════════════════════════════════════════════╣
    ║ Autenticación                                                         ║
    ║ Ingresa tu nombre de usuario                                          ║
    ╚═══════════════════════════════════════════════════════════════════════╝
    Nombre de usuario:"""
    limpiarPantalla()
    nombreUsuario = input(menu)
    contenido = {"usuario": nombreUsuario}
    enviarTransaccion(sock, json.dumps(contenido), LOGIN )
    serv, mensaje=escucharBus(sock) # msg: {'respuesta': {'id': 1, 'usuario': 'weebtor', 'rol': 'cliente'}}
    msg =  json.loads(mensaje[2:]) # los 2 primeros caracteres son OK
    # print(serv, msg)
    if serv == LOGIN:
        if msg["respuesta"] == "noNombre":
            input("No se ha encontrado el usuario, presione Enter para continuar")
            menuLogin() 
        else:
            # print(msg["respuesta"])
            global sesion
            sesion=msg["respuesta"]
            print(sesion)
            if sesion["rol"] == "cliente":
                # Menu cliente
                menuCliente()
            else:
                error = """
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║ Proceso cliente para proyecto de Arquitectura de Sistemas             ║
    ╠═══════════════════════════════════════════════════════════════════════╣
    ║ Autenticación                                                         ║
    ║ Lo sentimos, tu rol no pertenece a este cliente                       ║
    ╚═══════════════════════════════════════════════════════════════════════╝
    Presiona Enter para continuar..."""
                input(error)
                menuIngresar()
def menuCliente():
    menu = """
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║ Proceso cliente para proyecto de Arquitectura de Sistemas             ║
    ╠═══════════════════════════════════════════════════════════════════════╣
    ║ Menu cliente                                                          ║
    ║ Elige una opción                                                      ║
    ║ 1) Buscar local                                                       ║
    ║ 2) Revisar reservas                                                   ║
    ╚═══════════════════════════════════════════════════════════════════════╝
    Opción:"""
    opcionElegida = input(menu)
    if opcionElegida == "1":
        menuBuscarLocal()
        pass
    elif opcionElegida =="2":
        pass
    else:
        menuCliente()
    pass
def menuBuscarLocal():
    menu = """
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║ Proceso cliente para proyecto de Arquitectura de Sistemas             ║
    ╠═══════════════════════════════════════════════════════════════════════╣
    ║ Buscar local                                                          ║
    ║ Elige una opción y las palabras claves (separa con una ",")           ║
    ║ 1) Nombre                                                             ║
    ║ 2) Tipo de comida                                                     ║
    ║ 3) Comuna                                                             ║
    ║ 4) Todos los locales                                                  ║
    ╚═══════════════════════════════════════════════════════════════════════╝
    Comida:"""
    buscar = input(menu)
    buscar = buscar.split(",")
    for i in buscar:
        i = i.lstrip()
        i = i.rstrip()
        
    if buscar[0] == "1":
        contenido = {"buscarPor":"nombre","buscar":buscar[1]}
        pass
    elif buscar[0] == "2":
        contenido = {"buscarPor":"tipo_comida","buscar":buscar[1]}
        pass
    elif buscar[0] == "3":
        contenido = {"buscarPor":"comuna","buscar":buscar[1]}
        pass
    elif buscar[0] == "4":
        contenido = {"buscarPor":"todo"}
        
    enviarTransaccion(sock,json.dumps(contenido),BUSCAR)
    serv, mensaje=escucharBus(sock)
    # print("serv, msg:",serv, mensaje)
    respuesta = json.loads(mensaje[2:])
    listaLocalesObtenidos(respuesta["locales"])

def listaLocalesObtenidos(lista):
    menu = f"""
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║ Proceso cliente para proyecto de Arquitectura de Sistemas             ║
    ╠═══════════════════════════════════════════════════════════════════════╣
    ║ Locales encontrados                                                   ║
    ╚═══════════════════════════════════════════════════════════════════════╝
    Total: {len(lista)} Locales
    Locales:"""
    print(menu)
    for local in lista:
        info = f"""            ════════════════════════════════
            {local[0]} - {local[2]}
            Descripción: {local[3]}
            Lugar: {local[4]}
            Capacidad: {local[6]}
            Tipos de comida: {local[5]}
        """
        print(info)
    print("            ════════════════════════════════")


if __name__ == "__main__":
    # Conexion con el bus
    try:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 5000)
        print('Cliente: Conectandose a {} puerto {}'.format(*server_address))
        sock.connect(server_address)
    # En caso de error cierra la aplicacion
    except: 
        print("no se pudo conectar con el bus")
        quit()
    ###########
    menuIngresar()

    


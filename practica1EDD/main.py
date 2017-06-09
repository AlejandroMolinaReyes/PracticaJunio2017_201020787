import os
from estructuras import Lista
from usuario import Usuario

"""" ********************************* Menu Usuario  ****************************************  """

def opciones_usuario(nombre):
	valitacion = True

	while validacion:
		os.system("cls")
		print("************************ Bienvenido "+nombre+" *********************\n")
		print("1. Leer Archivo")
		print("2. Resolver operacion")
		print("3. Operar Matriz")
		print("4. Mostrar Usuarios")
		print("5. Mostrar cola")
		print("6. Cerrar sesión\n")
		print("Seleciona una opcion: ")
		opcion = input()
		


"""" *******************************************************************************************  """

"""" ********************************* Metodo menu princial *************************************  """

def menu_principal(opcion):
	os.system("cls")
	#--------------------  opcion 1
	if opcion=="1":
		print("************************ Crear nuevo usuario ***********************\n")
		print("Escriba su nombre de usuario nuevo:")
		nombre = input()
		print("Escriba una contraseña para el usuario nuevo:")
		contraseña = input()
		nuevo_usuario = Usuario(nombre,contraseña)
		global lista_usuarios
		buscar_nombre, buscar_contraseña = lista_usuarios.buscar_usuario(nombre)
		if buscar_nombre==nombre:
			print("\nError: Usuario ya existe! :(\n")
		else:
			lista_usuarios.agregar_final(nuevo_usuario)
			print("\nUsuario fue creado exitosamente :)\n")
	#----------------------  opcion 2
	elif opcion=="2":
		print("************************** Login **************************\n")
		print("ingrese su usuario:")
		nombre = input()
		print("ingrese su contraseña")
		contraseña = input();
		global lista_usuarios
		buscar_nombre, buscar_contraseña = lista_usuarios.buscar_usuario(nombre)
		if buscar_nombre==nombre and buscar_contraseña==contraseña:
			opciones_usuario(nombre)
		else:
			print("\nError: Usuario no esta registrado! :(\n")
	#----------------------   opcion3
	elif opcion=="3":
		print("************************** Login **************************\n")
		global validacion
		validacion = False
		print("\nEl sistema se cierra, Adios :3\n")
	else:
		print("************************ Bienvenido usuario ***********************************\n")
		print("Opcion no validad\n")
	os.system("pause")
	os.system("cls")

"""" *************************************************************************************************  """

"""" *********************************Menu principal del sistems *************************************  """

validacion = True
lista_usuarios = Lista()

while validacion==True:
	os.system("cls")
	print("************************ Bienvenido usuario ***********************************\n")
	print("1. Crear usuario")
	print("2. Ingresar usuario")
	print("3. Salir del programa\n")
	print("Seleciona una opcion: ")
	opcion = input()
	menu_principal(opcion)


"""" *************************************************************************************************  """
	

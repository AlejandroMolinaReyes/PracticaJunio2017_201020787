import os
from estructuras import Lista
from usuario import Usuario
from leerXML import cargaXML

"""" ********************************* Menu Matriz  ****************************************  """
def menu_matriz(usuario,opcion):
	#------------------------------------------------ opcion 1
	if opcion=="1":
		pass
	elif opcion=="2":
		pass
	elif opcion=="3":
		pass
	elif opcion=="4":
		pass
	else:
		print("\nOpcion no validad :(\n")
	os.system("pause")


"""" *****************************************************************************************  """

"""" ********************************* opcion Usuario  ****************************************  """

def menu_usuario(usuario,opcion):
	os.system("cls")
	#------------------------------------------------ opcion 1
	if opcion=="1":
		print("*************************** Cargar XML *************************\n")
		print("Escriba la direccion del archivo, por favor:")
		path = input().strip()
		insertar = True
		for tab , tab2 in cargaXML(path):
			if insertar:
				insertar = False
				usuario.crear_matriz(tab,tab2)
			else:
				usuario.agregar_operacion(tab)
		if insertar== False:
			usuario.set_validacionXML(True)
			print("\nCarga XML Exitosa! :3\n")
	#------------------------------------------------ opcion 2
	elif opcion=="2":
		print("************************* Operaciones *************************\n")
		if usuario.get_validacionXML():
			validarOpcion2 = True
			while validarOpcion2:
				os.system("cls")
				print("************************* Operaciones *************************\n")
				print("1. Operar siguiente")
				print("2. Regresar\n")
				print("Selecciona una opcion: ")
				opcion2 = input().strip()
				#------------------------------------------------ opcion 1
				if opcion2 == "1":
					os.system("cls")
					print("************************* Operaciones *************************\n")
					usuario.operar()
					print("")
					os.system("pause")
				#------------------------------------------------ opcion 2
				elif opcion2=="2":
					os.system("cls")
					print("********************** Operaciones **********************\n")
					print("Adios! :(\n")
					validarOpcion2 = False
				#------------------------------------------------ opcion invalidad
				else:
					os.system("cls")
					print("************************* Operaciones *************************\n")
					print("Opcion no validad\n")
					os.system("pause")
		else:
			print("No hay operaciones en la cola! :(\n")
	#------------------------------------------------ opcion 3
	elif opcion=="3":
		opcion3 = True
		while opcion3:
			os.system("cls")
			print("****************** Operaciones Matriz ******************\n")
			print("1. Ingresar dato")
			print("2. Operar transpuesta")
			print("3. Mostrar matriz original")
			print("4. Mostrar matriz transpuesta")
			print("5. Regresar\n")
			print("Selecciona una opcion: ")
			opcion3 = input().strip()
			if opcion3 == "5":
				os.system("cls")
				print("****************** Operaciones Matriz ******************\n")
				print("Adios! :(\n")
				break
			else:
				menu_matriz(usuario,opcion3)


	#------------------------------------------------ opcion 4
	elif opcion=="4":
		print("********************* Cola de operaciones ********************\n")
		global lista_usuarios
		lista_usuarios.recorrer_inicio_fin()
		lista_usuarios.recorrer_fin_inicio()
		print("")
	#------------------------------------------------ opcion 5
	elif opcion=="5":
		print("*************************** Lista de usuarios *************************\n")
		print("")
		usuario.mostrar_operacion()
		print("")
			
	#------------------------------------------------ opcion invalidad
	else:
		print("************************ Bienvenido "+usuario.get_nombre()+" *********************\n")
		print("Opcion no validad\n")

	os.system("pause")
	os.system("cls")


"""" *******************************************************************************************  """
def opciones_usuario(usuario):
	validar = True

	while validar:
		os.system("cls")
		print("************************ Bienvenido "+usuario.get_nombre()+" *********************\n")
		print("1. Leer Archivo")
		print("2. Resolver operacion")
		print("3. Operar Matriz")
		print("4. Mostrar Usuarios")
		print("5. Mostrar cola")
		print("6. Cerrar sesión\n")
		print("Selecciona una opcion: ")
		opcion = input().strip()
		#------------------------------------------------ opcion 6
		if opcion=="6":
			os.system("cls")
			print("*************************** Cierre de sesion *************************\n")
			print("Adios "+usuario.get_nombre()+"! :(\n")
			break
		#------------------------------------------------ opcion invalidad
		else:
			menu_usuario(usuario,opcion)




"""" *******************************************************************************************  """

"""" ********************************* Metodo menu princial *************************************  """

def menu_principal(opcion):
	os.system("cls")
	#--------------------  opcion 1
	if opcion=="1":
		print("************************ Crear nuevo usuario ***********************\n")
		print("Escriba su nombre de usuario nuevo:")
		nombre = input().strip()
		print("Escriba una contraseña para el usuario nuevo:")
		contraseña = input().strip()
		nuevo_usuario = Usuario(nombre,contraseña)
		global lista_usuarios
		usuario = lista_usuarios.buscar_usuario(nombre)
		if usuario==None:
			lista_usuarios.agregar_final(nuevo_usuario)
			print("\nUsuario fue creado exitosamente :)\n")
		elif usuario.get_nombre()==nombre:
			print("\nError: Usuario ya existe! :(\n")
	#----------------------  opcion 2
	elif opcion=="2":
		print("************************** Login **************************\n")
		print("ingrese su usuario:")
		nombre = input().strip()
		print("ingrese su contraseña")
		contraseña = input().strip()
		global lista_usuarios
		usuario = lista_usuarios.buscar_usuario(nombre)
		if usuario == None:
			print("\nError: Usuario no esta registrado! :(\n")
		elif usuario.get_nombre()==nombre and usuario.get_contraseña()==contraseña:
			opciones_usuario(usuario)
		else:print("\nError: contraseña incorrecta! :(\n")

	#----------------------   opcion3
	elif opcion=="3":
		print("************************** Cierre de sistema **************************\n")
		global validacion
		validacion = False
		print("\nEl sistema se cierra, Adios :3\n")
	#------------------------------------------------ opcion invalidad
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
	print("Selecciona una opcion: ")
	opcion = input().strip()
	menu_principal(opcion)

"""" *************************************************************************************************  """
	

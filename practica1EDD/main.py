import os
from estructuras import lista

"""" ********************************* Metodo menu princial *************************************  """

def menu_principal(opcion):
	os.system("cls")
	#--------------------  opcion 1
	if opcion=="1":
		print("************************ Crear nuevo usuario ***********************\n")
		print("Escriba su nombre de usuario nuevo:")
		usuario = input()
		print("Escriba una contraseña para el usuario nuevo:")
		contraseña = input()
		print("\nUsuario fue creado exitosamente\n")
	#----------------------  opcion 2
	elif opcion=="2":
		print("************************** Login **************************\n")
		print("ingrese su usuario:")
		usuario = input()
		print("ingrese su contraseña")
		contraseña = input();
		print("\nLogin exitoso\n")
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
	

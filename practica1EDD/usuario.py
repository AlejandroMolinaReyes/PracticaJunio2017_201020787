

class Usuario:

	def __init__(self,nombre,contraseña):
		self.__nombre = nombre
		self.__contraseña = contraseña

	def get_nombre(self):
		return self.__nombre

	def get_contraseña(self):
		return self.__contraseña



from .nodo import Nodo


class Lista:

	def __init__(self):
		self.__primero = None
		self.__ultimo = None

	def vacio(self):
		if self.__primero == None:
			return True
		else:
			return False


	def agregar_final(self, dato):
		if self.vacio():
			self.__primero = self.__ultimo = Nodo(dato)
		else:
			nuevo = Nodo(dato)
			self.__ultimo.siguiente = nuevo
			nuevo.anterior = self.__ultimo
			self.__ultimo = nuevo
		self.__primero.anterior = self.__ultimo
		self.__ultimo.siguiente = self.__primero

	def recorrer_inicio_fin(self):
		aux = self.__primero
		while aux:
			print(aux.dato.get_nombre(),aux.dato.get_contraseña())
			aux = aux.siguiente
			if aux == self.__primero:
				break

	def recorrer_fin_inicio(self):
		aux = self.__ultimo
		while aux:
			print(aux.dato.get_nombre(),aux.dato.get_contraseña())
			aux = aux.anterior
			if aux == self.__ultimo:
				break

	def buscar_usuario(self, nombre):
		aux = self.__primero
		usuario = None
		contraseña = None
		if self.__primero!=None:
			while aux:
				if aux.dato.get_nombre() == nombre:
					usuario = aux.dato.get_nombre()
					contraseña = aux.dato.get_contraseña()
					break
				aux = aux.siguiente
				if aux == self.__primero:
					break
				
				
		return usuario, contraseña
			







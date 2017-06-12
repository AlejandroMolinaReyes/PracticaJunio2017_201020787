from .nodo import Nodo

class Pila:
	def __init__(self):
		self.__primero = None

	def vacio(self):
		if self.__primero == None:
			return True
		else:
			return False
	def vaciar_pila(self):
		self.__primero = None

	def push(self, dato):
		if self.vacio():
			self.__primero = Nodo(dato)
		else:
			nuevo = Nodo(dato)
			nuevo.siguiente = self.__primero
			self.__primero = nuevo

	def pop(self):
		if self.vacio():
			return None
		elif self.__primero.siguiente==None:
			auxDato = self.__primero.dato
			self.__primero = None
			return auxDato
		else:
			auxDato = self.__primero.dato
			auxNodo = self.__primero.siguiente
			self.__primero.siguiente = None
			self.__primero = auxNodo
			return auxDato

	def mostrar(self):
		aux = self.__primero
		while aux!=None:
			print(aux.dato)
			aux = aux.siguiente






			

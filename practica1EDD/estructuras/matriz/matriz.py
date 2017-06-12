from nodoMatriz import NodoMatriz
from nodoCabecera import NodoCabecera

class Matriz:
	
	def __init__(self,x,y):
		self.__tamanoX = x
		self.__tamanoY = y
		self.__fila = None
		self.__columna = None
		self.crear_cabeceras(x,y)

	def crear_cabeceras(self,x,y):
		contador = 1
		while contador <= x:
			self.__columna = self.agregar_cabecera(self.__columna,contador)
			contador+=1
		contador = 1
		while contador<=y:
			self.__fila = self.agregar_cabecera(self.__fila,contador)
			contador +=1

	def agregar_cabecera(self,cabecera,dato):
		
		if cabecera==None:
			cabecera=NodoCabecera(dato)
		else:
			aux = cabecera
			while aux.siguiente!=None:
				aux = aux.siguiente
			aux.siguiente = NodoCabecera(dato)
		return cabecera

	def buscar_fila(self,posicion):
		aux = self.__fila
		while aux!=None:
			if aux.posicion == posicion:
				return aux
			aux = aux.siguiente

	def buscar_columna(self,posicion):
		aux = self.__columna
		while aux!=None:
			if aux.posicion = posicion:
				return aux
			aux = aux.siguiente


	def agregar_Nodo(self,x,y):
		if self.__fila.nodo==None and self.__columna.node==None:
			nuevo = NodoMatriz(x,y)
			self.__fila.nodo = nuevo
			self.__columna.nodo = nuevo
			nuevo.cabeceraFila = self.__fila
			nuevo.cabeceraColumna = self.__columna
		elif self.__fila.nodo==None and self.__columna.nodo!=None:
			contador = 2
			while contador<=x:
				nuevo = NodoMatriz(contador,1)
				auxCabecera = self.buscar_columna(contador)
				auxNodo = buscar_fila.nodo
				while auxNodo.siguiente!=None:
					auxNodo = auxNodo.siguiente
				auxNodo.siguiente = nuevo
				nuevo.anterior = auxNodo
				nuevo.cabeceraFila = auxCabecera
				auxCabecera.nodo = nuevo



	def mostra_cabeceras(self):
		aux = self.__columna
		while aux!=None:
			print("columna:",aux.posicion)
			aux = aux.siguiente
		aux = self.__fila
		while aux!=None:
			print("fila:",aux.posicion)
			aux = aux.siguiente

matriz = Matriz(5,5)
matriz.mostra_cabeceras()


		






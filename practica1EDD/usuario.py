from estructuras import Cola
from estructuras import Pila
#from estructuras import Matriz

class Usuario:

	def __init__(self,nombre,contraseña):
		self.__nombre = nombre
		self.__contraseña = contraseña
		self.__cola = Cola()
		self.__pila = Pila()
		#self.__matriz = Matriz()
		#self.__matrizTranspuesta = 
		self.__validacionXML = False

	def get_nombre(self):
		return self.__nombre

	def get_contraseña(self):
		return self.__contraseña

	def agregar_operacion(self, dato):
		self.__cola.enqueue(dato)

	def extraer_operacion(self):
		return self.__cola.dequeue()

	def mostrar_operacion(self):
		self.__cola.mostrar()

	def crear_matriz(self,x,y):
		pass

	def get_validacionXML(self):
		return self.__validacionXML

	def set_validacionXML(self, validar):
		self.__validacionXML = validar

	def operar(self):
		operacion = self.__cola.dequeue()
		aux = ""
		self.__pila.vaciar_pila()
		if operacion!=None:
			for caracter in operacion:
				#------------------------------------contatedo numero
				if caracter>='0' and caracter<='9':
					aux = aux + caracter
				#-------------------------------apilar numero
				elif caracter == " ":
					if aux!="":
						print("Apilando:",aux)
						self.__pila.push(int(aux))
					aux = ""
				#-------------------------------- sumo numeros
				elif caracter =="+":
					numero2 = self.__pila.pop()
					numero1 = self.__pila.pop()
					if numero1!=None and numero2!=None:
						resultado = numero1 + numero2
						print("Sumo: ",numero1,"+",numero2)
						self.__pila.push(resultado)
						print("Apilo:",resultado)
					else:
						print("Error de syntaxis :(")

				#-------------------- resto numeros
				elif caracter == "-":
					numero2 = self.__pila.pop()
					numero1 = self.__pila.pop()
					if numero1!=None and numero2!=None:
						resultado = numero1 - numero2
						print("Resto: ",numero1,"-",numero2)
						self.__pila.push(resultado)
						print("Apilo:",resultado)
					else:
						print("Error de syntaxis :(")
					
				#---------------------------- multiplico numeros
				elif caracter=="*":
					numero2 = self.__pila.pop()
					numero1 = self.__pila.pop()
					if numero1!=None and numero2!=None:
						resultado = numero1 * numero2
						print("Multiplico: ",numero1,"*",numero2)
						self.__pila.push(resultado)
						print("Apilo:",resultado)
					else:
						print("Error de syntaxis :(")
				#------------------------------ cacater raro
				elif caracter=="\t" or caracter == "\n":
					pass
				else:
					print('Caracter no reconocido:',caracter)
			print("Respuesta:",self.__pila.pop())			
		else:
			print("Ya no hay operaciones! :(")


import os 
from xml.etree import ElementTree 

def cargaXML(path):

	file_name = path
	try:
		full_file = os.path.abspath(os.path.join(file_name))
		dom = ElementTree.parse(full_file)
		matrizX = dom.find('matriz/x').text
		matrizY = dom.find('matriz/y').text
		yield matrizX ,matrizY
		operacion = dom.findall('operaciones/operacion')
		for tab  in operacion:
			yield tab.text.strip(), None
	except Exception as error:
		print("\nDireccion invalidad! :(\n")


#for tab , tab2 in cargaXML("c:/carga.xml"):
#	print(tab,tab2)



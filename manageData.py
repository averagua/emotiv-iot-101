# objetos de data de 16*256. Lista de 16 diccionarios de tamaño 256 donde se almacenarán las mediciones.

class DataBuff:
	
	def __init__(self,channels,bufsize):

		blankdict={}
		blanklist=[]
		
		for i in range(256):
			blankdict[str(i)]=0

		for j in range(16):
			blanklist[j]=blankdict

		self.datos=blanklist 	#Arreglo vacío
		self.index=0			#Contador de fila de datos agregada, si llega a 257, el arreglo se resetea.


	def add_data(datavector):
		#Agrega los datos en secuencia, resetea y agrega en la primera posición si el buffer está lleno
		if self.index<255:
			
			for i in range(16):
				self.datos[i][str(self.index)]=datavector[i]

			self.index+=1

		else: 
			self.flush()
			for i in range(16):
				self.datos[i][str(self.index)]=datavector[i]
			self.index+=1




	def flush():
		#Resetea el arreglo
		for i in range(16):
			for j in range(256):
				self.datos[i][str(j)]=0

		self.index=0

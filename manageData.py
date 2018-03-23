# objetos de data de 16*256. Lista de 16 diccionarios de tamaño 256 donde se almacenarán las mediciones.

class DataBuff:
	
	def __init__(self,channels,bufsize):

		blankdict={}
		blanksub={}
		
		self.chan=channels
		self.size=bufsize

		for i in range(bufsize):
			blanksub[str(i)]=0

		for j in range(channels):
			blankdict["chan"+str(j+1)]=blanksub

		self.data=blankdict 	#Nested dictionary, vacío (con puros ceros)
		self.index=0			#Contador de fila de datos agregada, si llega a 257, el arreglo se resetea.


	def add_data(self,datavector):
		#Agrega los datos en secuencia, resetea y agrega en la primera posición si el buffer está lleno
		if self.index<256:
			
			for i in range(self.size):
				self.data["chan"+str(i+1)][str(self.index)]=datavector[i]

			self.index+=1

		else: 
			self.flush()
			for i in range(self.chan):
				self.data["chan"+str(i+1)][str(self.index)]=datavector[i]
			self.index+=1




	def flush(self):
		#Resetea el arreglo
		for i in range(self.chan):
			for j in range(self.size):
				self.data["chan"+str(i+1)][str(j)]=0

		self.index=0

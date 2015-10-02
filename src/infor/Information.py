import resource
import psutil
from datetime import datetime
import socket

class Information:

	arrayListOption = 0

	def __init__(self):
		self.setOptions()


	def setOptions(self):
		self.arrayListOption = {
		'USOMEN': psutil.virtual_memory(),
		'SYSNOM': socket.gethostname(), 
		'DATHOR': datetime.now() , 
		'USOCPU': psutil.cpu_times ()  
		}  


	def getOptions(self, key):
		if (str(key) in self.arrayListOption): 
			stg = str(self.arrayListOption[key])
		else:
			stg = 'nada encontrado'
		return stg    
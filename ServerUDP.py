import socket

class ServerUDP:

    HOST = ''     # Endereco IP do Servidor
    PORT = 12200  # Porta que o Servidor esta
    udp = 0

    def __init__(self, host):
      self.setCon(host)

    @classmethod  
    def setCon(self,host):
	    self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #obj udp
	    orig = (host, self.PORT) # contatenando host e porta
	    self.udp.bind(orig)

    def getCon(self):
      	return self.udp 




import socket

HOST = 'localhost'  # Endereco IP do Servidor
PORT = 12200            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

print 'Para sair use CTRL+C\n'

msg = raw_input()

while msg <> '\x18':

    udp.sendto (msg, dest)
    modified, c = udp.recvfrom(2048)	
    print modified
    msg = raw_input() 

udp.close()
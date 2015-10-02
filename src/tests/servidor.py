from ServerUDP import ServerUDP
from Information import Information


objUDP = ServerUDP('')

while True:
    udp = objUDP.getCon()
    msg, c = udp.recvfrom(2048)
    modified = msg.upper()

    Info = Information()
    print modified
    udp.sendto(Info.getOptions(modified),c)
    del Info
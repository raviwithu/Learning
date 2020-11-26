import socket
import sys

#create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#bind the socket to port
server_address = ('0.0.0.0', 1947)
print("Strating up on %s port" , sys.stderr)
sock.bind(server_address)

#Listen for incoming connection
sock.listen(1)


while True:
    #wait for connection
    print("Waiting for connection")
    connection, client_address = sock.accept()

    try:
        print("connection from" , client_address)
        #receive the data in small chunks and retrasmit it
        while True:
            data = connection.recv(2048)
            
            #print("received data - %s", data)
            if data:
                #connection.sendall(data)
                #print("sending hello")
                #data = "Hello"
                #connection.send(data.encode())
                print("echo data...")
                connection.sendall(data)
            else:
                print("no more data from" , client_address)
                break



    finally:
        #clean up the connection
        connection.close()

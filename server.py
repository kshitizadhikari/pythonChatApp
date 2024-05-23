import socket
import threading
"""
create a server socket and bind it to a particular host and port 
set the limit of the number of clients
make it listen to connection from clients
accept connection when the client sends connection request    
"""

HOST = '127.0.0.1'
PORT = 1234
LISTENER_LIMIT = 5

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        print(f"Server started at {HOST} and the port used is: {PORT}")
    except:
        print (f"Unable to connect to Host: {HOST} and Port: {PORT}")
    
    server.listen(LISTENER_LIMIT)

    while 1:
        client, address = server.accept()

        print(f"Connected to client: {client}, Client Host: {address[0]}, Client Port: {address[1]}")



if __name__ == '__main__':
    main()
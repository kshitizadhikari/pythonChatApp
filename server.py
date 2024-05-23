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
active_clients = []


def listen_for_message(client, username):
    while 1:
        message = client.recv(2048).decode('utf-8')
        # if message == '':
        #     print(f"Message sent by {username} is empty")
        
        final_msg = f"{username}: {message}"
        send_message_to_all(final_msg)


#send message to all
def send_message_to_all(message):
    for client in active_clients:
        send_message(client[1], message)

#send message to one person
def send_message(client, message):
    client.sendall(message.encode())

#client handling function
def client_handler(client: socket):
    while 1:
        username = client.recv(1024).decode('utf-8')
        if username == '':
            raise Exception("Username empty")
        break
        
    active_clients.append((username, client))

    threading.Thread(target=listen_for_message, args=(client, username, )).start()
        


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
        print(f"Connected to client, Client Host: {address[0]}, Client Port: {address[1]}")

        threading.Thread(target=client_handler, args=(client, )).start()



if __name__ == '__main__':
    main()
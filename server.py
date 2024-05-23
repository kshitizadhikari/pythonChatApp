import socket
import threading

HOST = '127.0.0.1'
PORT = 1234
LISTENER_LIMIT = 5
active_clients = []

def listen_for_messages(client, username):
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message:
                final_msg = f"{username}: {message}"
                print(final_msg)
                send_message_to_all(client, final_msg)
            else:
                remove_client(client)
                break
        except:
            remove_client(client)
            break

def send_message_to_all(client, message):
    for user in active_clients:
        if user[1] != client:
            send_message(user[1], message)

def send_message(client, message):
    try:
        client.sendall(message.encode())
    except:
        remove_client(client)

def client_handler(client):
    while True:
        try:
            username = client.recv(1024).decode('utf-8')
            if username:
                active_clients.append((username, client))
                threading.Thread(target=listen_for_messages, args=(client, username)).start()
                break
            else:
                raise ValueError("Empty username received")
        except Exception as e:
            print(f"Error: {e}")
            client.close()
            break

def remove_client(client):
    for user in active_clients:
        if user[1] == client:
            active_clients.remove(user)
            print(f"{user[0]} has disconnected")
            break
    client.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
        print(f"Server started at {HOST} on port {PORT}")
    except Exception as e:
        print(f"Failed to bind server on {HOST}:{PORT}, Error: {e}")
        return
    
    server.listen(LISTENER_LIMIT)

    while True:
        try:
            client, address = server.accept()
            print(f"Connected to client at {address[0]}:{address[1]}")
            threading.Thread(target=client_handler, args=(client,)).start()
        except Exception as e:
            print(f"Error accepting connections: {e}")
            break
    
    server.close()

if __name__ == '__main__':
    main()

import socket
import threading

ServerHOST = '127.0.0.1'
ServerPort = 1234

def communicate_with_server(client):
    username = input("Enter username: ").strip()
    if not username:
        print("Username cannot be empty")
        return
    client.sendall(username.encode())
    
    # Start a thread to listen for messages from the server
    threading.Thread(target=listen_for_message_from_server, args=(client,)).start()
    
    # Main thread will handle sending messages to the server
    send_message_to_server(client, username)

def listen_for_message_from_server(client):
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if not message:
                # Server has closed the connection
                print("Server has closed the connection")
                client.close()
                break
            print(message)
        except Exception as e:
            print(f"Error: {e}")
            client.close()
            break

def send_message_to_server(client, username):
    while True:
        message = input(f"{username}: ").strip()
        if message:
            try:
                client.sendall(message.encode())
            except Exception as e:
                print(f"Error: {e}")
                client.close()
                break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((ServerHOST, ServerPort))
        print("Successfully connected to server")
        communicate_with_server(client)
    except Exception as e:
        print(f"Unable to connect to {ServerHOST}:{ServerPort}. Error: {e}")

if __name__ == '__main__':
    main()

import socket
import threading

"""
    create client socket
    connect to the server socket

"""

ServerHOST = '127.0.0.1'
ServerPort = 1234

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((ServerHOST, ServerPort))
        print("Successfully connected to server")
    except:
        print(f"Unable to connect to ServerHost: {ServerHOST}, ServerPort: {ServerPort}")
    


if __name__ == '__main__':
    main()
import time
from socket import *
import threading

def client_handle(conn,addr):
    print(f"Connected by {addr}")
    buffer_size = 1024
    msg = conn.recv(buffer_size).decode('utf-8')
    print(f"Message received: {msg}")
    response = "Hello from server"
    conn.send(response.encode('utf-8'))
    print("Hello message sent")
    conn.close()


def main():


    server_IP ='localhost'
    server_port = 12001
    server_address = ('',12001)
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('',12001))
    server_socket.listen(3)
    print("Server listening on port 12001")

    while 1 :
        conn,addr = server_socket.accept()
        client_thread = threading.Thread(target=client_handle, args=(conn,addr))
        client_thread.start()

if __name__ == "__main__":
    main()


























# server_socket.listen(3)
# print(" server is listening on port 8002.")

# client_socket,client_address = server_socket.accept()
# print (f"accepted connection from {client_address}")

# buffer_msg = client_socket.recv(1024).decode()
# print(f"Message received: {buffer_msg}")
# msg_sent = "hello form server"

# client_socket.send(msg_sent.encode())
# print ("message sent")

# client_socket.close()
# server_socket.close()



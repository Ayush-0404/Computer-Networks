import time
from socket import *

server_IP ='localhost'
server_port = 12000

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('',12000))


server_socket.listen(3)
print(" server is listening on port 8002.")

client_socket,client_address = server_socket.accept()
print (f"accepted connection from {client_address}")

buffer_msg = client_socket.recv(1024).decode()
print(f"Message received: {buffer_msg}")
msg_sent = "hello form server"

client_socket.send(msg_sent.encode())
print ("message sent")

client_socket.close()
server_socket.close()



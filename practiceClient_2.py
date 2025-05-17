from socket import *


def main(): 
    client_socket = socket(AF_INET,SOCK_STREAM)

    server_IP = 'localhost'
    server_port = 12000
    server_addr = (server_IP,server_port)


    try:
        client_socket.connect(server_addr)
        print("connected to server")

    except socket.error as e:
        print(f"connection failed: {e}")
        return

    msg_sent = "Hello from client"

    client_socket.send(msg_sent.encode())
    print("message from client side")

    buffer_msg = client_socket.recv(1024).decode()
    print (f"server response : {buffer_msg}")

    client_socket.close()

if __name__ == "__main__":
    main()




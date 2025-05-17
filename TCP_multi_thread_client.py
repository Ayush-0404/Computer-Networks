from socket import *
import threading

server_IP= ''

def client_task():
    server_IP = 'localhost'
    serever_port = 12001

    server_address = ((server_IP,serever_port))
    msg = "hello from client"
    buffer_size = 1024

    thread_id = threading.get_ident()

    try :
        c_sock = socket(AF_INET,SOCK_STREAM)

        c_sock.connect(server_address)
        print(f"Thread {thread_id}: Connected to server")
        c_sock.sendall(msg.encode('utf-8'))
        print(f"Thread {thread_id}: Hello message sent")

        msg_recieved = c_sock.recv(buffer_size).decode()
        print(f"Thread {thread_id}: Message received: {msg_recieved}")
        
    except socket.error as e:
        print(f"Thread {thread_id}: Socket error: {e}")

    finally:
        c_sock.close






def main():
    t1 = threading.Thread(target = client_task)
    t2 = threading.Thread(target= client_task)

    t1.start()
    t2.start()


    t1.join()
    t2.join()

if __name__ == "__main__":
    main()




from socket import *
import threading
import sys

server_IP= ''

# def address():
#     server_IP/H = sys.argv[1]
    # server_port = sys.argv[2]
    # f_name = sys.argv[3]

#     server_addr = ((server_IP,serever_port))
#     return server_addr

def client_work(server_IP,server_port,f_name):
    
    buffer_size = 4096

    thread_id = threading.get_ident()
    #print(f"Thread ID: {thread_id}")

    try :
        c_sock = socket(AF_INET,SOCK_STREAM) #TCP

        c_sock.connect((server_IP,int(server_port)))
        req = f"GET /{f_name} HTTP/1.1\r\nHost: {server_IP}\r\n\r\n"

        c_sock.send(req.encode())
        msg_recieved = c_sock.recv(buffer_size).decode()

        print(f"Server response:\n {msg_recieved}")

        # print(f"Thread {thread_id}: Connected to server")
        # c_sock.sendall(msg.encode('utf-8'))
        # print(f"Thread {thread_id}: Hello message sent")

        # msg_recieved = c_sock.recv(buffer_size).decode()
        # print(f"Thread {thread_id}: Message received: {msg_recieved}")
        
    except socket.error as e:
        print(f"Socket error: {e}")

    finally:
        c_sock.close



# def main():
#     t1 = threading.Thread(target = client_work)
#     t2 = threading.Thread(target= client_work)

#     t1.start()
#     t2.start()


#     t1.join()
#     t2.join()
def input_run():
    server_IP = sys.argv[1]
    server_port = sys.argv[2]
    f_name = sys.argv[3]

    client_work(server_IP,server_port,f_name)
    

if __name__ == "__main__":

    if len(sys.argv)!= 4:
        print("Please give arguments in specified format: python3 client.py server_host server_port filename")
        sys.exit(1)

    input_run()







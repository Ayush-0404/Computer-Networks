# # Import socket and threading modules
# from socket import *
# import threading
# import sys  # In order to terminate the program

# # Function to handle a client connection
# def handle_client(connectionSocket,addr):

#     print(f"Connected by {addr}")
#     thread_id = threading.get_ident()  # Get the thread ID
#     client_port = addr[1]  
    
#     # Print thread ID and port
#     print(f"Thread ID: {thread_id}, Client Port: {client_port}")
#     try:
#         # Receive the message from the client
#         message = connectionSocket.recv(1024).decode()
#         print(f"Message: {message}")  # Debug: Print the HTTP request
        
#         # Extract the filename from the HTTP request
#         filename = message.split()[1]
#         if filename == '/':
#             filename = '/index.html'  # Default to index.html if no file is specified

#         # Open and read the requested file
#         f = open(filename[1:], 'r')
#         outputdata = f.read()

#         # Send HTTP response header
#         connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
#         connectionSocket.send('Content-Type: text/html\r\n\r\n'.encode())

#         # Send the content of the requested file to the client
#         connectionSocket.send(outputdata.encode())
#         connectionSocket.send("\r\n".encode())
        
#     except IOError:
#         # Send response message for file not found
#         try:
#             connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
#             connectionSocket.send('Content-Type: text/html\r\n\r\n'.encode())
#             connectionSocket.send('<html><body><h1>404 Not Found</h1></body></html>'.encode())
#         except OSError as e:
#             print(f"Error sending 404: {e}")

#     finally:
#         # Close the client socket
#         connectionSocket.close()

# # Main server function to handle incoming connections
# def main():
#     # Create a socket for the server
#     serverSocket = socket(AF_INET, SOCK_STREAM)

#     # Prepare the server socket
#     serverPort = 8005
#     serverSocket.bind(('', serverPort))
#     serverSocket.listen(5)  # Listen for up to 5 connections

#     print(f'Server listening on port {serverPort}')
#     print('Ready to serve...')

#     while True:
#         # Accept a new connection
#         connectionSocket, addr = serverSocket.accept()
#         print(f"Connected by: {addr}")

#         # Create a new thread for each client connection
#         client_thread = threading.Thread(target=handle_client, args=(connectionSocket,addr))
#         client_thread.start()

#     # Close the server socket when done
#     serverSocket.close()

# if __name__ == "__main__":
#     main()

#import socket module
from socket import *
import sys  # In order to terminate the program
import threading  # Import threading module

# Function to handle client requests
def handle_client(connectionSocket,addr):
    try:
        thread_id = threading.get_ident()  # Get the thread ID
        client_port = addr[1]  
    
        print(f"Thread ID: {thread_id}, Client Port: {client_port}")
        # Receive and decode the client's request
        message = connectionSocket.recv(1024).decode()  
        if not message:
            connectionSocket.close()
            return

        # Parse the requested file name from the message
        filename = message.split()[1]
        f = open(filename[1:])  # Open the requested file (ignoring the first '/')

        # Read the file contents
        outputdata = f.read()

        # Send HTTP response headers
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())  # Assuming HTML content

        # Send the file content to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        # Send a blank line to indicate the end of content
        connectionSocket.send("\r\n".encode())

    except IOError:
        # If the file is not found, send a 404 response
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())

    finally:
        # Close the connection socket after serving the client
        connectionSocket.close()


# Main server function
def start_server():
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverPort = 12000
    serverSocket.bind(('', serverPort))  
    serverSocket.listen(5)  # Listen for incoming connections, with a maximum backlog of 5 clients

    print('Server is ready to serve...')

    while True:
        # Accept the connection from the client
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        # Create a new thread for each client
        client_thread = threading.Thread(target=handle_client, args=(connectionSocket,addr))
        client_thread.start()

# Start the server
if __name__ == "__main__":
    start_server()

# sys.exit() is not needed because the server runs indefinitely.

import sys
import socket

host = '127.0.0.1'
port = 5050

client_socket = socket.socket()
client_socket.connect((host, port))

if len(sys.argv) > 1:
    request = sys.argv[1]
else:
    request = "GET_NOTES"

# add newline delimiter
message = request + "\n"
client_socket.send(message.encode())

response = client_socket.recv(1024).decode()
print("Server response:")
print(response)

client_socket.close()

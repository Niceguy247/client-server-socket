import socket

host = '127.0.0.1'
port = 5050

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)
print("Server is running on port", port)

while True:
    conn, addr = server_socket.accept()
    print("Connected to client at", addr)

    data = conn.recv(1024).decode()
    if not data:
        conn.close()
        continue

    # remove newline for checking
    request = data.strip()
    print("Received request:", request)

    if request == "GET_NOTES":
        reply = "200 OK: Operating Systems Lecture 1 - Overview and Services\n"
    else:
        reply = "404 ERROR: Unknown request\n"

    conn.send(reply.encode())
    conn.close()

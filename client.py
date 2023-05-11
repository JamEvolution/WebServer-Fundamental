import socket

server_address = ('localhost', 5000)

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect(server_address)
# send to byte string
tcp_socket.send(b"Hi! Server. I am Client1")
# 32 byte data memory
data = tcp_socket.recv(32)
print("Server the response: ", data)
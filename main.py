import socket


class SocketServer:
    def __init__(self, server_ip, server_port):
        # AF_INET -> IP, SOCK_STREAM -> TCP, SOCK_DGRAM -> UDP
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # localhost -> 127.0.0.1, 5000 -> port
        self.server_ip = server_ip
        self.server_port = server_port
        self.server_address = (server_ip, server_port)

        self.tcp_socket.bind(self.server_address)

    def start(self):
        # 1 -> 1 client handle
        self.tcp_socket.listen(1)
        print(f"Custom Server started at IP:{self.server_ip} Port:{self.server_port}")

        while True:
            connection, client_address = self.tcp_socket.accept()
            print(f"Client {client_address} is connected to custom server.")
            # 1024 byte data memory -> 1KB
            data = connection.recv(1024)
            # data.decode() binary to string
            print("Received data: ", data.decode())

            header = "HTTP/1.1 200 OK\n"
            header += "Server: Custom\n"
            header += "Content-Type: text/html; charset=UTF-8\n"
            header += "\n"

            # body = "Hi! Class.I am The Boss Server"

            with open("index.html") as file_object:
                body = file_object.read()

            response = header + body

            print(response)
            connection.send(response.encode(encoding="UTF-8"))


socket_server = SocketServer('localhost', 5000)
socket_server.start()
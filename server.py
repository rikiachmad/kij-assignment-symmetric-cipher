import socket, logging

class Server:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    BUFFER_SIZE = 4096
    def __init__(self, host="0.0.0.0", port=65432):
        self.host = host
        self.port = port
        self.s.bind((host, port))

    def receive_file(self):
        self.s.listen(5)
        logging.info((f"Listening as {self.host}:{self.port}..."))

    def get_host(self):
        return self.host

    def set_host(self, host):
        self.host = host
        return
    
    def get_port(self):
        return self.port
    
    def set_port(self, port):
        self.port = port
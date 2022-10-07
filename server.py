import socket, logging, os
from tqdm import tqdm

class Server:
    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 4096

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self, host="0.0.0.0", port=65432):
        self.host = host
        self.port = port
        self.s.bind((host, port))

    def receive_file(self):
        self.s.listen(5)
        logging.info((f"Listening as {self.host}:{self.port}..."))
        logging.info((f"Waiting for connection..."))
        client_socket, address = self.s.accept()
        logging.info(f"{address} is connected.")

        received = client_socket.recv(self.BUFFER_SIZE).decode()
        self.in_filename, self.out_filename, self.filesize, self.cipher = received.split(self.SEPARATOR)

        filesize = int(self.filesize)

        progress = tqdm(range(filesize), f"Receiving {self.out_filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(self.out_filename, "wb") as f:
            while True:
                bytes_read = client_socket.recv(self.BUFFER_SIZE)
                if not bytes_read:    
                    break
                f.write(bytes_read)
                progress.update(len(bytes_read))

        client_socket.close()
        self.s.close()

    def get_host(self):
        return self.host

    def set_host(self, host):
        self.host = host
    
    def get_port(self):
        return self.port
    
    def set_port(self, port):
        self.port = port

    def get_info(self):
        return self.in_filename, self.out_filename, self.cipher
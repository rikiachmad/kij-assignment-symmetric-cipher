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
        client_socket, address = self.s.accept()
        logging.info(f"{address} is connected.")

        received = client_socket.recv(self.BUFFER_SIZE).decode()
        self.filename, self.filesize = received.split(self.SEPARATOR)

        filename = os.path.basename(self.filename)
        filesize = int(self.filesize)

        enc_filename = filename + ".enc"

        progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(enc_filename, "wb") as f:
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
        return
    
    def get_port(self):
        return self.port
    
    def set_port(self, port):
        self.port = port

    def get_file_info(self):
        return self.filename, self.filesize
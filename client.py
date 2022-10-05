import socket
import sys, os
from tqdm import tqdm

class Client():
    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 4096
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self, host="127.0.0.1", port=65432):
        self.host = host
        self.port = port
        self.s.connect((host, port))
    
    def send_file(self, filename):
        self.s.send(f"{filename}{self.SEPARATOR}{filesize}".encode())

        filesize = os.path.getsize(filename)
        progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        
        with open(filename, "rb") as f:
            while True:
                    bytes_read = f.read(self.BUFFER_SIZE)
                    if not bytes_read:
                        break
                    self.s.sendall(bytes_read)
                    progress.update(len(bytes_read))
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


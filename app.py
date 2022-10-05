import os, logging
from client import Client
from server import Server
class App:
    
    def __init__(self):
        pass

    def send_file(self, in_filename, encryption, chunksize=64*1024):
        if not self.file_exist(in_filename):
            logging.exception(f'File {in_filename} does not exist.')
            return

        out_filename = in_filename + '.enc'
        # create encryptor

        with open(in_filename, 'rb') as infile:
            with open(out_filename, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    outfile.write(encryptor.encrypt(chunk))

        client = Client(port = 5001)
        client.send_file(in_filename)
        
    def receive_file(self):
        server = Server(port = 5001)
        server.receive_file()
        filename, filesize = server.get_file_info
        # create decryptor

    def file_exist(self, filename):
        return os.path.isfile(filename)
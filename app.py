import os, logging, sys
from client import Client
from server import Server
from encdec import Encdec
class App:
    
    def __init__(self,chunk_size=64*1024):
        self.chunksize = chunk_size

    def send_file(self, in_filename, cipher):
        if not self.file_exist(in_filename):
            raise Exception(f'File {in_filename} does not exist.')
        print("path: ", in_filename)
        encryptor = Encdec(cipher, self.chunksize)
        out_filename = os.path.basename(in_filename) + '.enc'
        encryptor.encrypt_file(in_filename, out_filename)
        
        client = Client(port = 5001)
        client.send_file(os.path.basename(in_filename),out_filename, cipher)

        logging.info(f"Total Encryption time: {encryptor.get_enc_time()} nanoseconds")
        
    def receive_file(self):
        server = Server(port = 5001)
        server.receive_file()
        in_filename, out_filename, cipher = server.get_info()
        
        # create decryptor
        decryptor = Encdec(cipher, self.chunksize)
        decryptor.decrypt_file(in_filename, out_filename)

        logging.info(f"Total Decryption time: {decryptor.get_dec_time()} nanoseconds")
    def file_exist(self, filename):
        return os.path.isfile(filename)
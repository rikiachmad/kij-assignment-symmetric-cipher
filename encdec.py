import time
from telnetlib import EC
from Crypto.Cipher import AES, DES, ARC4
from base64 import b64encode, b64decode

class Encdec:
    ##encrypt/decrypt using aes, des & rc4.
    AES = "AES"
    DES = "DES"
    RC4 = "RC4"
    available_cipher=[AES, DES, RC4]

    def __init__(self, cipher=AES, chunk_size=64*1024):
        self.chunk_size = chunk_size
        cipher = cipher.upper()
        if cipher not in self.available_cipher:
            raise Exception("Cipher not valid. Available cipher: AES, DES, RC4")

        self.cipher = cipher
        if self.cipher == self.AES:
            self.init_AES()
        
        elif self.cipher == self.DES:
            self.init_DES()

        elif self.cipher == self.RC4:
            self.init_RC4()
        

    def encrypt_file(self, in_filename, out_filename):
        self.enc_time = 0
        try:
            with open(in_filename, 'rb') as infile:
                with open(out_filename, 'wb') as outfile:
                    while True:
                        chunk = infile.read(self.chunk_size)
                        if len(chunk) == 0:
                            break
                        start = time.perf_counter_ns()
                        enc_chunk = self.object.encrypt(chunk)
                        end = time.perf_counter_ns()

                        self.enc_time+=(end - start)
                        outfile.write(enc_chunk)
        except Exception as e:
            raise Exception(e)

    def decrypt_file(self, in_filename, out_filename):
        self.dec_time = 0
        try:
            with open(out_filename, 'rb') as infile:
                with open(in_filename, 'wb') as outfile:
                    while True:
                        chunk = infile.read(self.chunk_size)
                        if len(chunk) == 0:
                            break
                        
                        start = time.perf_counter_ns()
                        dec_chunk = self.object.decrypt(chunk)
                        end = time.perf_counter_ns()

                        self.dec_time+=(end - start)
                        outfile.write(dec_chunk)          
        except Exception as e:
            raise Exception(e)

    def init_AES(self):
        self.aes_key = b'AES 16 BYTES KEY'
        self.aes_nonce = b'8B NONCE'
        self.object = AES.new(self.aes_key, AES.MODE_CTR, nonce = self.aes_nonce)

    def init_DES(self):
        self.des_key = b'-8B KEY-'
        self.des_nonce = b'2B'
        self.object = DES.new(self.des_key, DES.MODE_CTR, nonce = self.des_nonce)
    
    def init_RC4(self):
        self.rc4_key = b'RC4 16 BYTES KEY'
        self.object = ARC4.new(self.rc4_key)
    
    def get_enc_time(self):
        return self.enc_time
    
    def get_dec_time(self):
        return self.dec_time

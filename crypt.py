import time
from base64 import b64encode, b64decode
from Crypto.Cipher import AES, DES, ARC4
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

class Crypt:
    ##encrypt/decrypt using aes(CBC), des & rc4.
    def __init__(self):
        self.aes_key = b'AES KEY'
        self.des_key = b'-8B kEY-'
        self.rc4_key = b'RC4 KEY'
        self.aes = AES.new(self.aes_key, AES.MODE_CBC)
        self.des = DES.new(self.des_key, DES.MODE_OFB)
        self.rc4 = ARC4.new(self.rc4_key)

    def encrypt_AES(self,data):
        data = self.add_padding(data)
        self.startTime()
        cypher_text  = self.aes.encrypt(data)
        self.endTime()

        time = self.end - self.start

        return cypher_text, time

    def decrypt_AES(self):
        pass

    def encrypt_DES(self):
        pass

    def decrypt_DES(self):
        pass
    
    def encrypt_RC4(self):
        pass

    def decrypt_RC4(self):
        pass

    def add_padding(self, data):
        return pad(data, AES.block_size)

    def start_time(self):
        self.start = time.time()

    def end_time(self):
        self.end = time.time()



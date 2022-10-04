import time
from base64 import b64encode, b64decode
from Crypto.Cipher import AES, DES, ARC4
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

class Crypt:
    ##encrypt/decrypt using aes(CBC), des & rc4.
    def __init__(self):
        self.aes_key = get_random_bytes(16)
        self.des_key = b'-8B kEY-'
        self.rc4_key = get_random_bytes(16)
        self.nonce = "JustRandomNonce"
        self.aes = AES.new(self.aes_key, AES.MODE_CTR, self.nonce)
        self.des = DES.new(self.des_key, DES.MODE_OFB)
        self.rc4 = ARC4.new(self.rc4_key)

    def encrypt_AES(self,plain_text):
        plain_text = self.add_padding(plain_text)
        cypher_text  = self.aes.encrypt(plain_text)

        return cypher_text

    def decrypt_AES(self, cypher_text):
        plain_text = self.remove_padding(self.aes.decrypt(cypher_text))

        return plain_text

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
    
    def remove_padding(self, data):
        return unpad(data, AES.block_size)

    def get_keys(self):
        return {
            "aes": self.aes_key,
            "des": self.des_key,
            "rc4": self.rc4_key,
            "nonce": self.nonce
        }



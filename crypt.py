import time
from base64 import b64encode, b64decode
import Crypto
from Crypto.Cipher import AES, DES, ARC4
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

class Crypt:
    ##encrypt/decrypt using aes, des & rc4.
    def __init__(self):
        self.aes_key = get_random_bytes(16)
        self.des_key = b'-8B kEY-'
        self.rc4_key = get_random_bytes(16)
        self.aes_nonce = get_random_bytes(16)
        self.des_nonce = get_random_bytes(6)
        self.aes = AES.new(self.aes_key, AES.MODE_CTR, nonce = self.aes_nonce)
        self.des = DES.new(self.des_key, DES.MODE_CTR, nonce = self.des_nonce)
        self.rc4 = ARC4.new(self.rc4_key)

    def encrypt_AES(self,plain_text):
        plain_text = self.add_padding(plain_text, AES.block_size)
        cypher_text  = self.aes.encrypt(plain_text)

        return cypher_text

    def decrypt_AES(self, cypher_text):
        plain_text = self.remove_padding(self.aes.decrypt(cypher_text),  AES.block_size)

        return plain_text

    def encrypt_DES(self, plain_text):
        plain_text = self.add_padding(plain_text, DES.block_size)
        cypher_text  = self.des.encrypt(plain_text)

        return cypher_text

    def decrypt_DES(self, cypher_text):
        plain_text = self.remove_padding(self.des.decrypt(cypher_text),  AES.block_size)

        return plain_text
    
    def encrypt_RC4(self, plain_text):
        cypher_text  = self.rc4.encrypt(plain_text)

        return cypher_text

    def decrypt_RC4(self, cypher_text):
        plain_text = self.rc4.decrypt(plain_text)

        return plain_text
    def add_padding(self, data, block_size):
        return pad(data, block_size)
    
    def remove_padding(self, data, block_size):
        return unpad(data, block_size)

    def get_keys(self):
        return {
            "aes": self.aes_key,
            "des": self.des_key,
            "rc4": self.rc4_key,
            "nonce": self.nonce
        }


## Alternative Class Design
# class Crypt:
#     ##encrypt/decrypt using aes(CBC), des & rc4.
#     AES = "AES"
#     DES = "DES"
#     RC4 = "RC4"
#     def __init__(self, encryption=AES):
#         self.encryption = encryption
#         if self.encryption == AES:
#             self.key = get_random_bytes(16)
#             self.nonce = get_random_bytes(16)
#             self.object = AES.new(self.key, AES.MODE_CTR, nonce = self.nonce)

#         self.aes_key = get_random_bytes(16)
#         self.des_key = b'-8B kEY-'
#         self.rc4_key = get_random_bytes(16)
#         self.aes_nonce = get_random_bytes(16)
#         self.des_nonce = get_random_bytes(6)
#         self.aes = AES.new(self.aes_key, AES.MODE_CTR, nonce = self.aes_nonce)
#         self.des = DES.new(self.des_key, DES.MODE_CTR, nonce = self.des_nonce)
#         self.rc4 = ARC4.new(self.rc4_key)

#     def encrypt(self, plain_text):
#         pass
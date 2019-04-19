from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1
import base64
import json
class DSS():
    def __init__(self, message = 'test'):
        self.message = message

    def set_message(self, message):
        self.message = message

    def gen_keys(self, bits, e=None):
        '''Generates the public and private keys for the object'''
        if(e==None):
            key = RSA.generate(bits)
        else:
            key = RSA.generate(bits, e=e)
        self.private_key = key.exportKey('DER')
        self.public_key = key.publickey().exportKey('DER')
        return self.public_key.hex()
    
    def gen_hash(self):
        h = SHA1.new()
        h.update(self.message.encode('utf8'))
        return h.hexdigest()

    def gen_DS(self, h):
        '''Generates the Digital Signature for the message by encrypting the hash
           of the message with private key'''
        h2 = SHA1.new()
        h2.update(self.message.encode('utf8'))
        h = h2.hexdigest()
        if(h == h2.hexdigest()):
            try:
                key = RSA.import_key(self.private_key)
                signature = pkcs1_15.new(key).sign(h2)
            except:
                return 
            self.signature = signature
            sig = str(base64.b64encode(bytes.fromhex(signature.hex())))
            sig64 = sig[1:]
            return signature.hex(), sig64
        else:
            raise ValueError

    def verify(self, ds, h):
        '''Decryptes the signature using Public key and compares the value with
           original hash'''
        h2 = SHA1.new()
        h2.update(self.message.encode('utf8'))
        if(h == h2.hexdigest()):
            key = RSA.import_key(self.public_key)
            try:
                pkcs1_15.new(key).verify(h, ds)
                s = "The signature is valid."
            except (ValueError, TypeError):
                s = "The signature is not valid."
            return s
        else:
            raise ValueError


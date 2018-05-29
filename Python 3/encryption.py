# PRE: Install Visual Studio 2017 Build Tools (?)
# PRE: pip install pycryptodome
# PRE: You've used ssh-keygen to create an public/private RSA key pair.
# PRE: The keypair is not passphrase protected.

import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Turns raw bytes into characters you can safely store in a text file.
# Necessary since I want to read the encrypted message back from a non-binary file.
import base64

home = os.environ['USERPROFILE'];
private_key_path = f'{home}\\.ssh\\usb_key_rsa'
public_key_path = f'{home}\\.ssh\\usb_key_rsa.pub'
private_key_file = open(private_key_path)
public_key_file = open(public_key_path)
private_key = private_key_file.read()
public_key = public_key_file.read()
private_key_object = RSA.importKey(private_key)
public_key_object =  RSA.importKey(public_key)

message = b"Hello, encryption!" # Yes, this has to be bytes.
encryption_cipher = PKCS1_OAEP.new(public_key_object)
encrypted_message = encryption_cipher.encrypt(message)

# We can store *this* in a file, base64 decode it to bytes, and then decrypt it.
encoded_encrypted_message = base64.b64encode(encrypted_message) # Binary bytes -> base64 bytes.
# Since all the bytes are now ASCII-compatible and UTF8 is too, the two sequences are identical.
encoded_encrypted_message_utf8 = encoded_encrypted_message.decode("utf-8") # base64 bytes -> UTF8.

decryption_cipher = PKCS1_OAEP.new(private_key_object)
decrypted_message = decryption_cipher.decrypt(encrypted_message)
decoded_decrypted_message = decrypted_message.decode("utf-8")

print(message)
print(encrypted_message)
print(encoded_encrypted_message)
print(encoded_encrypted_message_utf8)
print(decrypted_message)
print(decoded_decrypted_message)



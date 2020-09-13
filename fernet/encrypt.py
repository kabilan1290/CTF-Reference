from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)
f = Fernet(key)
token = f.encrypt("my deep dark secret")
f.decrypt(token)
print(token)


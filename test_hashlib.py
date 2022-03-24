import hashlib
password = "admin"
password = hashlib.md5(password.encode()).hexdigest()
print(password)
with open("crypt.py","w") as crypt: 
	crypt.write('''
import pyAesCrypt
print("---------------------------------------------------------------" )
file=input("File name: ")
password=input("Password: ")
bufferSize = 64*1024
try: 
	pyAesCrypt.encryptFile(str(file), str(file)+".crp", password, bufferSize)
except FileNotFoundError: 
	print("[x] File not found!")
else: 
	print("[+] File '"+str(file)+".crp' successfully saved!")
finally: 
	print("---------------------------------------------------------------")
''')
	print("[+] File: 'crypt.py' successfully saved!")

with open("key.py","w") as key: 
	key.write('''
import pyAesCrypt, os
print("---------------------------------------------------------------")
file=input("File name: ")
password=input("Password: ")
bufferSize = 64*1024
try: 
	pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, bufferSize)
except FileNotFoundError: 
	print("[x] File not found!")
except ValueError: 
	print("[x] Password is Fasle!")
else: 
	print("[+] File '"+str(os.path.splitext(file)[0])+"' successfully saved!")
finally: 
	print("---------------------------------------------------------------")
''')
	print("[+] File: 'key.py' successfully saved!")
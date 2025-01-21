from os import listdir
from os.path import isfile, join
from cryptography.fernet import Fernet

files = []
def get_files_names(dir: str):
	excluded_files = ["encryption.py", "encryption", "encryption.exe", "decryption.py", "decryption", "decryption.exe", "encryption_key.key"]
	try:
		list_of_dir = listdir(dir)
	except:
		list_of_dir = []
	for file in list_of_dir:
		if isfile(join(dir, file)) and file.split("\\")[-1] not in excluded_files:
			files.append(join(dir, file))
		else:
			get_files_names(join(dir, file))

def decrypt_files():
	try:
		with open("encryption_key.key", "rb") as f:
			key = f.read()
	except:
		print("File does not exist")
		return -1
	frenet = Fernet(key)
	for file in files:
		try:
			with open(file, "rb") as f:
				decrypted_data = f.read()
				encrypted_data = frenet.decrypt(decrypted_data)
			with open(file, "w") as f:
				f.write(encrypted_data.decode())
		except:
			continue

get_files_names("./")
decrypt_files()
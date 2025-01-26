import socket
import os
import time
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 8000))
sock.listen(1)

conn, addr = sock.accept()

if not os.path.isdir(addr[0]):
	os.makedirs(addr[0])

data = b''
while True:
	try:
		size_data = conn.recv(4)
		if not size_data:
			break
		
		screenshot_size = struct.unpack("!I", size_data)[0]

		screenshot_data = b""
		while len(screenshot_data) < screenshot_size:
			chunk = conn.recv(4096)
			if not chunk:
				break
			screenshot_data += chunk
		
		if screenshot_data:
			filename = f"{addr[0]}/{time.time()}.png"
			with open(filename, "wb") as f:
				f.write(screenshot_data)
	except socket.error as e:
		print(f"Socket error: {e}")
		break

conn.close()
sock.close()
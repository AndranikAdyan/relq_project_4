import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 8888))
sock.listen(1)

conn, addr = sock.accept()

with open(f"{addr[0]}.txt", "a") as f:
	while True:
		data = conn.recv(1024)
		if not data:
			break
		f.write(data.decode())
		f.flush()

conn.close()
sock.close()
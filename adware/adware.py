import os
import random
from PIL import Image
import webbrowser
import time

adds_path = "adds"

imgs = os.listdir(adds_path)

def open_image():
	img = Image.open(os.path.join(adds_path, random.choice(imgs)))
	img.show()

links = ["instagram.com", "youtube.com", "facebook.com"]
def open_link():
	link = random.choice(links)
	webbrowser.open(link)

def main():
	func = random.choice([open_image, open_link])
	func()

while True:
	time.sleep(3)
	main()
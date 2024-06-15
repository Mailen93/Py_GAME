import pygame
import sys

pygame.init()
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Eventos del teclado")

bandera = True

while bandera:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
        elif event.type == pygame.KEYDOWN:
            print(f"Tecla presionada: {event.key}")
        elif event.type == pygame.KEYUP:
            print(f"Tecla liberada: {event.key}")

pygame.quit()
sys.exit()
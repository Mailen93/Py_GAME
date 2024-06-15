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
            nombre = pygame.key.name(event.key)
            print(f"Tecla presionada: {nombre}")

pygame.quit()
sys.exit()
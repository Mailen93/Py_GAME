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
            cerrar = input("Está seguro de cerrar?")
            if cerrar == "Si":
                bandera = False
        elif event.type == pygame.MOUSEMOTION:
            # x,y = event.pos
            x = event.pos[0]
            y = event.pos[1]
            print(f"({x}, {y})")
        elif event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                print("Ruedita para arriba")
            else:
                print("Ruedita para abajo")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Izquierdo")
            elif event.button == 3:
                print("Derecho")
            elif event.button == 2:
                print("Ruedita")
            else:
                print(event.button)

pygame.quit()
sys.exit()
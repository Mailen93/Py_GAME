import pygame, sys
from pygame.locals import *

pygame.init() #Inicializo pygame

NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
VERDE_CLARO = (0,200,150)
BLANCO = (255,255,255)

PANTALLA = pygame.display.set_mode((500,400))
pygame.display.set_caption("Mi primer juego")

PANTALLA.fill(BLANCO)

pygame.draw.line(PANTALLA, VERDE, (100,100), (350,100), 5) #? X1,Y1 - X2, Y2 Linea horizontal
pygame.draw.line(PANTALLA, AZUL, (100,100), (350,250), 5) # Linea decreciente
pygame.draw.line(PANTALLA, ROJO, (200,200), (350,100), 5) # Linea creciente 
pygame.draw.line(PANTALLA, NEGRO, (100,200), (100,300), 5) # Linea vertical


flag = True
while flag == True: #Bucle infinito
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: #Pregunto si presiono la x de la ventana, el QUIT es el evento
                flag = False


    pygame.display.update() #Actualiza todos los elementos

pygame.quit()
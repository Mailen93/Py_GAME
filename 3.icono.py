import pygame

pygame.init() #Inicializo pygame

NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
VERDE_CLARO = (0,200,150)
BLANCO = (255,255,255)

ventana = pygame.display.set_mode((500, 200)) #Tamaño de la ventana, 500x200px
pygame.display.set_caption("Mi primer ventana") #Título de la ventana
#Traigo una imagen y la pongo como ícono:
icono = pygame.image.load("gatito.jpg") #Load devuelve una superficie, carga una imagen
pygame.display.set_icon(icono)

ventana.fill(VERDE_CLARO) #Rellena la ventana con un color

flag = True
while flag == True: #Bucle infinito
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: #Pregunto si presiono la x de la ventana, el QUIT es el evento
                flag = False
    
    pygame.display.update()

pygame.quit() #Apago pygame para que no esté corriendo todo el tiempo

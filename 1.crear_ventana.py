import pygame

pygame.init() #Inicializo pygame

pygame.display.set_mode((500, 200)) #Tamaño de la ventana, 500x200px
pygame.display.set_caption("Mi primer ventana") #Título de la ventana

flag = True
while flag == True: #Bucle infinito
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: #Pregunto si presiono la x de la ventana, el QUIT es el evento
                flag = False

pygame.quit() #Apago pygame para que no esté corriendo todo el tiempo

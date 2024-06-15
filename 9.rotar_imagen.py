import pygame

pygame.init() #Inicializo pygame

NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
VERDE_CLARO = (0,200,150)
BLANCO = (255,255,255)

ANCHO_VENTANA = 550
ALTO_VENTANA = 800

TAMAÑO_VENTANA = (ANCHO_VENTANA, ALTO_VENTANA)

ventana = pygame.display.set_mode(TAMAÑO_VENTANA) #Tamaño de la ventana, 500x200px

pygame.display.set_caption("Mi primer ventana") #Título de la ventana

#Traigo una imagen y la pongo como ícono:
icono = pygame.image.load("gatito.jpg") #Load devuelve una superficie, carga una imagen
pygame.display.set_icon(icono)

# ventana.fill(VERDE_CLARO) #Rellena la ventana con un color

fuente = pygame.font.SysFont("Arial", 30) #Define la configuración de la fuente
texto = fuente.render("Hola, ¿cómo estás?", False, ROJO, NEGRO)

imagen = pygame.image.load("gatito.jpg") #Load devuelve una surface, necesita el path de la img
imagen = pygame.transform.scale(imagen,(350,300)) #ancho - alto
imagen = pygame.transform.rotate(imagen,29) #permite rotar la imagen una cierta cantidad de grados

flag = True
while flag == True: #Bucle infinito
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: #Pregunto si presiono la x de la ventana, el QUIT es el evento
                flag = False
    ventana.blit(imagen,(25,30)) #Pegate en la superficie, coordenadas de dónde quiero blitear
    ventana.blit(texto,(300,100))
    

    pygame.display.update() #Actualiza todos los elementos

pygame.quit() 
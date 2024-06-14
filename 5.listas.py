import pygame

lista_nombres = ["Mario", "Gio", "Marcos", "Lucas", "Germán"]

pygame.init() #Inicializo pygame

NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
VERDE_CLARO = (0,200,150)
BLANCO = (255,255,255)

ANCHO_VENTANA = 600
ALTO_VENTANA = 300

TAMAÑO_VENTANA = (ANCHO_VENTANA, ALTO_VENTANA)

# ! CONSIDERACIONES!!
# ? Pygame es un contenedor de Python para la biblioteca SDL , que significa Simple DirectMedia Layer . 
# SDL brinda acceso multiplataforma a los componentes de hardware multimedia subyacentes de su sistema, como sonido, video, mouse, teclado y joystick.
# ? El módulo display permite controlar todo lo que tiene que ver con las ventanas y las pantallas de un programa. 
# ? Un objeto Surface representa un buffer de memoria de píxeles, la pantalla se representa también como una superficie.
# ? Sobre una superficie se pueden dibujar diferentes formas (rectángulos, círculos, elipses, líneas, etc..) 
# ? Se dibuja un círculo azul
# ? Se dibuja un cuadrado amarillo:
# pygame.draw.rect(screen, (255, 255, 0), (30, 30, 60, 60))
# ? pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
# ? Pygame provee control sobre los dispositivos de entrada más comunes :
# - Teclado (pygame.key )
# - Mouse (pygame.mouse)
# - Joystick (pygame.joystick)
# ? Pygame maneja todos sus mensajes de eventos a través de una cola de eventos. : pygame.event.get()
# ? La cola de eventos contiene objetos de evento pygame.event.EventType: 
# # Se verifica si el usuario cerro la ventana
# for event in pygame.event.get():
#     print(type(event)) # <class 'Event'>
# ? Todas instancias de Event contienen un identificador de tipo de evento y atributos específicos para ese tipo de evento:
## Se verifica si el usuario cerro la ventana
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
# ? Para poder fijar un evento que ocurran por tiempo:
# tick = pygame.USEREVENT + 0
# pygame.time.set_timer(tick,1000)
# while running:
#    for event in pygame.event.get():
#        if event.type == tick:
#        	print("Ya paso un segundo")
# ? Se verifica si el evento es el de una tecla presionada y luego se verifica cual es la tecla:
# for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#        if event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_x:
#                print("Se presiono la tecla X")
# ? Se verifica si el evento es el de una tecla presionada y luego se verifica cual es la tecla:
# from pygame.locals import K_x
# pressed_keys = pygame.key.get_pressed()
# if True in pressed_keys:
# if pressed_keys[K_x]:
#     	print("Se presiono la tecla X")
# ? Con el método load de la clase image se puede generar una superficie desde una imagen:
# imagen = pygame.image.load("00.png")
# print(type(imagen)) # <class 'pygame.Surface'>
# ? Para copiar la superficie de la imagen en la superficie de la pantalla o en otra superficie se debe utilizar blit() indicando la ubicación 
# imagen = pygame.image.load("00.png")
# print(type(imagen)) # <class 'pygame.Surface'>
# screen.blit(imagen,(50,50))
# ? El método render me permite obtener una superficie a partir de un texto.
# font = pygame.font.SysFont("Arial Narrow", 50)
# text = font.render("HOLA MUNDO", True, (255, 0, 0))
# print(type(text)) # <class 'pygame.Surface'>
# ? Para copiar la superficie del texto en la superficie de la pantalla o en otra superficie se debe utilizar blit() indicando la ubicación 
# font = pygame.font.SysFont("Arial Narrow", 50)
# text = font.render("HOLA MUNDO", True, (255, 0, 0))
# screen.blit(text,(50,50))
# ? Pygame usa objetos Rect para almacenar y manipular áreas rectangulares. Se crean a partir de las dimensiones de ancho, alto y la posición respecto al lado izquierdo y superior de un objeto:
#    pygame.Rect (left, top, width, height)
# ? En cada juego, cada objeto requiere un conjunto de límites fijos que definen el espacio que ocupa. Estos límites fijos son esenciales cuando el objeto interactúa o “choca” con otros objetos
# ? En Pygame se crean "Rectángulos" alrededor de los objetos para definir sus límites.
# ? La forma más básica de crear un objeto Rect en Pygame es simplemente pasar dos tuplas. La primera tupla (izquierda, arriba) representa la posición del Rect en la ventana, mientras que la segunda tupla (ancho, alto) representa las dimensiones del Rect.
# Se dibuja un cuadrado amarillo
# rectangulo = pygame.Rect((30, 30), (60,60))
# pygame.draw.rect(screen, (255, 255, 0), rectangulo)
# ? También es posible obtener un objeto Rect de una superficie y manipularlo:
# imagen_dona = pygame.image.load("00.png")
# rect_dona = imagen_dona.get_rect()
# rect_dona.centerx = 200
# rect_dona.centery = 100
# print(rect_dona.width,rect_dona.height) # 200 200
# screen.blit(imagen_dona,rect_dona)
# ? La forma más sencilla de comprobar colisiones es ver si se solapan los rectángulos de las distintas superficies.
# ? Para cada rectángulo, es posible comprobar si colisiona con otro:
# if rect_player.colliderect(rect_piedra):
# print("El jugador colisiona con la piedra")
# if rect_player.colliderect(rect_fuego):
# print("El jugador colisiona con el fuego")
# ? Es posible comprobar si un rectángulo colisiona con algún otro rectángulo de una lista de Rect:
# if rect_player.collidelist(lista_rect) >= 0:
# print("El jugador colisionó con la piedra")
# ? También es posible comprobar si colisiona una superficie con una coordenada:
# if event.type == pygame.MOUSEBUTTONDOWN :
# if rect_player.collidepoint(event.pos):
#    		print("CLICK sobre el jugador")
# ? Los formatos de archivos de sonido que Pygame soporta son MID, WAV y MP3. Si al play se le pasa -1 como argumento, se va a reproducir el sonido de manera indefinida:
# pygame.mixer.init()
# pygame.mixer.music.set_volume(0.7)
# sonido_fondo = pygame.mixer.Sound("fondo.wav")
# sonido_fondo.set_volume(0.2)
# sonido_fondo.play()
# sonido_fondo.stop()

#  En términos de programación, un sprite es una representación 2D de algo en la pantalla. Esencialmente, es una imagen. Pygame proporciona una clase Sprite , que está diseñada para contener una o varias representaciones gráficas de cualquier objeto del juego que se desee mostrar en la pantalla.



ventana = pygame.display.set_mode(ALTO_VENTANA) #Define las dimensiones de la ventana, devuelve una superficie
pygame.display.set_caption("Mi primer ventana") #Título de la ventana
#Traigo una imagen y la pongo como ícono:
icono = pygame.image.load("gatito.jpg") #Load devuelve una superficie, carga una imagen
pygame.display.set_icon(icono)

ventana.fill(VERDE_CLARO) #Rellena la ventana con un color

fuente = pygame.font.SysFont("Arial", 30) #Define la configuración de la fuente
texto = fuente.render("Hola, ¿cómo estás?", False, ROJO, NEGRO)

flag = True
while flag == True: #Bucle infinito
    y = 50
    lista_eventos = pygame.event.get() #Obtenemos una lista de eventos
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: #Pregunto si presiono la x de la ventana, el QUIT es el evento
                flag = False

    for nombre in lista_nombres:
        texto = fuente.render(nombre, False, ROJO, NEGRO)
        ventana.blit(texto,(50,y)) #Pegate en la superficie, vamos a ir bliteando (pegando superficies) sobre otras superficies
        y += 30
    pygame.display.update() #Actualiza todos los elementos

pygame.quit() #Apago pygame para que no esté corriendo todo el tiempo

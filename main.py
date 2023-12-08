import pygame

print("Este es un mensaje nuevo")
print("Prueba del repositorio")

# Inicializamos Pygame
pygame.init()

# Definimos las dimensiones de la ventana principal
ancho_ventana = 800
alto_ventana = 600

# Definimos los colores que utilizaremos
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Creamos la ventana principal
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Juego")

# Cargamos la imagen del título
imagen_titulo = pygame.image.load("sr tae.jpg")

# Cargamos imagen del juego
imagen_morgue = pygame.image.load("morguec.jpg")

# Definimos la fuente del texto
fuente = pygame.font.Font(None, 36)

# Definimos las opciones del menú
opciones_del_menu_principal = ["Juego", "Créditos", "Salir"]
opciones_del_menu_bienvenida = ['Continuar', "Regresar"]
posiciones_opciones_del_menu_principal = [(ancho_ventana // 10, 300), (ancho_ventana // 10, 350),
                                          (ancho_ventana // 10, 400)]
posiciones_opciones_del_menu_bienvenida = [(ancho_ventana // 2.5, 500), (ancho_ventana // 1.5, 500)]
opciones_principales = ["Información del cuerpo", "Teléfono", "Hablar con la esposa", "Causa", "Regresar"]
posiciones_opciones_principales = [(ancho_ventana // 1.5, 300), (ancho_ventana // 1.5, 350),
                                   (ancho_ventana // 1.5, 400), (ancho_ventana // 1.5, 450),
                                   (ancho_ventana // 1.5, 500)]

# Definimos las variables de control de la selección del usuario
opcion_seleccionada_x = 0
opcion_seleccionada_y = 0
en_menu_principal = True
en_pantalla_bienvenida = False
en_credito = False
en_menu_bienvenida = False
en_pantalla_de_juego = False


en_menu_cuerpo = False
en_pantalla_cuerpo_general = False
en_pantalla_de_telefono = False
en_pantalla_interrogatorio = False
en_pantalla_final = False

def display_botones_x(lista_nombres, coordenadas):
    # Dibujamos las opciones del menú
    for i in range(len(lista_nombres)):
        texto_opcion = fuente.render(lista_nombres[i], True, negro)
        rect_opcion = texto_opcion.get_rect(center=coordenadas[i])
        if i == opcion_seleccionada_x:
            pygame.draw.rect(ventana, negro, (
                rect_opcion.left - 10, rect_opcion.top - 10, rect_opcion.width + 20, rect_opcion.height + 20), 5)
        ventana.blit(texto_opcion, rect_opcion)


def display_botones_y(lista_nombres, coordenadas):
    # Dibujamos las opciones del menú
    for i in range(len(lista_nombres)):
        texto_opcion = fuente.render(lista_nombres[i], True, negro)
        rect_opcion = texto_opcion.get_rect(center=coordenadas[i])
        if i == opcion_seleccionada_y:
            pygame.draw.rect(ventana, negro, (
                rect_opcion.left - 10, rect_opcion.top - 10, rect_opcion.width + 20, rect_opcion.height + 20), 5)
        ventana.blit(texto_opcion, rect_opcion)

def menu_cuerpo():
    display_botones_y(opciones_principales, posiciones_opciones_principales)

def menu_bienvenida():
    display_botones_y(opciones_del_menu_bienvenida, posiciones_opciones_del_menu_bienvenida)

def menu_principal():
    # Dibujamos las opciones del menú
    display_botones_x(opciones_del_menu_principal, posiciones_opciones_del_menu_principal)



def pantalla_de_creditos():
    # Mostramos la ventana del juego
    ventana_credito = pygame.Surface((ancho_ventana, alto_ventana))
    ventana_credito.fill(blanco)

    # Dibujamos el texto de bienvenida
    texto_cre = fuente.render("Este juego fue creado por:", True, negro)
    rect_cre = texto_cre.get_rect(center=(ancho_ventana // 2, 200))
    ventana_credito.blit(texto_cre, rect_cre)

    texto_cre = fuente.render(f"Equipo EPOC", True, negro)
    rect_cre = texto_cre.get_rect(center=(ancho_ventana // 2, 250))
    ventana_credito.blit(texto_cre, rect_cre)

    # Mostramos la ventana del juego
    ventana.blit(ventana_credito, (0, 0))


def pantalla_de_bienvenida():
    # Mostramos la ventana del juego
    ventana_juego = pygame.Surface((ancho_ventana, alto_ventana))
    ventana_juego.fill(blanco)

    # Dibujamos el texto de bienvenida
    texto_bienvenida = fuente.render("¡Bienvenido al juego!", True, negro)
    rect_bienvenida = texto_bienvenida.get_rect(center=(ancho_ventana // 2, 50))
    ventana_juego.blit(texto_bienvenida, rect_bienvenida)

    texto_i = fuente.render("Ha sido convocada por la policía, requieren de su ayuda ", True, negro)
    rect_i = texto_i.get_rect(center=(ancho_ventana // 2, 200))
    ventana_juego.blit(texto_i, rect_i)

    texto_i = fuente.render("Un hombre acaba de morir, pero nadie sabe la causa", True, negro)
    rect_i = texto_i.get_rect(center=(ancho_ventana // 2, 250))
    ventana_juego.blit(texto_i, rect_i)

    texto_i = fuente.render("Algunos dicen que fue asesinado, otros dicen que fue suicidio", True, negro)
    rect_i = texto_i.get_rect(center=(ancho_ventana // 2, 300))
    ventana_juego.blit(texto_i, rect_i)

    texto_i = fuente.render("Dicen que usted es exceclente en estos casos", True, negro)
    rect_i = texto_i.get_rect(center=(ancho_ventana // 2, 350))
    ventana_juego.blit(texto_i, rect_i)

    texto_i = fuente.render("Esperamos pueda ayudarnos.", True, negro)
    rect_i = texto_i.get_rect(center=(ancho_ventana // 2, 400))
    ventana_juego.blit(texto_i, rect_i)

    # Mostramos la ventana del juego
    ventana.blit(ventana_juego, (0, 0))

    # Mostrar opciones
    menu_bienvenida()



def pantalla_cuerpo_general():
    opciones_cuerpo = ["Extremidades", "Cabeza", "Toraz"]
    posiciones_opciones_cuerpo = [(ancho_ventana // 1, 300), (ancho_ventana // 1, 350), (ancho_ventana // 1, 400)]

    #Mostrar ventana para elejir parte
    ventana_parte = pygame.Surface((ancho_ventana, alto_ventana))
    ventana_parte.fill(blanco)

    #Dibujamos el texto de parte del cuerpo a examinar
    texto_pregunta_cuerpo = fuente.render("Qué parte desea investigar?", True, negro)
    rect_cuerpo = texto_pregunta_cuerpo.get_rect(center=(ancho_ventana // 2, 50))
    ventana_parte.blit(texto_pregunta_cuerpo, rect_cuerpo)

    #Mostrar la ventana
    ventana.blit(ventana_parte, (0, 0))

def pantalla_telefono():
    pass

def pantalla_interrogatorio():
    pass

def pantalla_final():
    pass


def pantalla_de_juego():

    # Mostramos la ventana para jugar
    ventana_jugar = pygame.Surface((ancho_ventana, alto_ventana))
    ventana_jugar.fill(blanco)

    # Dibujamos el texto de bienvenida
    texto_inicial = fuente.render("Qué investigará primero?!", True, negro)
    rect_inicial = texto_inicial.get_rect(center=(ancho_ventana // 2, 50))
    ventana_jugar.blit(texto_inicial, rect_inicial)

    # Mostramos la ventana del juego
    ventana.blit(ventana_jugar, (0, 0))

    display_botones_x(opciones_principales, posiciones_opciones_principales)


def limpiar_pantalla():
    ventana.fill(blanco)

def display_menu_cuerpo():
    if en_menu_cuerpo:
        menu_cuerpo()
    if en_pantalla_cuerpo_general:
        pantalla_cuerpo_general()
    if en_pantalla_de_telefono:
        pantalla_telefono()
    if en_pantalla_interrogatorio:
        pantalla_interrogatorio()
    if en_pantalla_final:
        pantalla_final()
    if en_menu_bienvenida:
        menu_bienvenida()

    pygame.display.update()

def display_menu_bienvenida():
    if en_menu_bienvenida:
        menu_bienvenida()
    if en_pantalla_de_juego:
        pantalla_de_juego()
    if en_menu_principal:
        menu_principal()

    pygame.display.update()


def display_menu_principal():
    if en_menu_principal:
        menu_principal()

    elif en_pantalla_bienvenida:
        pantalla_de_bienvenida()

    elif en_credito:
        pantalla_de_creditos()

    elif en_pantalla_de_juego:
        pantalla_de_juego()

    pygame.display.update()


# Bucle principal del juego
while True:
    # Eventos del teclado y del mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                opcion_seleccionada_x -= 1
            if event.key == pygame.K_DOWN:
                opcion_seleccionada_x += 1
            if event.key == pygame.K_RIGHT:
                opcion_seleccionada_y += 1
            if event.key == pygame.K_LEFT:
                opcion_seleccionada_y -= 1
            if event.key == pygame.K_RETURN:
                if opcion_seleccionada_x == 0:
                    # Abrimos la ventana del juego
                    en_menu_principal = False
                    en_pantalla_bienvenida = True
                elif opcion_seleccionada_x == 1:
                    en_menu_principal = False
                    en_credito = True
                elif opcion_seleccionada_x == 2:
                    # Salimos del juego
                    pygame.quit()
                    quit()
                elif opcion_seleccionada_y == 0:
                    en_menu_bienvenida = False
                    en_pantalla_bienvenida = False
                    en_pantalla_de_juego = True
                elif opcion_seleccionada_y == 1:
                    en_menu_principal = True
                    en_menu_bienvenida = False
                opcion_seleccionada_x = -1




    # Limpiamos la pantalla
    limpiar_pantalla()

    # Dibujamos la imagen del título
    ventana.blit(imagen_titulo, (ancho_ventana // 2 - imagen_titulo.get_width() // 2.5, 20))

    # Comparamos las opciones del menu principal
    display_menu_principal()

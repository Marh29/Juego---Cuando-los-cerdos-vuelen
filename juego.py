import pygame
import cv2
import mediapipe as mp
import constantes_globales as cg
from objetos_juego import *
import time

#Iniciar pygame
pygame.init()
pygame.display.set_caption("Cuando los cerdos vuelen")
icono = pygame.image.load("picture/cerdo_icono.png")
pygame.display.set_icon(icono)

ventana = pygame.display.set_mode((cg.ancho_c,cg.alto_c))

#Inicias Mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

#Iniciar OpenCV
cap = cv2.VideoCapture(0)

#Objetos iniciales juego
portada = Titulo()
puntaje_actual = VerPuntajeAct()
jugador = Cerdito()

#Contadores
puntuacion_max = 0
puntuacion_act = 0
cont_obstaculo_1 = 0
cont_obstaculo_2 = 0
cont_puntos = 0

#Listas
l_obstaculos = []
l_puntos = []
l_elementos = []

#Controladores
empezar_juego = False
mostrar_puntaje = False
p_jugada = 0

with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face_mesh:

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    empezar_juego = True

        success, image = cap.read()
        if not success:
            continue

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        results = face_mesh.process(image)
        image.flags.writeable = True

        height, width, _ = image.shape

        # Imagen de fondo camarra
        background = image
        background = cv2.resize(image, (cg.alto_c,cg.ancho_c))
        background = pygame.surfarray.make_surface(background)

        ventana.blit(background, (0, 0))

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:

                #Resolver posición del punto en la nariz
                x = int(face_landmarks.landmark[4].x*width)
                y = int(face_landmarks.landmark[4].y*height)

                x = x*1.5
                y = y*1.5

                #print("x:",y,"y:",x)

            jugador.movimiento(y,x)
        jugador.dibujar(ventana)

        if empezar_juego == False:
        #-------------------------Portada Juego-------------------------    
            if p_jugada == 0:
                portada.dibujar(ventana, puntuacion_max)

                if puntuacion_act > puntuacion_max:
                    puntuacion_max = puntuacion_act
                    print("puntuacion maxima",puntuacion_max)

                puntuacion_act = 0
                cont_obstaculo_1 = 0
                cont_obstaculo_2 = 0
                cont_puntos = 0
            else:                    
                puntaje_actual.dibujar(ventana,puntuacion_act)
                p_jugada += 1
                if p_jugada == 200:
                    p_jugada = 0
        else:
        #-------------------------Juego-------------------------
            if mostrar_puntaje:
                mostrar_puntaje = False
                p_jugada = 1

                time.sleep(3)

                for e in l_elementos:
                    e.reiniciar()

                empezar_juego = False

            #Sistema de aparicion de elementos
            cont_obstaculo_1 += 1
            cont_obstaculo_2 += 1
            cont_puntos += 1

            if cont_obstaculo_1 == 230:
                nuevo = Obstaculo_1()
                l_obstaculos.append(nuevo)
                l_elementos.append(nuevo)
            if cont_obstaculo_2 == 100:
                nuevo = Obstaculo_2()
                l_obstaculos.append(nuevo)
                l_elementos.append(nuevo)
            if cont_puntos == 50:
                nuevo = Punto()
                l_puntos.append(nuevo)
                l_elementos.append(nuevo)

            if cont_obstaculo_1 == 230:
                cont_obstaculo_1 = 0
            if cont_obstaculo_2 == 100:
                cont_obstaculo_2 = 0
            if cont_puntos == 50:
                cont_puntos = 0

            #Mostrar elementos en pantalla
            for o in l_obstaculos:
                o.dibujar(ventana)
                
                if o.colision(jugador):
                    mostrar_puntaje = True
                    
            for p in l_puntos:
                p.dibujar(ventana)
                if p.colision(jugador):
                    l_puntos.remove(p)
                    puntuacion_act += 10
        #-----------------------------------------------

        if cv2.waitKey(5) & 0xFF == 27:
            break

        pygame.display.update()

cap.release()
pygame.quit()
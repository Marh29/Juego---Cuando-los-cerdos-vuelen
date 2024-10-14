import pygame
import constantes_globales as cg
import random as r
import sprites as s

def CalcularForma(sprite,px,py):
    return pygame.Rect(px,py,sprite.get_width(),sprite.get_height())

def ComprobarColision(a,b):
    return a.forma.colliderect(b.forma)

class Titulo:
    def __init__(self):
        self.image = s.portada
        self.forma = CalcularForma(self.image,((cg.ancho_c-cg.ancho_p)/2),((cg.alto_c-cg.alto_p)/2))
        self.fuente =pygame.font.Font(None,80)

    def dibujar(self, ventana,p_max):
        ventana.blit(self.image, self.forma)

        texto = f"Puntaje maximo: {p_max}"

        mensaje = self.fuente.render(texto,0,(241,148,138),(255,255,255))
        forma_m = mensaje.get_rect()
        forma_m.center = (cg.ancho_c/2,(cg.alto_c/2)+250)
        ventana.blit(mensaje, forma_m)
        #pygame.draw.rect(ventana, (250,0,0), self.forma)

class VerPuntajeAct:
    def __init__(self):
        self.fuente =pygame.font.Font(None,150)

    def dibujar(self,ventana,p_act,):
        texto = "Tú puntaje fue"

        mensaje = self.fuente.render(texto,0,(241,148,138),(255,255,255))
        forma_m = mensaje.get_rect()
        forma_m.center = (cg.ancho_c/2,(cg.alto_c/2)-75)

        puntuacion = self.fuente.render(str(p_act),0,(241,148,138),(255,255,255))
        forma_p = puntuacion.get_rect()
        forma_p.center = (cg.ancho_c/2,(cg.alto_c/2)+75)

        ventana.blit(mensaje, forma_m)
        ventana.blit(puntuacion, forma_p)

class Cerdito:
    def __init__(self):
        self.image = s.cerdo
        self.rect = self.image.get_rect()
        self.forma = CalcularForma(self.image,0,0)
        self.forma.center = (0,0)

    def movimiento(self, posicion_x, posicion_y):
        self.forma.x = posicion_x-(cg.w_personaje/2)
        self.forma.y = posicion_y-(cg.h_personaje/2)

    def dibujar(self, ventana):
        ventana.blit(self.image, self.forma)
        #pygame.draw.rect(ventana, (255,181,151), self.forma)

class Obstaculo_1:
    def __init__(self):
        self.image = r.choice([s.herramientas,s.paja,s.techo_azul,s.techo_rojo])
        self.forma = CalcularForma(self.image,cg.ancho_c,480)
        self.velocidad = 15

    def dibujar(self,ventana):
        self.forma.x -= self.velocidad
        ventana.blit(self.image, self.forma)
        #pygame.draw.rect(ventana, (147,81,22), self.forma)

    def colision(self,jugador):
        return ComprobarColision(self,jugador)

    def reiniciar(self):
        self.forma.y = cg.ancho_c

class Obstaculo_2:
    def __init__(self):
        velocidad = [10,15,18]
        posicion = [0,144,288,432,576]
        self.image = r.choice([s.cometa,s.gallina,s.roca])
        self.forma = CalcularForma(self.image,cg.ancho_c,r.choice(posicion))
        self.velocidad = r.choice(velocidad)

    def dibujar(self,ventana):
        self.forma.x -= self.velocidad
        ventana.blit(self.image, self.forma)
        #pygame.draw.rect(ventana, (149,165,166), self.forma)

    def colision(self,jugador):
        return ComprobarColision(self,jugador)

    def reiniciar(self):
        self.forma.y = cg.ancho_c

class Punto:
    def __init__(self):
        velocidad = [5,10,20,25]
        posicion = [0,120,240,360,480,600]
        self.image = r.choice([s.pera,s.uvas,s.zanahoria])
        self.rect = self.image.get_rect()
        self.forma = CalcularForma(self.image,cg.ancho_c,r.choice(posicion))
        self.velocidad = r.choice(velocidad)

    def dibujar(self,ventana):
        self.forma.x -= self.velocidad
        ventana.blit(self.image, self.forma)
        #pygame.draw.rect(ventana, (211,84,0), self.forma)

    def colision(self,jugador):
        return ComprobarColision(self,jugador)

    def reiniciar(self):
        self.forma.y = cg.ancho_c
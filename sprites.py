import pygame
import constantes_globales as cg

portada = pygame.transform.scale(pygame.image.load("picture/portada juego.png"),
                               (cg.port_ancho,cg.port_alto))

cerdo = pygame.transform.scale(pygame.image.load("picture/cerdo.png"),
                               (cg.w_personaje,cg.h_personaje))

pera = pygame.transform.scale(pygame.image.load("picture/pera.png"),
                               (cg.t_ancho_v,cg.t_alto_v))

uvas = pygame.transform.scale(pygame.image.load("picture/uvas.png"),
                               (cg.t_ancho_v,cg.t_alto_v))

zanahoria = pygame.transform.scale(pygame.image.load("picture/zanahoria.png"),
                               (cg.t_ancho_v,cg.t_alto_v))

herramientas = pygame.transform.scale(pygame.image.load("picture/herramientas.png"),
                               (cg.t_ancho_3,cg.t_alto_3))

paja = pygame.transform.scale(pygame.image.load("picture/paja.png"),
                               (cg.t_ancho_3,cg.t_alto_3))

techo_azul = pygame.transform.scale(pygame.image.load("picture/techo azul.png"),
                               (cg.t_ancho_3,cg.t_alto_3))

techo_rojo = pygame.transform.scale(pygame.image.load("picture/techo rojo.png"),
                               (cg.t_ancho_3,cg.t_alto_3))

cometa = pygame.transform.scale(pygame.image.load("picture/cometa.png"),
                               (cg.t_alto_5-20,cg.t_alto_5-20))

gallina = pygame.transform.scale(pygame.image.load("picture/gallina.png"),
                               (cg.t_alto_5-20,cg.t_alto_5-20))

roca = pygame.transform.scale(pygame.image.load("picture/roca.png"),
                               (cg.t_alto_5-20,cg.t_alto_5-20))
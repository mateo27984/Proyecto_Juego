import pygame
import random
nave_enemiga =pygame.image.load('Juego/assets/imagenes/boss_frame_0__1_-removebg-preview.png')
nave_enemiga=pygame.transform.scale(nave_enemiga,(300,247))
nave_imagen = pygame.image.load('Juego/assets/imagenes/Main Ship - Base - Slight damage.png')
meteorito_imagen = pygame.image.load('Juego/assets/imagenes/Meteor1.png')
tierra_imagen = pygame.image.load('Juego/assets/imagenes/tierra.png')
tierra_imagen = pygame.transform.scale(tierra_imagen, (400, 247))
pygame.mixer.init()
sonidos=(pygame.mixer.Sound('Juego/assets/sonidos/success-340660.mp3'),
pygame.mixer.Sound('Juego/assets/sonidos/error-126627.mp3'),
 pygame.mixer.Sound('Juego/assets/sonidos/explosion-312361.mp3'),
pygame.mixer.Sound('Juego/assets/sonidos/minifunk-67270.mp3'),
pygame.mixer.Sound('Juego/assets/sonidos/game-over-39-199830.mp3'),
pygame.mixer.Sound('Juego/assets/sonidos/11l-victory_sound_with_t-1749487402950-357606.mp3'))


class Tierra:
    def __init__(self,alto):
        self.imagen = tierra_imagen
        self.vida = 100
        self.x = 200
        self.y = alto - 150

    def recibir_danio(self, cantidad):
        self.vida = max(0, self.vida - cantidad)
        sonidos[2].play()

    def Dibujar(self, superficie):
     pygame.draw.rect(superficie, (255, 0, 0), (10, superficie.get_height() - 30, 200, 20))
     pygame.draw.rect(superficie, (0, 255, 0), (10, superficie.get_height() - 30, 200 * (self.vida / 100), 20))

     superficie.blit(self.imagen, (self.x, self.y))

    def explotado(self):
        return self.vida <= 0

class Nave:
    def __init__(self, ancho, alto):
        self.imagen = nave_imagen
        self.x = ancho // 2
        self.y = alto - 250
        self.speed = 6

    def mover(self, teclas, ancho):
        if teclas[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if teclas[pygame.K_RIGHT] and self.x < ancho - self.imagen.get_width():
            self.x += self.speed

    def Dibujar(self, superficie):
        superficie.blit(self.imagen, (self.x, self.y))

class Meteorito:
    def __init__(self, palabra, ancho):
        self.imagen = meteorito_imagen
        self.palabra = palabra
        self.x = random.randint(0, ancho - self.imagen.get_width())
        self.y = -50
        if len(palabra) <= 3:
            self.speed = 5
        elif len(palabra) <= 5:
            self.speed = 4
        else:
            self.speed = 2

    def update(self):
        self.y += self.speed

    def Dibujar(self, superficie, fuente, blanco):
        superficie.blit(self.imagen, (self.x, self.y))
        texto = fuente.render(self.palabra, True, blanco)
        superficie.blit(texto, (self.x + 10, self.y + 10))
"""class NaveEnemiga(Tierra):
    def __init__(self, alto):
        super().__init__(alto)
        self.imagen = nave_enemiga
        self.x = 80  
        self.y = 65
        self.vida = 110
    def Dibujar(self, superficie):
        pygame.draw.rect(superficie, (255, 0, 0), (self.x, self.y - 20, 100, 10))
        pygame.draw.rect(superficie, (0, 255, 0), (self.x, self.y - 20, 100 * (self.vida / 100), 10))
        superficie.blit(self.imagen, (self.x, self.y))"""
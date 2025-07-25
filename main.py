import pygame
import random
from clases import Nave, Tierra, Meteorito, sonidos

pygame.init()

Ancho = 800
Alto = 600
Ventana = pygame.display.set_mode((Ancho, Alto))
pygame.display.set_caption("Juego")

reloj = pygame.time.Clock()
FPS = 60

BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
fuente = pygame.font.SysFont(None, 36)

def generar_palabra():
    return random.choice(["sol", "luz", "nube", "fuego", "astro", "viento", "roca", "metal"])
nave = Nave(Ancho, Alto)
"""naveenemiga= NaveEnemiga(Alto)"""
tierra = Tierra(Alto)
meteoritos = []
palabra_actual = ""
score = 0
vidas = 3
spawn_timer = 0
game_over = False

while not game_over:
    reloj.tick(FPS)
    Ventana.fill((30, 30, 30))
    teclas = pygame.key.get_pressed()
    nave.mover(teclas, Ancho)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                palabra_actual = palabra_actual[:-1]
            elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                encontrado = False
                for m in meteoritos:
                    if palabra_actual.lower() == m.palabra:
                        meteoritos.remove(m)
                        score += 10
                        pygame.mixer.Sound(sonidos[0]).play()
                        encontrado = True
                        if score==10:
                          sonidos[3].play()
                        

                if not encontrado:
                    vidas -= 1
                    sonidos[1].play()
                palabra_actual = ""
            elif event.unicode.isalpha():
                palabra_actual += event.unicode
            


    spawn_timer += 1
    if spawn_timer > 90:
        meteoritos.append(Meteorito(generar_palabra(), Ancho))
        spawn_timer = 0

    for m in meteoritos[:]:
        m.update()
        m.Dibujar(Ventana, fuente, BLANCO)
        if pygame.Rect(m.x, m.y, m.imagen.get_width(), m.imagen.get_height()).colliderect(
            pygame.Rect(nave.x, nave.y, nave.imagen.get_width(), nave.imagen.get_height())):
            meteoritos.remove(m)
            vidas -= 1
            sonidos[1].play()
            continue
        if m.y + m.imagen.get_height() >= tierra.y:
            tierra.recibir_danio(10)
            meteoritos.remove(m)
    nave.Dibujar(Ventana)
    tierra.Dibujar(Ventana)
    """if score >= 100:
     naveenemiga.Dibujar(Ventana)"""
    pygame.draw.rect(Ventana, (50, 50, 50), (Ancho // 2 - 150, 60, 300, 40), border_radius=10)
    Ventana.blit(fuente.render(palabra_actual, True, BLANCO), (Ancho // 2 - 140, 65))
    Ventana.blit(fuente.render(f"Score: {score}", True, BLANCO), (10, 50))
    Ventana.blit(fuente.render(f"Vidas: {vidas}", True, BLANCO), (Ancho - 140, 50))
    if vidas <= 0 or tierra.explotado():
      game_over = True
      if tierra.explotado():
        mensaje = "¡La Tierra fue destruida!"
      else:
       mensaje = "¡Perdiste!"
      texto = fuente.render(mensaje, True, ROJO)
      Ventana.blit(texto, (Ancho // 2 - 180, Alto // 2))
      pygame.display.flip()
      pygame.time.wait(3000)


    pygame.display.flip()

pygame.quit()
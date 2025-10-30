import pygame
import sys

pygame.init()

LARGURA, ALTURA = 600, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pac-Man Simples")


PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
AZUL = (0, 0, 255)

pacman_x, pacman_y = 300, 300
velocidade = 5
raio = 20


relogio = pygame.time.Clock()


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        pacman_x -= velocidade
    if teclas[pygame.K_RIGHT]:
        pacman_x += velocidade
    if teclas[pygame.K_UP]:
        pacman_y -= velocidade
    if teclas[pygame.K_DOWN]:
        pacman_y += velocidade


    pacman_x = max(raio, min(LARGURA - raio, pacman_x))
    pacman_y = max(raio, min(ALTURA - raio, pacman_y))


    TELA.fill(PRETO)
    pygame.draw.circle(TELA, AMARELO, (pacman_x, pacman_y), raio)


    boca_angulo = 45 if teclas[pygame.K_RIGHT] else -45
    pygame.draw.arc(TELA, PRETO,
                    (pacman_x - raio, pacman_y - raio, raio * 2, raio * 2),
                    0.2, 3.0, 5)

    pygame.display.flip()
    relogio.tick(60)
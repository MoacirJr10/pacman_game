import math
import pygame

WIDTH, HEIGHT = 600, 600
SPEED, RADIUS = 300, 20

def main():
    pygame.init()
    try:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pac-Man - demonstracao")
        clock = pygame.time.Clock()
        position = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
        direction = pygame.Vector2(1, 0)
        pellets = [pygame.Vector2(x, y) for x in range(40, WIDTH, 40) for y in range(40, HEIGHT, 40)]
        score = 0
        font = pygame.font.Font(None, 30)
        running = True
        while running:
            dt = min(clock.tick(60) / 1000, 0.05)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False
            keys = pygame.key.get_pressed()
            movement = pygame.Vector2(int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT]), int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP]))
            if movement.length_squared():
                direction = movement.normalize()
                position += direction * SPEED * dt
            position.x = max(RADIUS, min(WIDTH - RADIUS, position.x))
            position.y = max(RADIUS, min(HEIGHT - RADIUS, position.y))
            remaining = [pellet for pellet in pellets if pellet.distance_to(position) > RADIUS + 3]
            score += len(pellets) - len(remaining)
            pellets = remaining
            screen.fill((0, 0, 0))
            for pellet in pellets:
                pygame.draw.circle(screen, (240, 240, 240), (round(pellet.x), round(pellet.y)), 3)
            center = (round(position.x), round(position.y))
            pygame.draw.circle(screen, (255, 255, 0), center, RADIUS)
            heading = math.atan2(direction.y, direction.x)
            opening = 0.12 + 0.45 * abs(math.sin(pygame.time.get_ticks() / 110))
            edge = [(round(position.x + RADIUS * 1.2 * math.cos(heading + a)), round(position.y + RADIUS * 1.2 * math.sin(heading + a))) for a in (-opening, opening)]
            pygame.draw.polygon(screen, (0, 0, 0), [center, *edge])
            screen.blit(font.render(f"Pontos: {score}" if pellets else f"Concluido! Pontos: {score}", True, (255, 255, 255)), (12, 10))
            pygame.display.flip()
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()

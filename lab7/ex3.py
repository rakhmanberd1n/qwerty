import pygame
import sys

pygame.init()
WHITE = (255, 255, 255)
RED = (255, 0, 0)

WIDTH, HEIGHT = 800, 800

BALL_SIZE = 50
BALL_RADIUS = 25

ball_x = (WIDTH - BALL_SIZE) // 2
ball_y = (HEIGHT - BALL_SIZE) // 2


def draw_ball():
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Moving Ball')

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)
    draw_ball()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y -= 20
            elif event.key == pygame.K_DOWN:
                ball_y += 20
            elif event.key == pygame.K_LEFT:
                ball_x -= 20
            elif event.key == pygame.K_RIGHT:
                ball_x += 20
                
    ball_x = max(BALL_RADIUS, min(WIDTH - BALL_RADIUS - BALL_SIZE, ball_x))
    ball_y = max(BALL_RADIUS, min(HEIGHT - BALL_RADIUS - BALL_SIZE, ball_y))
    pygame.display.flip()
    
    clock.tick(30)
pygame.quit()
sys.exit()
import pygame 
import random
pygame.init()

W, H = 800, 600
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (194, 255, 201)

paddleW = 200
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)



ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1



font = pygame.font.SysFont('comicsansms', 40)
text = font.render('Game Over', True, (255, 255, 255))
textRect = text.get_rect()
textRect.center = (W // 2, H // 2)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)
    
    pygame.draw.rect(screen, pygame.Color(110, 13, 248), paddle)
    pygame.draw.circle(screen, pygame.Color(110, 13, 248), ball.center, ballRadius)
    
    
    
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed


    
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    
    if ball.centery < ballRadius + 50: 
        dy = -dy
   
    if ball.colliderect(paddle) and dy > 0:
        dy = -dy
    if ball.y > H or ball.x > W:
        screen.fill((0, 0, 0))
        screen.blit(text, textRect)

    pygame.display.update()
    clock.tick(FPS)

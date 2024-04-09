import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((1080, 800))
clock = pygame.time.Clock()

radius = 10
x = 0
y = 0
done = False
radius_for_eraser = 0

RED = (230, 0, 0)
GREEN = (0, 230, 0)
BLUE = (0, 0, 230)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [RED, GREEN, BLUE]
color = WHITE


eraser = pygame.image.load("eraser.png")
eraser = pygame.transform.scale(eraser, (70,70))

def draw_rect(index):
    pygame.draw.rect(screen, colors[index], (index*40, 0, 40, 40))


def color_pick():
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if 0<x<40 and 0<y<40:
            return RED
        elif 40<x<80 and 0<y<40:
            return GREEN
        elif 80<x<120 and 0<y<40:
            return BLUE
        elif 120<x<160 and 0<y<60:
            return "rect"
        elif 160<x<200 and 0<y<40:
            return "circle"
        elif 1010<=x<=1080 and 0<=y<=70:
            return BLACK
    return color  

def painting(color):
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if color != "rect" and color != "circle" and color != BLACK:
            pygame.draw.circle(screen, color, (x,y), radius)
        elif color == "rect":
            pygame.draw.rect(screen, WHITE, (x,y, 40, 60), 4) 
        elif color == "circle":
            pygame.draw.circle(screen, WHITE, (x,y), 20, 4)
        elif color == BLACK:
            pygame.draw.circle(screen ,color, (x,y), 20, 27)
        
    
while not done:
    for event in pygame.event.get():
        
     
        if event.type == QUIT:
            done = True
        
        
        for i in range(len(colors)):
            draw_rect(i)
        pygame.draw.circle(screen, WHITE, (180,20), 20, 4)
        screen.blit(eraser, (1010, 0))
        pygame.draw.rect(screen, WHITE, (120, 0, 40, 60), 4)
        
        
        color = color_pick()
        painting(color)
        
        clock.tick(360)
        pygame.display.update()
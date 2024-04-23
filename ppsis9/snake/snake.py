import pygame as pg
import random,time


pg.init()


WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Змейка")
mus=pg.mixer.Sound(r"c:\Users\lenovo\Desktop\pp\ppsis9\snake\kk.mp3")



back_graund=pg.image.load(r"c:\Users\lenovo\Desktop\pp\ppsis9\snake\fsnake.png")
back_graund=pg.transform.scale(back_graund,(800,600))

clock = pg.time.Clock()
level = 1
font = pg.font.SysFont("comicsansms", 20)
font_big = pg.font.SysFont("comicsansms", 56)
status = "Начинающий"
game_over = font_big.render("Game Over", 1, "BLUE")
score = 0
apple_time = pg.USEREVENT + 1
apple_in_pole = True
apl_Count = 0
thre_point=1
time_aple=[8,11]
pg.time.set_timer(apple_time, 1000)

def draw_objects(snake, apple):
    screen.blit(back_graund,(0,0))
    for segment in snake:
        pg.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    if score%7==0 and thre_point==1:    
       pg.draw.rect(screen, RED, (apple[0] * CELL_SIZE, apple[1] * CELL_SIZE, CELL_SIZE*2, CELL_SIZE*2))
    else:
        pg.draw.rect(screen, RED, (apple[0] * CELL_SIZE, apple[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))


snake = [(GRID_WIDTH // 2 , GRID_HEIGHT // 2 )]
direction = pg.Vector2(1, 0)
apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
big_apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
fps = 6
apple_area = [(apple[0], apple[1]), (apple[0] + 1, apple[1]),
              (apple[0], apple[1] + 1), (apple[0] + 1, apple[1] + 1)]
mus.play()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == apple_time:
            apl_Count = (apl_Count + 1) % (time_aple[1]+1)
    
    
    keys = pg.key.get_pressed()
    if apl_Count == time_aple[0] and apple_in_pole == True:
        apple = (-10, -10)
        apple_in_pole = False
        thre_point=0
    if apl_Count == time_aple[1] and apple_in_pole == False:
        apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        apple_in_pole = True

    if keys[pg.K_UP] and direction.y != 1:
        direction = pg.Vector2(0, -1)
    elif keys[pg.K_DOWN] and direction.y != -1:
        direction = pg.Vector2(0, 1)
    elif keys[pg.K_LEFT] and direction.x != 1:
        direction = pg.Vector2(-1, 0)
    elif keys[pg.K_RIGHT] and direction.x != -1:
        direction = pg.Vector2(1, 0)

    snake_head = snake[0] + direction
    if snake_head[0] < 0 or snake_head[0] >= GRID_WIDTH or snake_head[1] < 0 or snake_head[1] >= GRID_HEIGHT or snake_head in snake:
        mus.stop()
        pg.mixer.Sound("g_o.mp3").play()
        screen.fill("Red")
        screen.blit(game_over, (250, 240))
        screen.blit(font.render(f"Ваш счет :{score}", True, GREEN), (250,400 ))
        screen.blit(font.render(f"Вы дошли до {level} уровня", True, GREEN), (250, 380))

        if level == 2:
            status = "Новичок"
        elif level == 3:
            status = "Любитель"
        elif level == 4:
            status = "Профессионал"
        elif level >= 5 and level<=7:
            status = "Мировой класс"
        elif level >= 8:
            status="Пока Легенда!"
        screen.blit(font_big.render(f"Ваш статус: {status}", True, GREEN), (150, 140))
        pg.display.flip()
        time.sleep(2)
        running = False

    snake.insert(0, snake_head)
    if score%7==0 and thre_point==1:
        if snake_head in apple_area:
            apple_in_pole = False
            apple = (-10, -10)
            apl_Count = time_aple[0]
            score += 3
            if score % 5 == 0:
                level += 1
                time_aple=[time_aple[0]-4,time_aple[1]-2]
                fps += 2
            pg.mixer.Sound('ymmu.mp3').play()
        else:
            snake.pop()
    else:
        if snake_head==apple:
            
                apple_in_pole = False
                apple = (-10, -10)
                apl_Count = time_aple[0]
                score += 1
                thre_point=1
                if score % 5 == 0:
                    level += 1
                    fps += 2
                pg.mixer.Sound("ymmu.mp3").play()
        else:
                snake.pop()
            
    if score%7==0 and thre_point==1:
            apple_area = [(apple[0], apple[1]), (apple[0] + 1, apple[1]),
                        (apple[0], apple[1] + 1), (apple[0] + 1, apple[1] + 1)]

    score_dr = font.render(f"Счет:{str(score)}", 1, GREEN)
    level_dr = font.render(f"Уровень:{str(level)}", 1, GREEN)
    draw_objects(snake, apple)
    screen.blit(score_dr, (10, 10))
    screen.blit(level_dr, (690, 10))

    pg.display.flip()
    clock.tick(fps)

pg.quit()
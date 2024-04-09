import pygame as pg
from pygame.locals import *
import random, sys
import time

from pygame.sprite import *

pg.init()
W, H = 400, 600
clock = pg.time.Clock()
screen = pg.display.set_mode((W, H))
screen.fill("white")
speed = 5
speed_player=5
score = 0
back_ground = pg.image.load("AnimatedStreet.png")
font = pg.font.SysFont("comicsansms", 60)
font_small = pg.font.SysFont("comicsansms", 20)
game_over = font.render("Game Over", True, "red")
coin=["coin1.png","coin2.png","coin3.png","coin4.png","coin5.png","coin6.png"]
coin_sheet_index = 0
bg_coin=["cn (2).png","cn (3).png","cn (4).png","cn (5).png","cn (6).png","cn (7).png",'cn (8).png',"cn (9).png","cn (10).png","cn (11).png"]
point=0
coin_sheet_index_= 0
player1=pg.image.load("Player.png")
player1=pg.transform.scale(player1,(player1.get_width()//4,player1.get_height()//4))
enem=pg.image.load("Enemy.png")
enem=pg.transform.scale(enem,(enem.get_width()//4,enem.get_height()//4))
class player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player1
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pg.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-speed, 0)
        if self.rect.right < 400:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(speed, 0)
        #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
        #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)


class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global x
        x=random.randint(4,7)
        self.image = pg.transform.scale(pg.image.load(coin[coin_sheet_index]), (pg.image.load(coin[coin_sheet_index]).get_width()//x, pg.image.load(coin[coin_sheet_index]).get_height()//x))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W-40), 0)

    def move(self):
        self.rect.move_ip(0, 4)
        
        if self.rect.top > 600:
            global x
            x=random.randint(4,7)
            self.rect.center = (random.randint(30, 370), -300)

    def update_image(self):
        global coin_sheet_index
        global x
        coin_sheet_index = (coin_sheet_index + 1) % len(coin)  # Обновляем индекс изображения монетки с учетом цикличности
        self.image = pg.transform.scale(pg.image.load(coin[coin_sheet_index]), (pg.image.load(coin[coin_sheet_index]).get_width()//x, pg.image.load(coin[coin_sheet_index]).get_height()//x))

class Big_Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(bg_coin[coin_sheet_index_]), (pg.image.load(bg_coin[coin_sheet_index_]).get_width()//7, pg.image.load(bg_coin[coin_sheet_index_]).get_height()//7))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W-40), 0)
    def move(self):
        self.rect.move_ip(0, 7)
        
        if self.rect.top > 600:
           
            self.rect.center = (random.randint(30, 370), -5000)

    def update_image(self):
        global coin_sheet_index_
        coin_sheet_index_ = (coin_sheet_index_ + 1) % len(bg_coin)  # Обновляем индекс изображения монетки с учетом цикличности
        self.image = pg.transform.scale(pg.image.load(bg_coin[coin_sheet_index_]), (pg.image.load(bg_coin[coin_sheet_index_]).get_width()//7, pg.image.load(bg_coin[coin_sheet_index_]).get_height()//7))


class Enemy(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = enem
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, W - 30), 0)

    def move(self):
        global score  # Делаем переменную score глобальной
        self.rect.move_ip(0, speed)
        if self.rect.top> 600:
            self.rect.top= 0
            score += 1
            self.rect.center = (random.randint(30, 370), 0)


p1 = player()
e1 = Enemy()
c1 = Coin()
c2=Big_Coin()
enemies = pg.sprite.Group()
enemies.add(e1)
all_sprites = pg.sprite.Group()
coins=pg.sprite.Group()
coins.add(c1)
bg_coins=pg.sprite.Group()
bg_coins.add(c2)
all_sprites.add(p1)
all_sprites.add(e1)
inc_speed = pg.USEREVENT + 1
coin_ap = pg.USEREVENT + 1
point_sh=False
pg.time.set_timer(coin_ap, 1)
pg.time.set_timer(inc_speed, 1000)
g = pg.mixer.Sound('background.mp3').play()
running = True

while running:

    
    screen.blit(back_ground, (0, 0))
    points=font_small.render(str(point), True, "yellow")
    scores = font_small.render(str(score), True, "black")
    screen.blit(scores, (10, 10))
    screen.blit(points, (W-30, 10))
    for en in all_sprites:
        screen.blit(en.image, en.rect)
        en.move()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == inc_speed:
            if point_sh==True:
                point_sh=False
        if event.type == coin_ap:
            c1.update_image()
            c2.update_image()
    screen.blit(c1.image, c1.rect)
    screen.blit(c2.image, c2.rect)
    c1.move()
    c2.move()
    if pg.sprite.spritecollideany(p1,coins):
        global x
        pg.mixer.Sound('ymmu.mp3').play()
        x=random.randint(4,7)
        c1.rect.center = (random.randint(30, 370), -500)
        
        point+=1
        if c1.image.get_width()==pg.image.load(coin[coin_sheet_index]).get_width()//4:
            point+=2
            point_sh=True
            pg.mixer.Sound("vf.mp3").play()
        
        speed+=0.1
    if pg.sprite.spritecollideany(p1,bg_coins):
        pg.mixer.Sound("vf.mp3").play()
        c2.rect.center = (random.randint(30, 370), -5000)
        point+=3
        point_sh=True
        
        speed+=0.2
    if point_sh==True:
        screen.blit(font.render("+3",1,"green"),(100,100))
    if pg.sprite.spritecollideany(p1, enemies):
        g.stop()
        pg.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        screen.fill("blue")
        screen.blit(game_over, (30, 250))
        screen.blit(font_small.render(f"У вас {point} monet ", True, "black"), (10, 10))

        screen.blit(font_small.render(f"Прошли  {score} копов", True, "black"), (10, 35))
        pg.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pg.quit()
        sys.exit()
    pg.display.update()
    clock.tick(60)
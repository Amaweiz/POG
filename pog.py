from pygame import *
from random import *
from time import time as timer

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Я в эти игры уже играл!!!')
background = transform.scale(image.load('Ani_backgr.png'), (win_width, win_height))
speed_x = 3
speed_y = 3

#mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()

#fire_sound = mixer.Sound('fire.ogg')

class Gameprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gameprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#direction = 'right'

#class Enemy(Gameprite):
#    def update(self):
#        self.rect.y += self.speed
#        global direction
#        direction = randint(0, 100)
#        if direction == 'right':
#            self.rect.x += self.speed
#        else:
#            self.rect.x -= self.speed
#        global lost
#        if self.rect.y > win_height:
#            self.rect.x = randint(80, win_width - 80)
#            self.rect.y = 0
##            lost = lost + 1
#
#class Bullet(Gameprite):
#    def update(self):
#        self.rect.y += self.speed
#        if self.rect.y < 0:
#            self.kill()
#
#class Wall(sprite.Sprite):
#    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
#        super().__init__
#        self.color_1 = color_1
#        self.color_2 = color_2
#        self.color_3 = color_3
#        self.width = wall_width
#        self.height = wall_height
#        self.image = Surface((self.width, self.height))
#        self.image.fill((color_1, color_2, color_3))
#        self.rect = self.image.get_rect()
#        self.rect.x = wall_x
#        self.rect.y = wall_y
#    def draw_wall(self):
#        window.blit(self.image, (self.rect.x, self.rect.y))
#
#font.init()
#font2 = font.SysFont('Arial', 36)
#
img_hero = 'paketka.png'
img_enemy = 'm9ch.png'
#img_bullet = 'ufo.png'
ship_1 = Player(img_hero, 5, win_height - 100, 80, 100, 10)
ship_2 = Player(img_hero, 600, win_height - 100, 80, 100, 10)
m9ch = Gameprite(img_enemy, 200, win_height - 100, 80, 100, 10)
#max_monsters = 5
#asteroids = sprite.Group()
#for i in range(1, 3):
#    asteroid = Enemy(img_hero, randint(30, win_width - 30), -40, 80, 50, randint(1, 7))
#    asteroids.add(asteroid)
#
#monsters = sprite.Group()
#for i in range(0, max_monsters):
#    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 3))
#    monsters.add(monster)
#
#bullets = sprite.Group()
#
#rel_time = False
#num_fire = 0
#max_lost = 5
#goal = 30
#lost = 0
#life = 3
#score = 0
game = True
finish = False
clock = time.Clock()
FPS = 140
#
#
#
font.init()
font1 = font.Font(None, 70)
lose1 = font1.render('Player 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('Player 2 LOSE!', True, (180, 0, 0))
#
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 

#        elif e.type == KEYDOWN:
#            if e.key == K_SPACE:
#                if direction == 'right':
#                    direction = 'left'
#                else:
#                    direction = 'right'
#
#
#                if num_fire < 5 and rel_time == False:
#                    num_fire = num_fire + 1
#                    fire_sound.play()
#                    ship.fire()
#
#                if num_fire >= 5 and rel_time == False:
#                    last_time = timer()
#                    rel_time = True
#            if e.key == K_r and finish == True:
#                score = 0
#                lost = 0
#                finish = False
#                num_fire = 0
#                rel_time = False
#                life = 3
#
#
#                for m in monsters:
#                    m.kill()
#                for b in bullets:
#                    b.kill()
#
#                ship_1.rect.x = 5
#                ship_1.rect.y = win_height - 100
#                for i in range(0, max_monsters):
#                    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
#                    monsters.add(monster)


    if not finish :
        window.blit(background, (0, 0))
        if m9ch.rect.y > win_height - 80 or m9ch.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(m9ch, ship_1) or sprite.collide_rect(m9ch, ship_2):
            speed_x *= -1.1
            speed_y *= 1.11 
        

        m9ch.rect.x += speed_x
        m9ch.rect.y += speed_y
        ship_1.update_l()
        ship_2.update_r()
#        monsters.update()
#        bullets.update()
#        asteroids.update()
#
        ship_1.reset()
        ship_2.reset()
        m9ch.reset() 
        if m9ch.rect.x < 0:
            window.blit(lose1, (200, 200))
            finish = True
        if m9ch.rect.x > 620:
            window.blit(lose2, (200, 200))
            finish = True
#        monsters.draw(window)
#        bullets.draw(window)
#        asteroids.draw(window)
#
#        if rel_time == True:
#            now_time = timer()
#            if now_time - last_time < 3:
#                reload = font2.render('Wait, reload...', 1, (150, 0, 0))
#                window.blit(reload,(260, 460))
#            else:
#                num_fire = 0
#                rel_time = False
#
#        collides = sprite.groupcollide(monsters, bullets, True, True)
#        for c in collides:
#            score = score + 1
#            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 3))
#            monsters.add(monster)
#
#        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
#            finish = True
#            window.blit(lose, (200, 200))
#            if max_monsters > 3:
#                max_monsters -=3
#
#        if sprite.spritecollide(ship, monsters, False) or sprite.spritecollide(ship, asteroids, False):
#            sprite.spritecollide(ship, monsters, True)
#            sprite.spritecollide(ship, asteroids, True)
#            life = life - 1
#
#        if life == 0 or lost >= max_lost:
#            finish = True
#            window.blit(lose, (200, 200))
#
#        if score >= goal:
#            finish = True
#            window.blit(win, (200, 200))
#            max_monsters += 2
#
        display.update()
    
    clock.tick(FPS)

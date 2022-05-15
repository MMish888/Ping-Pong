#Модули
from pygame import *
font.init()

#Окно игры
clock = time.Clock()
FPS = 100
x1 = 550
y1 = 350
x2 = 150
y2 = 350
step = 10
window = display.set_mode((1000, 500))
display.set_caption("Maze")
background = transform.scale(image.load("background.png"), (1000, 500))

#Классы
class GameSprite(sprite.Sprite):
     def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (100,100))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
     def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))  

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y > 5:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    a = "right"  
    def update(self):  
        if self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction != "left":
            self.rect.x += self.speed
        if self.rect.x >= 800:
            self.direction = "left"
        if self.rect.x <= 400:
            self.direction = "right"

        
#Объекты
Wizard = Player("Player 1.png", 150, 350, 5 )
#Rogue = Enemy("Rogue.png", 550, 350, 5 ) 
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('GAME OVER!', True, (255, 215, 0))

#Игровой цикл
game = True
finish = False
while game:
    clock.tick(FPS)
    

    display.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0)) 
        Wizard.update()

        Wizard.reset()




        #if sprite.collide_rect(Wizard, Portal):
            #window.blit(win,(255, 215)) 
            #finish = True

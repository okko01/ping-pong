from pygame import*
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,x,y,speed,size_x,size_y):
        super().__init__()
        self.speed=speed
        self.image=transform.scale(image.load(player_image),(size_x,size_y))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed
class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
class Ball(GameSprite):
    def update(self):
        pass
lost = 0


        
        
        
last=0
player1= Player("player1.png",680,0,6,85,85)
player= Player1("player.png",0,0,6,65,65)
ball = Ball ("ball.png",350,250,0,65,65)




visota=750
hirina=500
window = display.set_mode((visota,hirina))
display.set_caption("Шутер")
background = transform.scale(image.load("galaxy.png"),(750,500))

finish = False
clock = time.Clock()
FPS = 60
game = True
fire=0




while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))
    player.reset()
    player.update()
    player1.reset()
    player1.update()
    ball.reset()
    ball.update()
   

    
    clock.tick(FPS)
    display.update()
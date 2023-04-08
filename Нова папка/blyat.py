from pygame import *
import pygame
from random import *
pygame.init() 
back = (200, 255, 24)  
mw = pygame.display.set_mode((500, 500))  
background_image = pygame.image.load('qwert.jpg') 
clock = pygame.time.Clock()  
dx = 3 
dy = 3 
class Area():  
    def __init__ (self, x=0, y=0, width=10, height=10, color=None):  
        self.rect = pygame.Rect(x, y, width, height)  
        self.fill_color = back  
        if color:  
            self.fill_color = color  
    def color(self, new_color):  
        self.fill_color = new_color  
    def fill(self):  
        pygame.draw.rect(mw, self.fill_color, self.rect)  
    def collidepoint(self, x, y):  
        return self.rect.collidepoint(x, y)        
    def colliderect(self, rect):  
        return self.rect.colliderect(rect)  
  
  
class Label(Area):  
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):  
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)  
    def draw(self, shift_x=0, shift_y=0):  
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))  
  
  
class Picture(Area):  
    def __init__ (self, filename, x=0, y=0, width=10, height=10):  
        Area. __init__ (self, x=x, y=y, width=width, height=height, color=None)  
        self.image = pygame.image.load(filename)  
          
    def draw(self):  
        mw.blit(self.image, (self.rect.x, self.rect.y))  
 
     
move_left = False 
move_up = False 
move_down = False 
move_right = False 
ptax = Picture('qwerty.png', 0, 200, 70, 70)  
mer = Picture('qwer.png',0,450, 110, 65) 
mer2 = Picture('qwer.png',0,450, 110, 65) 
mer3 = Picture('qwer.png',0,450, 110, 65) 
while True: 
 
 
    mw.blit(background_image, (0, 0)) 
     
    mer3.rect.x-=3  
    mer2.rect.x-=4 
    mer.rect.x-=6 
    if mer.rect.colliderect(ptax.rect) or mer2.rect.colliderect(ptax.rect) or mer3.rect.colliderect(ptax.rect): 
        game_over = True 
        break 
         
         
         
    if mer.rect.x < 0:  
        mer.rect.y = randint(0,350) 
        mer.rect.x = 450 
    if mer2.rect.x < 0:  
        mer2.rect.y = randint(0,350) 
        mer2.rect.x = 450 
    if mer3.rect.x < 0:  
        mer3.rect.y = randint(0,350) 
        mer3.rect.x = 450 
 
     
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            game_over = True 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_w: 
                move_up = True 
            if event.key == pygame.K_s: 
                move_down = True 
            if event.key == pygame.K_a:  
                move_left = True 
            if event.key == pygame.K_d: 
                move_right = True 
        elif event.type == pygame.KEYUP: 
            if event.key == pygame.K_w: 
                move_up = False 
            if event.key == pygame.K_s: 
                move_down = False 
            if event.key == pygame.K_a: 
                move_left = False 
            if event.key == pygame.K_d: 
                move_right = False 
 
 
    if move_up and ptax.rect.y >-0:   
        ptax.rect.y -=4   
    if move_down and ptax.rect.y <410:  
        ptax.rect.y +=4  
    if move_left and ptax.rect.x >-0:   
        ptax.rect.x -=4   
    if move_right and ptax.rect.x <430:    
        ptax.rect.x +=4 
    if ptax.rect.x <1:  
        for i in range(5):  
            ptax.rect.x +=4 
    if ptax.rect.y <1:  
        for i in range(5):  
            ptax.rect.y +=4 
    if ptax.rect.x >430:  
        for i in range(5):  
            ptax.rect.x -=4 
    if ptax.rect.y >405:  
        for i in range(5):  
            ptax.rect.y -=4 
    

 
 
    ptax.draw() 
    mer.draw() 
    mer2.draw() 
    mer3.draw() 
    pygame.display.update() 
    clock.tick(58) 
 

mixer.init()
mixer.music.load('muzon.mp3')
mixer.music.play()
mixer.music.set_volume(0.2)

 
time_text = Label(150,150,50,50,back)  
time_text.set_text('Ти програв',60, (0,255,0))  
time_text.draw(10, 10) 
pygame.display.update() 
clock.tick(60)
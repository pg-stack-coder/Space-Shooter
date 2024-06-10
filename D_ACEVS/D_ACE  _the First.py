import pygame as py
import random
py.init()
win=py.display.set_mode((600,600),py.RESIZABLE)
py.display.set_caption('Pygame the first')
img=py.image.load(r'c:\Users\CS5\Pictures\3d wallpapers\earthsolar.jpg ')
img_=py.transform.scale(img,(600,600))
img_rect=img_.get_rect()
img2=py.image.load(r'C:\Users\CS5\Pictures\3d wallpapers\22 (2).png')
img2_=py.transform.scale(img2,(90,40))
img2_rect=img2_.get_rect(center=(300,500))
img3=py.image.load(r'C:\Users\CS5\Pictures\3d wallpapers\weapons_asteroid1.png')
img3_=py.transform.scale(img3,(40,40))
img3_rect=img3_.get_rect(center=(50,400))
img4=py.image.load(r'C:\Users\CS5\Pictures\3d wallpapers\blast.png')
img4_rect=img4.get_rect()
class asteroids:
    allasteroids=[]
    move=True 
    lives=25
    def __init__(self):
        asteroids.allasteroids.append(self)
        self.rect=img3_.get_rect()
        self.speed=0
        self.x_cor=random.randint(0,600)
        self.x_sp=random.randrange(-1,2) 
    def astralshower():
        for i in asteroids.allasteroids:
            win.blit(img3_,i.rect)
            i.rect.x=i.x_cor
            i.rect.y=i.speed
            i.x_cor+=i.x_sp
            i.speed+=1.25
            if i.speed>600 or i.rect.x<-30 or i.rect.x>600:
                i.speed=0
                i.x_cor=random.randint(100,500)
                i.x_sp=random.random()
                mult=random.randrange(-1,2)
                i.x_sp*=mult
        for obj in asteroids.allasteroids:
            if py.Rect.colliderect(obj.rect,img2_rect):
                asteroids.lives-=1
                if asteroids.lives==0:
                    asteroids.move = False
run=True
FPS=250
def draw(prag_gpt):
    if prag_gpt[py.K_RIGHT] and img2_rect.x<520:
        img2_rect.x +=1
    if prag_gpt[py.K_LEFT] and img2_rect.x>=0:
        img2_rect.x -=1
    if prag_gpt[py.K_UP] and img2_rect.y>350:
        img2_rect.y -=1
    if prag_gpt[py.K_DOWN] and img2_rect.y<520:
        img2_rect.y +=1
clock=py.time.Clock()  
max=0     
for i in range(3):asteroids()
while run:
    clock.tick(FPS)
    for event in py.event.get():
        if event.type==py.QUIT:
            run=False
    win.fill('light blue')
    win.blit(img_,img_rect)
    win.blit(img2_,img2_rect)
    if asteroids.move:
        asteroids.astralshower()
        key_pressed=py.key.get_pressed()
        draw(key_pressed)
    else:
        img4_rect.x=img2_rect.x-60
        img4_rect.y=img2_rect.y-40
        win.blit(img4,img4_rect)
    for i in asteroids.allasteroids:
        win.blit(img3_,i.rect)
    if max<10:
        num=random.randint(1,1000)
        if num == 1:
            asteroids()
            max+=1
    py.display.update()
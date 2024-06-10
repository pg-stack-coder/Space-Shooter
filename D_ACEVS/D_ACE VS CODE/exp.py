'''CAUTION :-
BEFORE RUNNING MAKE SURE YOU HAVE PY GAME AND PLEASE CHANGE THE IMAGE PATHS'''
import pygame as py
import random
py.init()
x=1366;y=768
win=py.display.set_mode((1326,728),py.RESIZABLE)
py.display.set_caption('Pygame the first')
#----------------------------------------------------|loading images|-----------------------------------------------
img=py.image.load(r'c:\Users\CS5\Pictures\3d wallpapers\earthsolar.jpg ')
img2=py.image.load(r'C:\Users\CS5\Pictures\3d wallpapers\22 (2).png')
img3=py.image.load(r'C:\Users\CS5\Pictures\3d wallpapers\weapons_asteroid1.png')
img4=py.image.load(r'C:\Users\CS5\Pictures\3d wallpapers\blast.png')
#-----------------------------------------------|Editing images|------------------------------------------------
img_=py.transform.scale(img,(x,y))
img2_=py.transform.scale(img2,(90,40))
img3_=py.transform.scale(img3,(40,40))
#-----------------------------------------------|get_rect|-------------------------------------------------------
img_rect=img_.get_rect()
img2_rect=img2_.get_rect(center=(300,500))
img3_rect=img3_.get_rect(center=(50,400))
img4_rect=img4.get_rect()
#-----------------------------------------------|Variables|-----------------------------------------------------
run=True
FPS=300
clock=py.time.Clock()  
max=0
#-----------------------------------------------|class and func|--------------------------------------------------
def retry():
    global img4_rect,run
    final=py.key.get_pressed()
    if final[py.K_SPACE]:
        run=True
        for i in asteroids.allasteroids:
            del i 
        asteroids.allasteroids.clear()
        img2_rect.x=300
        img2_rect.y=500
        asteroids.move=True
        for i in range(6):asteroids()
class asteroids:
    allasteroids=[]
    move=True 
    def __init__(self):
        asteroids.lives=25
        asteroids.allasteroids.append(self)
        self.rect=img3_.get_rect()
        self.speed=0
        self.x_cor=random.randint(0,1366)
        self.x_sp=random.randrange(-1,2) 
    def astralshower():
        for i in asteroids.allasteroids:
            win.blit(img3_,i.rect)
            i.rect.x=i.x_cor
            i.rect.y=i.speed
            i.x_cor+=i.x_sp
            i.speed+=1.25
            if i.speed>768 or i.rect.x<-30 or i.rect.x>1366:
                i.speed=0
                i.x_cor=random.randint(100,1266)
                i.x_sp=random.random()
                mult=random.randrange(-1,2)
                i.x_sp*=mult
        for obj in asteroids.allasteroids:
            if py.Rect.colliderect(obj.rect,img2_rect):
                asteroids.lives-=1
                if asteroids.lives==0:
                    global run
                    asteroids.move = False
def draw(prag_gpt):
    global run
    if prag_gpt[py.K_RIGHT] and img2_rect.x<1286:
        img2_rect.x +=1
    if prag_gpt[py.K_LEFT] and img2_rect.x>=0:
        img2_rect.x -=1
    if prag_gpt[py.K_UP] and img2_rect.y>350:
        img2_rect.y -=1
    if prag_gpt[py.K_DOWN] and img2_rect.y<688:
        img2_rect.y +=1
#-----------------------------------------------|Spawning Asteroids|----------------------------------------------------       
for i in range(6):asteroids()
#-----------------------------------------------|Main loop|-----------------------------------------------------------
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
        retry()
    for i in asteroids.allasteroids:
        win.blit(img3_,i.rect)
    if max<15:
        num=random.randint(1,1000)
        if num == 1:
            asteroids()
            max+=1
    py.display.update()
#-----------------------------------------------|Infinitely Moving Bg|----------------------------------------------
def infinite(a,bg_rect,bg_rect2):
    bg_rect.x-=3
    bg_rect2.x-=3
    if bg_rect.x<-a:
        bg_rect.x=a
    if bg_rect2.x<-a:
        bg_rect2.x=a
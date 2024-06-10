import pygame as py
import random
py.init()
x=1366;y=768
win=py.display.set_mode((1326,728),py.RESIZABLE)
py.display.set_caption('Pygame the first')
img=py.image.load(r'C:\Users\ACER\OneDrive\Pictures\images\earthsolar.jpg ')
img_=py.transform.scale(img,(x,y))
img_rect=img_.get_rect()
img2=py.image.load(r'C:\Users\ACER\OneDrive\Pictures\images\22 (2).png')
img2_=py.transform.scale(img2,(90,40))
img2_rect=img2_.get_rect(center=(300,500))
img3=py.image.load(r'C:\Users\ACER\OneDrive\Pictures\images\weapons_asteroid1.png')
img3_=py.transform.scale(img3,(40,40))
img3_rect=img3_.get_rect(center=(50,400))
img4_=py.image.load(r'C:\Users\ACER\OneDrive\Pictures\images\k.png')
img4=py.transform.scale(img4_,(250,200))
img4_rect=img4.get_rect()
img5_=py.image.load(r'C:\Users\ACER\OneDrive\Pictures\images\bullet.PNG')
img5=py.transform.scale(img5_,(50,100))
img5_rect=img5.get_rect()
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
class bullets(py.sprite.Sprite):
    ki=py.sprite.Group()
    cool=0
    def __init__(self,x,y):
        py.sprite.Sprite.__init__(self)
        self.image=py.Surface((50,100))
        self.rect=self.image.get_rect()
        self.image.blit(img5,(x+20,y-40))
        
        self.x=x+20
        self.y=y-40
    def drawb(self):
        win.blit(img5,(self.x,self.y))
    def shoot():
        bullets.cooldown()
        bullets.ki.draw(win)
        if bullets.cool==0:
            bullet=bullets(img2_rect.x,img2_rect.y)
            bullets.ki.add(bullet)
            bullets.cool=1
            bullets.ki.update()
    def update(self):
        self.y-=3
        if self.y>800:
            self.kill()
    def kill():
        for b in bullets.ki:
            if b.y>800:
                del b
    def cooldown():
        if bullets.cool==35:
            bullets.cool=0
        elif bullets.cool>0:
            bullets.cool+=1


            

            
                
class asteroids:
    allasteroids=[]
    move=True 
    def __init__(self):
        asteroids.lives=10
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
            i.speed+=3
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
                    asteroids.move = False
run=True
FPS=300
def infinite(a,bg_rect,bg_rect2):
    bg_rect.x-=3
    bg_rect2.x-=3
    if bg_rect.x<-a:
        bg_rect.x=a
    if bg_rect2.x<-a:
        bg_rect2.x=a
def draw(prag_gpt):
    if prag_gpt[py.K_RIGHT] and img2_rect.x<1286:
        img2_rect.x +=3
    if prag_gpt[py.K_LEFT] and img2_rect.x>=0:
        img2_rect.x -=3
    if prag_gpt[py.K_UP] and img2_rect.y>350:
        img2_rect.y -=3
    if prag_gpt[py.K_DOWN] and img2_rect.y<688:
        img2_rect.y +=3
clock=py.time.Clock()  
max=0
for i in range(6):asteroids()
while run:
    clock.tick(FPS)
    for event in py.event.get():
        if event.type==py.QUIT:
            run=False
    win.blit(img_,img_rect)
    win.blit(img2_,img2_rect)
    

    if asteroids.move:
        asteroids.astralshower()
        key_pressed=py.key.get_pressed()
        draw(key_pressed)
        bullets.shoot()
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


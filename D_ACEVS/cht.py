import pygame as py
import random
py.init()
py.font.init()
x=900;y=768
win=py.display.set_mode((860,728))
py.display.set_caption('Pygame the first')
img=py.image.load(r'C:\Users\ACER\OneDrive\Pictures\images\earthsolar.jpg ')
img_=py.transform.scale(img,(x,y))
img_rect=img_.get_rect()
img2=py.image.load(r'C:\Users\ACER\OneDrive\Pictures\images\22 (2).png')
img2_=py.transform.scale(img2,(90,40))
img2_rect=img2_.get_rect(center=(450,500))
img3=py.image.load(r'C:\Users\ACER\OneDrive\Pictures\images\weapons_asteroid1.png')
img3_=py.transform.scale(img3,(40,40))
img3_rect=img3_.get_rect(center=(50,400))
img4_=py.image.load(r'C:\Users\ACER\OneDrive\Pictures\images\k.png')
img4=py.transform.scale(img4_,(250,200))
img4_rect=img4.get_rect()
img5_=py.image.load(r'C:\Users\ACER\OneDrive\Pictures\images\bullet.PNG')
img5=py.transform.scale(img5_,(50,100))
img5_rect=img5.get_rect()
img6_=py.image.load(r'C:\Users\ACER\OneDrive\Pictures\images\bomb.png')
img6=py.transform.scale(img6_,(60,60))
img6_rect=img6.get_rect()
img7=py.image.load(r'C:\Users\ACER\OneDrive\Pictures\images\freeze.png')
img7_=py.transform.scale(img7,(40,40))
img7_rect=img7_.get_rect()
img8=py.image.load(r'C:\Users\ACER\OneDrive\Pictures\images\life.png')
img8_=py.transform.scale(img8,(55,55))
img8_rect=img8_.get_rect()
lives=3;points=0
generate_power=True
start=wincheck=freeze_var=False
font=py.font.SysFont("comicsans",30,bold=True)
font1=py.font.SysFont("comicsans",100,bold=True)
target=random.randint(50,100)
d={1:img6,2:img7_,3:img8_}
def retry():
    global img4_rect,lives,start,target,wincheck,points,generate_power
    final=py.key.get_pressed()
    if final[py.K_SPACE] or final[py.K_KP_ENTER]:
        target=random.randint(50,101)
        points=0
        start=False
        wincheck=False
        lives=3
        powers.power.clear()
        bullets.ki.clear()
        asteroids.allasteroids.clear()
        img2_rect.x=300
        img2_rect.y=500
        asteroids.move=generate_power=True
        for i in range(5):asteroids()
        redraw_scene()
        challenge()
def redraw_scene():
    win.blit(img_, img_rect)  
    win.blit(img2_, img2_rect) 
    text()  
    py.display.update()
class bullets:
    ki=[]
    cool=0
    def __init__(self,x,y):
        self.x=x+20
        self.y=y-40
        self.rect=img5.get_rect(topleft=(self.x,self.y))
    def drawb(self):
        win.blit(img5,self.rect)
    def shoot():
        bullets.cooldown()
        if bullets.cool==0:
            bullet=bullets(img2_rect.x,img2_rect.y)
            bullets.ki.append(bullet)
            bullets.cool=1
        for bull in bullets.ki:
            bull.move()
    def move(self):
        self.rect.y-=3
    def kill():
        for b in bullets.ki:
            if b.y<-25:
                bullets.ki.remove(b)
    def coll():
        global points
        for bullet in bullets.ki:
            for asteroid in asteroids.allasteroids:
                if bullet.rect.colliderect(asteroid.rect):
                    points+=1
                    bullets.ki.remove(bullet)
                    asteroids.allasteroids.remove(asteroid)
                    py.display.update()
                    break
    def cooldown():
        if bullets.cool==50:
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
        self.speed=random.randint(-25,0)
        self.x_cor=random.randint(70,700)
        self.x_sp=random.randrange(-1,2) 
        mult=random.randrange(-1,2)
        self.x_sp*=mult
    def astralshower():
        global freeze_var,generate_power
        for i in asteroids.allasteroids:
            i.rect.x=i.x_cor
            i.rect.y=i.speed
            win.blit(img3_,i.rect)
            if freeze_var==False:
                i.x_cor+=i.x_sp
                i.speed+=1
            if i.x_cor<0 or i.x_cor>820:
                i.x_sp*=-1
        for obj in asteroids.allasteroids:
            if py.Rect.colliderect(obj.rect,img2_rect):
                asteroids.lives-=1
                if asteroids.lives==0:
                    asteroids.move = False
                    generate_power=False
def power_chance():
    global d,generate_power
    pc=random.randint(1,700)
    if pc==1 and generate_power:
        chosen=random.choice(list(d.keys()))
        powers(d[chosen])
        powers.condition=True
        return chosen
    return None
class powers:
    power=[]
    condition=False
    cooldown=0
    chosen=None
    def __init__(self,image):
        powers.power.append(self)
        self.rect=image.get_rect()
        self.speed=random.randint(-50,0)
        self.x_cor=random.randint(70,700)
        self.x_sp=random.randrange(-1,2) 
        mult=random.randrange(-1,2)
        self.x_sp*=mult
    def descend(image):
        global generate_power
        for i in powers.power:
            if i.rect.y<730:
                i.rect.x=i.x_cor
                i.rect.y=i.speed
                win.blit(image,i.rect)
                i.x_cor+=i.x_sp
                i.speed+=1
            else:
                generate_power=True
                powers.condition=False
                powers.power.remove(i)
            if i.x_cor<0 or i.x_cor>820:
                i.x_sp*=-1
    def life():
        global lives
        lives+=1
        py.display.update()
    def bomb():
        white_surface = py.Surface((win.get_width(), win.get_height()))
        white_surface.fill((255, 255, 255))
        win.blit(white_surface, (0, 0))
        py.display.update()
        py.time.delay(1000)
        asteroids.allasteroids.clear()
        bullets.ki.clear()
    def freeze():
        global freeze_var,generate_power
        generate_power=False
        freeze_var=True
    def buff():
        global generate_power,freeze_var,power_var
        for bullet in bullets.ki:
            for power in powers.power:
                if bullet.rect.colliderect(power.rect):
                    power_var=True
                    generate_power=True
                    powers.power.remove(power)
                    bullets.ki.remove(bullet)
                    if power.chosen == 1:
                        powers.bomb()
                    elif power.chosen == 3:
                        powers.life()
                    if powers.cooldown<600:
                            if power.chosen == 2:
                                powers.freeze()
                    else:
                        freeze_var=False
                    break
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
    global speed_var
    if prag_gpt[py.K_RIGHT] and img2_rect.x<x-130:
        img2_rect.x +=3
    if prag_gpt[py.K_LEFT] and img2_rect.x>=0:
        img2_rect.x -=3
    if prag_gpt[py.K_UP] and img2_rect.y>350:
        img2_rect.y -=3
    if prag_gpt[py.K_DOWN] and img2_rect.y<668:
        img2_rect.y +=3
def challenge():
    global start,target
    if start==False:
        challenge_label=font.render(f"Score {target} points to beat the game",1,(255,255,255))
        win.blit(challenge_label,(200,300))
        py.display.update()
        py.time.delay(5000)
        start=True
def win_check():
    global points,target,wincheck
    if points==target:
        wincheck=True
        asteroids.move=False
        if wincheck:
            win_label=font1.render(f"You Win",1,(255,255,255))  
            win.blit(win_label,(200,300))
        retry()
def text():
    global lives,points,target,start,generate_power
    lives_label=font.render(f"Lives:{lives}",1,(255,255,255))  
    win.blit(lives_label,(10,10))
    points_label=font.render(f"Points:{points}",1,(255,255,255))  
    win.blit(points_label,(700,10))
    points_label=font.render(f"Target:{target}",1,(255,255,255))  
    win.blit(points_label,(500,10))
    if lives==0 or asteroids.move==False:
        generate_power=False
        if wincheck==False:
            asteroids.move=False
            lose_label=font1.render(f"You Lose",1,(255,255,255))  
            win.blit(lose_label,(200,300))
            retry()
clock=py.time.Clock()  
max=co=0
current_power_up=None
power_var=True
for i in range(5):asteroids()
while run:
    clock.tick(FPS)
    for event in py.event.get():
            if event.type==py.QUIT:
                run=False
    win.blit(img_,img_rect)
    win.blit(img2_,img2_rect)
    challenge()
    if start:
        win_check()
        for bul in bullets.ki:
                bul.drawb()
        if power_var:
            if powers.cooldown<600:
                powers.cooldown+=1
            else:
                generate_power=True
                freeze_var=power_var=False
                powers.cooldown=0
        if asteroids.move:
            asteroids.astralshower()
            chosen_power = power_chance()
            if chosen_power is not None and powers.condition:
                powers.chosen=chosen_power
                current_power_up = d[chosen_power] 
                generate_power=False
            if current_power_up is not None:
                powers.descend(current_power_up)
            key_pressed=py.key.get_pressed()
            draw(key_pressed)
            bullets.shoot()
            powers.buff()
            bullets.coll()
            bullets.kill()
        elif wincheck==False:
            img4_rect.x=img2_rect.x-60
            img4_rect.y=img2_rect.y-40
            win.blit(img4,img4_rect)
            retry()
        if asteroids.allasteroids==[]:
            for i in range(3):
                asteroids()
        for i in asteroids.allasteroids:
            win.blit(img3_,i.rect)
            if i.rect.y>728:
                asteroids.allasteroids.remove(i)
                lives-=1
        text()
        chance=random.randint(1,100)
        if chance == 1:
            asteroids()
        py.display.update()
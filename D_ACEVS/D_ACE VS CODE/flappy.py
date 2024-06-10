import pygame as py
py.init()
x=1326;y=728
win=py.display.set_mode((x,y))
#-------------------------------------------|loading images|---------------------------------------------------------
img_=py.image.load(r'C:\Users\CS5\Pictures\3d wallpapers\Flappy Birds\Images12`3\OIP (1).jpg')
img2_=py.image.load(r'C:\Users\CS5\Pictures\3d wallpapers\Flappy Birds\Images\pumpkin_face_light_2.png')
img3_=py.image.load(r'C:\Users\CS5\Pictures\3d wallpapers\Flappy Birds\Images12`3\pipe-green-down.jpg')
img4_=py.image.load(r'C:\Users\CS5\Pictures\3d wallpapers\Flappy Birds\Images12`3\pipe-green-up.png')
#-------------------------------------------|Editing images|----------------------------------------------------------------------------
img2=py.transform.scale(img2_,(80,70))
img=py.transform.scale(img_,(x,y))
#--------------------------------------------|get_rect|--------------------------------------------------------------------------
img2_rect=img2_.get_rect(topleft=(200,y/2))
img_rect=img.get_rect(topleft=(0,0))
img_rect2=img.get_rect(topleft=(x,0))
up_rect=img3_.get_rect()
down_rect=img4_.get_rect()
win.blit(img,img_rect)
obs=False
var=-10
run=play=True
#--------------------------------------------|defining functions|---------------------------------------------------------------------------
def jump():
    global var,obs
    var=-10
    obs=True
def move(k):
    if k[py.K_UP]:jump()
    if k[py.K_SPACE]:pause()
    if k[py.K_p]:pilay()
def pause():
    global play
    if play==True:play=False
def pilay():
    global play
    if play==False:play=True
def infinite(a,bg_rect,bg_rect2):
    bg_rect.x-=3
    bg_rect2.x-=3
    if bg_rect.x<-a:bg_rect.x=a
    if bg_rect2.x<-a:bg_rect2.x=a
clock=py.time.Clock()
#-----------------------------------------------|main loop|-----------------------------------------------------------
while run:
    clock.tick(45)
    for i in py.event.get():
        if i.type==py.QUIT:
            run=False
    if play:
        win.blit(img,img_rect)
        win.blit(img,img_rect2)
        win.blit(img2,img2_rect)
        infinite(x,img_rect,img_rect2)
        if obs:
            img2_rect.y+=(2*var+1)//2
            var+=1
    key_pressed=py.key.get_pressed()
    move(key_pressed)
    py.display.update()
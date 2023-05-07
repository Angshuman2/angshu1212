"""animation from download.png"""

import pygame
pygame.init()
screen_w,screen_h=600,400
window=pygame.display.set_mode((screen_w,screen_h))
run=1
bg=(100,100,100)
image=pygame.image.load("download.png")
def sheet(img,wd,hg,fr,fr1):
    imag=pygame.Surface((wd,hg),pygame.SRCALPHA,32).convert_alpha()
    imag.blit(img,(10,10),(fr,fr1,wd,hg))
    imag=pygame.transform.rotate(imag,(45))
    imag=pygame.transform.scale(imag,(100,100))
    return imag
frame=[]
frame.append(sheet(image,60,70,25,10))
frame.append(sheet(image,60,70,25,75))
frame.append(sheet(image,60,70,90,75))
frame.append(sheet(image,60,70,90,10))
frame.append(sheet(image,60,70,150,10))
frame.append(sheet(image,60,70,150,75))
frame.append(sheet(image,60,70,215,75))
frame.append(sheet(image,60,70,215,10))
frame.append(sheet(image,60,70,275,10))
frame.append(sheet(image,60,70,275,75))
cl=pygame.time.Clock()
i=0
while run:
    window.fill(bg)
    window.blit(frame[i],(150,50))
    i+=1
    if i==len(frame)-1:
        i=0
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=0
    pygame.display.update()
    cl.tick(30)
pygame.quit()
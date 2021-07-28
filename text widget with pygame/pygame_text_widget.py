# modules
import pygame,time
from pygame.locals import *
# initialize all imported pygame modules
pygame.init()
# variable
height,width=200,500
window=pygame.display.set_mode((width,height)) # main window
pygame.display.set_caption("Typing widget")  # name of widget
run=True
txt=""
green_yellow=(157,255,50) # RGB colour
black=(0,0,0)
red=(255,0,0)
text_height,text_width=10,10
dict_value=0
cursor_var,cursor_time,cursor=0,0,0
dict_txt={dict_value:[text_height,txt]}
starting_time=time.time()
next_line,previous_line=0,0
# function of text 
def main_text(text,size,colour,x,y,text_type,bold,italic):
    font=pygame.font.SysFont(text_type,size,bold,italic)
    show_font=font.render(text,True,colour)
    window.blit(show_font,(x,y))
    return show_font.get_width()
# pygame loop
while run:
    txt=dict_txt[dict_value][1]
    window.fill(green_yellow)
    # cursor blink
    if round(time.time()-starting_time,1)<=0.5:
        cursor_time=1
    else:
        cursor_time=0
        if round(time.time()-starting_time,1)>=1.0:
            starting_time=time.time()
    # pygame events
    for event in pygame.event.get():
        if event.type==QUIT:
            run=False
        if event.type==KEYDOWN:
            if event.key==K_BACKSPACE:
                txt=txt[:-1]
                if len(dict_txt[dict_value][1])==0 and dict_value>=1:  # previous line
                    dict_txt.pop(dict_value)
                    text_height-=25
                    dict_value-=1
                    txt=dict_txt[dict_value][1]
                    previous_line=1
            elif event.key==K_RETURN:
                next_line=1
            else:
                if cursor<=(width-25):
                    txt+=event.unicode # join text with entered keys
                previous_line=0
    # dict... of text
    dict_txt[dict_value][1]=txt 
    # write text in widget
    for i in dict_txt.keys():
        cursor_var+=1
        cursor=main_text(dict_txt.get(i)[1],20,red,text_width,dict_txt.get(i)[0],"times",True,False)
        if cursor_var==len(list(dict_txt.keys())) and cursor_time:
            main_text("|",20,black,text_width+cursor,text_height,"helvetica",False,False)
    # next line
    if cursor>(width-25) and previous_line==0:
        next_line=1
    if next_line==1 and text_height<height-40:  
        text_height+=25
        dict_value+=1
        txt=""
        dict_txt[dict_value]=[text_height,txt]
        next_line=0
    cursor_var=0
    # update window
    pygame.display.update()









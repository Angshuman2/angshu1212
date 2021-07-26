import pygame
from pygame.locals import *
import random,os,json,time,sys
pygame.init() # initialize all library of pygame
pygame.mixer.init() # initialize all mixer library
# highest score
write_highest_score={"1st":["Empty",0],"2nd":["Empty",0],"3rd":["Empty",0]}
def write_open_file(name_file,write_f):
    with open(name_file,"w") as h_score:
        h_score.write(json.dumps(write_f))
if os.path.exists(os.getcwd()+"\\snake_game_highest.json")==0:    # if no such file in directory
    write_open_file("snake_game_highest.json",write_highest_score)
def open_json_file():
    with open("snake_game_highest.json","r") as h_score:
        highest_score1=json.load(h_score)
        return highest_score1    
highest_score_list=["1st","2nd","3rd"]
# os path for picture and music
pic=os.getcwd()+"\\pic"
music=os.getcwd()+"\\music\\"
# upload picture
intro_pic=pygame.image.load(pic+"\\intro.jpg")
background=pygame.image.load(pic+"\\background.jpg")
apple=pygame.image.load(pic+"\\apple.png")
star_p=pygame.image.load(pic+"\\star.png")
body=pygame.image.load(pic+"\\body.png")
snk_down=pygame.image.load(pic+"\\headdown.png")
snk_right=pygame.image.load(pic+"\\headright.png")
snk_left=pygame.image.load(pic+"\\headleft.png")
snk_up=pygame.image.load(pic+"\\headup.png")
arrow=pygame.image.load(pic+"\\arrow.png")
finish_pic=pygame.image.load(pic+"\\finish.jpg")
tailup=pygame.image.load(pic+"\\tailup.png")
taildown=pygame.image.load(pic+"\\taildown.png")
tailright=pygame.image.load(pic+"\\tailright.png")
tailleft=pygame.image.load(pic+"\\tailleft.png")
multiply_pic=pygame.image.load(pic+"\\multiply.png")
explode_pic=pygame.image.load(pic+"\\explode.png")
bomb_pic=pygame.image.load(pic+"\\bomb.png")
clock_pic=pygame.image.load(pic+"\\clock.png")
border_pic=pygame.image.load(pic+"\\border.jpg")
messagebox_pic=pygame.image.load(pic+"\\messagebox.jpg")
yesno_pic=pygame.image.load(pic+"\\yes_no.png")
option_pic=pygame.image.load(pic+"\\option.png")
left_arrow_black_pic=pygame.image.load(pic+"\\left side arrow black.png")
left_arrow_yellow_pic=pygame.image.load(pic+"\\left side arrow yellow.png")
right_arrow_yellow_pic=pygame.image.load(pic+"\\right side arrow yellow.png")
right_arrow_black_pic=pygame.image.load(pic+"\\right side arrow black.png")
key_up_pic=pygame.image.load(pic+"\\key up.png")
key_left_pic=pygame.image.load(pic+"\\key right.png")
key_down_pic=pygame.image.load(pic+"\\key down.png")
key_right_pic=pygame.image.load(pic+"\\key left.png")
play_pic=pygame.image.load(pic+"\\play.png")
# game window height and width
window_height=400
window_width=800
window=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Snake Game")
# rgb color that use
orange=(255,102,0)
hexx=(32,16,48)
blue_black=(0,0,43)
black=(0,0,0)
white=(255,255,255)
light_blue=(10,50,120)
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)
green_yellow=(157,255,50)
dark_yellow=(155,181,60)
magneta=(160,2,92)
pink=(255,0,255)
grey=(194,197,204)
sky=(205,240,255)
clock_fps=pygame.time.Clock()
text_y=20
# dict for music
# helps to change the music
music_dict={1:"music1",2:"music2",3:"music3",4:"music4",5:"off"}
var_music2=1
# function for music
# supported only wav file
def music_play(name):
    mus=pygame.mixer.Sound(name)
    pygame.mixer.Channel(1).play(mus)
# identify rank and name in game window (it appear when game paused)
def rank(s,dict_s):
    for key,value in dict_s.items():
        if s==value[1]:
            xx=key
            xxx=value[0]
    return xx,xxx
# function that identfy the rank and name after game over and shows your rank in game window
def save_score_file(a,dic):
    for key,value in dic.items():
        if a>value[1]:
            save_pos=key
            break
    return save_pos
# function for text
def text(txt,color,x,y,siz,txt_n,bold,italica,cursor=0):
    font=pygame.font.SysFont(txt_n,siz,bold,italica)
    screen_txt=font.render(txt,True,color)
    window.blit(screen_txt,(x,y))
    if cursor==1:
        return screen_txt.get_width()
# plot snake
def plot_snake(lst,snhead):
    len_snake=len(lst)
    tp=5
    if len_snake>2:
        if abs(lst[1][0]-lst[2][0])!=0:
            tp=abs(lst[1][0]-lst[2][0])
        elif abs(lst[1][1]-lst[2][1])!=0:
            tp=abs(lst[1][1]-lst[2][1])
    # for body
    for x in lst[1:len_snake-1]:
        window.blit(body,(x[0],x[1]))
    # for head
    if snhead=="right":
        window.blit(snk_right,(lst[len_snake-1][0]-2,lst[len_snake-1][1]-5))
    elif snhead=="left":
        window.blit(snk_left,(lst[len_snake-1][0]-8,lst[len_snake-1][1]-5))
    elif snhead=="up":
        window.blit(snk_up,(lst[len_snake-1][0]-5,lst[len_snake-1][1]-8))
    else:
        window.blit(snk_down,(lst[len_snake-1][0]-5,lst[len_snake-1][1]-2))
    # for tail
    if lst[0][1]-lst[1][1]==tp:
        window.blit(tailup,(lst[0][0],lst[0][1]-2))
    elif lst[1][1]-lst[0][1]==tp:
        window.blit(taildown,(lst[0][0],lst[0][1]+2))
    elif lst[1][0]-lst[0][0]==tp:
        window.blit(tailright,(lst[0][0]+2,lst[0][1]))
    elif lst[0][0]-lst[1][0]==tp:
        window.blit(tailleft,(lst[0][0]-2,lst[0][1]))
# function for plot objects
def plot_things(width,height):
    x=random.randint(30,width-30)
    y=random.randint(30,height-60)
    return x,y
# main game loop
def game_loop():
    # variable that use for game
    highest_score=open_json_file()
    highest_score_clone=open_json_file()
    keys={K_RIGHT:[5,0,"right",5,0],K_LEFT:[-5,0,"left",-5,0],K_UP:[0,-5,"up",0,-5],K_DOWN:[0,5,"down",0,5]}
    false_x=0
    false_y=0
    bonas_tm=0
    bonas_tm_counter=1
    main_bonas_tm=0
    bonas=0
    bonas_false=0
    bonas_counter=1
    bonas_pause_tm=0
    bonas_pause_tm_counter=0
    less_size_tm=0
    less_size_tm_counter=1
    main_less_size_tm=0
    less_size=0
    less_size_false=0
    less_size_counter=1
    less_size_pause_tm=0
    less_size_pause_tm_counter=0
    clock_tm=0
    clock_tm_counter=1
    main_clock_tm=0
    clock=0
    clock_false=0
    clock_counter=1
    clock_pause_tm=0
    clock_pause_tm_counter=0
    menu=155
    intro_val=1
    snk_head="right"
    check=1
    speed=1
    game_over=False
    run=True
    main_x=window_width/2
    false_main_x=window_width/2
    main_y=window_height/2
    false_main_y=window_height/2
    fps=30
    score=0
    movement_x=0
    movement_y=0
    snk_size=3
    snk_list=[[main_x-5,main_y],[main_x,main_y]] # main snake list
    false_snk_list=[[main_x-5,main_y],[main_x,main_y]] # fake snake list that helps to game over after touch with another part of sanke
    food_x,food_y=plot_things(window_width,window_height)
    food_a,food_b=plot_things(window_width,window_height)
    food_n,food_m=plot_things(window_width,window_height)
    food_c,food_d=plot_things(window_width,window_height)
    pause=False
    apple_cnt=0
    star_cnt=0
    bomb_cnt=0
    clock_cnt=0
    explode_display=0
    game_over_tm=0
    main_game_tm=0
    main_game_tm_counter=0
    game_tm_counter=0
    game_tm_counter2=0
    display_tm_hr=2
    display_tm_min=00
    i,d=1,0
    poss_N=0
    poss_Y=0
    show_save_widget,show_mouse_text_save=0,0
    write_text=""
    save_score_file3,save_score_file4,te,cursor_tm,cursor_tm1=0,0,0,0,0
    not_save,not_save1,not_save2,not_save3,not_save4=0,0,0,1,0
    option_val=1
    rr=1
    cs1,cs2,cs3,cs4=1,1,1,1
    var_music=1
    timer_music_var=1
    # global var to keep the music same in every game loop
    global var_music2
    # while true
    while run:
        # music (it supports mp3 sound too)
        if var_music2<5:
            if var_music:
                pygame.mixer.music.load(music+music_dict.get(var_music2)+".mp3")
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play(-1)
                var_music=0
        else:
            pygame.mixer.music.stop()
        # show highest score in game
        if intro_val==3:
            pygame.mouse.set_visible(1)
            window.fill(grey)
            window.blit(border_pic,(200,0))
            text("Highest Score :-",red,250,55,20,"times",1,1)
            text("______________________",blue_black,245,60,20,"times",1,1)
            text("______________________",green,255,65,20,"times",1,1)
            text("______________________",orange,265,70,20,"times",1,1)
            text("1st...-> ",black,250,130,15,"Times",1,1)
            text("2nd...-> ",black,280,180,15,"Times",1,1)
            text("3rd...-> ",black,310,230,15,"Times",1,1)
            text(highest_score.get("1st")[0],hexx,310,128,20,"times",0,1)
            text(highest_score.get("2nd")[0],hexx,340,177,20,"times",0,1)
            text(highest_score.get("3rd")[0],hexx,370,226,20,"times",0,1)
            if highest_score.get("1st")[0]!="Empty" and highest_score.get("1st")[1]!=0:
                text(str(highest_score.get("1st")[1]),dark_yellow,430,128,20,"times",1,1)
            if highest_score.get("2nd")[0]!="Empty" and highest_score.get("2nd")[1]!=0:
                text(str(highest_score.get("2nd")[1]),dark_yellow,460,178,20,"times",1,1)
            if highest_score.get("3rd")[0]!="Empty" and highest_score.get("3rd")[1]!=0:
                text(str(highest_score.get("3rd")[1]),dark_yellow,490,227,20,"times",1,1)
            text("<< Back...",red,450,320,20,"times",1,1)
            poss=pygame.mouse.get_pos()
            click_a=pygame.mouse.get_pressed()
            # mouse position for back
            if (poss[0]<=523 and poss[0]>=450) and (poss[1]>=323 and poss[1]<=337) and click_a[0]==1:
                music_play(music+"select option.wav")
                intro_val=1
            # event loop
            for event in pygame.event.get():
                if event.type==QUIT:
                    run=False
                    sys.exit()
                if event.type==KEYDOWN:
                    if event.key==K_BACKSPACE:
                        music_play(music+"select option.wav")
                        intro_val=1
            pygame.display.update()
        # play game 
        elif intro_val==2:
            # if pause
            if pause==True:
                pygame.mouse.set_visible(1)
                # mouse position use for backspace after game started
                poss_Y,poss_N=pygame.mouse.get_pos()
                click_c=pygame.mouse.get_pressed()
                # if press yes 
                if poss_Y>=390 and poss_Y<=445 and poss_N>=262 and poss_N<=292 and click_c[0]==1:
                    music_play(music+"select option.wav")
                    game_loop()
                # if press no
                elif poss_Y>=445 and poss_Y<=490 and poss_N>=262 and poss_N<=292 and click_c[0]==1:
                    music_play(music+"select option.wav")
                    d=0
                    pause=False
                # time stopped if game paused
                if check==2: # main time
                    game_tm_counter=(time.time()-main_game_tm_counter)+game_tm_counter2
                if bonas_tm_counter==2: # star time
                    bonas_pause_tm=time.time()-bonas_pause_tm_counter
                if less_size_tm_counter==2: # bomb time
                    less_size_pause_tm=time.time()-less_size_pause_tm_counter
                if clock_tm_counter==2: # clock time
                    clock_pause_tm=time.time()-clock_pause_tm_counter
                # explode snake head if game over
                if explode_display==1:
                    window.blit(explode_pic,(main_x-20,main_y-10))
                    pygame.draw.rect(window,green_yellow,[280,0,600,text_y])
                    # need 3 seconds to go next after game over
                    if (time.time()-game_over_tm)>=3:
                        pause=False
                        game_over=True
                # if not game over but paused 
                else:
                    text("PAUSED...",white,350,320,30,"times",False,True)
                    pygame.draw.rect(window,green_yellow,[280,0,600,text_y])
                    text("Press  'S'  to start the game....",red,280,0,15,"times",False,True)
                # show highest score that you have to beat in game window after paused
                show_highest_score_list=[]
                for aa in highest_score_list:
                    if score<=highest_score.get(aa)[1] and highest_score.get(aa)[0]!="Empty" and highest_score.get(aa)[1]!=0:
                        show_highest_score_list.append(highest_score.get(aa)[1])
                if len(show_highest_score_list)==0:
                    if score>0:
                        text("You are in 1st position, score : "+str(score),magneta,550,0,15,"times",True,True)
                else:
                    highest_score_shown=min(show_highest_score_list)
                    rank_highest_score,name_highest_score=rank(highest_score_shown,highest_score)
                    text(rank_highest_score+" position ( "+name_highest_score+") :-  "+str(highest_score_shown),magneta,550,0,15,"times",True,True)
                # event loop
                for event in pygame.event.get():
                    if event.type==QUIT:
                        run=False
                        sys.exit()
                    if event.type==KEYDOWN:
                        if event.key==K_s and d==0: # if paused start after click on S 
                            pause=False
                pygame.display.update()
            elif game_over==True:
                pygame.mouse.set_visible(1)
                window.blit(finish_pic,(0,0))
                # check wheather your score in position or not
                if (score>highest_score.get("1st")[1] or score>highest_score.get("2nd")[1] or score>highest_score.get("3rd")[1]) and not_save3:
                    not_save1=1
                    not_save=1
                    not_save3=0
                # color that need to see error when writing name
                blue_red1=(0,0,255)
                blue_red2=(0,0,255)
                for event in pygame.event.get():
                    if event.type==QUIT:
                        run=False
                        sys.exit()
                    if event.type==KEYDOWN:
                        if event.key==K_RETURN:
                            if not_save!=1: # if you are not in position go directly to main loop
                                music_play(music+"select option.wav")
                                game_loop()
                            else: # if you are in position pop up message
                                music_play(music+"error.wav")
                                not_save4=1
                                not_save2=1
                                not_save1=0
                        elif event.key==K_BACKSPACE: # delete last letter
                            write_text=write_text[:-1]
                        else:
                            if event.key>=97 and event.key<=122 and show_mouse_text_save==1: # ASCII code to (you can enter only letters)
                                if len(write_text)<=9 and not_save1: # length of text within 2 to 10
                                    write_text+=event.unicode
                                else: # else error popup with sound
                                    music_play(music+"error.wav")
                                    blue_red2=(255,0,0)
                            else: # if number error popup with sound
                                music_play(music+"error.wav")
                                blue_red1=(255,0,0)
                if not_save4==0:
                    text("Game Over.......",red,300,140,30,"times",False,True)
                    text("You have scored "+str(score),black,300,175,20,"times",False,True)
                    text(("Press 'Enter' to go main menu.."), blue, 300, 200, 20,"times",False,True)
                    if not_save1: # if in position
                        if save_score_file3==0:
                            save_score_file2=save_score_file(score,highest_score)
                            save_score_file3=1
                        if save_score_file4==0:
                            if score>highest_score.get("3rd")[1]:
                                if score>highest_score.get("2nd")[1]:
                                    if score>highest_score.get("1st")[1]:
                                        text("You are in 1st position,,,",black,300,250,25,"times",1,1)
                                    else:
                                        text("You are in 2nd position,,,",black,300,250,25,"times",1,1)
                                else:
                                    text("You are in 3rd position,,,",black,300,250,25,"times",1,1)
                            if not show_save_widget: # before click in here
                                pygame.draw.rect(window,orange,[363,282,80,30])
                                pygame.draw.rect(window,blue,[362,281,81,31],1)
                            text("Click                to save your score",black,300,280,25,"times",1,1) 
                            text(" here ",black,372,280,25,"times",1,1)
                            save_mouse_pos=pygame.mouse.get_pos()
                            save_click_mouse=pygame.mouse.get_pressed()
                            if save_mouse_pos[0]>=360 and save_mouse_pos[0]<=440 and save_mouse_pos[1]>=281 and save_mouse_pos[1]<=311:
                                if not show_save_widget:
                                    pygame.draw.rect(window,grey,[363,282,80,30])
                                    text(" here ",red,372,280,25,"times",1,0) # change here text
                                    if save_click_mouse[0]==1:
                                        music_play(music+"select option.wav")
                                        show_save_widget=1
                    if save_score_file4==0:
                        if show_save_widget==1: # after click here
                            if cursor_tm1==0: # cursor time for blink
                                cursor_tm=time.time()
                                cursor_tm1=1
                            show_mouse_text_save=1 
                            show_mouse_save_text=pygame.mouse.get_pressed()
                            show_mouse_save_pos=pygame.mouse.get_pos()
                            if show_mouse_save_pos[0]>=502 and show_mouse_save_pos[1]>=330 and show_mouse_save_pos[0]<=540 and show_mouse_save_pos[1]<=342 and show_mouse_save_text[0]==1:  
                                if len(write_text)>=2: # save game score
                                    if save_score_file2!="3rd":
                                        for sav in highest_score_list[highest_score_list.index(save_score_file2)+1:]:
                                            highest_score_clone[sav][0]=highest_score[highest_score_list[highest_score_list.index(sav)-1]][0]
                                            highest_score_clone[sav][1]=highest_score[highest_score_list[highest_score_list.index(sav)-1]][1]
                                    highest_score_clone[save_score_file2][0]=write_text.title() 
                                    highest_score_clone[save_score_file2][1]=score
                                    highest_score=highest_score_clone
                                    music_play(music+"select option.wav")
                                    write_open_file("snake_game_highest.json",highest_score)
                                    save_score_file4=1
                                    show_mouse_text_save=0
                                    cursor_tm1=0
                                    not_save=0
                                    not_save1=0
                                else: # error popup with sound if text less then 2
                                    music_play(music+"error.wav")
                                    blue_red2=(255,0,0)
                            # enter name box
                            text("Enter name :- ",black,160,325,20,"times",1,1)
                            pygame.draw.rect(window,sky,[300,325,175,25])
                            text("Save...",red,500,325,20,"times",1,1)
                            text("1.Use only letters.",blue_red1,300,355,13,"helvetica",0,0)
                            text("2.Use minimum 2 charecters and maxium 10 characters",blue_red2,300,375,15,"times",0,0) 
                        te=text(write_text,blue_black,302,324,20,"monospace",1,1,1)
                    if show_mouse_text_save==1:
                        cursor_tm2=round(time.time()-cursor_tm,1)
                        if cursor_tm2<=0.5: # blink cursor
                            text("|",black,302+te,323,20,"helvetica",0,0)
                        else:
                            if cursor_tm2>=1:
                                cursor_tm1=0
                if not_save2==1: # error popup if not saved
                    window.blit(messagebox_pic,(200,100))
                    window.blit(yesno_pic,(340,230))
                    text("You did not save the score,,,",black,280,120,18,"times",1,1)
                    text("Wanted to go main menu,,,",black,310,150,18,"times",1,1)
                    text("You will loss the progress,,,",black,340,180,18,"times",1,1)
                    poss_Mx,poss_My=pygame.mouse.get_pos()
                    click_MM=pygame.mouse.get_pressed()
                    if poss_Mx>=390 and poss_Mx<=445 and poss_My>=262 and poss_My<=292 and click_MM[0]==1:
                        music_play(music+"select option.wav")
                        game_loop()
                    elif poss_Mx>=445 and poss_Mx<=490 and poss_My>=262 and poss_My<=292 and click_MM[0]==1:
                        music_play(music+"select option.wav")
                        not_save2=0
                        not_save4=0
                        not_save1=1
                pygame.display.update()
            else: # game window
                pygame.mouse.set_visible(0)
                window.blit(background,(0,0))
                plot_snake(snk_list,snk_head) # plot snake
                window.blit(apple,(food_x,food_y))
                for event in pygame.event.get():
                    if event.type==QUIT:
                        run=False
                        sys.exit()
                    if event.type==KEYDOWN:
                        if event.key==K_p: # p for pause
                            pause=True
                        elif event.key==K_BACKSPACE:
                            if check!=1: # if started game after press backspace
                                music_play(music+"error.wav")
                                pause=True
                                d=1
                                window.blit(messagebox_pic,(200,100))
                                window.blit(yesno_pic,(340,230))
                                text("You started the game,,,",black,300,140,18,"times",1,1)
                                text("Going back,,,",black,330,170,18,"times",1,1)
                                text("You will loss the progress,,,",black,360,200,18,"times",1,1)
                            else: # if not started
                                music_play(music+"select option.wav")
                                game_loop()
                        elif event.key in keys:
                            if check==1: # time start for game (only for first time it can enter)
                                main_game_tm=time.time()
                            check=2
                            movement_x=keys[event.key][0]
                            movement_y=keys[event.key][1]
                            false_x=keys[event.key][3]
                            false_y=keys[event.key][4]
                            snk_head=keys[event.key][2]
                if abs(main_x-food_x)<15 and abs(main_y-food_y)<15: # if eat a apple
                    music_play(music+"apple.wav")
                    apple_cnt+=1
                    score+=10
                    keys[K_RIGHT][0]+=0.2
                    keys[K_LEFT][0]-=0.2
                    keys[K_UP][1]-=0.2
                    keys[K_DOWN][1]+=0.2
                    speed+=1
                    snk_size+=1
                    food_x,food_y=plot_things(window_width,window_height)
                    if bonas_counter==1:
                        bonas+=bonas_false
                        bonas+=10
                        bonas_false=0
                    else:
                        bonas_false+=10
                    if less_size_counter==1:
                        less_size+=less_size_false
                        less_size+=10
                        less_size_false=0
                    else:
                        less_size_false+=10
                    if clock_counter==1:
                        clock+=clock_false
                        clock+=10
                        clock_false=0
                    else:
                        clock_false+=10
                if bonas==70: # plot star
                    bonas_counter=2
                    bonas_tm+=1
                    window.blit(star_p,(food_a,food_b))
                    if bonas_tm_counter==1:
                        main_bonas_tm=time.time()
                        bonas_tm_counter=2
                    if bonas_tm_counter==2:
                        bonas_tm=(time.time()-main_bonas_tm)-bonas_pause_tm
                        bonas_pause_tm_counter=time.time()
                    if bonas_tm>=3: # time for visible star
                        bonas_pause_tm=0
                        bonas_counter=1
                        bonas_tm_counter=1
                        bonas_tm=0
                        bonas=0
                        food_a,food_b=plot_things(window_width,window_height)
                    if abs(main_x-food_a)<20 and abs(main_y-food_b)<20: # after eat a star
                        music_play(music+"star.wav")
                        star_cnt+=1
                        bonas_counter=1
                        bonas_tm_counter=1
                        bonas=0
                        bonas_tm=0
                        score+=10
                        food_a,food_b=plot_things(window_width,window_height)
                if less_size==100: # plot bomb
                    less_size_counter=2
                    less_size_tm+=1
                    window.blit(bomb_pic,(food_n,food_m))
                    if less_size_tm_counter==1:
                        main_less_size_tm=time.time()
                        less_size_tm_counter=2
                    if less_size_tm_counter==2:
                        less_size_tm=(time.time()-main_less_size_tm)-less_size_pause_tm
                        less_size_pause_tm_counter=time.time()
                    if less_size_tm>=3: # time for visible bomb
                        less_size_pause_tm=0
                        less_size_counter=1
                        less_size_tm_counter=1
                        less_size_tm=0
                        less_size=0
                        food_n,food_m=plot_things(window_width,window_height)
                    if abs(main_x-food_n)<20 and abs(main_y-food_m)<20: # after eat a bomb
                        music_play(music+"small.wav")
                        bomb_cnt+=1
                        less_size_counter=1
                        less_size_tm_counter=1
                        less_size=0
                        less_size_tm=0
                        for aa in range(5): # snake size decrease
                            del snk_list[aa]
                            del false_snk_list[aa]
                        snk_size-=5
                        food_n,food_m=plot_things(window_width,window_height)
                if clock==150: # plot clock
                    clock_counter=2
                    clock_tm+=1
                    window.blit(clock_pic,(food_c,food_d))
                    if clock_tm_counter==1:
                        main_clock_tm=time.time()
                        clock_tm_counter=2
                    if clock_tm_counter==2:
                        clock_tm=(time.time()-main_clock_tm)-clock_pause_tm
                        clock_pause_tm_counter=time.time()
                    if clock_tm>=3: # time for clock
                        clock_pause_tm=0
                        clock_counter=1
                        clock_tm_counter=1
                        clock_tm=0
                        clock=0
                        food_c,food_d=plot_things(window_width,window_height)
                    if abs(main_x-food_c)<20 and abs(main_y-food_d)<20: # after eat a clock
                        music_play(music+"time.wav")
                        clock_cnt+=1
                        clock_counter=1
                        clock_tm_counter=1
                        clock=0
                        clock_tm=0
                        # increase time
                        display_tm_min+=15
                        if display_tm_min>=60: 
                            display_tm_hr+=1
                            display_tm_min-=60
                        food_c,food_d=plot_things(window_width,window_height)
                # show some objects in main game window
                pygame.draw.rect(window,green_yellow,[0,0,800,text_y])
                pygame.draw.rect(window,green_yellow,[0,375,800,text_y+5])
                text("Score = "+str(score),blue,10,0,15,"times",False,True)
                text("Speed = "+str(speed),black,720,0,15,"times",False,True)
                text("Press  'P'  to pause the game....",red,280,0,15,"times",False,True)
                window.blit(apple,(5,376))
                window.blit(multiply_pic,(28,378))
                text(str(apple_cnt),black,55,375,20,"helvetica",True,False)
                window.blit(star_p,(100,376))
                window.blit(multiply_pic,(130,378))
                text(str(star_cnt),black,160,375,20,"helvetica",True,False)
                window.blit(bomb_pic,(220,376))
                window.blit(multiply_pic,(250,378))
                text(str(bomb_cnt),black,285,375,20,"helvetica",True,False)
                window.blit(clock_pic,(325,376))
                window.blit(multiply_pic,(365,378))
                text(str(clock_cnt),black,400,375,20,"helvetica",True,False)
                text("Time Remain :- ",blue_black,570,375,20,"Times",False,True)
                if len(str(display_tm_min))==1:
                    pygame.draw.rect(window,green_yellow,[700,375,800,text_y+5])
                    text(str(display_tm_hr)+":0"+str(display_tm_min),black,720,375,20,"Times",True,True)    
                else:
                    pygame.draw.rect(window,green_yellow,[700,375,800,text_y+5])
                    text(str(display_tm_hr)+":"+str(display_tm_min),black,720,375,20,"Times",True,True)
                # if time over
                if display_tm_hr==0 and display_tm_min==0:
                    pygame.mixer.music.stop()
                    music_play(music+"game over.wav")
                    game_over_tm=time.time()
                    explode_display=1
                    pause=True
                # if only 5 seconds more    
                if display_tm_hr==0 and display_tm_min<5 and display_tm_min>0 and timer_music_var:
                    timer_music=pygame.mixer.Sound(music+"timer.wav")
                    pygame.mixer.Channel(0).play(timer_music)
                    timer_music_var=0
                # time for game
                main_game_tm_counter=time.time()
                game_tm=time.time()-(main_game_tm+game_tm_counter)
                game_tm_counter2=game_tm_counter
                if int(game_tm)==i:
                    i+=1
                    if display_tm_min==0:
                        display_tm_hr-=1
                        display_tm_min=60
                    display_tm_min-=1
                    timer_music_var=1
                    if display_tm_hr==-1:
                        display_tm_min=0
                # snake 
                main_x+=movement_x
                main_y+=movement_y
                false_main_x+=false_x
                false_main_y+=false_y
                false_head=[]
                head=[]
                head.append(main_x)
                head.append(main_y)
                false_head.append(false_main_x)
                false_head.append(false_main_y)
                if check==1:
                    snk_list.insert(0,head)
                    false_snk_list.insert(0,false_head)
                else:
                    snk_list.append(head)
                    false_snk_list.append(false_head)
                if len(snk_list)>=snk_size:
                    del snk_list[0]
                    del false_snk_list[0]
                if check!=1: # if game over
                    if (int(main_x)>=window_width-10) or (int(main_x)<=0) or (int(main_y)>=window_height-(text_y+15)) or (int(main_y)<=text_y) or false_head in false_snk_list[:-1]:
                        pygame.mixer.music.stop()
                        music_play(music+"game over.wav")
                        game_over_tm=time.time()
                        explode_display=1
                        pause=True
                clock_fps.tick(fps) # fps
                pygame.display.update()
        elif intro_val==4: # game instruction window
            window.fill(sky)
            window.blit(option_pic,(100,15))
            text("<< Back...",red,700,360,20,"times",1,1)
            poss_o=pygame.mouse.get_pos()
            click_o=pygame.mouse.get_pressed()
            if (poss_o[0]<=774 and poss_o[0]>=701) and (poss_o[1]>=364 and poss_o[1]<=377) and click_o[0]==1: # for back
                music_play(music+"select option.wav")
                intro_val=1
            for event in pygame.event.get():
                if event.type==QUIT:
                    run=False
                    sys.exit()
                if event.type==KEYDOWN:
                    if event.key==K_RIGHT and option_val<3:
                        music_play(music+"select option.wav")
                        option_val+=1
                        pass
                    elif event.key==K_LEFT and option_val>1:
                        music_play(music+"select option.wav")
                        option_val-=1
                        pass
                    elif event.key==K_BACKSPACE:
                        music_play(music+"select option.wav")
                        intro_val=1
            if option_val==1: # first page
                r1=(220,20,60)
                r2=(34,139,34)
                r3=(34,139,34)
                text("movement".upper(),magneta,330,45,25,"helvetica",1,1)
                text("__________",black,325,50,25,"times",1,0)
                window.blit(right_arrow_yellow_pic,(650,170))
                window.blit(right_arrow_black_pic,(670,170))
                text("1. Press    to move up.",blue,200,110,18,"monospace",1,1)
                text("2. Press    to move right.",blue,200,146,18,"monospace",1,1)
                text("3. Press    to move down.",blue,200,182,18,"monospace",1,1)
                text("4. Press    to move left.",blue,200,218,18,"monospace",1,1)
                window.blit(key_up_pic,(250,108))
                window.blit(key_right_pic,(234,128))
                window.blit(key_down_pic,(250,148))
                window.blit(key_left_pic,(266,200))
                text("5. Press 'P' to pause the game.",blue,200,254,18,"monospace",1,1)
                text("6. Press 'S' to start the game.",blue,200,290,18,"monospace",1,1)
            elif option_val==2: # second page
                r2=(220,20,60)
                r1=(34,139,34)
                r3=(34,139,34)
                text("point".upper(),magneta,340,45,25,"helvetica",1,1)
                text("______",black,332,50,25,"times",1,0)
                window.blit(left_arrow_black_pic,(70,170))
                window.blit(left_arrow_yellow_pic,(90,170))
                window.blit(right_arrow_yellow_pic,(650,170))
                window.blit(right_arrow_black_pic,(670,170))
                text("1.  increase 10 points and speed.",blue,200,110,18,"monospace",1,1)
                text("2.  increase 10 points but not speed.",blue,200,140,18,"monospace",1,1)
                text("(It will be visible after eating 7 apples)",hexx,245,155,15,"times",0,1)
                text("3.  decrease the length of snake.",blue,200,185,18,"monospace",1,1)
                text("(It will be visible after eating 10 apples)",hexx,245,200,15,"times",0,1)
                text("4.  gives 15 seconds extra.",blue,200,230,18,"monospace",1,1)
                text("(It will be visible after eating 15 apples)",hexx,245,245,15,"times",0,1)
                window.blit(apple,(220,108))
                window.blit(star_p,(220,138))
                window.blit(bomb_pic,(222,183))
                window.blit(clock_pic,(212,228))
                text("Note :",red,200,270,15,"times",1,1)
                text("______",black,197,273,15,"times",1,0)
                text("(Except apple other objects will stay for 3 seconds)",red,200,290,15,"times",0,1)
            elif option_val==3: # third page
                r3=(220,20,60)
                r2=(34,139,34)
                r1=(34,139,34)
                text("in game".upper(),magneta,330,45,25,"helvetica",1,1)
                text("________",black,325,50,25,"times",1,0)
                window.blit(left_arrow_black_pic,(70,170))
                window.blit(left_arrow_yellow_pic,(90,170))
                text("1. Total time 2 minutes.",blue,200,110,18,"monospace",1,1)
                text("2. Game over if touch the border.",blue,200,130,18,"monospace",1,1)
                text("3. Game over if touch the snake body.",blue,200,150,18,"monospace",1,1)
                text("Note :",red,200,200,15,"times",1,1)
                text("______",black,197,204,15,"times",1,0)
                text("If score is in the first three,",red,200,224,15,"times",0,1)
                text("you will get a option to save score.",red,200,244,15,"times",0,1)
            pygame.draw.circle(window,r1,(380,370),5)
            pygame.draw.circle(window,r2,(400,370),5)
            pygame.draw.circle(window,r3,(420,370),5)
            pygame.display.update()
        else: # option window
            pygame.mouse.set_visible(1)
            window.fill(green_yellow)
            pygame.draw.rect(window,dark_yellow,[45,5,700,391])
            window.blit(intro_pic,(90,13))
            pygame.draw.rect(window,blue,[498,48,80,23],1)
            window.blit(play_pic,(500,50))
            text("press 1 to change the music",orange,470,70,15,"times",0,0)
            text(music_dict.get(var_music2).upper(),blue,525,52,13,"times",0,0)
            text("Snake Game...",magneta,200,50,30,"times",False,True)
            text("______________",black,190,57,28,"times",False,True)
            text("Play",red,300,150,25,"times",False,True)
            text("Highest Score",pink,300,190,25,"Times",False,True)
            text("Instruction",orange,300,230,25,"Times",False,True)
            text("Quit",black,300,270,25,"Times",False,True)
            poss1_x,poss1_y=pygame.mouse.get_pos()
            click_b=pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type==QUIT:
                    run=False
                    sys.exit()
                if event.type==KEYDOWN:
                    pygame.mouse.set_pos(100,100)
                    if event.key==K_DOWN:
                        if menu<275:
                            music_play(music+"click.wav")
                            menu+=40
                    elif event.key==K_UP:
                        if menu>155:
                            music_play(music+"click.wav")
                            menu-=40
                    elif event.key==K_RETURN:
                        music_play(music+"select option.wav")
                        if menu==155:
                            intro_val=2
                        elif menu==275:
                            rr=0
                        elif menu==235:
                            intro_val=4
                        elif menu==195:
                            intro_val=3
                    elif event.key==K_1:
                        var_music2+=1
                        var_music=1
                        if var_music2>5:
                            var_music2=1
            if poss1_x>=303 and poss1_x<=349 and poss1_y>=155 and poss1_y<=173:
                cs2,cs3,cs4=1,1,1
                if cs1:
                    music_play(music+"click.wav")
                    cs1=0
                menu=155
                if click_b[0]==1:
                    music_play(music+"select option.wav")
                    intro_val=2
            elif poss1_x>=303 and poss1_x<=444 and poss1_y>=195 and poss1_y<=215:
                cs1,cs3,cs4=1,1,1
                if cs2:
                    music_play(music+"click.wav")
                    cs2=0
                menu=195
                if click_b[0]==1:
                    music_play(music+"select option.wav")
                    intro_val=3
            elif poss1_x>=303 and poss1_x<=419 and poss1_y>=238 and poss1_y<=255:
                cs1,cs2,cs4=1,1,1
                if cs3:
                    music_play(music+"click.wav")
                    cs3=0
                menu=235
                if click_b[0]==1:
                    music_play(music+"select option.wav")
                    intro_val=4
            elif poss1_x>=303 and poss1_x<=345 and poss1_y>=277 and poss1_y<=294:
                cs1,cs2,cs3=1,1,1
                if cs4:
                    music_play(music+"click.wav")
                    cs4=0
                menu=275
                if click_b[0]==1:
                    rr=0
            window.blit(arrow,(260,menu))
            pygame.display.update()
        if rr==0:
            run=False
            sys.exit()

game_loop()
pygame.quit()
quit()
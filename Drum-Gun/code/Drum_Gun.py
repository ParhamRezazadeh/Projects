# لودينگ بازي
def loading():
    white = (255,255,255)
    gray = (30,30,30)

    # کشيدن عکس
    disp.blit(Drum, ((w/100)*20,(h/100)*14))
    flag = False

    # فور يراي حساب زمان
    for time in range(740):

        # از اين بازه زماني تا اون يکي شکلي رو بکشه
        if time < 120:
            pygame.draw.rect(disp, (white),((w/100)*2,(h/1000)*933,(w/100)*96,(h/1000)*30))
            pygame.display.update()

            
        elif 120 < time < 240:
            pygame.draw.rect(disp, (gray),((w/1000)*22,(h/10000)*9382,(w/100)*2,(h/1000)*20))
            pygame.display.update()
            
            
        elif 240 < time < 300:
            pygame.draw.rect(disp, (gray),((w/1000)*22,(h/10000)*9382,(w/100)*20,(h/1000)*20))
            pygame.display.update()

        
        elif 300 < time < 500:
            pygame.draw.rect(disp, (gray),((w/1000)*22,(h/10000)*9382,(w/100)*35,(h/1000)*20))
            pygame.display.update()

        elif 500 < time < 620:
            pygame.draw.rect(disp, (gray),((w/1000)*22,(h/10000)*9382,(w/100)*55,(h/1000)*20))
            pygame.display.update()
            
        elif 620 < time < 740:
            pygame.draw.rect(disp, (gray),((w/1000)*22,(h/10000)*9382,(w/1000)*756,(h/1000)*20))
            pygame.display.update()
            
        pygame.display.update()
        # تنظيم سرعت
        # يعني 150 فريم بر ثانيه
        pygame.time.Clock().tick(150)

# sign in بازي
def signin(sign, Name):
    
    # اگر قبلا sign in نکرده
    if sign == '1':
        Name = ""
        # متغيير کليک کردن روي قسمتي براي نوشتن
        active = False
        disp.blit(welcome,(0,0))
        pygame.display.update()
        eror = ""
        xmouse = ymouse = 0
        # وايل براي تايپ اسم
        while sign == '1':  
            for event in pygame.event.get():
                # اگر با موس کليک کرد
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # مکان موس
                    (xmouse,ymouse) = event.pos

                # اگه دکمه اي را فشار داد
                if event.type == pygame.KEYDOWN:
                    # اگه روي قسمت براي نوشتن کليک کرده بود
                    if active == True:
                        # اگه دکمه اينتر را زد
                        if event.key == pygame.K_RETURN:
                            # اگه طول اسم بيشتر از 3 بود تموم بشه
                            if len(Name) > 3:
                                sign = 0
                            # اگه نبود ارور بنويسه
                            else:
                                eror = "Your name must be bigger than 3 characters !"

                        # اگه دکمه بک اسپيس رو فشار بده يکي از کلمه ها رو پاک کنه
                        elif event.key == pygame.K_BACKSPACE:
                            Name = Name[:-1]
                        # اگه اين دکمه ها نبود اونو به ليست اسم اضافه کنه
                        else:
                            if len(Name) < 9:
                                Name += event.unicode
                                

            # اگه کليک بين قسمت براي نوشتن اسم بود         
            if (w/1000)*292 < xmouse < (w/1000)*292 + (w/1000)*265 and (w/1000)*225 < ymouse < (w/1000)*225 + (w/1000)*45:
                active = True

            # اگه دکمه اوکي رو زد
            elif (w/1000)*557 < xmouse < (w/1000)*557 + (w/1000)*127 and (w/1000)*225 < ymouse < (w/1000)*225 + (w/1000)*45:

                # اگه بيشتر 3 بود بره بيرون
                if len(Name) > 3:
                    sign = 0

                # اگه نبود ارور بده
                else:
                    eror = "Your name must be bigger than 3 characters !"
                    hello = True

            # اگه جاي ديگري رو زد از قسمت نوشتن بيرون بره
            else:
                if xmouse != 0 and ymouse != 0:
                    active = False
                

            xmouse = ymouse = 0

            # تعريف فونت
            txt = font.render(Name, True, (0,0,0))
            txt2 = font2.render(eror, True, (30,30,30))

            # اگه روي قسمت نوشتن بزنه اينو بکشه
            if active == True:
                disp.blit(welcome,(0,0))

            # برعکس بالا
            elif active == False:
                disp.blit(welcome2,(0,0))

            # کشيدن
            disp.blit(txt, ((w/100)*31, (h/100)*42))
            disp.blit(txt2, ((w/1000)*10, (h/1000)*965))
            pygame.display.update()


        # نوشتن در فايل
        sign = 0
        file = open('../text/sign.txt', 'w')
        file.write(Name+'\n')
        file.write(str(sign)+'\n')
        file.close()
        print('Saving your name ...')
        pygame.display.update()
        time.sleep(0.5)
    return Name

def render ():
    global lenth, x_page, y_page
    for i in range(lenth[1]):
        for j in range(lenth[0]):
            if map2[i,j] == 0:
                disp.blit(Yello_Grass, (((w/1000)*j*36 + x_page), ((w/1000)*i*36 + y_page)))
            if map2[i,j] == 2:
                disp.blit(Green_Grass, (((w/1000)*j*36 + x_page), ((w/1000)*i*36 + y_page)))
            if map2[i,j] == 3:
                disp.blit(Box, (((w/1000)*j*36 + x_page), ((w/1000)*i*36 + y_page)))

def find():
    map1 = open("../text/map_array", "r")
    khat = map1.readline()
    lenth = khat.split()
    lenth[0], lenth[1] = int(lenth[0]), int(lenth[1])
    map2 = np.array([(1,)*lenth[0]]*lenth[1])
    i = 0
    j = 0
    for i in range(lenth[0]*lenth[1]):
        khat = map1.readline()
        j = i//lenth[0]
        map2[j, i%lenth[0]] = int(khat)
    map1.close()
    return map2, lenth

def event1(x_event, y_event):
    global flag_design
    # event - پیدا کردن تغییر ها و ایونت ها
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                flag_design = True
                s.send('close the game'.encode())
                print ('close the game')
            if event.key==pygame.K_UP:
                y_event=3
            if event.key==pygame.K_DOWN:
                y_event=-3
            if event.key==pygame.K_LEFT:
                x_event=3
            if event.key==pygame.K_RIGHT:
                x_event=-3
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                y_event=0
            if event.key==pygame.K_DOWN:
                y_event=0
            if event.key==pygame.K_LEFT:
                x_event=0
            if event.key==pygame.K_RIGHT:
                x_event=0

    return x_event, y_event

def client():
    global x_player, y_player, x_Enemy, y_Enemy, w, x_page, y_page
    pygame.draw.rect(disp, (255,255,255), (x_player, y_player, (w/1000)*36, (w/1000)*36))
    pygame.draw.rect(disp, (0,0,0), ((x_Enemy + x_page), (y_Enemy + y_page), (w/1000)*36, (w/1000)*36))
    

def updates(x_page, y_page):
    global w,h,lenth,x_event,y_event,x_player,y_player,map2, x_client, y_client
    
    for i in range(lenth[1]):
        for j in range(lenth[0]):
            if map2[i,j] == 3:
                for o in range(4):
                    if j*(round((w/1000)*36)) + x_page == x_player + round((w/1000)*36) - o and i*(round((w/1000)*36))+y_page < y_player < i*(round((w/1000)*36)) + round((w/1000)*54) + y_page :
                        if x_event == -3:
                            x_event = 0
                    if j*(round((w/1000)*36)) + round((w/1000)*36) + x_page == x_player - o and i*(round((w/1000)*36))+y_page < y_player < i*(round((w/1000)*36)) + round((w/1000)*54) + y_page :
                        if x_event == 3:
                            x_event = 0
                    if j*(round((w/1000)*36)) + x_page == x_player + round((w/1000)*36) - o and i*(round((w/1000)*36))+y_page < y_player + (round((w/1000)*36)) < i*(round((w/1000)*36)) + round((w/1000)*54) + y_page :
                        if x_event == -3:
                            x_event = 0
                    if j*(round((w/1000)*36)) + round((w/1000)*36) + x_page == x_player - o and i*(round((w/1000)*36))+y_page < y_player + (round((w/1000)*36)) < i*(round((w/1000)*36)) + round((w/1000)*54) + y_page :
                        if x_event == 3:
                            x_event = 0

                    if j*(round((w/1000)*36))+x_page < x_player < j*(round((w/1000)*36)) + round((w/1000)*36) + x_page and i*(round((w/1000)*36)) + round((w/1000)*54) + y_page == y_player - o :
                        if y_event == 3:
                            y_event = 0

                    if j*(round((w/1000)*36))+x_page < x_player < j*(round((w/1000)*36)) + round((w/1000)*36) + x_page and i*(round((w/1000)*36)) + y_page == y_player + round((w/1000)*36)  - o :
                        if y_event == -3:
                            y_event = 0

                    if j*(round((w/1000)*36))+x_page < x_player + (round((w/1000)*36)) < j*(round((w/1000)*36)) + round((w/1000)*36) + x_page and i*(round((w/1000)*36)) + round((w/1000)*54) + y_page == y_player - o :
                        if y_event == 3:
                            y_event = 0

                    if j*(round((w/1000)*36))+x_page < x_player + (round((w/1000)*36)) < j*(round((w/1000)*36)) + round((w/1000)*36) + x_page and i*(round((w/1000)*36)) + y_page == y_player + round((w/1000)*36)  - o :
                        if y_event == -3:
                            y_event = 0



    
    x_page += x_event
    y_page += y_event

    x_client = -x_page + x_player
    y_client = -y_page + y_player

    if x_page >= 0:
        x_page = -1
        if x_event == 3:
            x_player -= 3

    if x_page > -(w//2):
        if x_event == -3:
            if x_player < (w//2):
                x_player +=3
                x_page -= x_event

    if x_page <= -1*(w//1000)*36*(lenth[0]-14):
        x_page = -1*(w//1000)*36*(lenth[0]-14)+1
        if x_event == -3:
            x_player += 3

    if x_page <= -1*(w//1000)*36*(lenth[0]-14)+w//4+1:
        if x_event == 3:
            if x_player >= w//2:
                x_player -=3
                x_page -= x_event
        

    if y_page >= 0:
        y_page = -1
        if y_event == 3:
            y_player -= 3

    if y_page > -(h//2):
        if y_event == -3:
            if y_player < (h//2):
                y_player +=3
                y_page -= y_event


    if y_page <= -1*(w//1000)*36*(lenth[1]-5):
        y_page = -1*(w//1000)*36*(lenth[1]-5)+1
        if y_event == -3:
            y_player += 3

    if y_page <= -1*(w//1000)*36*(lenth[1]-5)+h//4+1:
        if y_event == 3:
            if y_player >= h//2:
                y_player -=3
                y_page -= y_event

    return x_page, y_page

#فانکشن دریافت اطلاعات از سرور بازی
    
def receive():
    # آوردن متغیر به فانکشن با دستور گلوبال (بدون نیاز به گرفتن ورودی
    global flag_design, x_page, y_page
    # تا زمانی که حلقه بازی می چرخد(حلقه لابی بازی
    while flag_design:
        #گرفتن داده از سرور
        data = s.recv(1024).decode()
        #اگر داده برابر با accept بود
        if data == 'accept':
            # حلقه لابی تمام می شود
            flag_design = False
            data = s.recv(1024).decode()
            if data == 'player 1':
                x_page = 1
                y_page = 1
            elif data == 'player 0':
                x_page = -1*(w//1000)*36*(lenth[0]-16)
                y_page = -1*(w//1000)*36*(lenth[1]-10)


def recv_situ():
    global x_Enemy, y_Enemy, flag_design
    while not flag_design:
        a = s.recv(1024).decode().split()
        if a[0] == 'winner':
            flag_disign = True
        else:
            x_Enemy = int(a[0])
            y_Enemy = int(a[1])
    



# صدا زدن کتابخانه ها
import pygame, time, socket, threading
from random import *
import numpy as np

#لود کردن کتابخانه پایگیم
pygame.init()

#هاست و پورت برای وصل شدن به سرور
HOST = 'localhost'
PORT = 5023

#وصل شدن به سرور با استفاده از هاست و پورت
s = socket.socket()
s.connect((HOST, PORT))

# درست کردن صفحه اندازه صفحه خود کامپيوتر
disp = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
# گرفتن اندازه صفحه کامپيوتر شما
w, h = pygame.display.get_surface().get_size()

# varible - متغیر ها

xmouse = ymouse = 0

flag_chracter = 1
flag_design = True
flag_game = True
flag_send_ready = 'unready'

ready = -1
invite = -1

score_file = open('../text/score.txt','r')
Score = score_file.readline()
Score = Score[:-1]
score_file.close()

sign_file = open('../text/sign.txt','r')
Name = sign_file.readline()
Name = Name[:-1]
sign = sign_file.readline()
sign = sign[:-1]
sign_file.close()

arrow = 0

v = 1

character_file = open('../text/character.txt','r')
c = character_file.readline()
c = c[:-1]
character_file.close()

xs = w/100
ys = h/100

cx = 170
cy = 421

mx = 450
my = 8

rux = 38
ruy = 155

rdx = 38
rdy = 460

charx = [(w/1000)*25] * 3
chary = [(h/100)*30 ,(h/100)*50 ,(h/100)*70]
lock = [True] * 9
lock[0] = False


time_music = 0

victory_file = open('../text/victory.txt','r')
solo = victory_file.readline()
solo = solo[:-1]
duo = victory_file.readline()
duo = duo[:-1]
three = victory_file.readline()
three = three[:-1]
victory_file.close()


flag_setting = -1
flag_profile = -1
flag_location = -1
flag_music = 1
flag_help = -1
flag_progile = -1

# Game

map2, lenth = find()

# طول و عرض ها

x_event = 0
y_event = 0

x_player = w//2
y_player = h//2

x_page = 1
y_page = 1

x_Enemy = 0
y_Enemy = 0

x_client = -x_page + x_player
y_client = -y_page + y_player

# lobby 
# تعريف عکس ها و اندازه دادن (حتي فونت ها و آهنگ ها)

number = pygame.font.Font('../font/zorque.ttf', round((w/1000)*22))

score = number.render(str(Score) , True, (255, 255, 255))

solo_score = number.render(solo , True, (255, 255, 255))

duo_score = number.render(duo , True, (255, 255, 255))

three_score = number.render(three , True, (255, 255, 255))

invite_image = pygame.image.load('../images/lobby/invite.png')
invite_image = pygame.transform.scale(invite_image , (round((w/100)*11) , round((h/1000)*78)))

cancel = pygame.image.load('../images/lobby/cancel.png')
cancel = pygame.transform.scale(cancel , (round((w/100)*11) , round((h/1000)*78)))


Ready = pygame.image.load('../images/lobby/ready.png')
Ready = pygame.transform.scale(Ready, (round((w/100)*12) , round((h/1000)*95)))

Notready = pygame.image.load('../images/lobby/notready.png')
Notready = pygame.transform.scale(Notready, (round((w/100)*12) , round((h/1000)*95)))

Character = pygame.image.load('../images/lobby/Character.png')
Character  = pygame.transform.scale(Character , (round((w/1000)*155) , round((h/100)*9)))

Characters1 = pygame.image.load('../images/lobby/characters1.png')
Characters1  = pygame.transform.scale(Characters1 , (round((w/100)*10) , round((h/100)*60)))

Characters2 = pygame.image.load('../images/lobby/characters2.png')
Characters2  = pygame.transform.scale(Characters2 , (round((w/100)*10) , round((h/100)*60)))

Characters3 = pygame.image.load('../images/lobby/characters3.png')
Characters3  = pygame.transform.scale(Characters3 , (round((w/100)*10) , round((h/100)*60)))

setting = pygame.image.load('../images/lobby/setting.png')
setting  = pygame.transform.scale(setting , (round((w/1000)*45) , round((h/1000)*72)))

b_ground = pygame.image.load('../images/lobby/background.png')
b_ground = pygame.transform.scale(b_ground, (w , h))

avatar = pygame.image.load('../images/lobby/avatar.png')
avatar = pygame.transform.scale(avatar, (round((w/100)*24) , round((h/1000)*85)))

coin = pygame.image.load('../images/lobby/Coin.png')
coin = pygame.transform.scale(coin, (round((w/100)*13) , round((h/1000)*72)))

arrow_up = pygame.image.load('../images/lobby/arrow_up.png')
arrow_up = pygame.transform.scale(arrow_up, (round((w/1000)*22) , round((h/1000)*55)))

arrow_down = pygame.image.load('../images/lobby/arrow_down.png')
arrow_down = pygame.transform.scale(arrow_down, (round((w/1000)*22) , round((h/1000)*55)))

profile = pygame.image.load('../images/lobby/profile.png')
profile  = pygame.transform.scale(profile , (w , h))

back = pygame.image.load('../images/lobby/back.png')
back = pygame.transform.scale(back, (round((w/100)*6) , round((h/100)*9)))

Lock = pygame.image.load('../images/lobby/lock.png')
Lock  = pygame.transform.scale(Lock , (round((w/100)*4) , round((h/100)*7)))

music = pygame.mixer.music.load('../music/music.oga')
click = pygame.mixer.Sound('../music/click.wav')

# setting

setting1 = pygame.image.load('../images/lobby/setting1.png')
setting1  = pygame.transform.scale(setting1 , (round((w/100)*43) , round((h/100)*75)))

close = pygame.image.load('../images/lobby/close.png')
close  = pygame.transform.scale(close , (round((w/1000)*35) , round((h/1000)*60)))

music1 = pygame.image.load('../images/lobby/music1.png')
music1  = pygame.transform.scale(music1 , (round((w/1000)*135) , round((h/1000)*85)))

music2 = pygame.image.load('../images/lobby/music2.png')
music2  = pygame.transform.scale(music2 , (round((w/1000)*135) , round((h/1000)*85)))

help1 = pygame.image.load('../images/lobby/help.png')
help1  = pygame.transform.scale(help1 , (round((w/100)*43) , round((h/100)*75)))

# ------ #

# Character #

man = pygame.image.load('../images/characters/man.png')
man = pygame.transform.scale(man,  (round((w/1000)*305) , round((h/100)*54)))

devil = pygame.image.load('../images/characters/devil.png')
devil = pygame.transform.scale(devil, (round((w/1000)*305) , round((h/100)*54)))

ice = pygame.image.load('../images/characters/ice.png')
ice = pygame.transform.scale(ice, (round((w/1000)*305) , round((h/100)*54)))

india_man = pygame.image.load('../images/characters/india_man.png')
india_man = pygame.transform.scale(india_man, (round((w/1000)*305) , round((h/100)*54)))

knight = pygame.image.load('../images/characters/knight.png')
knight = pygame.transform.scale(knight, (round((w/1000)*305) , round((h/100)*54)))

magic = pygame.image.load('../images/characters/magic.png')
magic = pygame.transform.scale(magic, (round((w/1000)*305) , round((h/100)*54)))

mami = pygame.image.load('../images/characters/mami.png')
mami = pygame.transform.scale(mami, (round((w/1000)*305) , round((h/100)*54)))

skull = pygame.image.load('../images/characters/skull.png')
skull = pygame.transform.scale(skull, (round((w/1000)*305) , round((h/100)*54)))

vampire = pygame.image.load('../images/characters/vampire.png')
vampire = pygame.transform.scale(vampire, (round((w/1000)*305) , round((h/100)*54)))

# Avatar

man_avatar = pygame.image.load('../images/characters/man_avatar.png')
man_avatar = pygame.transform.scale(man_avatar, (round((w/100)*5) , round((h/1000)*78)))

man_avatar1 = pygame.image.load('../images/characters/man_avatar.png')
man_avatar1 = pygame.transform.scale(man_avatar1, (round((w/1000)*113) , round((h/1000)*182)))

devil_avatar = pygame.image.load('../images/characters/devil_avatar.png')
devil_avatar = pygame.transform.scale(devil_avatar, (round((w/100)*5) , round((h/1000)*78)))

devil_avatar1 = pygame.image.load('../images/characters/devil_avatar.png')
devil_avatar1 = pygame.transform.scale(devil_avatar1, (round((w/1000)*113) , round((h/1000)*182)))

ice_avatar = pygame.image.load('../images/characters/ice_avatar.png')
ice_avatar = pygame.transform.scale(ice_avatar, (round((w/100)*5) , round((h/1000)*78)))

ice_avatar1 = pygame.image.load('../images/characters/ice_avatar.png')
ice_avatar1 = pygame.transform.scale(ice_avatar1, (round((w/1000)*113) , round((h/1000)*182)))

india_man_avatar = pygame.image.load('../images/characters/india_man_avatar.png')
india_man_avatar = pygame.transform.scale(india_man_avatar, (round((w/100)*5) , round((h/1000)*78)))

india_man_avatar1 = pygame.image.load('../images/characters/india_man_avatar.png')
india_man_avatar1 = pygame.transform.scale(india_man_avatar1, (round((w/1000)*113) , round((h/1000)*182)))

knight_avatar = pygame.image.load('../images/characters/knight_avatar.png')
knight_avatar = pygame.transform.scale(knight_avatar, (round((w/100)*5) , round((h/1000)*78)))

knight_avatar1 = pygame.image.load('../images/characters/knight_avatar.png')
knight_avatar1 = pygame.transform.scale(knight_avatar1, (round((w/1000)*113) , round((h/1000)*182)))

magic_avatar = pygame.image.load('../images/characters/magic_avatar.png')
magic_avatar = pygame.transform.scale(magic_avatar, (round((w/100)*5) , round((h/1000)*78)))

magic_avatar1 = pygame.image.load('../images/characters/magic_avatar.png')
magic_avatar1 = pygame.transform.scale(magic_avatar1, (round((w/1000)*113) , round((h/1000)*182)))

mami_avatar = pygame.image.load('../images/characters/mami_avatar.png')
mami_avatar = pygame.transform.scale(mami_avatar, (round((w/100)*5) , round((h/1000)*78)))

mami_avatar1 = pygame.image.load('../images/characters/mami_avatar.png')
mami_avatar1 = pygame.transform.scale(mami_avatar1, (round((w/1000)*113) , round((h/1000)*182)))

skull_avatar = pygame.image.load('../images/characters/skull_avatar.png')
skull_avatar = pygame.transform.scale(skull_avatar, (round((w/100)*5) , round((h/1000)*78)))

skull_avatar1 = pygame.image.load('../images/characters/skull_avatar.png')
skull_avatar1 = pygame.transform.scale(skull_avatar1, (round((w/1000)*113) , round((h/1000)*182)))

vampire_avatar = pygame.image.load('../images/characters/vampire_avatar.png')
vampire_avatar = pygame.transform.scale(vampire_avatar, (round((w/100)*5) , round((h/1000)*78)))

vampire_avatar1 = pygame.image.load('../images/characters/vampire_avatar.png')
vampire_avatar1 = pygame.transform.scale(vampire_avatar1, (round((w/1000)*113) , round((h/1000)*182)))

# -------- #

# Game
Green_Grass = pygame.image.load("../images/ingame/Green Grass.png")
Green_Grass = pygame.transform.scale(Green_Grass, (round((w/1000)*36), round((w/1000)*54)))
Yello_Grass = pygame.image.load("../images/ingame/Yello Grass.png")
Yello_Grass = pygame.transform.scale(Yello_Grass, (round((w/1000)*36), round((w/1000)*54)))
Box = pygame.image.load("../images/ingame/Box.png")
Box = pygame.transform.scale(Box, (round((w/1000)*36), round((w/1000)*54)))

# -------- #

# loading

Drum = pygame.image.load('../images/lobby/logo.png')
Drum = pygame.transform.scale(Drum, (round((w/100)*60) , round((h/100)*60)))

#loading()

# -------- #

# sign in

welcome = pygame.image.load('../images/lobby/welcome.png')
welcome = pygame.transform.scale(welcome, (w , h))

welcome2 = pygame.image.load('../images/lobby/welcome2.png')
welcome2 = pygame.transform.scale(welcome2, (w , h))

font = pygame.font.Font(None, round((w/1000)*40))
font2 = pygame.font.Font(None, round((w/1000)*20))

Name = signin(sign,Name)

names = pygame.font.Font('../font/Arista20AlternateRegular-jy89.ttf', round((w/1000)*30))
names2 = pygame.font.Font('../font/Arista20AlternateRegular-jy89.ttf', round((w/1000)*42))

#فرستادن اسم به سرور
s.send(Name.encode())
    

while flag_game:
    # -------- #

    flag_send_ready = 'unready'
    ready = -1
    invite = -1


    #ساختن یک ترد برای گرفتن داده از سرور از طریق فانکشن recive!
    thread_receive = threading.Thread(target = receive)
    thread_receive.start()

    #پخش کردن آهنگ
    pygame.mixer.music.play()

    #:تا زمانی که متغیر درست است flag_design == True:
    while flag_design:
        # events
        # روخداد هاي کيبورد يا ايونت
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                finish = True
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                (xmouse,ymouse) = event.pos
                
            
        disp.fill((30,30,30))
        name = names.render(Name , True, (255, 255, 255))
        name2 = names2.render(Name , True, (255, 255, 255))

    
        # updates
        # اگر روي دکمه ي ... زد
        #بالاي هر ايف اسم دکمه اي کليک کرده را مي نويسم

        # READY
        if (w/1000)*860 < xmouse < (w/1000)*860+round((w/100)*12) and (h/100)*87 < ymouse < (h/100)*87+round((h/1000)*95) and flag_setting == -1 and flag_profile == -1:
            click.play()
            ready = -ready

        # کاراکتر
        elif (w/1000)*695 < xmouse < (w/1000)*695 + round((w/1000)*155) and (h/1000)*873 < ymouse < (h/1000)*873 + round((h/100)*9) and flag_setting == -1 and flag_profile == -1:
            flag_chracter = -flag_chracter
            click.play()

        # اينوايت
        elif (w/1000)*865 < xmouse < (w/1000)*865 + round((w/100)*11) and (h/1000)*780 < ymouse < (h/1000)*780 + round((h/1000)*78) and flag_setting == -1 and flag_profile == -1:
            click.play()
            invite = -invite

        # ستينگ
        elif (w/1000)*949 < xmouse < (w/1000)*949 + round((w/1000)*45) and (h/1000)*11 < ymouse < (h/1000)*11 + round((h/1000)*72) and flag_profile == -1:
            click.play()
            flag_setting = -flag_setting
            if flag_help == 1:
                flag_help = -1

        # زربدر قرمز ستينگ
        elif (w/1000)*655  < xmouse < (w/1000)*655 + round((w/1000)*35) and  (h/1000)*120 < ymouse < (h/1000)*120 + round((h/1000)*60) and flag_profile == -1 and flag_setting == 1:
            click.play()
            if flag_setting == 1:
                flag_setting = -flag_setting
            if flag_help == 1:
                flag_help = -flag_help

        # موزيک خاموش
        elif (w/1000)*470 < xmouse < (w/1000)*470 + round((w/1000)*70) and  (h/1000)*594 < ymouse < (h/1000)*594 + round((h/1000)*85) and flag_setting == 1 and flag_music == 1 and flag_help == -1  and flag_profile == -1:
            flag_music = -flag_music
            time_music = 8999
            click.play()

        # موزيک روشن
        elif (w/1000)*405 < xmouse < (w/1000)*405 + round((w/1000)*68) and  (h/1000)*594 < ymouse < (h/1000)*594 + round((h/1000)*85) and flag_setting == 1 and flag_music == -1 and flag_help == -1  and flag_profile == -1  and flag_profile == -1:
            flag_music = -flag_music
            click.play()

        # راهنما
        elif (w/100)*41 < xmouse < (w/100)*41 + round((w/1000)*135) and  (h/1000)*463 < ymouse < (h/1000)*463 + round((h/1000)*85) and flag_setting == 1 and flag_help == -1 and flag_profile == -1:
            flag_help = 1
            click.play()

        # پروفايل
        elif 0  < xmouse <  round((w/100)*9) + (w/100)*10 and  0 < ymouse < round((h/1000)*84) and flag_setting == -1 and flag_help == -1  and flag_profile == -1:
            flag_profile = 1
            click.play()

        # دکمه برگشت در قسمت پروفايل
        elif 0  < xmouse < round((w/100)*6) and  0 < ymouse < round((h/100)*9) and flag_setting == -1 and flag_help == -1  and flag_profile == 1:
            flag_profile = -1
            click.play()

        # اگر زد روي دکمه کاراکتر
        if flag_chracter == -1:
            character_file = open('character.txt','w')

            # 3 لاين وجود دارد
            # و 3 قسمت هم براي هر لاين وجو
            for i in range(3):
                # اگر کليک آن داخل يکي از آن قسمت ها بود
                if charx[i] < xmouse < charx[i] + round((w/100)*10) and chary[i] < ymouse < chary[i] + round((h/100)*20) and flag_setting == -1 and flag_profile == -1:
                    click.play()
                    # اگر لاين اول بود
                    if i == 0:
                        # قسمن اول بود
                        if arrow == 0:
                            # اگر قغل نبود
                            if lock[0] == False:
                                c = 'man'
                        # قسمت دوم بود
                        elif arrow == 1:
                            if lock[1] == False:
                                c = 'ice'
                        # ...
                        elif arrow == 2:
                            if lock[2] == False:
                                c = 'india'

                    # اگر لاين دوم بود
                    elif i == 1:
                        if arrow == 0:
                            if lock[3] == False:
                                c = 'skull'
                        elif arrow == 1:
                            if lock[4] == False:
                                c = 'vampire'
                        elif arrow == 2:
                            if lock[5] == False:
                                c = 'mami'

                    # اگر لاين سوم بود
                    elif i == 2:
                        if arrow == 0:
                            if lock[6] == False:
                                c = 'knight'
                        elif arrow == 1:
                            if lock[7] == False:
                                c = 'devil'
                        elif arrow == 2:
                            if lock[8] == False:
                                c = 'magic'

            # فلش بالا در قسمت کاراکتر
            if (w/1000)*65 < xmouse < (w/1000)*65 + round((w/1000)*22) and (h/1000)*255 < ymouse < (h/1000)*255 + round((h/1000)*45) and flag_setting == -1:
                    if arrow == 1:
                        arrow = 0
                        click.play()
                    if arrow == 2:
                        arrow = 1
                        click.play()

            # فلش پايين در قسمت کاراکتر
            elif (w/1000)*65 < xmouse < (w/1000)*65 + round((w/1000)*22) and (h/100)*89 < ymouse < (h/100)*89 + round((h/1000)*45) and flag_setting == -1:
                    if arrow == 1:
                        arrow = 2
                        click.play()
                    if arrow == 0:
                        arrow = 1
                        click.play()

            character_file.write(c + '\n')
            character_file.close()

        # قطع و وصل شدن آهنگ
        if flag_music == 1:
            time_music += 1
            if time_music == 9000:
                time_music = 0
                pygame.mixer.music.play()
        else:
            pygame.mixer.music.stop()

        
        xmouse = ymouse = 0

        #ready, unready - آماده بودن و نبودن برای شرکت در بازی

        #اگر متغیر ردی == 1 باشد (زمانی این اتفاق می افتد که اگر کاربر دکمه ردی را بزند این متغیر ۱ می شود) 
        #و اگر متغیر دوم برابر آماده نبودن باشد وارد شود (متغیر دوم برای جلوگیری از فرستادن مداوم پیام ها است.
        if ready == 1 and flag_send_ready == 'unready':
            #پیام آماده بودن است
            msg = 'ready'
            #فرستادن پیام
            s.send(msg.encode())
            #متغیر برای جلوگیری از مداوم فرستادن برابر با ردی می شود
            flag_send_ready = 'ready'
        #اگر متغیر ردی == 2 باشد (زمانی این اتفاق می افتد که اگر کاربر دکمه آن ردی را بزند این متغیر ۲ می شود) 
        #و اگر متغیر دوم برابر آماده بودن باشد وارد شود (متغیر دوم برای جلوگیری از فرستادن مداوم پیام ها است
        if ready != 1 and flag_send_ready == 'ready':
            #پیام آماده نبودن است
            msg = 'unready'
            #فرستادن پیام
            s.send(msg.encode())
            #متغیر برای جلوگیری از مداوم فرستادن برابر با آن ردی می شود
            flag_send_ready = 'unready'
        
        # draw
        # کشيدن
        
        disp.blit(b_ground, (0,0))
    
        disp.blit(avatar, (0,0))

        disp.blit(name, ((w/1000)*55,(h/1000)*25))
    
        disp.blit(Character, (((w/1000)*695), ((h/1000)*874)))
    
        disp.blit(setting, ((w/1000)*949, (h/1000)*11))
    
        disp.blit(coin, ((w/1000)*812, (h/1000)*12))
    
        disp.blit(score, ((w/1000)*855, (h/1000)*24))
    
        solo_score = number.render(str(solo) , True, (255, 255, 255))
        duo_score = number.render(str(duo) , True, (255, 255, 255))
        three_score = number.render(str(three) , True, (255, 255, 255))

        # اگه ردي بود
        if ready == -1:
            disp.blit(Ready, (((w/1000)*860),((h/100)*87)))

        # اگه ردي نبود
        elif ready == 1:
            disp.blit(Notready, (((w/1000)*860),((h/100)*87)))

        if invite == -1:
            disp.blit(invite_image , (((w/1000)*865),((h/1000)*780)))

        elif invite == 1:
            disp.blit(cancel , (((w/1000)*865),((h/1000)*780)))


    # Lock + character line

        # اگر روي دکمه کاراکتر زده بود
        if flag_chracter == -1:

            # اگر لاين اول بود
            if arrow == 0:

                # گشيدن لاين اول
                disp.blit(Characters1, (((w/1000)*25),((h/100)*30)))

                # اگه قفل بودي چيزي از لاين اول اونو بکشه
                if lock[1] == True:
                    disp.blit(Lock , (((w/1000)*55),((h/1000)*565)))
                if lock[2] == True:
                    disp.blit(Lock , (((w/1000)*55),((h/1000)*750)))

            if arrow == 1:
                disp.blit(Characters2, (((w/1000)*25),((h/100)*30)))

            
                if lock[3] == True:
                    disp.blit(Lock , (((w/1000)*55),((h/1000)*365)))
                if lock[4] == True:
                    disp.blit(Lock , (((w/1000)*55),((h/1000)*565)))
                if lock[5] == True:
                    disp.blit(Lock , (((w/1000)*55),((h/1000)*750)))

            if arrow == 2:
                disp.blit(Characters3, (((w/1000)*25),((h/100)*30)))

            
                if lock[6] == True:
                    disp.blit(Lock , (((w/1000)*55),((h/1000)*365)))
                if lock[7] == True:
                    disp.blit(Lock , (((w/1000)*55),((h/1000)*565)))
                if lock[8] == True:
                    disp.blit(Lock , (((w/1000)*55),((h/1000)*750)))

            disp.blit(arrow_up, (((w/1000)*65),((h/1000)*255)))
            disp.blit(arrow_down, (((w/1000)*65),((h/100)*89)))
        

    # Looby Big character

        # اگر کاراکتر شما ... بود
        if c == 'man':
            disp.blit(man, (((w/100)*35),((h/100)*30)))
            disp.blit(man_avatar, (0,0))
        elif c == 'ice':
            disp.blit(ice, (((w/100)*35),((h/100)*30)))
            disp.blit(ice_avatar, (0,0))
            
        elif c == 'india':
            disp.blit(india_man, (((w/100)*35),((h/100)*30)))
            disp.blit(india_man_avatar, (0,0))
            
        elif c == 'skull':
            disp.blit(skull, (((w/100)*35),((h/100)*30)))
            disp.blit(skull_avatar, (0,0))
            
        elif c == 'vampire':
            disp.blit(vampire, (((w/100)*35),((h/100)*30)))
            disp.blit(vampire_avatar, (0,0))
            
        elif c == 'mami':
            disp.blit(mami, (((w/100)*35),((h/100)*30)))
            disp.blit(mami_avatar, (0,0))
            
        elif c == 'knight':
            disp.blit(knight, (((w/100)*35),((h/100)*30)))
            disp.blit(knight_avatar, (0,0))
            
        elif c == 'devil':
            disp.blit(devil, (((w/100)*35),((h/100)*30)))
            disp.blit(devil_avatar, (0,0))
            
        elif c == 'magic':
            disp.blit(magic, (((w/100)*35),((h/100)*30)))
            disp.blit(magic_avatar, (0,0))
            
    # Profile avatar

        # اگه دکمه پروفايل رو زد
        if flag_profile == 1:
            disp.blit(profile, (0,0))
            if flag_profile == 1 and flag_setting == -1:
                # کشدن اسم و دکمه برگشت
                disp.blit(name2, (((w/1000)*475),((h/1000)*295)))
                disp.blit(back, (0,0))

                # اگه کاراکتر شما ... بود
                if c == 'man':
                    disp.blit(man_avatar1, (((w/100)*32),((h/1000)*190)))
                elif c == 'ice':
                    disp.blit(ice_avatar1, (((w/100)*32),((h/1000)*190)))
                elif c == 'india':
                    disp.blit(india_man_avatar1, (((w/100)*32),((h/1000)*190)))
                elif c == 'skull':
                    disp.blit(skull_avatar1, (((w/100)*32),((h/1000)*190)))
                elif c == 'vampire':
                    disp.blit(vampire_avatar1, (((w/100)*32),((h/1000)*190)))
                elif c == 'mami':
                    disp.blit(mami_avatar1, (((w/100)*32),((h/1000)*190)))
                elif c == 'knight':
                    disp.blit(knight_avatar1, (((w/100)*32),((h/1000)*190)))
                elif c == 'devil':
                    disp.blit(devil_avatar1, (((w/100)*32),((h/1000)*190)))
                elif c == 'magic':
                    disp.blit(magic_avatar1, (((w/100)*32),((h/1000)*190)))
            disp.blit(solo_score, (((w/100)*48),((h/1000)*554)))
            disp.blit(duo_score, (((w/100)*48),((h/1000)*656)))
            disp.blit(three_score, (((w/100)*48),((h/1000)*758)))

    # Setting

        # اگه روي دکمه ستينگ زد
        if flag_setting == 1:
            disp.blit(setting1, ((w/100)*26,(h/100)*12))
            disp.blit(close, ((w/1000)*655,(h/1000)*120))

            # اگه موسيقي روشن بود
            if flag_music == 1:
                disp.blit(music1, ((w/1000)*405,(h/1000)*594))
            # اگه موسيقي روشت نبود
            if flag_music == -1:
                disp.blit(music2, ((w/1000)*405,(h/1000)*594))
        
        # اگه دکمه راهنما را زد
        if flag_help == 1:
            disp.blit(help1, ((w/100)*26,(h/100)*12))
            disp.blit(close, ((w/1000)*655,(h/1000)*120))
            
        # نوشتن متغيير ها در فايل ها
        score_file = open('../text/score.txt','w')
        score_file.write(Score +'\n')
        score_file.close()


        victory_file = open('../text/victory.txt','w')
        victory_file.write(str(solo) +'\n')
        victory_file.write(str(duo) +'\n')
        victory_file.write(str(three) +'\n')
        victory_file.close()

        pygame.display.update()
        pygame.time.delay(0) 
        pygame.time.Clock().tick(240)

    # Game
    pygame.mixer.music.stop()

    disp.fill((249,165,117))

    recive_situ = threading.Thread(target = recv_situ)
    recive_situ.start()

    send_num = 1
    
    # طول و عرض ها

    x_event = 0
    y_event = 0

    x_player = w//2
    y_player = h//2

    x_Enemy = 0
    y_Enemy = 0

    x_client = -x_page + x_player
    y_client = -y_page + y_player

    while (not flag_design) and flag_design != '':
        pygame.time.delay(0)
        pygame.time.Clock().tick(240)
        pygame.display.update()
        disp.fill((249,165,117))
        # updates - آپدیت کردن صفحه نمایش
        client()
        render()
        x_event, y_event = event1(x_event, y_event)
        x = [x_player, x_page]
        y = [y_player, y_page]
        x_page, y_page = updates(x_page, y_page)
        if (x_client != x[0]-x[1] or y_client != y[0]-y[1]) or (x_client != x[0]-x[1] and y_client != y[0]-y[1]) or send_num == 1:
            s.send((str(x_client) + ' ' + str(y_client)).encode())
            send_num = 0

pygame.quit()

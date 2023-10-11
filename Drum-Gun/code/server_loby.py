# صدا زدن کتابخانه ها
import socket, threading

import numpy as np
# فانکشن قبول کردن کاربر برای گرفتن اسم-آدرس و اضافه کردن آن به لیست متصل ها
def accept_client():
    global thread_client
    while True:
        #accept - قبول کردن کاربر و گرفتن آدرس آن
        (s, addr) = sock.accept()
        #گرفتن اسم از کاربر
        uname = s.recv(1024).decode()
        #اضافه کردن آدرس و اسم کاربر به لیست متصل ها
        CONNECTION_LIST.append((uname, s))
        #چاپ کردن (کاربر الان وصل شد
        print('%s is now connected' %uname)
        #ساخت ترد برای گرفتن پیام ها از کاربر توسط فانکشن broadcast_usr
        thread_client.append(threading.Thread(target = broadcast_usr, args=[uname, s, len(thread_client)-1]))
        thread_client[len(thread_client)-1].start()

#فانکشن گرفتن داده از کاربر
def broadcast_usr(uname, s, Last):
    while True:
        #گرفتن داده
        data = s.recv(1024).decode()
        # چاپ داده
        #اگر داده مربوط به ردی و آن ردی بودن باشد 
        if data == 'ready' or data == 'unready':
            #وارد تابع ردی شود
            ready_func(s, uname, data)

        #اگر مربوط به دعوت باشد
        if data == 'invite':
            #وارد تابع دعوت شود
            invite_func(s, uname, data)

        if data == 'close':
            s.close()
            CONNECTION_LIST.remove((uname, s))
            thread_client.pop(Last)
            break
    print (uname,'is now disconnect')
            

#تابع ردی
def ready_func(cs_sock, sen_name, msg):
    #چک کردن کاربر در بین لیست متصل ها
    for client in CONNECTION_LIST:
        #اگر آدرس خونه اول کاربر (لیست متصل ها) با آدرس ورودی یکی بود
        if client[1] == cs_sock:
            #اگر پیام ردی بود
            if msg == 'ready':
                #اضافه کردن کاربر با آدرس و اسم به لیست ردی
                READY.append((sen_name, cs_sock))
                # چاپ لیست ردی
                print (READY)
            #اگر آن ردی بود
            elif msg == 'unready':
                #از لیست ردی حذفش کند
                READY.remove((sen_name, cs_sock))
                #چاپ لیست ردی
                print (READY)
    #شروع ترد از تابع چک ردی
    thread_ab = threading.Thread(target = chek_ready)
    thread_ab.start()

#تابع دعوت
def invite_func(cs_sock, sen_name, msg):
    #چک کردن کاربر در بین لیست متصل ها
    for client in CONNECTION_LIST:
        #اگر آدرس خونه اول کاربر (لیست متصل ها) با آدرس ورودی یکی بود 
        if client[1] == cs_sock:
            #اگر پیام اینوایت بود
            if msg == 'invite':
                #ساخت لیست آنلاین
                ONLINE = []
                #چک کردن کاربران آنلاین در بین لیست متصل ها
                for Online_players in CONNECTION_LIST:
                    #اگر آدرس خونه اول کاربران آنلاین (لیست متصل ها) با آدرس ورودی یکی نبود 
                    if Online_players[1] != cs_sock:
                        #کاربر آنلاین به لیست آنلاین اضافه شود
                        ONLINE.append(Online_players[0])
                #لیست کاربران آنلاین را به کاربر می فرستد
                cs_sock.send(str(ONLINE).encode())
                
#تابع چک کردن آماده بودن
def chek_ready():
    #تا زمانی که طول لیست ردی بزرگتر و مساوی ۲ بود
    while len(READY) >= 2:
        #ساخت لیست x برای دسته بندی کاربر ها تا ۲ به ۲ وارد مسابقه شوند 
        x = []
        #چک کردن کاربر در بین لیست ردی
        for client in READY:
            #اگر طول رشته ردی بزرگتر مساوی ۲ است و طول رشته ایکس کمتر مساوی ۲ بود
            if len(x) <= 2 and len(READY) >= 2: 
                #به لیست ایکس کاربر را اضافه می کنیم
                x.append(client)
            #اگر نه
            else:
                #حلقه فور قطع شود
                break
        #صدا زدن تابع فرستادن قبول شدن به کاربر ها
        send_accept(x)
        #خارج کردن کاربر هایی که به بازی رفتند از لیست ردی
        READY.remove((x[0]))
        READY.remove((x[1]))
        
        
#تابع فرستادن قبولی
def send_accept(x):
    #چک کردن کاربر بین لیست بازی
    for client in x:
        #فرستادن قبولی به آدرس کاربر ها
        client[1].send('accept'.encode())
        

    for i in range(len(x)):
        if i == 1:
            GAME.append(threading.Thread(target = Game_func, args=[x[i], x[i-1], len(thread_client)-1]))
            GAME[len(GAME)-1].start()
            x[i][1].send(('player' + ' ' + str(i)).encode())
        else:
            GAME.append(threading.Thread(target = Game_func, args=[x[i], x[i+1], len(thread_client)-1]))
            GAME[len(GAME)-1].start()
            x[i][1].send(('player' + ' ' + str(i)).encode())

def Game_func(Host, enemy, Last):
    while True:
        x = Host[1].recv(1024).decode()
        if x != 'close the game':
            enemy[1].send(x.encode())
        else:
            enemy[1].send('winner'.encode())
            GAME = []
            break

# socket - درست کردن آدرس
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind - ساخت پورت و هاست و گرفتن کاربر
HOST = 'localhost'
PORT = 5023
sock.bind((HOST, PORT))

# listen - منتظر ماندن برای گرفتن کاربر
sock.listen(1)
#ساخت لیست های مربوطه
thread_client = []
CONNECTION_LIST = []
READY = []
GAME = []

#ساخت ترد به تابع قبولی کاربر
thread_ac = threading.Thread(target = accept_client)
thread_ac.start()

import tkinter as tk
from PIL import Image,ImageTk
from speedtest import Speedtest

def speed_calculate():
    # Calculate Internet Speed (Mbps)
    speed_test = Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()

    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)

    down_label.config(text = str(download_speed) + "Mbps")
    up_label.config(text = str(upload_speed) + "Mbps") 

# Window
root = tk.Tk()
root.geometry('320x620')
root.config(background='white')
root.iconbitmap(r'icon.ico')
root.title("Speed Test")
root.resizable(width=False, height=False)

background_canvas= tk.Canvas(root, width= 320, height= 620)
background = ImageTk.PhotoImage(Image.open("Background.png"))

background_canvas.place(x=0,y=0)
background_canvas.create_image(160,310,image=background)

button_image = ImageTk.PhotoImage(Image.open("Button.png"))
button = tk.Button(root, text = "Start Internet Speed Test" , bd=0, image=button_image, highlightthickness=0, command = speed_calculate)
button.place(x = 30, y = 510)

down_label = tk.Label(root, text="0.0 Mbps", bg = 'White', font = ("Verdana", 12))
down_label.place(x = 45, y = 435)
up_label = tk.Label(root, text="0.0 Mbps", bg = 'White', font = ("Verdana", 12))
up_label.place(x = 200, y = 435)

info_label = tk.Label(root, text="Wait 30 Seconds After Pressing The Button", bg = 'White', fg = '#474747', font = ("Verdana", 8))
info_label.place(x = 38, y = 488)

root.mainloop()
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
import googletrans
import textblob
import pyttsx3

# End in : 8/10/2021

def translate_it():
	translated_text.delete(1.0, tk.END)

	try:
		for key, value in languages.items():
			if (value == original_combo.get()):
				from_language_key = key

		for key, value in languages.items():
			if (value == translated_combo.get()):
				to_language_key = key

		words = textblob.TextBlob(original_text.get(1.0, tk.END))

		words = words.translate(from_lang=from_language_key , to=to_language_key)

		translated_text.insert(1.0, words)

	except:
		pass

def read_it1():
	engine.say(str(original_text.get("1.0",tk.END)))
	engine.runAndWait()

def read_it2():
	engine.say(str(translated_text.get("1.0",tk.END)))
	engine.runAndWait()

engine = pyttsx3.init()
root = tk.Tk()
root.title('Language Translator')
root.geometry("1200x420")
root.resizable(width=False, height=False)
root.iconbitmap(r'icon.ico')

background_canvas= tk.Canvas(root, width= 1200, height= 420)
background = ImageTk.PhotoImage(Image.open("Background.png"))
background_canvas.place(x=0,y=0)
background_canvas.create_image(600,210,image=background)

button_image = ImageTk.PhotoImage(Image.open("Button.png"))
sound_image = ImageTk.PhotoImage(Image.open("Sound.png"))

languages = googletrans.LANGUAGES
language_list = list(languages.values())

original_text = tk.Text(root, height=10, width=40, bd=0, font=("Verdana", 12))
original_text.place(x=40,y=180)

translate_button = tk.Button(root, bd=0, image=button_image, command=translate_it)
translate_button.place(x=565,y=172)

translated_text = tk.Text(root, height=10, width=40, bd=0, font=("Verdana", 12))
translated_text.place(x=660,y=180)

original_combo = ttk.Combobox(root, width=45,height=10, value=language_list, font=("Seogeo UI", 14), state='readonly')
original_combo.current(21)
original_combo.place(x=30,y=105)

translated_combo = ttk.Combobox(root, width=45,height=10, value=language_list, font=("Seogeo UI", 14), state='readonly')
translated_combo.current(26)
translated_combo.place(x=652,y=105)

sound_button1 = tk.Button(root, bd=0, image=sound_image, command=read_it1)
sound_button1.place(x=495,y=320)

sound_button2 = tk.Button(root, bd=0, image=sound_image, command=read_it2)
sound_button2.place(x=1115,y=320)

root.mainloop()
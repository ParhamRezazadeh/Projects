import tkinter as tk
import math

#+-----------++-----------++-----------++-----------+
#| Functions || Functions || Functions || Functions |
#+-----------++-----------++-----------++-----------+

#....................................................

#+---------------------+
#| Reset Buttons color |
#+---------------------+
def reset_color():
   button_division.config(
      bg = 'gray75')
   button_multiply.config(
      bg = 'gray75')
   button_minus.config(
      bg = 'gray75')
   button0.config(
      bg = 'gainsboro')
   button1.config(
      bg = 'gainsboro')
   button2.config(
      bg = 'gainsboro')
   button3.config(
      bg = 'gainsboro')
   button4.config(
      bg = 'gainsboro')
   button_x.config(
      bg = 'gray75')
   button5.config(
      bg = 'gainsboro')
   button6.config(
      bg = 'gainsboro')
   button7.config(
      bg = 'gainsboro')
   button8.config(
      bg = 'gainsboro')
   button9.config(
      bg = 'gainsboro')
   button_plus.config(
      bg = 'gray75')
   button_percent.config(
      bg = 'gray75')
   button_float.config(
      bg = 'gainsboro')

#+------------------------------------------+
#| Reset Calculator When esc Button Pressed |
#+------------------------------------------+
def esc_pressed(e):
   c_pressed()

#+---------------------------------------------+
#| Close Calculator Window when alt+f4 Pressed |
#+---------------------------------------------+
def alt_f4(event):
   win.destroy()

#+---------------------------------------+
#| Do Calculation (=) when Enter Pressed |
#+---------------------------------------+
def enter_pressed(e):
   global enterp
   equal()
   enterp = enterp + 1
   if enterp == 2:
      c_pressed()
   win.after(150, reset_color)

#+------------------------------------------+
#| Delete Characters When Backspace Pressed |
#+------------------------------------------+
def backspace_pressed(e):
   global num
   if len(num) == 1 or (len(num) == 2 and int(num)<1):
      num = '0'
   else:
      num = num[0:len(num)-1]
   screen.set(num)
   win.after(150, reset_color)

#+--------------------------------------+
#| Change Button color when mouse on it |
#+--------------------------------------+
def on_enter(e):
   e.widget['background'] = 'gray70'
def on_leave(e):
   e.widget['background'] = 'gainsboro'

def on_enter_math(e):
   e.widget['background'] = 'gray70'
def on_leave_math(e):
   e.widget['background'] = 'gray75'
#+--------------------------------------+


#+----------------------------------------------------------------+
#| Show numbers when u pressed key or click on that number button |
#+----------------------------------------------------------------+
def num_pressed (this):
   global num, dotnum
   if len(calculation.get())+1 <= 18:
      calculation.config(font = ("Verdana", 20), width=18)
   elif len(calculation.get())+1 <= 20 and len(calculation.get())+1 > 18:
      calculation.config(font = ("Verdana", 16), width=24)

   if num == '0':
      num = ''
   if len(num) < 18:
      if this != 0:
         num = num + str(this)
      elif this == 0 and num != '0':
         num = num + '0'

   screen.set(num)

#+-----------------------------------------+
#| Reset Claculation When C Button Pressed |
#+-----------------------------------------+
def c_pressed():
   global num, endnum, eql, what_type, sqrt_check
   calculation.config(font = ("Verdana", 20), width=18)
   what_type, num,endnum, eql = 'i', '0', 0, 0
   sqrt_check = False
   win.after(150, reset_color)
   screen.set('0')

#+----------------------------------------------------+
#| Change to Float When Dot (.) Button Or key pressed |
#+----------------------------------------------------+
def dot_pressed():
   global dotnum, num, what_type
   try:
      a = int(calculation.get())
      dotnum = float(dotnum)
      num = num+'.'
      what_type = 'f'
      screen.set(calculation.get()+'.0')
      dotnum = '0'
   except:
      a = 1

#+----------------------------------------+
#| Makes the number negative and positive |
#+----------------------------------------+
def change_pressed():
   if float(calculation.get()) > 0:
      screen.set('-'+calculation.get())
   elif float(calculation.get()) < 0:
      screen.set(calculation.get()[1:])

#+--------------------------+
#| Calculate sqrt of number |
#+--------------------------+
def sqrt_pressed():
   global endnum, what_type, num

   if float(calculation.get()) >= 0:
      justhere = math.sqrt(float(calculation.get()))
      screen.set(round(justhere,8))
      num = str(round(justhere,8))
   else:
      screen.set("Invalid")
   what_type = 'f'

#+----------------------------------------------+
#| Check Operators (+-/*^) From Buttons or keys |
#+----------------------------------------------+
def math_pressed(that):
   global mathsign, first_time, count, sqrt_check
   calculation.config(font = ("Verdana", 20), width=18)
   if first_time == True and count == 0:
      math_pressed_calculate(that)
   else:
      math_pressed_calculate(mathsign)
   mathsign = that
   if that == '/':
      screen.set('÷')
   elif that == '*':
      screen.set('×')
   else:
      screen.set(that)

#+---------------------------------------------+
#| Get Operators (+-/*^) and Numbers From keys |
#+---------------------------------------------+
def key_pressed(event):

   #+-----------------------+
   #| Get Numbers From keys |
   #+-----------------------+
   if event.char == '1':
      button1.config(bg = 'gray70')
      num_pressed(1)
   elif event.char == '2':
      button2.config(bg = 'gray70')
      num_pressed(2)
   elif event.char == '3':
      button3.config(bg = 'gray70')
      num_pressed(3)
   elif event.char == '4':
      button4.config(bg = 'gray70')
      num_pressed(4)
   elif event.char == '5':
      button5.config(bg = 'gray70')
      num_pressed(5)
   elif event.char == '6':
      button6.config(bg = 'gray70')
      num_pressed(6)
   elif event.char == '7':
      button7.config(bg = 'gray70')
      num_pressed(7)
   elif event.char == '8':
      button8.config(bg = 'gray70')
      num_pressed(8)
   elif event.char == '9':
      button9.config(bg = 'gray70')
      num_pressed(9)
   elif event.char == '0':
      button0.config(bg = 'gray70')
      num_pressed(0)

   #+---------------------------------+
   #| Get Operators (+-/*^) From keys |
   #+---------------------------------+
   elif event.char == '+':
      math_pressed('+')
      button_plus.config(bg = 'gray70')
   elif event.char == '-':
      math_pressed('-')
      button_minus.config(bg = 'gray70')
   elif event.char == '/':
      math_pressed('/')
      button_division.config(bg = 'gray70')
   elif event.char == '*':
      math_pressed('*')
      button_multiply.config(bg = 'gray70')
   elif event.char == '^':
      math_pressed('^')
      button_x.config(bg = 'gray70')

   elif event.char == '.':
      dot_pressed()
      button_float.config(bg = 'gray70')

   elif event.char == '=':
      equal()

   win.after(150, reset_color)

#+----------------------------+
#| Do all (+-/*^) Calculation |
#+----------------------------+
def math_pressed_calculate (that):
   global num, endnum, mathsign, eql , invalid, what_type, count, first_time, sqrt_check, enterp
   enterp = 0

   if invalid == True:
      invalid = False
      screen.set("0")

   if what_type == 'i':
      justnum = int(calculation.get())
   else:
      justnum = float(calculation.get())

#  -----
#  | + |
#  -----
   if that == '+':
      if eql == 0:
         endnum = endnum + justnum

      elif eql == 1:
         endnum = justnum

#  -----
#  | - |
#  -----
   elif that == '-':
      if eql == 0 and endnum > justnum:
         endnum = endnum - justnum

      if eql == 0 and endnum < justnum:
         endnum = justnum - endnum
            
      elif eql == 1:
         endnum = justnum

   
#  -----
#  | * |
#  -----
   elif that == '*':
      if endnum == 0 and justnum != '0':
         endnum = 1
      if eql == 0:
         endnum = endnum * justnum
      elif eql == 1:
         endnum = justnum
   
#  -----
#  | / |
#  -----
   elif that == '/':
      if eql == 0 and endnum != 0:
         endnum = endnum / justnum
      elif eql == 1 and endnum != 0:
         if count > 1:
            endnum = endnum / justnum
         else:
            endnum = justnum
      else:
         endnum = justnum
      what_type = 'f'

#  -------
#  | x^y |
#  -------
   elif that == '^':
      if endnum == 0 and justnum != '0':
         endnum = justnum
      elif endnum == 0 and justnum == '0':
         c_pressed()
      else:
         if eql == 0:
            endnum = justnum
         elif eql == 1:
            if count > 1:
               endnum = endnum ** justnum
               
            if count < 2:
               endnum = justnum

   num ,eql= '0',0
   count = count+1
   win.after(150, reset_color)

#+---------------------------------------------+
#| Calculate And Show numbers When (=) Pressed |
#+---------------------------------------------+
def equal():
   global mathsign, num, endnum, eql, invalid, what_type, count, first_time
   too_large = False
   calculation.config(font = ("Verdana", 20), width=18)
   if what_type == 'i':
      justnum = int(calculation.get())
   else:
      justnum = float(calculation.get())

#  -----
#  | + |
#  -----
   if mathsign == '+':
      endnum = endnum + justnum

#  -----
#  | - |
#  -----
   elif mathsign == '-':
      endnum = endnum - justnum

#  -----
#  | * |
#  ----- 
   elif mathsign == '*':
      if endnum == 0:
         endnum = 1
      eql = 1
      endnum = endnum * justnum

#  -----
#  | / |
#  -----
   elif mathsign == '/':
      what_type = 'f'
      if justnum != 0:
         endnum = endnum / justnum
      else:
         invalid = True
         endnum = 0

#  -------
#  | x^y |
#  -------
   elif mathsign == '^':
      if justnum != 0:
         if justnum < 101:
            endnum = endnum ** justnum
         else:
            too_large = True
      else:
         endnum = 0

#  +---------------------+
#  | Check number Digits |
#  +---------------------+
   a, b, c, newnum, check = 0, 0, 0, 0, False
   for i in (str(endnum)):
      if check == True:
         c = c+1
      else:
         a = a+1
      if check == True and i == '0':
         b = b+1
      if i == '.':
         check = True

#  +--------------------------------------------------------------+
#  | Check if there is just zero afte dot(.) make that num to int |
#  +--------------------------------------------------------------+
   if b == c and b != 0 and c != 0:
      newnum = str(endnum)
      endnum = int(newnum[:a-1])

#  +---------------------------------------------------+
#  | Check if result is too large make decimal smaller |
#  +---------------------------------------------------+
   elif c > 8 and a < 4:
      endnum = round(endnum,10)

   elif c > 6 and a <= 6 and a >= 4:
      endnum = round(endnum,8)

   elif c > 6 and a < 8 and a > 6:
      endnum = round(endnum,6)

   elif c > 6 and a <= 10 and a >= 8:
      endnum = round(endnum,4)

#  +------------------------------------------------+
#  | Check if result is too large make font smaller |
#  +------------------------------------------------+
   if len(str(endnum))+1 <= 18:
      calculation.config(font = ("Verdana", 20), width=18)

   elif len(str(endnum))+1 <= 20 and len(str(endnum))+1 > 18:
      calculation.config(font = ("Verdana", 16), width=24)

   elif len(str(endnum))+1 > 20 and len(str(endnum))+1 <= 25:
      calculation.config(font = ("Verdana", 14), width=26)

   elif len(str(endnum))+1 > 25:
      calculation.config(font = ("Verdana", 10), width=38)

#  +-------------------------------------------------------------------+
#  | Check if result is more that 36 digits Show 'Result is too Large' |
#  +-------------------------------------------------------------------+ 
   if len(str(endnum)) < 37:
      if invalid == False:
         screen.set(endnum)
      else:
         screen.set("Cant divide")
   else:
      screen.set("Result too large")
      endnum = 0
   if too_large == True:
      screen.set("Result too large")
      endnum = 0
      too_large = False

   num = str(endnum)
   count, eql, first_time = 0, 1, False
   win.after(150, reset_color)

#+------++------++------++------++------++------+
#| Main || Main || Main || Main || Main || Main |
#+------++------++------++------++------++------+

#................................................

#+--------------------------+
#| Make Window And Add Icon |
#+--------------------------+
win = tk.Tk()
win.title("Calculator")
win.resizable(width=False, height=False)
win.config(bg="gray75")
win.iconbitmap(r'calculator_icon.ico')


#+----------------------------------+
#| Bind Keyboard keys to Calculator |
#+----------------------------------+
win.bind("<Key>",key_pressed)
win.bind('<Return>',enter_pressed)
win.bind("<Escape>", esc_pressed)
win.bind("<BackSpace>", backspace_pressed)
win.bind('<Alt-F4>', alt_f4)

screen = tk.StringVar()
screen.set("0")

#+-----------+
#| Variables |
#+-----------+
endnum, eql, count, enterp = 0, 0, 0, 0
first_time = True
mathsign = str()
invalid = False
what_type = 'i'
num , dotnum= str(0), str(0)

#+--------+
#| Entery |
#+--------+
calculation = tk.Entry(win, textvariable = screen, state = 'readonly', font = ("Verdana", 20), bd = 0, insertwidth=8, width=18, justify=tk.RIGHT)
calculation.grid(columnspan=4,ipady=30,ipadx=3)

#+----------------------+
#| Make Numbers Buttons |
#+----------------------+
button1 = tk.Button(win, text='1', command=lambda: num_pressed(1), bg="gainsboro",bd=0, cursor = "hand2", padx=28, pady=12, font=("Helvetica", 14, "bold"))
button1.grid(row=2, column=0, sticky=tk.W)
button1.bind('<Enter>', on_enter)
button1.bind('<Leave>', on_leave)

button2 = tk.Button(win, text='2', command=lambda: num_pressed(2), bg="gainsboro",bd=0, cursor = "hand2", padx=28, pady=12, font=("Helvetica", 14, "bold"))
button2.grid(row=2, column=1, sticky=tk.W)
button2.bind('<Enter>', on_enter)
button2.bind('<Leave>', on_leave)

button3 = tk.Button(win, text='3', command=lambda: num_pressed(3), bg="gainsboro",bd=0, cursor = "hand2", padx=28, pady=12, font=("Helvetica", 14, "bold"))
button3.grid(row=2, column=2, sticky=tk.W)
button3.bind('<Enter>', on_enter)
button3.bind('<Leave>', on_leave)

button4 = tk.Button(win, text='4', command=lambda: num_pressed(4),bg="gainsboro",bd=0, cursor = "hand2", padx=28, pady=12, font=("Helvetica", 14, "bold"))
button4.grid(row=3, column=0, sticky=tk.W)
button4.bind('<Enter>', on_enter)
button4.bind('<Leave>', on_leave)

button5 = tk.Button(win, text='5', command=lambda: num_pressed(5), bg="gainsboro",bd=0, cursor = "hand2", padx=28, pady=12, font=("Helvetica", 14, "bold"))
button5.grid(row=3, column=1, sticky=tk.W)
button5.bind('<Enter>', on_enter)
button5.bind('<Leave>', on_leave)

button6 = tk.Button(win, text='6', command=lambda: num_pressed(6),bg="gainsboro",bd=0, cursor = "hand2", padx=28, pady=12, font=("Helvetica", 14, "bold"))
button6.grid(row=3, column=2, sticky=tk.W)
button6.bind('<Enter>', on_enter)
button6.bind('<Leave>', on_leave)

button7 = tk.Button(win, text='7', command=lambda: num_pressed(7),bg="gainsboro",bd=0, cursor = "hand2", padx=28, pady=12, font=("Helvetica", 14, "bold"))
button7.grid(row=4, column=0, sticky=tk.W)
button7.bind('<Enter>', on_enter)
button7.bind('<Leave>', on_leave)

button8 = tk.Button(win, text='8', command=lambda: num_pressed(8),bg="gainsboro",bd=0, cursor = "hand2", padx=28, pady=12, font=("Helvetica", 14, "bold"))
button8.grid(row=4, column=1, sticky=tk.W)
button8.bind('<Enter>', on_enter)
button8.bind('<Leave>', on_leave)

button9 = tk.Button(win, text='9', command=lambda: num_pressed(9),bg="gainsboro",bd=0, cursor = "hand2", padx=28, pady=12, font=("Helvetica", 14, "bold"))
button9.grid(row=4, column=2, sticky=tk.W)
button9.bind('<Enter>', on_enter)
button9.bind('<Leave>', on_leave)

button0 = tk.Button(win, text='0', command=lambda: num_pressed(0),bg="gainsboro",bd=0, cursor = "hand2", padx=28, pady=12, font=("Helvetica", 14, "bold"))
button0.grid(row=5, column=1, sticky=tk.W)
button0.bind('<Enter>', on_enter)
button0.bind('<Leave>', on_leave)
#---------------------

#+-------------------+
#| Make Math Buttons |
#+-------------------+
button_float = tk.Button(win, text='.', command=dot_pressed, bg="gainsboro",bd=0, cursor = "hand2", padx=31, pady=12, font=("Helvetica", 14, "bold"))
button_float.grid(row=5, column=2)
button_float.bind('<Enter>', on_enter)
button_float.bind('<Leave>', on_leave)

button_plus = tk.Button(win, text='+', command=lambda: math_pressed('+'), bg="gray75",bd=0, cursor = "hand2", padx=28, pady=12, font=("Helvetica", 14, "bold"))
button_plus.grid(row=4, column=3, sticky=tk.W)
button_plus.bind('<Enter>', on_enter_math)
button_plus.bind('<Leave>', on_leave_math)

button_minus = tk.Button(win, text='-', command=lambda: math_pressed('-'),bg="gray75",bd=0, cursor = "hand2", padx=27, pady=11, font=("Verdana", 14, "bold"))
button_minus.grid(row=3, column=3, sticky=tk.W)
button_minus.bind('<Enter>', on_enter_math)
button_minus.bind('<Leave>', on_leave_math)

button_multiply = tk.Button(win, text='×', command=lambda: math_pressed('*'),bg="gray75",bd=0, cursor = "hand2", padx=28, pady=12, font=("Helvetica", 14, "bold"))
button_multiply.grid(row=2, column=3, )
button_multiply.bind('<Enter>', on_enter_math)
button_multiply.bind('<Leave>', on_leave_math)

button_division = tk.Button(win, text='÷', command=lambda: math_pressed('/'),  bg="gray75",bd=0, cursor = "hand2", padx=28, pady=12, font=("Helvetica", 14, "bold"))
button_division.grid(row=1, column=3, )
button_division.bind('<Enter>', on_enter_math)
button_division.bind('<Leave>', on_leave_math)

button_equal = tk.Button(win, text='=', command= equal, bg='gray75',bd=0, cursor = "hand2", padx=26, pady=8, font=("Arial", 17))
button_equal.grid(row=5, column=3, )
button_equal.bind('<Enter>', on_enter_math)
button_equal.bind('<Leave>', on_leave_math)

button_percent = tk.Button(win, text='-/+', command=change_pressed, bg="gray75",bd=0, cursor = "hand2", padx=22, pady=12, font=("Helvetica", 14))
button_percent.grid(row=1, column=0, )
button_percent.bind('<Enter>', on_enter_math)
button_percent.bind('<Leave>', on_leave_math)

button_clear = tk.Button(win, text='C', command = c_pressed ,bg='gainsboro',bd=0, cursor = "hand2", padx=27, pady=12, font=("Helvetica", 14))
button_clear.grid(row=5, column=0)
button_clear.bind('<Enter>', on_enter)
button_clear.bind('<Leave>', on_leave)

button_sqrt = tk.Button(win, text='√', command=sqrt_pressed, bg="gray75",bd=0, cursor = "hand2", padx=28, pady=12, font=("Helvetica", 14, "bold"))
button_sqrt.grid(row=1, column=1, sticky=tk.W)
button_sqrt.bind('<Enter>', on_enter_math)
button_sqrt.bind('<Leave>', on_leave_math)

button_x = tk.Button(win, text='x^y', command=lambda: math_pressed('^'), bg="gray75",bd=0, cursor = "hand2", padx=21, pady=12, font=("Helvetica", 14))
button_x.grid(row=1, column=2, sticky=tk.W)
button_x.bind('<Enter>', on_enter_math)
button_x.bind('<Leave>', on_leave_math)
#---------------------

win.mainloop()
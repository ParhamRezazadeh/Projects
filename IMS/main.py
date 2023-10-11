from datetime import datetime , timedelta
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
import datetime as dt
import tkinter as tk
import sqlite3

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib, numpy, sys
matplotlib.use('TkAgg')

class Ims:
    def __init__(self):
        self.selected_file = ''
        self.canvas = ['', '']
        self.check = None
        self.code = 0
        self.draw()
        
    def draw(self):
        self.win=tk.Tk()
        self.win.title('Inventory Management Software')
        self.win.resizable(width=False, height=False)
        self.win.iconbitmap(r'image/icon2.ico')
        self.win.config(bg = 'white')
        self.screen_width = self.win.winfo_screenwidth()
        self.screen_width = int((self.screen_width/3)*2)
        self.screen_height = self.win.winfo_screenheight()
        self.screen_height = int((self.screen_height/3)*2)
        self.win.geometry(f'{self.screen_width}x{self.screen_height}+{int(self.screen_width/4)}+{int(self.screen_height/4)}')
        self.win.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.frame_button = tk.Frame(self.win, bg="#212121", height = self.screen_height/16, width=self.screen_width)
        self.frame_button.pack(anchor=tk.W, expand=False, side=tk.TOP)
        
        self.top_label = tk.Label(self.win, text = 'Sold Out Stuff Bar Chart',bg = 'white',fg = '#007355', font=('SegoeUI', self.screen_width//60))
        self.top_label.pack(pady = self.screen_height/32)

        self.button_home = tk.Button(self.win, text = 'Home', bg='#007355', fg='white', bd = 0, font=('SegoeUI', self.screen_width//90), command = self.button_home_pressed)
        self.button_home.place(x= 0,y=0, width=self.screen_width/8, height=self.screen_height/16)

        self.button_available = tk.Button(self.win, text = 'Available', bg='#212121', fg='white', bd = 0, font=('SegoeUI', self.screen_width//90), command = self.button_available_pressed)
        self.button_available.place(x = (self.screen_width/8), y = 0, width=self.screen_width/8, height=self.screen_height/16)
        
        self.button_sold_out = tk.Button(self.win, text = 'Sold Out', bg='#212121', fg='white', bd = 0, font=('SegoeUI', self.screen_width//90), command = self.button_sold_out_pressed)
        self.button_sold_out.place(x = 2 * (self.screen_width/8) , y = 0, width=self.screen_width/8, height=self.screen_height/16)

        self.button_add = tk.Button(self.win, text = 'Add', bg='#212121', fg='white', bd = 0, font=('SegoeUI', self.screen_width//90), command=lambda: self.open_win2('add'))

        self.search_frame = tk.Frame(self.win, highlightbackground='black', highlightthickness=1, bg = 'white')
        
        val = ["All", 'Audio Equipment', 'TV', 'Tools', 'kids cloth', 'Menswear', 'Ladieswear', 'kitchenware', 'Carpet', 'Furniture', 'Decorative', 'Nuts',
               'Fruit', 'vegetables', 'Flowers', 'Plants', 'Stationery', 'Travel Accessories', 'Sanitary', 'Makeup', 'Bag', 'Shoes', 'Toys', 'Sports']
        self.search_combobox = ttk.Combobox(self.win, textvariable = str(),values= val, state='readonly')
        
        val = ["All", "1 Days Ago" ,"3 Days Ago" , "7 Days Ago", "30 Days Ago"]
        self.time_combobox = ttk.Combobox(self.win, textvariable = str(),values= val, state='readonly')
        
        self.search_entry = ttk.Entry(self.win, font=('SegoeUI', self.screen_width//90))
        self.button_search = tk.Button(self.win, text = 'Search', bg='#007355', fg='white', bd = 0, font=('SegoeUI', self.screen_width//90), command = self.search)

        columns = ('Code', 'Name',  'Price', 'Numbers')
        self.available_tree = ttk.Treeview(self.win, columns=columns, height=self.screen_height//20)

        style = ttk.Style()
        style.configure("Treeview", rowheight = int((self.screen_height - (self.screen_height/6) - self.screen_height/28)/5), font=('SegeoeUI', self.screen_width//100))
        style.configure("Treeview.Heading", font=('SegeoeUI', self.screen_width//90))
        # style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        
        self.available_tree.column('#0', minwidth=int(self.screen_width/10), width = int(self.screen_width/10), stretch=False, anchor = 'center')
        
        self.available_tree.heading('Code', text = 'Code')
        self.available_tree.column('Code', minwidth=int(self.screen_width/12), width = int(self.screen_width/12), stretch=False, anchor = 'center')
        
        self.available_tree.heading('Name', text = 'Name')
        self.available_tree.column('Name', minwidth=int(self.screen_width/4), width = int(self.screen_width/4), stretch=False, anchor = 'center')
        
        self.available_tree.heading('Price', text = 'Price')
        self.available_tree.column('Price', minwidth=int(self.screen_width/4), width = int(self.screen_width/4), stretch=False, anchor = 'center')
        
        self.available_tree.heading('Numbers', text = 'Numbers')
        self.available_tree.column('Numbers', minwidth=int(self.screen_width/5.24), width = int(self.screen_width/5.24), stretch=False, anchor = 'center')

        self.scrollbar = ttk.Scrollbar(self.win, orient=tk.VERTICAL, command = self.available_tree.yview)
        self.available_tree.configure(yscroll=self.scrollbar.set)

        columns = ('Code', 'Name',  'Price', 'Numbers')
        self.sold_out_tree = ttk.Treeview(self.win, columns=columns, show='headings', height=self.screen_height//20)

        self.sold_out_tree.heading('Code', text = 'Code')
        self.sold_out_tree.column('Code', minwidth=int(self.screen_width/8), width = int(self.screen_width/8), stretch=False, anchor = 'center')
        
        self.sold_out_tree.heading('Name', text = 'Name')
        self.sold_out_tree.column('Name', minwidth=int(self.screen_width/4), width = int(self.screen_width/4), stretch=False, anchor = 'center')
        
        self.sold_out_tree.heading('Price', text = 'Price')
        self.sold_out_tree.column('Price', minwidth=int(self.screen_width/4), width = int(self.screen_width/4), stretch=False, anchor = 'center')
        
        self.sold_out_tree.heading('Numbers', text = 'Numbers')
        self.sold_out_tree.column('Numbers', minwidth=int(self.screen_width/4)-1, width = int(self.screen_width/4)-1, stretch=False, anchor = 'center')

        self.scrollbar2 = ttk.Scrollbar(self.win, orient=tk.VERTICAL, command = self.sold_out_tree.yview)
        self.sold_out_tree.configure(yscroll=self.scrollbar2.set)

        self.frame_button2 = tk.Frame(self.win, bg="#007355", width = self.screen_width/8, height=self.screen_height)
        self.info_button = tk.Button(self.win, text = 'More Info', bg='#007355', fg='white', bd = 0, font=('SegoeUI', self.screen_width//90), command = self.more_info)
        self.edit_button = tk.Button(self.win, text = 'Edit Item', bg='#007355', fg='white', bd = 0, font=('SegoeUI', self.screen_width//90), command=lambda: self.open_win2('edit'))
        self.sell_some_button = tk.Button(self.win, text = 'Sell Item', bg='#007355', fg='white', bd = 0, font=('SegoeUI', self.screen_width//90), command = self.show_sell)
        self.delete_button = tk.Button(self.win, text = 'Delete', bg='#007355', fg='white', bd = 0, font=('SegoeUI', self.screen_width//90), command = self.delete)

        self.load_data()
        self.win.mainloop()

    def load_data(self):
        self.count = 0
        self.connection = sqlite3.connect('data/data.db')
        self.connection.execute(''' CREATE TABLE IF NOT EXISTS available
            (code INT, category TEXT, name TEXT, price TEXT, numbers TEXT, column TEXT, row TEXT,date TEXT, image BLOB);''')
        self.cursor = self.connection.execute("SELECT * from available")
        mylist = []
        self.image_list = []
        for row in self.cursor:
            filename = f'data/image/{self.count}.png'
            self.writeTofile(row[-1], filename)
            
            self.image_list.append(Image.open(filename))
            self.image_list[-1]= self.image_list[-1].resize((int(self.screen_width/14),int(self.screen_width/14)), Image.ANTIALIAS)
            self.image_list[-1] = ImageTk.PhotoImage(self.image_list[-1])
            self.available_tree.insert(parent="",index="end",image = self.image_list[-1], values = [self.count+1, row[2], row[3], row[4]])
            self.count += 1
            
            mylist.append([self.count, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
        
        self.cursor.execute('DELETE FROM available;',)
        self.connection.commit()
        
        for row in mylist:
            command = "INSERT INTO available (code,category,name,price,numbers,column,row,date,image) values (?,?,?,?,?,?,?,?,?)"
            data = tuple(row)
            self.cursor.execute(command, data)
            self.connection.commit()
            
        self.sold_out_count = 0
        self.connection.execute(''' CREATE TABLE IF NOT EXISTS sold_out
            (code INT, category TEXT, name TEXT, price TEXT, numbers TEXT, column TEXT, row TEXT,date TEXT, image BLOB);''')
        self.cursor = self.connection.execute("SELECT * from sold_out")
        mylist = []
        for row in self.cursor:
            self.sold_out_tree.insert('', tk.END, values = [self.sold_out_count+1, row[2], row[3], row[4]])
            self.sold_out_count += 1
            
            mylist.append([self.sold_out_count, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
        
        self.cursor.execute('DELETE FROM sold_out;',)
        self.connection.commit()
        
        for row in mylist:
            command = "INSERT INTO sold_out (code,category,name,price,numbers,column,row,date,image) values (?,?,?,?,?,?,?,?,?)"
            data = tuple(row)
            self.cursor.execute(command, data)
            self.connection.commit()
            
        self.draw_barchart(list(self.connection.execute("SELECT * from sold_out")), 'Most Sell', self.screen_width, 4, 0) 
        self.draw_barchart(list(self.connection.execute("SELECT * from sold_out")), 'Most Price', self.screen_width/2, 3, 1)
        self.canvas[0].draw()
        self.canvas[1].draw()

    def button_home_pressed(self):
        self.button_home.config(bg = '#007355')
        self.button_available.config(bg = '#212121')
        self.button_sold_out.config(bg = '#212121')

        self.available_tree.place_forget()
        self.sold_out_tree.place_forget()
        self.button_add.place_forget()
        
        self.frame_button.config(width = self.screen_width)
        self.frame_button2.place_forget()
        self.info_button.place_forget()
        self.edit_button.place_forget()
        self.sell_some_button.place_forget()
        self.delete_button.place_forget()
        
        self.search_frame.place_forget()
        self.search_combobox.place_forget()
        self.button_search.place_forget()
        self.search_entry.place_forget()
        self.time_combobox.place_forget()
        
        self.draw_barchart(list(self.connection.execute("SELECT * from sold_out")), 'Most Sell', self.screen_width, 4, 0) 
        self.draw_barchart(list(self.connection.execute("SELECT * from sold_out")), 'Most Price', self.screen_width/2, 3, 1)

    def button_available_pressed(self):
        self.check = 'available'
        self.sold_out_tree.place_forget()
        self.available_tree.place(x=0, y=self.screen_height/16, width= self.screen_width - (self.screen_width/8), height= self.screen_height - (self.screen_height/6))
        # self.scrollbar.place(x = self.screen_width - ((self.screen_width/64)*9) - 1, y =(self.screen_height/16)+1, width = self.screen_width/64, height = self.screen_height - (self.screen_height/6)-2)
        
        self.update_buttons()
        self.button_available.config(bg = '#007355')
        self.button_sold_out.config(bg = '#212121')
    
    def button_sold_out_pressed(self):
        self.check = 'sold_out'
        self.sold_out_tree.place(x=0, y=self.screen_height/16, width= self.screen_width - (self.screen_width/8), height= self.screen_height - (self.screen_height/6))
        self.available_tree.place_forget()
        
        self.update_buttons()
        self.button_available.config(bg = '#212121')
        self.button_sold_out.config(bg = '#007355')

        self.delete_button.place(x = self.screen_width - self.screen_width / 8, y = (self.screen_height/6)*2, width=self.screen_width/8, height=self.screen_height/6)
        self.sell_some_button.place_forget()
        
    def update_buttons(self):
        self.frame_button.config(width = self.screen_width - (self.screen_width / 8))
        self.frame_button2.place(x = self.screen_width - self.screen_width / 8, y = 0)
        self.info_button.place(x = self.screen_width - self.screen_width / 8, y = (self.screen_height/6)*0, width=self.screen_width/8, height=self.screen_height/6)
        self.edit_button.place(x = self.screen_width - self.screen_width / 8, y = (self.screen_height/6)*1, width=self.screen_width/8, height=self.screen_height/6)
        self.sell_some_button.place(x = self.screen_width - self.screen_width / 8, y = (self.screen_height/6)*2, width=self.screen_width/8, height=self.screen_height/6)
        self.delete_button.place(x = self.screen_width - self.screen_width / 8, y = (self.screen_height/6)*3, width=self.screen_width/8, height=self.screen_height/6)
        self.button_add.place(x= 3 * (self.screen_width/8) , y = 0, width=self.screen_width/8, height=self.screen_height/16)
        
        self.search_frame.place(x = 0,y = self.screen_height - self.screen_height/8, width=self.screen_width - self.screen_width/8, height=self.screen_height/8)
        self.time_combobox.place(x = self.screen_width/64, y = self.screen_height - self.screen_height/12 + self.screen_height/128, width=self.screen_width/8, height=self.screen_height/16 - self.screen_height/64)
        self.search_combobox.place(x = self.screen_width/8 + self.screen_width/32, y = self.screen_height - self.screen_height/12 + self.screen_height/128, width=self.screen_width/8, height=self.screen_height/16 - self.screen_height/64)
        self.button_search.place(x= ((self.screen_width/8)*5)+ self.screen_width/24,y=self.screen_height - self.screen_height/12, width=self.screen_width/8, height=self.screen_height/16)
        self.search_entry.place(x= self.screen_width/4 + self.screen_width/24 + self.screen_width/128,y = self.screen_height - self.screen_height/12, width=(self.screen_width - (self.screen_width/2)) - self.screen_width/8 - self.screen_width/64, height=self.screen_height/16)
        self.button_home.config(bg = '#212121')
        
        for item in self.canvas[1].get_tk_widget().find_all():
            self.canvas[1].get_tk_widget().delete(item)
        self.canvas[1].get_tk_widget().place_forget()

        for item in self.canvas[0].get_tk_widget().find_all():
            self.canvas[0].get_tk_widget().delete(item)
        self.canvas[0].get_tk_widget().place_forget()
        
    def draw_barchart(self, element, string, location, index, number):
        for n in range(len(element)-1, 0, -1):
            for i in range(n):
                if int(element[i][index]) > int(element[i+1][index]):
                    element[i], element[i + 1] = element[i + 1], element[i]
        element.reverse()
        
        y = []
        x = []
        n = 0
        for i in element:
            y.append(int(i[index]))
            if i[2] in x:
                a = str(i[2])+'-'+str(n)
            else:
                a = i[2]
            x.append(a)
            n += 1
            if n == 6:
                break
        
        f = plt.figure()
        plt.bar(x, y, color = '#007355')
        plt.title(string)
        plt.xlabel("Names")
        
        for i in range(len(x)):
            plt.text(i, y[i], y[i],ha = 'center', color = 'black')

        self.canvas[number] = FigureCanvasTkAgg(f, master=self.win)
        self.canvas[number].get_tk_widget().place(x =self.screen_width - location, y = self.screen_height/5, width=self.screen_width/2, height=self.screen_height/1.5)

    def on_closing(self):
        self.connection.close()
        self.win.destroy()
            
    def search(self):
        if self.search_combobox.get() == '' or self.search_combobox.get() == 'All':
            a = 'name'
            b = self.search_entry.get()
        else:
            if self.search_entry.get() != '':
                a = 'name'
                b = self.search_entry.get()
            else:
                a = 'category'
                b = self.search_combobox.get()
                
        c = 9999
        if self.time_combobox.get() != '' and self.time_combobox.get() != 'All':
            c = str(self.time_combobox.get()).split()[0]
        
        if self.check == 'available':
            cursor = self.connection.execute(f"SELECT * FROM available WHERE {a} LIKE ?", ('%' + b + '%',))
            for i in self.available_tree.get_children():
                self.available_tree.delete(i)
        else:
            cursor = self.connection.execute(f"SELECT * FROM sold_out WHERE {a} LIKE ?", ('%' + b + '%',))
            for i in self.sold_out_tree.get_children():
                self.sold_out_tree.delete(i)
        
        now_time = dt.datetime.now()
        fetch = cursor.fetchall()
        for row in fetch:
            datetime_object = datetime.strptime(row[-2]+':00.000000', '%Y-%m-%d %H:%M:%S.%f')
            difference = now_time - datetime_object
            
            if self.search_combobox.get() != '' and self.search_combobox.get() != 'All':
                if row[1] == self.search_combobox.get():
                    if int(difference.days) <= int(c):
                        if self.check == 'available':
                            self.available_tree.insert('', tk.END, values = ['', row[0], row[2], row[3], row[4]])
                        else:
                            self.sold_out_tree.insert('', tk.END, values = [row[0], row[2], row[3], row[4]])
            else:
                if int(difference.days) <= int(c):
                    if self.check == 'available':
                        self.available_tree.insert('', tk.END, values = ['', row[0], row[2], row[3], row[4]])
                    else:
                        self.sold_out_tree.insert('', tk.END, values = [row[0], row[2], row[3], row[4]])
            
    def more_info(self):
        try:
            if self.check == 'available':
                self.item_details = self.available_tree.item(self.available_tree.selection()[0])
                i = list(self.cursor.execute("SELECT * FROM available WHERE code=?", (int(self.item_details['values'][1]),)))
            else:
                self.item_details = self.sold_out_tree.item(self.sold_out_tree.selection()[0])
                i = list(self.cursor.execute("SELECT * FROM sold_out WHERE code=?", (int(self.item_details['values'][0]),)))
            
            self.win_info = tk.Tk()
            self.win_info.title('Product Information')
            self.win_info.resizable(width=False, height=False)
            self.win_info.geometry(f'{int(self.screen_width/4)}x{int(self.screen_height/2)}+{int(self.screen_width/1.6)}+{int(self.screen_height/2)}')
            self.win_info.config(bg = 'white')
            
            tk.Label(self.win_info, bg = 'white', text = f'Code  :  {i[0][0]}', font=('SegoeUI', self.screen_width//100)).pack(pady=10)
            tk.Label(self.win_info, bg = 'white', text = f'Category  :  {i[0][1]}', font=('SegoeUI', self.screen_width//100)).pack(pady=10)
            tk.Label(self.win_info, bg = 'white', text = f'Name  :  {i[0][2]}', font=('SegoeUI', self.screen_width//100)).pack(pady=10)
            tk.Label(self.win_info, bg = 'white', text = f'Price  :  {i[0][3]}', font=('SegoeUI', self.screen_width//100)).pack(pady=10)
            tk.Label(self.win_info, bg = 'white', text = f'Numbers  :  {i[0][4]}', font=('SegoeUI', self.screen_width//100)).pack(pady=10)
            tk.Label(self.win_info, bg = 'white', text = f'Column  :  {i[0][5]}', font=('SegoeUI', self.screen_width//100)).pack(pady=10)
            tk.Label(self.win_info, bg = 'white', text = f'Row  :  {i[0][6]}', font=('SegoeUI', self.screen_width//100)).pack(pady=10)
            tk.Label(self.win_info, bg = 'white', text = f'Add Date  :  {i[0][7]}', font=('SegoeUI', self.screen_width//100)).pack(pady=10)
        except:
            self.message()
            
    def message(self):
        tk.messagebox.showinfo('Error', 'Please Select A Product From List', icon='info')
            
    def open_win2(self, get):
        try:
            self.win2.destroy()
        except:
            pass
        try:
            if get != 'add':
                if self.check == 'available':
                    self.item_details = self.available_tree.item(self.available_tree.selection()[0])
                else:
                    self.item_details = self.sold_out_tree.item(self.sold_out_tree.selection()[0])
        except:
            self.message()
            return

        self.win2=tk.Tk()
        self.win2.resizable(width=False, height=False)
        self.win2.geometry(f'{int(self.screen_width/3)}x{int(self.screen_height/1.4)}+{int(self.screen_width/1.7)}+{int(self.screen_height/2.5)}')
        self.win2.config(bg = 'white')

        self.win2_top_label = tk.Label(self.win2,bg = 'white', text = 'Enter New Stuff Informations', font=('SegoeUI', self.screen_width//90))
        self.win2_top_label.pack(pady = 5)

        self.frame = tk.Frame(self.win2, highlightbackground='#007355', highlightthickness=1)
        self.frame.place(x = self.screen_width/128, y = self.screen_height/14, width = self.screen_width/3 - (self.screen_width/64), height=self.screen_height/4.3)

        tk.Label(self.frame, text = 'Information', font=('SegoeUI', self.screen_width//95)).pack(pady = 10)

        tk.Label(self.win2, text = 'Category', font=('SegoeUI', self.screen_width//110)).place(x = self.screen_width/64, y = self.screen_height/6.5)

        val = ['Audio Equipment', 'TV', 'Tools', 'kids cloth', 'Menswear', 'Ladieswear', 'kitchenware', 'Carpet', 'Furniture', 'Decorative', 'Nuts',
               'Fruit', 'vegetables', 'Flowers', 'Plants', 'Stationery', 'Travel Accessories', 'Sanitary', 'Makeup', 'Bag', 'Shoes', 'Toys', 'Sports']
        self.combobox = ttk.Combobox(self.win2, textvariable = str(),values= val, state='readonly')
        self.combobox.place(x = self.screen_width/13, y = self.screen_height/6.5 + self.screen_height/360, width = self.screen_width/14)

        tk.Label(self.win2, text = 'Name', font=('SegoeUI', self.screen_width//110)).place(x = self.screen_width/5.5, y = self.screen_height/6.5)
        self.name_entry = ttk.Entry(self.win2)
        self.name_entry.place(x = self.screen_width/4.2, y = self.screen_height/6.5 + self.screen_height/360, width = self.screen_width/14)

        tk.Label(self.win2, text = 'Price', font=('SegoeUI', self.screen_width//110)).place(x = self.screen_width/64, y = self.screen_height/4.2)
        self.price_entry =  ttk.Entry(self.win2)
        self.price_entry.place(x = self.screen_width/13, y = self.screen_height/4.2 + self.screen_height/360, width = self.screen_width/14)

        tk.Label(self.win2, text = 'Number', font=('SegoeUI', self.screen_width//110)).place(x = self.screen_width/5.5, y = self.screen_height/4.2)
        self.count_entry =  ttk.Entry(self.win2)
        self.count_entry.place(x = self.screen_width/4.2, y = self.screen_height/4.2 + self.screen_height/360, width = self.screen_width/14)

        self.frame2 = tk.Frame(self.win2, highlightbackground='#007355', highlightthickness=1, height = int(self.screen_height//6.5), width = int(self.screen_width//3.1))
        self.frame2.place(x = self.screen_width/128, y = self.screen_height/3.2 , width = self.screen_width/3 - (self.screen_width/64), height=self.screen_height/6.2)

        tk.Label(self.frame2, text = 'Location', font=('SegoeUI', self.screen_width//95)).pack(pady = 10)

        tk.Label(self.win2, text = 'Column', font=('SegoeUI', self.screen_width//110)).place(x = self.screen_width/64, y = self.screen_height/2.5)
        self.column_entry = ttk.Entry(self.win2, width = int(self.screen_width/80))
        self.column_entry.place(x = self.screen_width/13, y = self.screen_height/2.5 + self.screen_height/360, width = self.screen_width/14)

        tk.Label(self.win2, text = 'Row', font=('SegoeUI', self.screen_width//110)).place(x = self.screen_width/5.2, y = self.screen_height/2.5)
        self.row_entry = ttk.Entry(self.win2, width = int(self.screen_width/80))
        self.row_entry.place(x = self.screen_width/4.2, y = self.screen_height/2.5 + self.screen_height/360, width = self.screen_width/14)

        self.frame3 = tk.Frame(self.win2, highlightbackground='#007355', highlightthickness=1)
        self.frame3.place(x = self.screen_width/128, y = self.screen_height/2.05, width = self.screen_width/3 - (self.screen_width/64), height=self.screen_height/7.5)

        self.image_label = tk.Label(self.frame3, text = 'Image', font=('SegoeUI', self.screen_width//95))
        self.image_label.pack(pady = 10)
        self.image_button = tk.Button(self.win2, text = 'Select Image', bg = '#007355', fg='white', bd = 0, font=('SegoeUI', self.screen_width//100, 'bold'), command = self.select_file)
        self.image_button.place(x = self.screen_width/56, y = self.screen_height/1.8, width=self.screen_width/3.35, height=self.screen_height/26)

        if get == 'add':
            self.win2.title('Add Product')
            self.add_save_button = tk.Button(self.win2, text = 'Add', bg = '#007355', fg='white', bd = 0, font=('SegoeUI', self.screen_width//90, 'bold'), width=self.screen_width//100, command = self.add_button_pressed)
            self.add_save_button.pack(side = tk.BOTTOM, pady = self.screen_height/48)
            
            self.win2_top_label.config(text = 'Enter New Stuff Informations')
            self.image_label.config(text = 'Image')
            self.image_button.config(state= 'normal', text = 'Select Image')
            
        else:
            self.win2.title('Edit Product')
            
            if self.check == 'available':
                i = list(self.cursor.execute("SELECT * FROM available WHERE code=?", (int(self.item_details['values'][1]),)))
            else:
                i = list(self.cursor.execute("SELECT * FROM sold_out WHERE code=?", (int(self.item_details['values'][0]),)))
                
            self.combobox.set(i[0][1])
            self.name_entry.insert(0, i[0][2])
            self.price_entry.insert(0, i[0][3])
            self.count_entry.insert(0, i[0][4])
            self.column_entry.insert(0, i[0][5])
            self.row_entry.insert(0, i[0][6])
            
            self.win2_top_label.config(text = 'Edit Stuff Informations')
            self.edit_save_button = tk.Button(self.win2, text = 'Save', bg = '#007355', fg='white', bd = 0, font=('SegoeUI', self.screen_width//90, 'bold'), width=self.screen_width//100, command = self.edit_button_pressed)
            self.edit_save_button.pack(side = tk.BOTTOM, pady = self.screen_height/48)
            self.image_label.config(text = 'Image (Disable)')
            self.image_button.config(state= 'disable', text = 'Disable')
            
    def edit_button_pressed(self):
        if self.check == 'available':
            self.cursor.execute(f'''UPDATE available SET category = '{self.combobox.get()}', name = '{self.name_entry.get()}', price = '{self.price_entry.get()}',
                                numbers = '{self.count_entry.get()}', column = '{self.column_entry.get()}', row = '{self.row_entry.get()}' WHERE code = {self.item_details['values'][1]};''')
            self.available_tree.item(self.available_tree.selection()[0], text = self.item_details['text'], values = ('',self.item_details['values'][1], self.name_entry.get(), self.price_entry.get(), self.count_entry.get()))
        else:
            self.cursor.execute(f'''UPDATE sold_out SET category = '{self.combobox.get()}', name = '{self.name_entry.get()}', price = '{self.price_entry.get()}',
                                numbers = '{self.count_entry.get()}', column = '{self.column_entry.get()}', row = '{self.row_entry.get()}' WHERE code = {self.item_details['values'][0]};''')
            self.sold_out_tree.item(self.sold_out_tree.selection()[0], text = self.item_details['text'], values = (self.item_details['values'][0], self.name_entry.get(), self.price_entry.get(), self.count_entry.get()))
            
        self.connection.commit()
        self.win2.destroy()

    def select_file(self):
        self.selected_file = filedialog.askopenfilename()
        self.image_button.config(text = self.selected_file, font=('SegoeUI', self.screen_width//140), width=self.screen_width//24)
        self.convertToBinaryData()

    def convertToBinaryData(self):
        f = open(self.selected_file, mode = 'rb')
        self.blobdata = f.read()
        f.close()
        
    def writeTofile(self, data, filename):
        with open(filename, 'wb') as file:
            file.write(data)

    def add_button_pressed(self):
        if self.check == 'available':
            self.count += 1
            self.available_tree.insert('', tk.END, values = ['', self.count, self.name_entry.get(),self.price_entry.get(),self.count_entry.get()])
            
            command = "INSERT INTO available (code,category,name,price,numbers,column,row,date,image) values (?,?,?,?,?,?,?,?,?)"
            data = self.count,self.combobox.get(), self.name_entry.get(),self.price_entry.get(),self.count_entry.get(),self.column_entry.get(),self.row_entry.get(),str(dt.datetime.now())[:-10],self.blobdata

        else:
            self.sold_out_count += 1
            self.sold_out_tree.insert('', tk.END, values = [self.sold_out_count, self.name_entry.get(),self.price_entry.get(),self.count_entry.get()])
            
            command = "INSERT INTO sold_out (code,category,name,price,numbers,column,row,date,image) values (?,?,?,?,?,?,?,?,?)"
            data = self.count,self.combobox.get(), self.name_entry.get(),self.price_entry.get(),self.count_entry.get(),self.column_entry.get(),self.row_entry.get(),str(dt.datetime.now())[:-10],self.blobdata
        
        self.cursor.execute(command, data)
        self.connection.commit()
        self.win2.destroy()

    def delete(self):
        msg_box = tk.messagebox.askquestion('Delete Product', 'Are you sure you want delete this stuff ?', icon='question')
        if msg_box == 'yes':
            if self.check == 'available':
                self.item_details = self.available_tree.item(self.available_tree.selection()[0])
                self.cursor.execute(f"DELETE FROM available WHERE code = {self.item_details['values'][1]}")
                self.available_tree.delete(self.available_tree.selection()[0])

            else:
                self.item_details = self.sold_out_tree.item(self.sold_out_tree.selection()[0])
                self.cursor.execute(f"DELETE FROM sold_out WHERE code = {self.item_details['values'][0]}")
                self.sold_out_tree.delete(self.sold_out_tree.selection()[0])
            self.connection.commit()
                
            
    def show_sell(self):
        try:
            self.item_details = self.available_tree.item(self.available_tree.selection()[0])
            self.sell_win=tk.Tk()
            self.sell_win.title('Sell Product')
            self.sell_win.resizable(width=False, height=False)
            self.sell_win.geometry(f'{int(self.screen_width/3)}x{int(self.screen_height/3)}+{int(self.screen_width/1.7)}+{int(self.screen_height/2)}')

            tk.Label(self.sell_win, text = 'Enter The Amount To Sell', font=('SegoeUI', self.screen_width//100)).pack(pady = self.screen_height/64)
            self.sell_count_entry = ttk.Entry(self.sell_win, font=('SegoeUI', self.screen_width//100))
            self.sell_count_entry.place(x = self.screen_width/12,y = self.screen_height/12 - self.screen_height/128, width= self.screen_width/6, height=self.screen_height/28)
            
            tk.Label(self.sell_win, text = 'Enter Sell Price', font=('SegoeUI', self.screen_width//100)).pack(pady = self.screen_height/12 - self.screen_height/64)
            self.sell_price_entry = ttk.Entry(self.sell_win, font=('SegoeUI', self.screen_width//100))
            self.sell_price_entry.place(x = self.screen_width/12,y = self.screen_height/5- self.screen_height/64, width= self.screen_width/6, height=self.screen_height/28)
            
            self.sell_save_button = tk.Button(self.sell_win, text = 'Save', bg = '#007355', fg='white', bd = 0, font=('SegoeUI', self.screen_width//90, 'bold'), command = self.sell)
            self.sell_save_button.place(x = self.screen_width/12,y = self.screen_height/3 - (self.screen_height/64)*5, width= self.screen_width/6, height=self.screen_height/22)
        except:
            self.message()
            
    def sell(self):
        if int(self.sell_count_entry.get()) > 0:
            new_number = str(int(self.item_details['values'][4]) - int(self.sell_count_entry.get()))
            
            self.cursor.execute(f'''UPDATE available SET numbers = '{new_number}' WHERE code = {self.item_details['values'][1]};''')
            self.available_tree.item(self.available_tree.selection()[0], text = self.item_details['text'], values = ('', self.item_details['values'][1], self.item_details['values'][2], self.item_details['values'][3], new_number))
            self.sold_out_tree.insert('', tk.END, values = [self.item_details['values'][1], self.item_details['values'][2], self.sell_price_entry.get(), self.sell_count_entry.get()])

            row = list(self.cursor.execute("SELECT * FROM available WHERE code=?", (int(self.item_details['values'][1]),)))
            command = "INSERT INTO sold_out (code,category,name,price,numbers,column,row,date,image) values (?,?,?,?,?,?,?,?,?)"
            data = row[0][0], row[0][1], row[0][2], self.sell_price_entry.get(), self.sell_count_entry.get(), row[0][5], row[0][6], str(dt.datetime.now())[:-10], row[0][8]
            self.cursor.execute(command, data)

            self.connection.commit()
            self.sell_win.destroy()
        else:
            tk.messagebox.showinfo('Error', 'Only Positive Numbers Are Acceptable', icon='info')
            


# ------------ LOGIN ------------ #
class Login:
    def __init__(self):
        self.check = 1
        self.check_entry = False
        self.load_data()
        self.draw()
        
    def load_data(self):
        self.win=tk.Tk()
        self.win.title('IMS Login')
        self.screen_width = self.win.winfo_screenwidth()
        self.screen_height = self.win.winfo_screenheight()
        self.win.geometry(f'600x400+{(self.screen_width-600)//2}+{(self.screen_height-400)//2}')
        self.win.iconbitmap(r'image/icon.ico')
        self.win.resizable(width=False, height=False)
        self.win.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.background_canvas= tk.Canvas(self.win, width= 600, height= 400)

        self.password_entry = tk.Entry(self.win, bd=0, highlightthickness=0, font=("Segoe UI", 12), fg='#b4c1c8')
        self.password_entry.bind('<FocusIn>', self.on_entry_click_entry)
        self.password_entry.bind('<FocusOut>', self.on_focusout_entry)
        self.password_entry.insert(0, "Enter Password")

        self.password_entry2 = tk.Entry(self.win, bd=0, highlightthickness=0, font=("Segoe UI", 12), fg='#b4c1c8')
        self.password_entry2.bind('<FocusIn>', self.on_entry_click_entry2)
        self.password_entry2.bind('<FocusOut>', self.on_focusout_entry2)
        self.password_entry2.insert(0, "New Password")

        self.show_button = tk.Button(self.win, text = 'Show', bd = 0, bg = 'white', font=("Segoe UI", 11), command = self.show_button_clicked)
        self.show_button2 = tk.Button(self.win, text = 'Show', bd = 0, bg = 'white', font=("Segoe UI", 11), command = self.show_button_clicked2)

        self.bottom_label = tk.Label(self.win, text = 'By Parham Rezazade')
        self.login_button = tk.Button(self.win, text = 'Login', bg = '#151515', fg='white', bd = 0, font=('SegoeUI', 14, 'bold') ,command = self.end)
        self.change_pass_button = tk.Button(self.win, text = 'Change Pass',bg = '#d2d8d8', fg='#6e6e6e', bd = 0, font=('SegoeUI', 14, 'bold'), command = self.change_pass)
        
        self.exit_button = tk.Button(self.win, text = 'Exit',bg = '#151515', fg='white', bd = 0, font=('SegoeUI', 14, 'bold'), command = self.exit_pressed)

        self.login_back_button = tk.Button(self.win, text = 'Login',bg = '#d2d8d8', fg='#6e6e6e', bd = 0, font=('SegoeUI', 14, 'bold'), command = self.draw)
        self.save_button = tk.Button(self.win, text = 'Save Changes', bg = '#151515', fg='white', bd = 0, font=('SegoeUI', 14, 'bold'), command = self.change)
        
        self.connection = sqlite3.connect('data/data.db')
        self.connection.execute(''' CREATE TABLE IF NOT EXISTS login (pass TEXT);''')
        self.cursor = self.connection.execute("SELECT * from login")
        for pas in self.cursor:
            self.passowrd = list(pas)[0]
    
    def draw(self):
        self.check = 1
        self.background_canvas.place(x=0,y=0)
        self.background = ImageTk.PhotoImage(Image.open("image/background.png"))
        self.background_canvas.create_image(300,200,image=self.background)
        
        if self.password_entry.get() == 'Old Password':
            self.password_entry.delete(0, "end")
            self.password_entry.insert(0, "Enter Password")
            self.password_entry.config(fg = '#b4c1c8')

        self.save_button.place_forget()
        self.password_entry2.place_forget()
        self.save_button.place_forget()
        self.login_back_button.place_forget()
        
        self.password_entry.place(x = 80, y = 149, width = 400, height = 50)
        self.show_button.place(x = 505, y = 153, width=60, height=40)
        self.change_pass_button.place(x = 300, y=0, height = 68, width = 300)
        self.login_button.place(x = 33, y = 238, height = 51, width=534)
        self.exit_button.place(x = 33, y = 325, height = 51, width=534)
        
        self.win.mainloop()
        
    def exit_pressed(self):
        self.win.destroy()
        
    def end(self):
        if self.password_entry.get() == self.passowrd:
            self.on_closing()
            Ims()
            
    def change_pass(self):
        self.check = 2
        self.login_button.place_forget()
        self.change_pass_button.place_forget()
        self.exit_button.place_forget()
        
        self.background = ImageTk.PhotoImage(Image.open("image/background2.png"))
        self.background_canvas.create_image(300,200,image=self.background)
        
        self.login_back_button.place(x = 0, y=0, height = 68, width = 300)
        self.password_entry2.place(x = 80, y = 235, width = 400, height = 50)
        self.show_button2.place(x = 505, y = 239, width=60, height=40)
        self.save_button.place(x = 33, y = 325, height = 51, width=534)
        
        if self.check_entry == False and (self.password_entry.get == 'Enter Password' or self.password_entry.get == 'Old Password'):
            self.password_entry.delete(0, "end")
            self.password_entry.insert(0, "Old Password")
            self.password_entry.config(fg = '#b4c1c8')
        
    def change(self):
        if self.password_entry.get() == self.passowrd:
            self.cursor.execute(f'''UPDATE login SET pass = '{self.password_entry2.get()}' WHERE pass = {self.passowrd};''')
            self.connection.commit()
            
            self.passowrd = self.password_entry2.get()
            self.password_entry.delete(0, "end")
            self.password_entry2.delete(0, "end")
            self.draw()

    def on_entry_click_entry(self, event):
        self.check_entry = True
        if self.password_entry.get() == 'Enter Password' or self.password_entry.get() == 'Old Password':
            self.password_entry.delete(0, "end")
            self.password_entry.insert(0, '')
            self.password_entry.config(fg = 'black')
            self.password_entry.config(show='*')
            
    def on_focusout_entry(self, event):
        if self.password_entry.get() == '' or self.password_entry.get() == 'Old Password':
            if self.check == 1:
                self.password_entry.insert(0, 'Enter Password')
            else:
                self.password_entry.insert(0, 'Old Password')
            self.password_entry.config(fg = '#b4c1c8')
            self.password_entry.config(show='')
            
    def on_entry_click_entry2(self, event):
        self.check_entry = False
        if self.password_entry2.get() == 'New Password':
            self.password_entry2.delete(0, "end")
            self.password_entry2.insert(0, '')
            self.password_entry2.config(fg = 'black')
            self.password_entry2.config(show='*')
            
    def on_focusout_entry2(self, event):
        if self.password_entry2.get() == '':
            self.password_entry2.insert(0, 'New Password')
            self.password_entry2.config(fg = '#b4c1c8')
            self.password_entry2.config(show='')
            
    def show_button_clicked(self):
            if self.password_entry.cget('show') == '*':
                self.password_entry.config(show='')

            elif self.password_entry.cget('show') == '' and self.password_entry.get() != 'Old Password' and self.password_entry.get() != 'Enter Password':
                self.password_entry.config(show='*')
                
    def show_button_clicked2(self):
            if self.password_entry2.cget('show') == '*':
                self.password_entry2.config(show='')

            elif self.password_entry2.cget('show') == '' and self.password_entry2.get() != 'New Password':
                self.password_entry2.config(show='*')

    def on_closing(self):
        self.win.destroy()
        self.connection.close()

# Login()
Ims()
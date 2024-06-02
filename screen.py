import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Toplevel
from datetime import datetime, timedelta
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from weather import get_temp
from model import clothes
import random

area_dict = {"臺北市": "臺北", "新北市": "新北", "桃園市": "桃園", "臺中市": "臺中", "臺南市": "臺南", "高雄市": "高雄", "基隆市": "基隆", "新竹縣": "新竹", "苗栗縣": "苗栗", "彰化縣": "彰化", "南投縣": "南投", "雲林縣": "雲林", "嘉義市": "嘉義", "屏東縣": "屏東", "嘉義市": "嘉義", "宜蘭縣": "宜蘭", "花蓮縣": "花蓮", "臺東縣": "臺東"}

class InputFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.date_label = ttk.Label(self, text="選擇日期(YYYY/MM/DD)：")
        self.date_label.config(background="#d3e5ee", font=("Arial", 30))
        self.date_label.pack()

        mindate = datetime.today()
        maxdate = mindate + timedelta(days=10)
        self.cal = DateEntry(self, selectmode='day', showweeknumbers=False, mindate=mindate, maxdate=maxdate, weekendbackground='#FFFFFF', selectforeground='#FFFFFF', date_pattern='yyyy/mm/dd')
        self.cal.config(font=("Arial", 30))
        self.cal.pack(pady=20)

        self.area_label = ttk.Label(self, text="選擇地區：")
        self.area_label.config(background="#d3e5ee", font=("Arial", 30))
        self.area_label.pack(pady=5)

        self.box = ttk.Combobox(self, values=list(area_dict.keys()), width=12, font=('Arial 30'))
        self.box.pack(pady=20)

        self.start_button = ttk.Button(self, text="開始！", command=self.start_button_click)
        self.start_button.pack(pady=20)
    
    def start_button_click(self):
        self.pack_forget()
        area = area_dict[self.box.get()]
        selected_date = self.cal.get().split('/')
        date = datetime(int(selected_date[0]), int(selected_date[1]), int(selected_date[2]))
        delta = date - datetime.today()
        days_after_today = delta.days + 1
        high, low, rain = get_temp(days_after_today, area)
        up, down, shoes = clothes(high, low)
        print(high, low)
        print(up, down, shoes)
        result_frame = ResultFrame(root, self, self.box.get(), self.cal.get(), high, low, rain, up, down, shoes)
        result_frame.pack()


class ResultFrame(tk.Frame):
    def __init__(self, parent, input_frame, area, date, high, low, rain, up, down, shoes, *args, **kwargs):
        super().__init__(parent, width=1440, height=1080, *args, **kwargs)
        
        self.input_frame = input_frame
        
        self.canvas = tk.Canvas(self, bg="black", width=1440, height=1080, highlightthickness=0)
        self.canvas.pack()
        
        self.background_image = Image.open("pic/back2.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.canvas.create_image(720, 540, image=self.background_photo)
        
        self.canvas.create_text(720, 200, text=f'地區：{area}\n日期：{date}\n今日最高溫：{high}°C\n今日最低溫：{low}°C\n降雨機率：{rain}%\n', font=('Arial', 30))

        if up != (3 or 4):
            if down == 0:
                down_num = random.randint(8, 10)
            elif down == 1:
                down_num = random.randint(1, 5)
            else:
                down_num = random.randint(6, 7)
            self.down_image = Image.open(f"pic/down{down_num}.png")
            self.down_photo = ImageTk.PhotoImage(self.down_image)
            self.canvas.create_image(745, 709, image=self.down_photo)
    
        if up == 0:
            up_num = random.randint(1, 3)
        elif up == 1:
            up_num = random.randint(4, 8)
        elif up == 2:
            up_num = random.randint(16, 19)
        elif up == 3:
            up_num = 21
        elif up == 4:
            up_num = random.randint(13, 15)
        elif up == 5:
            up_num = random.randint(10, 12)
        else:
            up_num = 9
        self.up_image = Image.open(f"pic/up{up_num}.png")
        self.up_photo = ImageTk.PhotoImage(self.up_image)
        self.canvas.create_image(745, 709, image=self.up_photo)
        
        self.shoes_image = Image.open(f"pic/shoes{shoes+1}.png")
        self.shoes_photo = ImageTk.PhotoImage(self.shoes_image)
        self.canvas.create_image(745, 709, image=self.shoes_photo)

        self.return_button = ttk.Button(self, text="返回", command=self.return_to_input_frame)
        self.return_button.place(x=900, y=950)
    
    def return_to_input_frame(self):
        self.pack_forget()
        self.input_frame.pack(pady=20)


root = tk.Tk()
root.title("讓我來尋找您的一日穿搭")
root.geometry("1440x1080")

background_image = Image.open("pic/back.png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0)

style = ttk.Style()
style.configure("TEntry", font=("Helvetica", 30))
style.configure("TButton", font=("Arial", 30), foreground="#CD5C5C")
style.configure('TCombobox', arrowsize=30)
style.configure('TListbox', font=('Arial', 30))
style.configure('TFrame', background="#d3e5ee")

input_frame = InputFrame(root)
input_frame.config(bg="#d3e5ee")
input_frame.pack(pady=20)

root.mainloop()

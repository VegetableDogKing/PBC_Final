import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Toplevel
from datetime import datetime, timedelta
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from weather import get_temp

area_dict = {"臺北市": "臺北", "新北市": "新北", "桃園市": "桃園", "臺中市": "臺中", "臺南市": "臺南", "高雄市": "高雄", "基隆市": "基隆", "新竹縣": "新竹", "苗栗縣": "苗栗", "彰化縣": "彰化", "南投縣": "南投", "雲林縣": "雲林", "嘉義市": "嘉義", "屏東縣": "屏東", "嘉義市": "嘉義", "宜蘭縣": "宜蘭", "花蓮縣": "花蓮", "臺東縣": "臺東"}

class InputFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.date_label = ttk.Label(self, text="選擇日期(YYYY/MM/DD)：")
        self.date_label.config(background="#FFF0F5", font=("Arial", 30))
        self.date_label.pack()

        mindate = datetime.today()
        maxdate = mindate + timedelta(days=11)
        self.cal = DateEntry(self, selectmode='day', showweeknumbers=False, mindate=mindate, maxdate=maxdate, weekendbackground='#FFFFFF', selectforeground='#FFFFFF', date_pattern='yyyy/mm/dd')
        self.cal.config(font=("Arial", 30))
        self.cal.pack(pady=20)

        self.area_label = ttk.Label(self, text="選擇地區：")
        self.area_label.config(background="#FFF0F5", font=("Arial", 30))
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
        print(high, low, rain)
        
        result_frame.pack()

root = tk.Tk()
root.title("讓我來尋找您的一日穿搭")
root.geometry("2560x1440")
background_image = Image.open("65816-television-firewatch-campo-wallpaper-desktop-4k-santo.png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0)

style = ttk.Style()
style.configure("TEntry", font=("Helvetica", 30))
style.configure("TButton", font=("Arial", 30), foreground="#CD5C5C")
style.configure('TCombobox', arrowsize=30)
style.configure('TListbox', font=('Arial', 30))
style.configure('TFrame', background="#FFF0F5")

input_frame = InputFrame(root)
input_frame.pack(pady=20)

result_frame = ttk.Frame(root)
result_label = ttk.Label(result_frame, text="")
result_label.pack(pady=20)

root.mainloop()

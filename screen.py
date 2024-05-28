import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Toplevel
from datetime import datetime, timedelta
from tkcalendar import DateEntry

area_dict = {"臺北市": "臺北", "新北市": "新北", "桃園市": "桃園", "臺中市": "臺中", "臺南市": "臺南", "高雄市": "高雄", "基隆市": "基隆", "新竹縣": "新竹", "苗栗縣": "苗栗", "彰化縣": "彰化", "南投縣": "南投", "雲林縣": "雲林", "嘉義市": "嘉義", "屏東縣": "屏東", "嘉義市": "嘉義", "宜蘭縣": "宜蘭", "花蓮縣": "花蓮", "臺東縣": "臺東"}

def start_button_click():
    # Hide the input frame
    input_frame.pack_forget()
    
    area = area_dict[box.get()]
    selected_date = cal.get().split('/')
    date = datetime(int(selected_date[0]), int(selected_date[1]), int(selected_date[2]))
    print(date)
    # Calculate the number of days after today
    today = datetime.today()
    delta = date - today
    days_after_today = delta.days
    
    print(days_after_today)
    
    # Show the result frame
    result_frame.pack()

# Create main window
root = tk.Tk()
root.title("讓我來尋找您的一日穿搭")
root.geometry("2560x1440")
root.configure(background='#FFF0F5')


# Define a style for larger fonts
style = ttk.Style()
style.configure("TEntry", font=("Helvetica", 30))
style.configure("TButton", font=("Arial", 30), foreground="#CD5C5C")
style.configure('TCombobox',arrowsize = 30)
style.configure('TListbox', font=('Arial', 30))
style.configure('TFrame', background="#FFF0F5")

# Input frame
input_frame = ttk.Frame(root, width=2560, height=1440)
input_frame.pack(pady=20)
# input_frame.pack_propagate(False)
# input_frame.config(style="TFrame")
background_image = tk.PhotoImage(file="65816-television-firewatch-campo-wallpaper-desktop-4k-santo.png")
background_label = tk.Label(input_frame, image=background_image)
background_label.place(x=0, y=0)

# Date entry
date_label = ttk.Label(input_frame, text="選擇日期(YYYY/MM/DD)：")
date_label.config(background="#FFF0F5", font=("Arial", 30))
date_label.pack()
today = datetime.today().strftime('%Y-%-m-%-d %H:%M:%S').split(' ')[0].split('-')
end_date = (datetime.today() + timedelta(days=11)).strftime('%Y-%-m-%-d %H:%M:%S').split(' ')[0].split('-')

mindate = datetime.today()
maxdate = mindate + timedelta(days=11)
cal = DateEntry(input_frame, selectmode='day',showweeknumbers=False, mindate=mindate, maxdate=maxdate, year=int(today[0]), month=int(today[1]), day=int(today[2]), weekendbackground='#FFFFFF', selectforeground='#FFFFFF', date_pattern='yyyy/mm/dd')
cal.config(font=("Arial", 30))
cal.pack(pady=20)

area_label = ttk.Label(input_frame, text="選擇地區：")
area_label.config(background="#FFF0F5", font=("Arial", 30))
area_label.pack(pady=5)
box = ttk.Combobox(input_frame, values=['臺北市', '新北市', '桃園市', '臺中市', '臺南市', '高雄市', '基隆市', '新竹縣', '新竹市', '苗栗縣', '彰化縣', '南投縣', '雲林縣', '嘉義市', '屏東縣', '宜蘭縣', '花蓮縣', '臺東縣'], width=12, font=('Arial 30'))
box.pack(pady=20)

# Start button
start_button = ttk.Button(input_frame, text="開始！", command=start_button_click)
start_button.pack(pady=20)

# Result frame for displaying results
result_frame = ttk.Frame(root)
result_label = ttk.Label(result_frame, text="")
result_label.pack()

# Result frame for displaying results
result_frame = ttk.Frame(root, width=2560, height=1440)

# Load the background image for the result frame
background_image = tk.PhotoImage(file="65816-television-firewatch-campo-wallpaper-desktop-4k-santo.png")
background_label = tk.Label(result_frame, image=background_image)
background_label.place(x=0, y=0)

root.mainloop()

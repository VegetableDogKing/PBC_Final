import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Toplevel
from datetime import datetime, timedelta
from tkcalendar import Calendar, DateEntry

def show_error_message(title, message):
    # Create a new Toplevel window for the custom messagebox
    error_window = Toplevel(root)
    error_window.title(title)
    error_window.geometry("300x150")
    
    # Message label
    message_label = ttk.Label(error_window, text=message, wraplength=250, justify="center", font=('Helvetica 15'))
    message_label.pack(pady=20)
    
    # OK button to close the messagebox
    ok_button = tk.Button(error_window, text="OK", command=error_window.destroy, font=("Helvetica", 14), width=10)
    ok_button.pack(pady=10)

def start_button_click():
    
    

    # Hide the input frame
    input_frame.pack_forget()

    # Show the result frame
    
    result_frame.pack(pady=20)

# Create main window
root = tk.Tk()
root.title("讓我來尋找您的一日穿搭")
root.geometry("1280x720")
root.configure(background='#FFF0F5')

# Define a style for larger fonts
style = ttk.Style()
style.configure("TEntry", font=("Helvetica", 30))
style.configure("TButton", font=("Arial", 30), foreground="#CD5C5C")
style.configure('TCombobox',arrowsize = 30)
style.configure('TListbox', font=('Arial', 30))
style.configure('TFrame', background="#FFF0F5")

# Input frame
input_frame = ttk.Frame(root, width=1000, height=500)
input_frame.pack(pady=150)
# input_frame.pack_propagate(False)
input_frame.config(style="TFrame")

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
box = ttk.Combobox(input_frame, values=['臺北市', '新北市', '桃園市', '臺中市', '臺南市', '高雄市', '基隆市', '新竹縣', '新竹市', '苗栗縣', '彰化縣', '南投縣', '雲林縣', '嘉義縣', '嘉義市', '屏東縣', '宜蘭縣', '花蓮縣', '臺東縣', '澎湖縣', '金門縣', '連江縣'], width=12, font=('Arial 30'))
box.pack(pady=20)

# Start button
start_button = ttk.Button(input_frame, text="開始！", command=start_button_click)
start_button.pack(pady=20)

# Result frame for displaying results
result_frame = ttk.Frame(root)
result_label = ttk.Label(result_frame, text="")
result_label.pack()

root.mainloop()
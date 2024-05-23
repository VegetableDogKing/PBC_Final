import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Toplevel
from datetime import datetime

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
    mood = mood_entry.get()
    date = date_entry.get()

    # Validate date
    try:
        datetime.strptime(date, '%Y/%m/%d')
    except ValueError:
        show_error_message("錯誤日期", "請按照 YYYY/MM/DD 的方式輸入日期")
        return

    # Hide the input frame
    input_frame.pack_forget()

    # Show the result frame
    result_label.config(text=f"Mood: {mood}\nDate: {date}\nWeather and outfit recommendation will be displayed here.")
    result_frame.pack(pady=20)

# Create main window
root = tk.Tk()
root.title("穿搭")
root.geometry("1280x720")
root.configure(background='black')

# Define a style for larger fonts
style = ttk.Style()
style.configure("TLabel", font=("Arial", 50))
style.configure("TEntry", font=("Helvetica", 24))
style.configure("TButton", font=("Arial", 50))
style.configure('W.TCombobox',arrowsize = 23)

# Input frame
input_frame = ttk.Frame(root)
input_frame.pack(pady=20)

# Mood entry
mood_label = ttk.Label(input_frame, text="輸入你的心情：")
mood_label.pack(pady=5)
mood_entry = ttk.Entry(input_frame, width=50, font=('Arial 24'))
mood_entry.pack(pady=5)

# Date entry
date_label = ttk.Label(input_frame, text="輸入日期(YYYY/MM/DD)：")
date_label.pack(pady=5)
date_entry = ttk.Entry(input_frame, width=50, font=('Arial 24'))
date_entry.pack(pady=20)

box = ttk.Combobox(input_frame, values=['臺北市', '新北市', '桃園市', '臺中市', '臺南市', '高雄市', '基隆市', '新竹縣', '新竹市', '苗栗縣', '彰化縣', '南投縣', '雲林縣', '嘉義縣', '嘉義市', '屏東縣', '宜蘭縣', '花蓮縣', '臺東縣', '澎湖縣', '金門縣', '連江縣'], width=49, font=('Arial 24'), style='W.TCombobox')
box.pack(pady=5)

# Start button
start_button = ttk.Button(input_frame, text="開始！", command=start_button_click)
start_button.pack(pady=20)

# Result frame for displaying results
result_frame = ttk.Frame(root)
result_label = ttk.Label(result_frame, text="")
result_label.pack()

root.mainloop()

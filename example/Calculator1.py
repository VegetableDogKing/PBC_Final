import tkinter as tk
import tkinter.font as tkFont

class Calculator(tk.Frame):
  
  def __init__(self):
    tk.Frame.__init__(self) 
    self.grid()
    self.createWidgets()

  def createWidgets(self):
    f1 = tkFont.Font(size = 48, family = "Courier New")
    f2 = tkFont.Font(size = 32, family = "Courier New")
	
    self.lblNum = tk.Label(self, text = "0", height = 1, width = 7, font = f1) 
    self.btnNum1 = tk.Button(self, text = "1", command = self.clickBtnNum1, height = 1, width = 2, font = f2) 
    self.lblNum.grid(row = 0, column = 0)
    self.btnNum1.grid(row = 1, column = 0)

  def clickBtnNum1(self):
    self.lblNum.configure(text = self.lblNum.cget("text") + "1")

cal = Calculator()
cal.master.title("My Calculator")
cal.mainloop()

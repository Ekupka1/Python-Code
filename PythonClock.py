# Practice python code, making a clock- Youtube vid
# Ethan Kupka
# 3/24/2021 python

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

def time():
    string= strftime('%H:%M:%S %p') # Military time
    #string= strftime('%I:%M:%S:%p') # By 12Hr
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font= ("ds_digital", 80), background= "black", foreground= "cyan")
label.pack(anchor='center')

time()
mainloop()

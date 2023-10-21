import tkinter as tk

import tkinter as ttk

import datetime

from time import strftime

root = tk.Tk()

canvas = tk.Canvas(root, height=400, width=600)

canvas.pack()


label_1 = tk.Label(root, text = "DIGITAL CLOCK",font="bold, 60", background="#9B59B6", foreground="white")

label_1.place(relx = 0, rely = 0, relheight=0.3, relwidth=1)


def time():

    string = strftime("%I:%M:%S %A")

    label.config(text = string)
    
    label.after(1000, time)

label = tk.Label(root, font = "ds-digital 50", background="#A9CCE3", foreground="black")

label.place(relx = 0, rely = 0.3, relheight= 0.2, relwidth = 1)

time()

root.mainloop()

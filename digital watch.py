import tkinter as tk
from time import strftime

win=tk.Tk()
win.title("Akash")


def time():
    string = strftime('%H %M %S %p \n %D')
    label.config(text=string)
    label.after(1000,time)

label = tk.Label(win, font=('calibbri', 50, 'bold'), bg='pink',foreground='black')
label.pack(anchor='center')

time()

win.mainloop()

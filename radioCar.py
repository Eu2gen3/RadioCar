from tkinter import *
from tkinter import ttk
import time as tm
import datetime as dt
import sys
import calendar


root = Tk()

root.title("Radio Car")
root.geometry("400x250")

style = ttk.Style()
style.theme_use("classic")
style.configure("TNotebook.Tab", background="red", font="helvetica 10")
style.map("TNotebook.Tab", background=[("selected", "green")])
tab_control = ttk.Notebook(root)


def display_time():
    current_time = tm.strftime("%I:%M:%S:%p")
    clock_label = ttk.Label(tab1, font="arial 50", text=current_time)
    root.after(200, display_time)
    clock_label.place(x=5, y=70)


date = dt.datetime.now()
format_date = f"(date:%a, %b, %d, %Y)"
w = ttk.Label(root, text=f"¨{dt.datetime.now():%a, %b, %d, %Y}",  font=("helvetica", 20))
w.place(x=70, y=160)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

tab_control.add(tab1, text="Welcome")
ttk.Label(tab1, text="Pantella Principal")
photo_b = PhotoImage(file="previous.png")
b = Button(tab1, image=photo_b, width=45, height=30, bg="red", )
b.place(x=5, y=5)
photo_n = PhotoImage(file="next.png")
b = Button(tab1, image=photo_n, width=45, height=30, bg="red")
b.place(x=340, y=2)
photo_s = PhotoImage(file="settings.png")
b = Button(tab1, image=photo_s, width=45, height=30, bg="red")
b.place(x=5, y=180)
photo_e = PhotoImage(file="logout.png")
b = Button(tab1, image=photo_e, width=45, height=30, bg="red")
b.place(x=340, y=180)


tab_control.add(tab2, text="Radio")
ttk.Label(tab2, text="Radio Settings")
b = Button(tab2, text="Back", width=7, height=1, bg="red")
b.place(x=2, y=5)
b = Button(tab2, text="Forward", width=7, height=1, bg="red")
b.place(x=330, y=5)
b = Button(tab2, text="Settings", width=7, height=1, bg="red")
b.place(x=2, y=190)
b = Button(tab2, text="Exit", width=7, height=1, bg="red")
b.place(x=330, y=190)

tab_control.add(tab3, text="Phone")
ttk.Label(tab3, text="Phone Settings")
b = Button(tab3, text="Back", width=7, height=1, bg="red")
b.place(x=2, y=5)
b = Button(tab3, text="Forward", width=7, height=1, bg="red")
b.place(x=330, y=5)
b = Button(tab3, text="Settings", width=7, height=1, bg="red")
b.place(x=2, y=190)
b = Button(tab3, text="Exit", width=7, height=1, bg="red")
b.place(x=330, y=190)

tab_control.add(tab4, text="CarSettings")
ttk.Label(tab4, text="Car Settings")
b = Button(tab4, text="Back", width=7, height=1, bg="red")
b.place(x=2, y=5)
b = Button(tab4, text="Forward", width=7, height=1, bg="red")
b.place(x=330, y=5)
b = Button(tab4, text="Settings", width=7, height=1, bg="red")
b.place(x=2, y=190)
b = Button(tab4, text="Exit", width=7, height=1, bg="red")
b.place(x=330, y=190)


tab_control.pack(expand=50, fill="both")


display_time()
root.mainloop()

root.mainloop()

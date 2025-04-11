from tkinter import *
from tkinter import ttk
import math
import time
import  tkinter as tk
def New_Window(x):
    ws = tk.Toplevel()
    ws.geometry("600x100")
    question1=tk.Label(ws,text=x)
    question1.place(x=0,y=50)
    ws.mainloop()

window=tk.Tk()
window.geometry("1100x800")
window.title("Escape Room")

settings=tk.Label(window,text="Sie stehen vor 6 verschiedenen Türen," "\n"
                   "welche alle ein Hinweis oder eine Aufgabe haben," "\n"
" doch es gibt nur eine richtige reihenfolge," "\n"
" die zur richtigen tür führt", font=("Arial", 12))

settings.place(x=750,y=30)
settings.lift()
door1=tk.Label(text="Door 1", font=5)
door1.place(x=70,y=0)
canvas=tk.Canvas()
canvas.place(x=15,y=22)
canvas.create_rectangle(10,10,150,250, fill="yellow")
canvas.create_rectangle(18,18,142,142,fill= "blue")
canvas.create_rectangle(120,150,150,140,fill= "black")
button1 = tk.Button(window, text="Click ME", bg='White', fg='Black',command=lambda: New_Window("Diese Tür ist an zweiter Stelle in der richtigen Reihenfolge.""\n""Hinweis: lügner schreiben ihre eigene wahrheit"))
button1.place(x=60, y=80)    

door2=tk.Label(text="Door 2", font=5)
door2.place(x=235,y=0)
canvas=tk.Canvas()
canvas.place(x=180,y=22)
canvas.create_rectangle(10,10,150,250)
canvas.create_rectangle(18,18,142,142,fill= "black")
canvas.create_rectangle(120,150,150,140,fill= "black")
button2 = tk.Button(window, text="Click ME", bg='White', fg='Black',command=lambda: New_Window("Zähle die Nummern der ersten und der dritten Tür. Sie ergeben 7."))
button2.place(x=225, y=80) 

door3=tk.Label(text="Door 3", font=5)
door3.place(x=410,y=0)
canvas=tk.Canvas()
canvas.place(x=360,y=22)
canvas.create_rectangle(10,10,150,250,fill= "red")
canvas.create_rectangle(18,18,142,142, fill= "green")
canvas.create_rectangle(120,150,150,140,fill= "black")
button3 = tk.Button(window, text="Click ME", bg='White', fg='Black',command=lambda: New_Window("Wenn du mich als zweite Tür betrittst, wirst du scheitern"))
button3.place(x=410, y=80) 


door4=tk.Label(text="Door 4", font=5)
door4.place(x=70,y=280)
canvas=tk.Canvas()
canvas.place(x=15,y=310)
canvas.create_rectangle(10,10,150,250, fill="yellow")
canvas.create_rectangle(18,18,142,142, fill= "green")
canvas.create_rectangle(120,150,150,140,fill= "black")
button4 = tk.Button(window, text="Click ME", bg='White', fg='Black',command=lambda: New_Window("Die Nummer dieser Tür ist doppelt so groß wie die Ziffernsumme der letzten Tür"))
button4.place(x=60, y=370)   

door5=tk.Label(text="Door 5", font=5)
door5.place(x=235,y=280)
canvas=tk.Canvas()
canvas.place(x=180,y=310)
canvas.create_rectangle(10,10,150,250, fill="red")
canvas.create_rectangle(18,18,142,142, fill= "blue")
canvas.create_rectangle(120,150,150,140,fill= "black")
button5 = tk.Button(window, text="Click ME", bg='White', fg='Black',command=lambda: New_Window("Die Differenz zwischen dieser Türnummer und der nächsten beträgt 1."))
button5.place(x=225, y=370) 

door6=tk.Label(text="Door 6", font=5)
door6.place(x=410,y=280)
canvas=tk.Canvas()
canvas.place(x=360,y=310)
canvas.create_rectangle(10,10,150,250, fill="yellow")
canvas.create_rectangle(18,18,142,142, fill= "green")
canvas.create_rectangle(120,150,150,140,fill= "black")
button6 = tk.Button(window, text="Click ME", bg='White', fg='Black',command=lambda: New_Window("Ich komme an letzter Stelle."))
button6.place(x=410, y=370)  





window.mainloop()
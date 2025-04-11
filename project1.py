
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import PhotoImage
import time
from PIL import Image, ImageTk 

def new_window(x):
    ws = tk.Toplevel()
    ws.geometry("600x100")
    question1 = tk.Label(ws, text=x, wraplength=500)
    question1.place(x=0, y=50)
    return ws

class Door:
    def __init__(self, master, x, y, text, color, command):
        self.master = master
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.command = command
        self.create_door()

    def create_door(self):
        door_label = tk.Label(self.master, text=self.text, font=("Arial", 12))
        door_label.place(x=self.x, y=self.y)
        canvas = tk.Canvas(self.master, width=160, height=270)

        # Make sure all widgets are above the background
        settings.lift()
        
        
        
        canvas.place(x=self.x-55, y=self.y+22)
        canvas.create_rectangle(10, 10, 150, 250, fill=self.color)
        canvas.create_rectangle(18, 18, 142, 142, fill="#0AC3CA")
        canvas.create_rectangle(120, 150, 150, 140, fill="black")
        button = tk.Button(self.master, text="Click ME", bg='White', fg='Black', command=self.command)
        button.place(x=self.x-5, y=self.y+80)

window = tk.Tk()
window.geometry("1100x800")
window.title("Escape Room")
# Proper canvas and image implementation

canva = tk.Canvas(window, width=1100, height=800)
img = Image.open("by.jpg")
img = img.resize((1100, 800), Image.LANCZOS)  # Resize to window dimensions
image = ImageTk.PhotoImage(img)
canva.create_image(0, 0, image=image, anchor="nw")
canva.pack(fill="both", expand=True)
# Keep reference to prevent garbage collection
canva.image = image  

settings = tk.Label(window, text="Sie stehen vor 6 verschiedenen Türen,\n"
                   "welche alle ein Hinweis oder eine Aufgabe haben,\n"
                   "doch es gibt nur eine richtige Reihenfolge,\n"
                   "die zur richtigen Tür führt", font=("Arial", 12), wraplength=400)
settings.place(x=750, y=30)
settings.lift()

doors = [
    Door(window, 70, 0, "Door 1",  "yellow", lambda: [ws := new_window("GLH TXHUVXPPH GLHVHU GUHL CDKOHQ HUJLHW HLQH GUHL" ), ws.after(30000, ws.destroy)]),  #die Quersumme dieser drei Zahlen ergibt eine drei
    Door(window, 235, 0, "Door 2", "black", lambda: [ws := new_window("CDKOH GLH QXPPEU GHU HUVW HQG GHU GULWWHQ WXU. VLH HUJHEHQ 7."), ws.after(30000, ws.destroy)]),  #Zähle die Nummern der ersten und der dritten Tür. Sie ergeben 7
    Door(window, 410, 0, "Door 3", "red", lambda: [ws := new_window("ELOGH GHQ GXFKVFKQLWW GHU HUVW HQ GULWWHQ XQG CZHLWHQ WXU. GHU GXUFKVFKQLWW HUJHHE VHFKV"), ws.after(30000, ws.destroy)]), #Bilde den Durchschnitt der ersten, dritten und der zweiten Tür. der durchscnnitt ergibt sechs
    Door(window, 70, 280, "Door 4", "yellow", lambda: [ws := new_window("glh qxpphu ghlvhu wxu lwvlqgq dgglq rxrphq yruq dohq yrukhqwjh qxuhq"), ws.after(30000, ws.destroy)]), #die nummer dieser tür ist die addition von allen vorherigen türen
    Door(window, 235, 280, "Door 5", "red", lambda: [ws := new_window("Dieser Code ist nach einem bekannten römischen Diktator aufgebaut "), ws.after(30000, ws.destroy)]),
    Door(window, 410, 280, "Door 6", "yellow", lambda: [ws := new_window("GLH TXHUVXPPH GHU HUVW HQ WXU VDJW GLU, DQ ZHOFKH VWHOOH VLH NRPPW"), ws.after(30000, ws.destroy)]) #die quersumme der 1 tür sagt dir an welche stelle sie kommt
]
"""def on_closing():
    Properly close the application after destroying all windows
    # Destroy any existing Toplevel windows first
    for child in window.winfo_children():
        if isinstance(child, tk.Toplevel):
            child.destroy()
    # Schedule main window destruction after 500ms
    window.after(500, window.destroy)"""

#window.protocol("WM_DELETE_WINDOW", on_closing)

def get_input(x):
    """Returns the text content from the input field"""
    return txt.get('1.0', 'end-1c').strip()

def second_windows():
    # Close current window after 500ms
    window.after(500, window.destroy)
    
    # Create new main window
    win = tk.Tk()
    win.title("Nächster Raum")
    win.geometry("1100x800")
    
    # Add victory message
    label = tk.Label(win, 
                   text="Herzlichen Glückwunsch!\nSie haben den Raum erfolgreich verlassen!",
                   font=("Arial", 24))
    label.pack(pady=200)
    
    win.mainloop()


def end_window():
    """Check if user entered the correct code (5326)"""
    user_input = get_input("u got the right code")
    try:
        if int(user_input) == 4239:
            second_windows()  # Transition to next room
        else:
            ws = new_window("Incorrect code! Try again.")
            ws.after(2000, ws.destroy)  # Auto-close after 2 seconds
    except ValueError:
        ws = new_window("Please enter a valid number!")
        ws.after(2000, ws.destroy)  # Auto-close after 2 seconds


# Add instruction label
instruction = tk.Label(window, 
                      text="Enter the secret code to escape:", 
                      font=("Arial", 12))
instruction.place(x=600, y=250)

# Improved text input
txt = tk.Text(window, height=5, width=30, font=("Arial", 12), 
             padx=10, pady=10, wrap=tk.WORD)
txt.place(x=600, y=280)

# Improved submit button
btn = tk.Button(window, text="Submit Code", command=end_window,
               font=("Arial", 12), padx=20, pady=5)
btn.place(x=650, y=380)
# Create canvas for background image


 # Fallback background color
window.mainloop()

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

def new_window(x):
    ws = tk.Toplevel()
    ws.geometry("600x100")
    question1 = tk.Label(ws, text=x, wraplength=500)
    question1.place(x=0, y=50)
    return ws

class Door:
    def __init__(self, master, x, y, text, color, command, image_path=None):
        self.master = master
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.command = command
        self.image_path = image_path
        self.create_door()

    def create_door(self):
        # Create clickable image label
        if self.image_path:
            try:
                img = Image.open(self.image_path)
                img = img.resize((160, 270), Image.LANCZOS)
                self.door_img = ImageTk.PhotoImage(img)
                self.label = tk.Label(self.master, image=self.door_img)
                self.label.place(x=self.x-55, y=self.y+22)
                self.label.image = self.door_img  # Keep reference
                # Make label clickable
                self.label.bind("<Button-1>", lambda e: self.command())
            except Exception as e:
                print(f"Error loading image: {e}")
                # Fallback to invisible clickable area
                canvas = tk.Canvas(self.master, width=160, height=270,
                                 highlightthickness=0, bd=0)
                canvas.place(x=self.x-55, y=self.y+22)
                canvas.bind("<Button-1>", lambda e: self.command())
        else:
            # Original invisible clickable area
            canvas = tk.Canvas(self.master, width=160, height=270,
                             highlightthickness=0, bd=0)
            canvas.place(x=self.x-55, y=self.y+22)
            canvas.bind("<Button-1>", lambda e: self.command())

# [Rest of the file remains exactly the same as previous version...]
window = tk.Tk()
window.geometry("1100x800")
window.title("Escape Room")

# Background image
canva = tk.Canvas(window, width=1100, height=800)
try:
    img = Image.open("by.jpg")
    img = img.resize((1100, 800), Image.LANCZOS)
    image = ImageTk.PhotoImage(img)
    canva.create_image(0, 0, image=image, anchor="nw")
    canva.image = image  
except:
    canva.configure(bg='white')
canva.pack(fill="both", expand=True)

settings = tk.Label(window, 
                   text="Sie stehen vor 6 verschiedenen Türen,\n"
                   "welche alle ein Hinweis oder eine Aufgabe haben,\n"
                   "doch es gibt nur eine richtige Reihenfolge,\n"
                   "die zur richtigen Tür führt", 
                   font=("Arial", 12), wraplength=400)
settings.place(x=750, y=30)
settings.lift()

doors = [
    Door(window, 70, 0, "Door 1", "yellow", 
        lambda: [ws := new_window("GLH TXHUVXPPH GLHVHU GUHL CDKOHQ HUJLHW HLQH GUHL"), ws.after(30000, ws.destroy)],
        "escape_room/door.jpg"),
    # [Other doors remain the same...]
    Door(window, 235, 0, "Door 2", "black", 
        lambda: [ws := new_window("CDKOH GLH QXPPEU GHU HUVW HQG GHU GULWWHQ WXU. VLH HUJHEHQ 7."), ws.after(30000, ws.destroy)],
        "escape_room/door.jpg"),
    Door(window, 410, 0, "Door 3", "red", 
        lambda: [ws := new_window("ELOGH GHQ GXFKVFKQLWW GHU HUVW HQ GULWWHQ XQG CZHLWHQ WXU. GHU GXUFKVFKQLWW HUJHHE VHFKV"), ws.after(30000, ws.destroy)],
        "escape_room/door.jpg"),
    Door(window, 70, 280, "Door 4", "yellow", 
        lambda: [ws := new_window("glh qxpphu ghlvhu wxu lwvlqgq dgglq rxrphq yruq dohq yrukhqwjh qxuhq"), ws.after(30000, ws.destroy)],
        "escape_room/door.jpg"),
    Door(window, 235, 280, "Door 5", "red", 
        lambda: [ws := new_window("Dieser Code ist nach einem bekannten römischen Diktator aufgebaut"), ws.after(30000, ws.destroy)],
        "escape_room/door.jpg"),
    Door(window, 410, 280, "Door 6", "yellow", 
        lambda: [ws := new_window("GLH TXHUVXPPH GHU HUVW HQ WXU VDJW GLU, DQ ZHOFKH VWHOOH VLH NRPPW"), ws.after(30000, ws.destroy)],
        "escape_room/door.jpg")
]

# [Rest of UI elements and functions remain unchanged...]
def get_input(x):
    return txt.get('1.0', 'end-1c').strip()

def second_windows():
    window.after(500, window.destroy)
    win = tk.Tk()
    win.title("Nächster Raum")
    win.geometry("1100x800")
    label = tk.Label(win, 
                   text="Herzlichen Glückwunsch!\nSie haben den Raum erfolgreich verlassen!",
                   font=("Arial", 24))
    label.pack(pady=200)
    win.mainloop()

def end_window():
    user_input = get_input("u got the right code")
    try:
        if int(user_input) == 4239:
            second_windows()
        else:
            ws = new_window("Incorrect code! Try again.")
            ws.after(2000, ws.destroy)
    except ValueError:
        ws = new_window("Please enter a valid number!")
        ws.after(2000, ws.destroy)

# UI Elements
instruction = tk.Label(window, 
                      text="Enter the secret code to escape:", 
                      font=("Arial", 12))
instruction.place(x=600, y=250)

txt = tk.Text(window, height=5, width=30, font=("Arial", 12), 
             padx=10, pady=10, wrap=tk.WORD)
txt.place(x=600, y=280)

btn = tk.Button(window, text="Submit Code", command=end_window,
               font=("Arial", 12), padx=20, pady=5)
btn.place(x=650, y=380)

window.mainloop()

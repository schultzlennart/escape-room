from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import os


class NumberRectangle:
    def __init__(self, master, x, y, number, color="lightblue", display_canvas=None):
        self.master = master
        self.x = x
        self.y = y
        self.number = number
        self.color = color
        self.display_canvas = display_canvas
        self.create_rectangle()

    def create_rectangle(self):
        # Create completely transparent clickable area
        self.click_area = tk.Frame(self.master, 
                                 width=40, 
                                 height=40,
                                 highlightthickness=0,
                                 bd=0,
                                 bg="")
        self.click_area.place(x=self.x, y=self.y)
        self.click_area.bind("<Button-1>", lambda e: self.on_click())

    def on_click(self):
        if hasattr(self, 'display_canvas') and self.display_canvas:
            current_text = self.display_canvas.itemcget("display", "text")
            new_text = current_text + str(self.number)
            self.display_canvas.itemconfig("display", text=new_text)
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
    img = Image.open("tür.jpg")
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
        lambda: [ws := new_window("GLH TXHUVXPPH GLHVHU GUHL CDKOHQ HUJLHW HLQH GUHL"), ws.after(3000, ws.destroy)],    #die Quersumme dieser drei Zahlen ergibt eine drei
        "escape_room/door.jpg"),
    # [Other doors remain the same...]
    Door(window, 235, 0, "Door 2", "black", 
        lambda: [ws := new_window("CDKOH GLH QXPPEU GHU HUVW HQG GHU GULWWHQ WXU. VLH HUJHEHQ 7."), ws.after(30000, ws.destroy)],   #Zähle die Nummern der ersten und der dritten Tür. Sie ergeben 7 
        "escape_room/door.jpg"),
    Door(window, 410, 0, "Door 3", "red", 
        lambda: [ws := new_window("ELOGH GHQ GXFKVFKQLWW GHU HUVWHQ GULWWHQ XQG CZHLWHQ WXU. GHU GXUFKVFKQLWW HUJHHE VHFKV"), ws.after(30000, ws.destroy)],    #Bilde den Durchschnitt der ersten, dritten und zweiten Tür. der durchscnnitt sollte sechs ergeben im caesar
        "escape_room/door.jpg"),
    Door(window, 70, 280, "Door 4", "yellow", 
        lambda: [ws := new_window("glh qxpphu ghlvhu wxu lwvlqgq dgglq rxrphq yruq dohq yrukhqwjh qxuhq"), ws.after(30000, ws.destroy)],    # die nummer dieser tür ist die addition von allen vorherigen türen
        "escape_room/door.jpg"),
    Door(window, 235, 280, "Door 5", "red", 
        lambda: [ws := new_window("Dieser Code ist nach einem bekannten römischen Diktator aufgebaut"), ws.after(30000, ws.destroy)],   
        "escape_room/door.jpg"),
    Door(window, 410, 280, "Door 6", "yellow", 
        lambda: [ws := new_window("GLH TXHUVXPPH GHU HUVW HQ WXU VDJW GLU, DQ ZHOFKH VWHOOH VLH NRPPW"), ws.after(30000, ws.destroy)],  #die Quersumme der esten tür sagt dir, an welche stelle sie kommt
        "escape_room/door.jpg")
]

# [Rest of UI elements and functions remain unchanged...]
def get_input(x):
    return txt.get('1.0', 'end-1c').strip()




def next_level():
    for widget in window.winfo_children():
        widget.destroy()
    # Add new UI elements after clearing
    canva = tk.Canvas(window, width=1100, height=800)
    try:
        img = Image.open("tresor.jpg")
        img = img.resize((1100, 800), Image.LANCZOS)
        image = ImageTk.PhotoImage(img)
        canva.create_image(0, 0, image=image, anchor="nw")
        canva.image = image  
    except:
        canva.configure(bg='blue')
    canva.pack(fill="both", expand=True)

    display = tk.Canvas(window, width=300, height=100, bg="white")
    display.place(x=250, y=400)
    display.create_text(150, 50, text="", font=("Arial", 24), tags="display")
    #The next level is created here
    def another_lvl():
        if display.itemcget("display", "text") == "1215311":
            for widget in window.winfo_children():
                widget.destroy()
            lvl3()
            ws=new_window("wow didnt think u could do it, congrats")
            ws.after(3000, ws.destroy)
        else:
            ws=new_window("u got it wrong, try again!")
            ws.after(3000, ws.destroy)
    next_btn = tk.Button(window, text="Start Next Challenge", 
                               command=another_lvl,
                               font=("Arial", 14))
    next_btn.place(x=500, y=200)

    coords = {
        0: (620, 466), 1: (572, 322), 2: (620, 322), 3: (668, 322), 4: (572, 370),
        5: (620, 370), 6: (668, 370), 7: (572, 418), 8: (620, 418), 9: (668, 418)
    }
    
    next_quiz=tk.Label(window,text="charlie",font=("Arial",36))
    next_quiz.place(x=50,y=50)
    nq1=tk.Label(window,text="lima",font=("Arial",36))
    nq1.place(x=500,y=50)
    nq2=tk.Label(window,text="oscar",font=("Arial",36))
    nq2.place(x=800,y=50)
    nq3=tk.Label(window,text="kilo",font=("Arial",36))
    nq3.place(x=800,y=600) 

    for num, (x, y) in coords.items():
        NumberRectangle(window, x, y, num, display_canvas=display)
        
    def clear_sequence():
        display.itemconfig("display", text="")
    
    clear_btn = tk.Button(window, text="Clear",command=clear_sequence,
                         font=("Arial", 12))
    clear_btn.place(x=400, y=500)
    # Add new instruction label
    new_label = tk.Label(window, 
                        text="You've cleared the first room!\nNow solve the next puzzle:\n find out what the names are saying,\n put them in the right order\n and get the right combination",
                        font=("Arial", 16))
    new_label.place(x=220, y=275)




#the next floor

def lvl3():
    canva = tk.Canvas(window, width=1100, height=800)
    try:
        img = Image.open("by.jpg")
        img = img.resize((1100, 800), Image.LANCZOS)
        image = ImageTk.PhotoImage(img)
        canva.create_image(0, 0, image=image, anchor="nw")
        canva.image = image  
    except:
        canva.configure(bg='blue')
    canva.pack(fill="both", expand=True)
    left= tk.Label( window, text="left",font=("Arial", 36))
    left.place(x=150,y=50)
    right=tk.Label(window,text="right",font=("Arial",36))
    right.place(x=880,y=50)
    middle=tk.Label( window, text="middle",font=("Arial", 36))
    middle.place(x=500,y=50)

    # Create invisible rectangles on the background canvas with tags
    rectanglel = canva.create_rectangle(65, 150, 65+250, 150+520, outline="", fill="", tags="left")
    rectanglem = canva.create_rectangle(410, 150, 410+270, 150+520, outline="", fill="", tags="middle")
    rectangler = canva.create_rectangle(780, 150, 780+250, 150+520, outline="", fill="", tags="right")

    # Define a single click handler for all rectangles
    def on_click(event):
        clicked_items = event.widget.find_withtag("current")
        if not clicked_items:
            return
        tags = event.widget.gettags(clicked_items[0])
        if "left" in tags:
            print("Clicked left area")

    # Clear the window
            for widget in window.winfo_children():
                widget.destroy()

    # Create new canvas
            canvas = tk.Canvas(window, width=1100, height=800)

    # Try to load background image
            try:
                bg_image = Image.open("schatten.jpg")
                bg_image = bg_image.resize((1100, 800), Image.LANCZOS)
                bg_photo = ImageTk.PhotoImage(bg_image)
                canvas.create_image(0, 0, image=bg_photo, anchor="nw")
                canvas.image = bg_photo  # Keep a reference
            except Exception as e:
                print("Image loading failed:", e)
                canvas.configure(bg='blue')

            canvas.pack(fill="both", expand=True)
        elif "middle" in tags:
            print("Clicked middle area")

    # Clear the window
            for widget in window.winfo_children():
                widget.destroy()

    # Create new canvas
            canvas = tk.Canvas(window, width=1100, height=800)

    # Try to load background image
            try:
                bg_image = Image.open("book.jpg")
                bg_image = bg_image.resize((1100, 800), Image.LANCZOS)
                bg_photo = ImageTk.PhotoImage(bg_image)
                canvas.create_image(0, 0, image=bg_photo, anchor="nw")
                canvas.image = bg_photo  # Keep a reference
            except Exception as e:
                print("Image loading failed:", e)
                canvas.configure(bg='blue')

            canvas.pack(fill="both", expand=True)
        elif "right" in tags:
            print("Clicked right area")

    # Clear the window
            for widget in window.winfo_children():
                widget.destroy()

    # Create new canvas
            canvas = tk.Canvas(window, width=1100, height=800)

    # Try to load background image
            try:
                bg_image = Image.open("awll.jpg")
                bg_image = bg_image.resize((1100, 800), Image.LANCZOS)
                bg_photo = ImageTk.PhotoImage(bg_image)
                canvas.create_image(0, 0, image=bg_photo, anchor="nw")
                canvas.image = bg_photo  # Keep a reference
            except Exception as e:
                print("Image loading failed:", e)
                canvas.configure(bg='blue')

            canvas.pack(fill="both", expand=True)

    # Add intentionally incorrect riddle statements
            riddle_text = (
                "2 + 2 = 5\n"                        # V
                "Hauptstadt von Frankreich = Rom\n"  # P
                "Die Farbe der Sonne = Blau\n"       # G
                "Gegenteil von heiß = Banane\n"      # K
                "Wasser gefriert bei = 50°C\n"       # N
                "Die Quadratwurzel von 9 = 1\n"      # D
                "Es gibt __ Tage in der Woche = 10\n" # S
                "Die Erde ist flach = Ja"            # R
            )

            riddle_label = tk.Label(window, text=riddle_text, font=("Helvetica", 14), bg="white", justify="left")
            riddle_label.place(x=50, y=50)

    # Solution word based on false statements: VPGKNDSR

            
            # return "break"

    # Bind the single click handler to all rectangles
    canva.tag_bind("left", "<Button-1>", on_click)
    canva.tag_bind("middle", "<Button-1>", on_click)
    canva.tag_bind("right", "<Button-1>", on_click)









def end_window():
    user_input = get_input("u got the right code")
    
    try:
        if int(user_input) == 4239:
            next_level()
            # Add new UI elements for the next challenge
            
            ws=new_window("you cleared the first room")
            ws.after(2000, ws.destroy)
            
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

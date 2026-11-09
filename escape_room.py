
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

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
                                 width=20, 
                                 height=20,
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
                img = img.resize((160, 350), Image.LANCZOS)
                self.door_img = ImageTk.PhotoImage(img)
                self.label = tk.Label(self.master, image=self.door_img, 
                                   highlightthickness=0, bd=0, relief="flat")
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
#Room canvas
def load_room(bg_image_path,):
    clear_window()
    canvas = tk.Canvas(window, width=1100, height=800)
    try:
        bg_image = Image.open(bg_image_path)
        bg_image = bg_image.resize((1100, 800), Image.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        canvas.image = bg_photo
        
    except Exception as e:
        print("Image loading failed:", e)
        canvas.configure(bg='blue')
    canvas.pack(fill="both", expand=True)

# Background image
canva = tk.Canvas(window, width=1100, height=800)
try:
    img = Image.open("lvl1_bg.png")
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
                   "die zur richtigen Lösung führt", 
                   font=("Arial", 12), wraplength=400)
settings.place(x=400, y=70)
settings.lift()

doors = [
    Door(window, 260, 135, "Door 1", "yellow", 
        lambda: [ws := new_window("4-9-5 19-21-13-13-5 4-9-5-19-5-18 4-18-5-9 26-1-8-12-5-14 5-18-7-9-2-20 5-9-14-5 1-3-8-20 \nWelcher Satz ergibt sich aus diesen Buchstaben"), ws.after(120000, ws.destroy)],    #die summe dieser drei Zahlen ergibt eine acht
        image_path="door.jpg"),
    # [Other doors remain the same...]
    Door(window, 445, 135, "Door 2", "black", 
        lambda: [ws := new_window("2-3-3-444-33-777-33 3-444-33 6-88-6-6-33-777-6 3-33-777 33-777-7777-8-33-6 88-6-3 3-33-777 3-777-444-8-8-33-6 9999-444-333-333-33-777 7777-444-33 33-777-4-33-22-33-6 7777-33-22-7777"), ws.after(120000, ws.destroy)],   #addiere die Nummern der ersten und der dritten ZIffer. Sie ergeben sechs 
        image_path="door.jpg"),
    Door(window, 617, 135, "Door 3", "red", 
        lambda: [ws := new_window("dBile edn Drcthsnuiurdh dre etrsnen, drhteicn nud tzcwenet dnu dre lztense Zfifer. rde ducrhsnnticit oslteh rvei rgenbee"), ws.after(120000, ws.destroy)],    #Bilde den Durchschnitt der ersten, dritten und zweiten und der letzten  Ziffer. der durchscnnitt sollte vier ergeben,  
        image_path="door.jpg"),
    Door(window, 780, 135, "Door 4", "yellow", 
        lambda: [ws := new_window("9999-2-44-555-33-66 4-33-777-2-3-33 7777-444-66-3 222-666-3-33-7777 3-33-7777 9999-444-333-333-33-777-66 2-555-555-33\n Ähnlich wie Tür 2"), ws.after(120000, ws.destroy)],  #alle Ziffern des Codes sind gerade Zahlen
        image_path="door.jpg")  
]

# [Rest of UI elements and functions remain unchanged...]
def get_input(x):
    return txt.get('1.0', 'end-1c').strip()

def end_window():
    user_input = get_input("u got the right code")
    #Try if the 1st lvl is solved correctly
    try:
        if int(user_input) == 4228:
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
                      font=("Arial", 15))
instruction.place(x=450, y=520)

txt = tk.Text(window, height=1, width=10, font=("Arial", 12), 
             padx=10, pady=10, wrap=tk.WORD)
txt.place(x=460, y=555)

btn = tk.Button(window, text="Submit Code", command=end_window,
               font=("Arial", 12), padx=20, pady=5)
btn.place(x=580, y=555)

def next_level():
    clear_window()
    # Add new UI elements after clearing
    canva = tk.Canvas(window, width=1100, height=800)
    try:
        img = Image.open("lvl2_bg.png")
        img = img.resize((1100, 800), Image.LANCZOS)
        image = ImageTk.PhotoImage(img)
        canva.create_image(0, 0, image=image, anchor="nw")
        canva.image = image  
    except:
        canva.configure(bg='blue')
    canva.pack(fill="both", expand=True)

    display = tk.Canvas(window, width=105, height=20, bg="silver")
    display.place(x=730, y=467)
    display.create_text(50, 10, text="", font=("Arial", 10), tags="display")
    
    
    def lvl_2():
        try:
            current_text = display.itemcget("display", "text")
            if current_text == "31215311":
                ws = new_window("wow didnt think u could do it, congrats")
                ws.after(3000, lambda: [ws.destroy(), lvl3()])
            else:
                ws = new_window("u got it wrong, try again!")
                ws.after(3000, ws.destroy)
        except tk.TclError:
            # Handle case where display canvas might be destroyed
            ws = new_window("Error accessing display. Please restart.")
            ws.after(3000, ws.destroy)
    next_btn = tk.Button(window, text="Start Next Challenge",bg="silver", 
                               command=lvl_2,
                               font=("Arial", 10))
    next_btn.place(x=880, y=465)
    
    def clear_sequence():
        display.itemconfig("display", text="")
    
    clear_btn = tk.Button(window, text="Clear",command=clear_sequence,bg="silver",font=("Arial", 10))
    clear_btn.place(x=840, y=465)

    coords = {
        0: (937, 416), 1: (910, 331), 2: (935, 331), 3: (961, 331), 4: (911, 358),
        5: (935, 358), 6: (962, 358), 7: (910, 388), 8: (935, 388), 9: (962, 388)
    }

    
    
    nq3=tk.Label(window,padx=18,pady=2,text="kilo",font=("Arial",30), highlightthickness=0, fg="black")
    nq3.place(x=530,y=480)
    
    for num, (x, y) in coords.items():
        NumberRectangle(window, x, y, num, display_canvas=display)
        
    

#the next floor

def lvl3():
    clear_window()
    
    # Create new canvas for level 3
    canva = tk.Canvas(window, width=1100, height=800)
    try:
        bg_image = Image.open("by.jpg")
        bg_image = bg_image.resize((1100, 800), Image.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        canva.create_image(0, 0, image=bg_photo, anchor="nw")
        canva.image = bg_photo
    except Exception as e:
        print("Image loading failed:", e)
        canva.configure(bg='blue')
    canva.pack(fill="both", expand=True)

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
            clear_window()
            
            # Create new canvas for archive cabinet - load left_tag.png first
            canvas = tk.Canvas(window, width=1100, height=800, highlightthickness=0)
            try:
                bg_image = Image.open("left_tag.png")
                bg_image = bg_image.resize((1100, 800), Image.LANCZOS)
                bg_photo = ImageTk.PhotoImage(bg_image)
                canvas.create_image(0, 0, image=bg_photo, anchor="nw")
                canvas.image = bg_photo  # Keep reference to prevent garbage collection
            except Exception as e:
                print("Image loading failed:", e)
                canvas.configure(bg='brown')
            canvas.pack(fill="both", expand=True)
            
            # Now draw everything directly on the same canvas (no second canvas on top)
            
            # Draw cabinet border
            canvas.create_rectangle(45, 145, 1055, 555, width=8)
            canvas.create_text(550, 165, text="ARCHIV SCHUBLADEN", font=("Arial", 20, "bold"), fill="yellow")
        
            
            # Title
            title_label = tk.Label(window, 
                                  text="Nur wer die richtigen Ereignisse verbindet, kann das Archiv öffnen.",
                                  font=("Arial", 20), fg="white", bg="#623412")
            title_label.place(x=280, y=20)
            
            # Instruction
            instruction_label = tk.Label(window,
                                        text="Klicke auf die Schubladen für Hinweisen \nOrdne die Ereignisse chronologisch. Die letzten Ziffern ergeben den Code.",
                                        font=("Arial", 20), fg="white", bg="#623412")
            instruction_label.place(x=280, y=60)
            
            # Archive cabinet data - 5 drawers with historical events
            # Each drawer: (year, event_name, last_digit)
            drawers = {
                1: {"year": 1789, "event": "Französische Revolution", "digit": "9"},
                2: {"year": 1969, "event": "Mondlandung", "digit": "9"},
                3: {"year": 1453, "event": "Fall von Konstantinopel", "digit": "3"},
                4: {"year": 1960, "event": "Erfindung des Internets", "digit": "0"},
                5: {"year": 476, "event": "Untergang des Weströmischen Reiches", "digit": "6"}
            }
            
            # Track selected drawers in order
            selected_drawers = []
            
            # Create 5 clickable drawer rectangles
            drawer_positions = [
                (100, 260, "Schublade 1\nFranzösische Revolution"),
                (295, 260, "Schublade 2\nMondlandung"),
                (485, 260, "Schublade 3\nFall von Konstantinopel"),
                (670, 260, "Schublade 4\nErfindung des Internets"),
                (845, 260, "Schublade 5\nUntergang des\n Weströmischen Reiches")
            ]
            
            # Draw 5 drawers directly on the same canvas
            drawer_buttons = []

            # Define functions BEFORE they are used in tag_bind
            def show_drawer_content(drawer_num):
                """Show content when a drawer is clicked"""
                drawer_info = drawers[drawer_num]
                
                # Show the event in a new window
                event_window = tk.Toplevel()
                event_window.geometry("500x200")
                event_window.title(f"Schublade {drawer_num}")
                
                """event_label = tk.Label(event_window,
                                      text=f"Jahr: {drawer_info['year']}\n\n{drawer_info['event']}\n\nLetzte Ziffer: {drawer_info['digit']}",
                                      font=("Arial", 14),
                                      wraplength=450)
                event_label.pack(expand=True)"""
                
                # Auto-close the window after 5 seconds (5000 milliseconds)
                event_window.after(5000, event_window.destroy)
                
                # Add to selection if not already selected
                # Drawers are now just for viewing info, no automatic verification
                if drawer_num not in selected_drawers:
                    selected_drawers.append(drawer_num)
                    # Update instruction label - just for tracking, no verification
                    instruction_label.config(text=f"Klicke auf die Schubladen für Hinweise!\nAusgewählte: {len(selected_drawers)}\nAusgewählte Nummern: {selected_drawers}")

                # Automatic verification removed - only submit button verifies the code
            
            def verify_archive_code():
                """Verify if the selected drawers are in correct chronological order"""
                # The correct chronological order (earliest to latest):
                # 476 (Schublade 5) → 1453 (Schublade 3) → 1789 (Schublade 1) → 1969 (Schublade 2)
                # Digits: 6, 3, 9, 9
                
                correct_order = [5, 3, 1, 4]  # Drawer numbers in chronological order
                expected_code = "6390"
                
                # Get the digits from selected drawers in order
                user_code = ""
                for drawer_num in selected_drawers:
                    user_code += drawers[drawer_num]["digit"]
                
                print(f"User selected: {selected_drawers}")
                print(f"User code: {user_code}")
                print(f"Expected code: {expected_code}")
                
                if user_code == expected_code:
                    # Correct! Show success and proceed
                    ws = new_window("Richtig! Das Archiv öffnet sich! Du hast den Code 6399 gefunden!\nProbiere ein anderes Rätsel")
                    ws.after(3000, lambda: [ws.destroy(), lvl3()])
                else:
                    # Wrong! Show failure and restart
                    ws = new_window(f"Falsch! Dein Code: {user_code}. Versuche es nochmal!")
                    ws.after(3000, lambda: [ws.destroy()])
                    lvl3()
                    

            
            # Now create the drawer elements as transparent clickable frames
            for i, (x, y, text) in enumerate(drawer_positions, 1):
                # Create a transparent frame for each drawer - truly invisible
                drawer_canvas = tk.Canvas(window,

                                        width=180, 
                                        height=130,
                                        highlightthickness=0,
                                        bg="#623412"
                                        )
                                        
                                        
                drawer_canvas.place(x=x, y=y)
                
                # Draw the title on the drawer canvas
                drawer_canvas.create_text(90, 50, text=text, font=("Arial", 10), fill="black")
                
                # Each drawer has a different task
                def create_task_handler(drawer_num):
                    def show_task():
                        tasks = {
                            1: "Task 1: Find the year of the French Revolution\nAnswer: 1789",
                            2: "Task 2: Find the year of the Moon landing\nAnswer: 1969",
                            3: "Task 3: Find the year of the Fall of Constantinople\nAnswer: 1453",
                            4: "Task 4: Find the year the Internet was invented\nAnswer: 1960",
                            5: "Task 5: Find the year of the Fall of the Western Roman Empire\nAnswer: 476"
                        }
                        ws = new_window(tasks.get(drawer_num, "No task"))
                        ws.after(5000, ws.destroy)
                    return show_task
                
                # Bind click event to show the specific task for each drawer
                drawer_canvas.bind("<Button-1>", lambda e, d=i: create_task_handler(d)())
                drawer_buttons.append(drawer_canvas)
            
            # Code input field at the bottom
            
            
            code_entry = tk.Entry(window, font=("Arial", 14), width=10)
            code_entry.place(x=500, y=580)
            
            def submit_code():
                user_code = code_entry.get().strip()
                if user_code == "6390":
                    ws = new_window("Richtig! Das Archiv öffnet sich! Du hast den Code 6399 gefunden!")
                    ws.after(3000, lambda: [ws.destroy(), lvl3()])
                else:
                    ws = new_window(f"Falsch! Dein Code: {user_code}. Versuche es nochmal!")
                    ws.after(3000, ws.destroy)
            
            submit_btn = tk.Button(window,
                                  text="Code prüfen",
                                  font=("Arial", 11),
                                  command=submit_code)
            submit_btn.place(x=620, y=580)
            
            # Bring labels to front
            title_label.lift()
            instruction_label.lift()
            submit_btn.lift()
            code_entry.lift()
            submit_btn.lift()
            
        elif "middle" in tags:
            print("Clicked middle area")
            
            # Clear the window
            clear_window()

            # Create new canvas
            canvas = tk.Canvas(window, width=1100, height=800)

            # Try to load background image (bibo.jpg)
            try:
                bg_image = Image.open("bibo.jpg")
                bg_image = bg_image.resize((1100, 800), Image.LANCZOS)
                bg_photo = ImageTk.PhotoImage(bg_image)
                canvas.create_image(0, 0, image=bg_photo, anchor="nw")
                canvas.image = bg_photo  # Keep a reference
                

            except Exception as e:
                print("Image loading failed:", e)
                canvas.configure(bg='blue')

            canvas.pack(fill="both", expand=True)

            # Store user inputs for further use
            user_inputs = {}
            current_riddle = [1]  # Track current riddle number
            
            # Add a button that's the size of a rectangle (160x270 like the doors)
            button_click_count = [0]  # Use list to make it mutable in nested function
            
            # Function to show a canvas window for each try - shows one at a time
            def show_try_canvas(try_number):
                # Create a new window
                try_window = tk.Toplevel()
                try_window.geometry("400x400")
                try_window.title(f"Riddle {try_number}")
                try_window.after(30000, try_window.destroy)  # 30 seconds timeout
                
                # Create canvas in the window
                canvas = tk.Canvas(try_window, width=400, height=400, bg="black")
                canvas.pack(fill="both", expand=True)
                
                # Different riddles for each try
                riddles = {
                    1: ("Riddle 1: Ich starb im Jahr LXXVI vor Christus.\nMein Tod brachte das Ende einer Republik. \n mein Name beginnt C und endet mit R", "Caesar"),
                    2: ("Riddle 2: Ich bin die Summe aus 8 und 4.\nMeine Hälfte ist die Antwort.", "6"),
                    3: ("Riddle 3: Ich bin eine Zahl zwischen 1 und 10.\nVerdoppelt mich und ihr erhaltet die die gleiche zahl quadriert.", "2")
                }
                
                riddle_text, correct_answer = riddles.get(try_number, ("No riddle", ""))
                
                # Add text to canvas
                canvas.create_text(200, 50, text=f"Riddle {try_number}/3", font=("Arial", 16, "bold"), fill="black")
                canvas.create_text(200, 100, text=riddle_text, font=("Arial", 11), fill="white")
                
                # Add input field for user answer
                canvas.create_text(200, 200, text="Your answer:", font=("Arial", 12), fill="black")
                input_field = tk.Entry(try_window, font=("Arial", 12), width=25)
                input_field.place(x=100, y=220)
                
                # Result label
                result_label = tk.Label(try_window, text="", font=("Arial", 12))
                result_label.place(x=100, y=280)
                
                # Function to verify answer immediately after submission
                def verify_and_continue():
                    user_answer = input_field.get().strip()
                    user_inputs[try_number] = user_answer
                    print(f"Riddle {try_number} input: {user_answer}")
                    
                    if user_answer == correct_answer:
                        # Correct! Show success and move to next riddle
                        result_label.config(text=f"Correct! ✓", fg="green")
                        print(f"Riddle {try_number}: Correct!")
                        try_window.destroy()
                        
                        if try_number < 3:
                            # Show next riddle
                            current_riddle[0] = try_number + 1
                            show_try_canvas(try_number + 1)
                        else:
                            # All 3 riddles completed correctly
                            ws = new_window("All 3 Correct! Congratulations! Try another riddle.")
                            ws.after(3000, lambda: [ws.destroy(), lvl3()])
                    else:
                        # Wrong! Show error and allow retry
                        result_label.config(text=f"Wrong! Expected '{correct_answer}', try again!", fg="red")
                        print(f"Riddle {try_number}: Wrong! Expected '{correct_answer}', got '{user_answer}'")
                        # Don't close window, let user try again
                
                # Add submit button
                submit_btn = tk.Button(try_window, text="Submit Answer", command=verify_and_continue, font=("Arial", 11))
                submit_btn.place(x=140, y=250)
                
                # Progress indicator
                canvas.create_text(200, 370, text=f"Riddle {try_number} of 3", font=("Arial", 10), fill="black")
                
                return try_window
            
            def restart_riddle(riddle_num):
                """Restart a specific riddle"""
                # Clear the specific riddle from user_inputs to allow fresh attempt
                if riddle_num in user_inputs:
                    del user_inputs[riddle_num]
                show_try_canvas(riddle_num)
            
            def toggle_button_visibility():
                button_click_count[0] += 1
                print(f"Button clicked {button_click_count[0]} times")
                
                # Show first riddle on first click
                if button_click_count[0] == 1:
                    show_try_canvas(1)
                    print("First riddle shown")
                else:
                    # Already shown the riddle
                    ws = new_window("You're already on a riddle! Answer it first.")
                    ws.after(2000, ws.destroy)
                
            # Create a button the size of a rectangle (width=160, height=270 like the doors)
            # This button will be reused - no need to create new one each time
            secret_button = tk.Button(window, 
                                     text="Click me!\n(3 tries)", 
                                     font=("Arial", 14),
                                     command=toggle_button_visibility,
                                     bg="lightblue"

                                     )
            secret_button.place(width=1100, height=800)
            
            # Track if there's already a riddle window open
            riddle_window_open = [False]
            
            # Override toggle_button_visibility to prevent multiple windows
            def toggle_button_visibility():
                if riddle_window_open[0]:
                    # Already a window open - show message but don't create new window
                    ws = new_window("You're already on a riddle! Answer it first.")
                    ws.after(2000, ws.destroy)
                    return
                
                button_click_count[0] += 1
                print(f"Button clicked {button_click_count[0]} times")
                
                # Show first riddle on first click
                if button_click_count[0] == 1:
                    riddle_window_open[0] = True
                    show_try_canvas(1)
                    print("First riddle shown")
                else:
                    # Already shown the riddle
                    ws = new_window("You're already on a riddle! Answer it first.")
                    ws.after(2000, ws.destroy)
            
            # Override show_try_canvas to track window state
            original_show_try_canvas = show_try_canvas
            
            def show_try_canvas(try_number):
                # Create a new window
                try_window = tk.Toplevel()
                try_window.geometry("400x450")
                try_window.title(f"Riddle {try_number}")
                try_window.resizable(False, False)
                
                # Create canvas in the window
                canvas = tk.Canvas(try_window, width=400, height=450, bg="lightblue")
                canvas.pack(fill="both", expand=True)
                
                # Different riddles for each try
                riddles = {
                    1: ("Riddle 1: Ich starb im Jahr LXXVI vor Christus.\nMein Tod brachte das Ende einer Republik. \nMein Name beginnt C und endet mit R", "Caesar"),
                    2: ("Riddle 2: Ich bin die Summe aus 8 und 4.\nMeine Hälfte ist die Antwort.", "6"),
                    3: ("Riddle 3: Ich bin eine Zahl zwischen 1 und 10.\nVerdoppelt mich und ihr erhaltet die gleiche Zahl quadriert.", "2")
                }
                
                riddle_text, correct_answer = riddles.get(try_number, ("No riddle", ""))
                
                # Add text to canvas
                canvas.create_text(200, 40, text=f"Riddle {try_number}/3", font=("Arial", 18, "bold"), fill="black")
                canvas.create_text(200, 100, text=riddle_text, font=("Arial", 12), fill="darkblue")
                
                # Add input field for user answer
                canvas.create_text(200, 200, text="Your answer:", font=("Arial", 14), fill="black")
                input_field = tk.Entry(try_window, font=("Arial", 14), width=25)
                input_field.place(x=100, y=220)
                input_field.focus()
                
                # Result label
                result_label = tk.Label(try_window, text="", font=("Arial", 12))
                result_label.place(x=50, y=280)
                
                # Function to verify answer immediately after submission
                def verify_and_continue():
                    user_answer = input_field.get().strip()
                    user_inputs[try_number] = user_answer
                    print(f"Riddle {try_number} input: '{user_answer}'")
                    
                    if not user_answer:
                        result_label.config(text="Please enter an answer!", fg="orange")
                        return
                    
                    if user_answer == correct_answer:
                        # Correct! Show success and move to next riddle
                        result_label.config(text=f"Correct! ✓", fg="green", font=("Arial", 14, "bold"))
                        print(f"Riddle {try_number}: Correct!")
                        
                        
                        if try_number < 3:
                            # Show next riddle after a short delay
                            try_window.after(1500, lambda: show_try_canvas(try_number + 1))
                        else:
                            # All 3 riddles completed correctly
                            ws = new_window("All 3 Correct! Congratulations! Try another riddle.")
                            ws.after(3000, lambda: [ws.destroy(), lvl3()])
                    else:
                        # Wrong! Show error and allow retry - window STAYS OPEN
                        result_label.config(text=f"Wrong! Expected '{correct_answer}', try again!", fg="red", font=("Arial", 12))
                        print(f"Riddle {try_number}: Wrong! Expected '{correct_answer}', got '{user_answer}'")
                        # Window stays open - user can try again
                        # Clear the input field for retry
                        input_field.delete(0, tk.END)
                
                # Add submit button
                submit_btn = tk.Button(try_window, text="Submit Answer", command=verify_and_continue, 
                                     font=("Arial", 12), bg="lightgreen", padx=20, pady=5)
                submit_btn.place(x=140, y=260)
                
                # Add Enter key binding to submit
                input_field.bind('<Return>', lambda e: verify_and_continue())
                
                # Progress indicator
                canvas.create_text(200, 420, text=f"Riddle {try_number} of 3", font=("Arial", 10), fill="black")
                
                # Track when window is closed
                def on_window_close():
                    riddle_window_open[0] = False
                    try_window.destroy()
                
                try_window.protocol("WM_DELETE_WINDOW", on_window_close)
                
                return try_window
            
                
        elif "right" in tags:
            print("Clicked right area")

            # Clear the window
            clear_window()

            # Create new canvas
            canvas = tk.Canvas(window, width=1100, height=800)

            # Try to load background image
            try:
                bg_image = Image.open("right_tag.png")
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
                "Die Erde ist flach = Ja"            # N
            )
            riddle_label = tk.Label(window, text=riddle_text, font=("Helvetica", 25), bg="white", justify="left")
            #riddle_label.place(x=70, y=70)
            riddle_hint = tk.Label(window, text="give the first letter of the right answer of this riddle",font=("Helvetica", 15))
            riddle_hint.place(x=130,y=50)



            ridd = tk.Text(window, height=6, width=34, font=("Arial", 12), padx=18, pady=6, wrap=tk.WORD)
            ridd.place(x=605, y=380)
            def check_code():
                us_input = ridd.get("1.0", "end-1c").strip().upper()
                if us_input == "VPGKNDSN":
                    print("Correct answer!")
                    new_window("You won!")
                    fin_window()
                    
                else:

                    clear_window()
                    lvl3()
                    print("Wrong answer!")
                    new_window("You lost!, try again")
            btn = tk.Button(window, text="Submit Code    ", command=check_code,
                                font=("Arial", 13), padx=35, pady=4)
            btn.place(x=660, y=500)

            # UI

    # Solution word based on false statements: VPGKNDSR

            
            # return "break"

    # Bind the single click handler to all rectangles
    canva.tag_bind("left", "<Button-1>", on_click)
    canva.tag_bind("middle", "<Button-1>", on_click)
    canva.tag_bind("right", "<Button-1>", on_click)

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()


def fin_window():
    clear_window()
    c=tk.Canvas(width=1100, height=800)
    c.pack(fill="both", expand=True)
    winner=tk.Label(c,text="You escaped the Escape Room!",font=("Arial", 60),bg="white")
    winner.place(relx= 0.5, rely=0.5, anchor="center")
    # Destroy the complete window after 5 seconds
    window.after(5000, window.destroy)

#Lvl 3 in the middle    
def lvl3_middle():
    clear_window()
    m=tk.Canvas(width=1100, height=800, bg="white")
    m.place(x=0, y=0, width=1100, height=800)
    m.create_text(550, 400, text="The answer you gave was correct, but sadly this was not the right exit. Try another room :)", font=("Arial", 60), fill="black", anchor="center")
    ans = tk.Canvas(width=300, height=100,bg="blue")
    ans.place(x=1100, y=800, anchor="se")
    ans.lift()



window.mainloop()
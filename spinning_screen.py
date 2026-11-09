import tkinter as tk
import math
import time

class SpinningScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Spinning Screen")
        self.master.geometry("800x600")
        self.master.configure(bg='black')
        
        # Create canvas
        self.canvas = tk.Canvas(master, width=800, height=600, bg='black', highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        # Animation variables
        self.angle = 0
        self.spinning = False
        self.objects = []
        
        # Create spinning elements
        self.create_spinning_elements()
        
        # Start button
        self.start_btn = tk.Button(master, text="Start Spinning", command=self.start_spinning, 
                                 font=("Arial", 14), bg="green", fg="white")
        self.start_btn.place(x=350, y=500)
        
        # Stop button
        self.stop_btn = tk.Button(master, text="Stop Spinning", command=self.stop_spinning, 
                                font=("Arial", 14), bg="red", fg="white")
        self.stop_btn.place(x=450, y=500)
        
    def create_spinning_elements(self):
        # Create a central circle
        self.center_x = 400
        self.center_y = 300
        
        # Create multiple circles that will spin
        for i in range(8):
            angle = (i * 45) * math.pi / 180
            radius = 150
            x = self.center_x + radius * math.cos(angle)
            y = self.center_y + radius * math.sin(angle)
            
            # Create colored circles
            colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'cyan']
            circle = self.canvas.create_oval(x-30, y-30, x+30, y+30, 
                                           fill=colors[i], outline='white', width=2)
            self.objects.append(circle)
        
        # Create center circle
        self.center_circle = self.canvas.create_oval(self.center_x-50, self.center_y-50,
                                                   self.center_x+50, self.center_y+50,
                                                   fill='white', outline='black', width=3)
        
        # Create spinning text
        self.text = self.canvas.create_text(self.center_x, self.center_y, 
                                          text="SPINNING", font=("Arial", 20, "bold"),
                                          fill='black')
        
    def start_spinning(self):
        if not self.spinning:
            self.spinning = True
            self.animate()
            
    def stop_spinning(self):
        self.spinning = False
        
    def animate(self):
        if self.spinning:
            self.angle += 5  # Rotation speed
            self.update_positions()
            self.master.after(50, self.animate)  # 50ms delay
            
    def update_positions(self):
        # Update positions of all circles
        for i, obj in enumerate(self.objects):
            base_angle = (i * 45) * math.pi / 180
            total_angle = (base_angle + self.angle * math.pi / 180)
            radius = 150
            
            x = self.center_x + radius * math.cos(total_angle)
            y = self.center_y + radius * math.sin(total_angle)
            
            self.canvas.coords(obj, x-30, y-30, x+30, y+30)
            
        # Add pulsing effect to center circle
        pulse = abs(math.sin(self.angle * 0.05)) * 20
        self.canvas.coords(self.center_circle, 
                          self.center_x-50-pulse, self.center_y-50-pulse,
                          self.center_x+50+pulse, self.center_y+50+pulse)

class AdvancedSpinningScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Spinning Screen")
        self.master.geometry("1000x700")
        self.master.configure(bg='black')
        
        # Create canvas
        self.canvas = tk.Canvas(master, width=1000, height=700, bg='black', highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        # Animation variables
        self.angle = 0
        self.spinning = False
        self.particles = []
        
        # Create advanced spinning elements
        self.create_advanced_elements()
        
        # Control frame
        self.control_frame = tk.Frame(master, bg='black')
        self.control_frame.place(x=50, y=650)
        
        # Speed control
        self.speed_label = tk.Label(self.control_frame, text="Speed:", fg='white', bg='black')
        self.speed_label.pack(side=tk.LEFT)
        
        self.speed_scale = tk.Scale(self.control_frame, from_=1, to=20, orient=tk.HORIZONTAL,
                                   bg='black', fg='white', troughcolor='gray')
        self.speed_scale.set(5)
        self.speed_scale.pack(side=tk.LEFT)
        
        # Start/Stop buttons
        self.start_btn = tk.Button(self.control_frame, text="Start", command=self.start_spinning,
                                 bg="green", fg="white")
        self.start_btn.pack(side=tk.LEFT, padx=5)
        
        self.stop_btn = tk.Button(self.control_frame, text="Stop", command=self.stop_spinning,
                                bg="red", fg="white")
        self.stop_btn.pack(side=tk.LEFT, padx=5)
        
    def create_advanced_elements(self):
        # Create spiral effect
        self.center_x = 500
        self.center_y = 350
        
        # Create spiral arms
        for arm in range(6):
            arm_angle = arm * 60
            for radius in range(20, 200, 20):
                angle = arm_angle * math.pi / 180
                x = self.center_x + radius * math.cos(angle)
                y = self.center_y + radius * math.sin(angle)
                
                # Create particles along spiral
                particle = self.canvas.create_oval(x-5, y-5, x+5, y+5,
                                                 fill='white', outline='cyan')
                self.particles.append((particle, arm, radius))
        
        # Create central star
        self.star = self.create_star(self.center_x, self.center_y, 100, 8, 'yellow')
        
        # Create outer ring
        self.ring = self.canvas.create_oval(self.center_x-200, self.center_y-200,
                                          self.center_x+200, self.center_y+200,
                                          outline='cyan', width=2)
        
    def create_star(self, x, y, size, points, color):
        points_list = []
        for i in range(points * 2):
            angle = i * math.pi / points
            if i % 2 == 0:
                r = size
            else:
                r = size / 2
            px = x + r * math.cos(angle)
            py = y + r * math.sin(angle)
            points_list.extend([px, py])
        return self.canvas.create_polygon(points_list, fill=color, outline='white')
        
    def start_spinning(self):
        if not self.spinning:
            self.spinning = True
            self.animate()
            
    def stop_spinning(self):
        self.spinning = False
        
    def animate(self):
        if self.spinning:
            self.angle += self.speed_scale.get()
            self.update_positions()
            self.master.after(30, self.animate)
            
    def update_positions(self):
        # Update spiral particles
        for particle, arm, radius in self.particles:
            base_angle = arm * 60 * math.pi / 180
            total_angle = (base_angle + self.angle * math.pi / 180)
            
            x = self.center_x + radius * math.cos(total_angle)
            y = self.center_y + radius * math.sin(total_angle)
            
            self.canvas.coords(particle, x-5, y-5, x+5, y+5)
            
            # Add color cycling
            colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
            color_index = int((self.angle / 10) % len(colors))
            self.canvas.itemconfig(particle, fill=colors[color_index])
            
        # Rotate star
        self.canvas.coords(self.star, self.create_star_coords(self.center_x, self.center_y, 
                                                            100 + 20 * math.sin(self.angle * 0.05), 8))
        
    def create_star_coords(self, x, y, size, points):
        coords = []
        for i in range(points * 2):
            angle = i * math.pi / points + self.angle * math.pi / 180
            if i % 2 == 0:
                r = size
            else:
                r = size / 2
            px = x + r * math.cos(angle)
            py = y + r * math.sin(angle)
            coords.extend([px, py])
        return coords

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    
    # Create simple spinning screen
    spinning = SpinningScreen(root)
    
    # Or create advanced spinning screen
    # advanced = AdvancedSpinningScreen(root)
    
    root.mainloop()

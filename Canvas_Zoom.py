import tkinter as tk

class Canvaszoom:
    def __init__(self,canvas):
        self.canvas=canvas
        self.flag_to_set_1=False
        self.flag_to_set_2=False
        self.scale_factor = 1.0
        self.canvas.bind("<MouseWheel>", self.scroll)
    def set_1(self):
        self.scale_factor=1.0
    def scroll(self,event):
        if not self.flag_to_set_1:
            if event.delta > 0:  # Scrolling up
               self. flag_to_set_1=True
               self. flag_to_set_2=False
               self.set_1()
                
        if not self.flag_to_set_2:
            if event.delta < 0:  # Scrolling up
                self.flag_to_set_1=False
                self.flag_to_set_2=True
                self.set_1()  
            
                
        
        
        
        if event.delta > 0:  # Scrolling up
            
          
                
            
            self.scale_factor *= 1.01
        else:  # Scrolling down
            self.scale_factor /= 1.01
        
        # Limit the scale factor within a specific range
       
        self.canvas.scale("all", event.x, event.y, self.scale_factor, self.scale_factor)
    

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
# Create some shapes on the canvas
rect = canvas.create_rectangle(50, 50, 150, 150, fill='blue')
circle = canvas.create_oval(200, 50, 300, 150, fill='red')
Canvaszoom(canvas)
root.mainloop()














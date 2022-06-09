import tkinter as Tk
from l_system import turtle_interprate
from fonc_file import save_content, open_file
import re
import turtle as tur
from tkinter import filedialog
from PIL import Image
import os


class GUI:
    def get_variable(self, arg):       
        rotate, iteration, line_length = 0, 0, 0
        axiom, key_value_pair, key, value = "", "", "", ""
        rules_list, start_point = [], []
        rules = {}
        content_text_rules = re.sub("\n", "", self.text_rules.get(0.0, Tk.END)[1:])
            
        axiom = self.entry_axiom.get()
        rotate = float(self.entry_rotation.get())
        iteration = int(self.entry_iteration.get())
        line_length = float(self.entry_line_length.get())
        
        start_point = self.entry_start_point.get().split(",")
        start_point[0], start_point[1] = float(start_point[0]), float(start_point[1])
        
        rules_list = content_text_rules.split("#")
        for line in rules_list:
            key_value_pair = line.split(":")
            key = key_value_pair[0]
            value = key_value_pair[1]
            rules[key] = value
        
        if arg == "Draw":
            turtle_interprate(l_string=axiom, rules=rules, rotate=rotate, number_of_iteration=iteration, line_length=line_length, start_point=start_point)
        if arg == "Save":
            save_content(l_string=axiom, rules_list=rules_list, rotate=rotate, number_of_iteration=iteration, line_length=line_length, start_point=start_point)
    
    
    def save_image(self):
        screen = tur.getscreen()
        filename = filedialog.asksaveasfilename(initialdir="/", title="Save as...", filetypes=(("Jpeg files", "*.jpeg"), ("All files", "*.")), defaultextension=(("Jpeg files", "*.jpeg"), ("All files", "*.")))
        screen.getcanvas().postscript(file="output.eps")
        img = Image.open("output.eps")
        img.save("%s" % (filename), "jpeg")
        img.close()
        os.remove("output.eps")
        

    def insert_info(self, l_string, rules_list, rotate, number_of_iteration, line_length, start_point):
        if start_point == []:
            start_point = [0, -500]
        self.entry_axiom.delete(0, Tk.END)
        self.entry_axiom.insert(0, l_string)
        self.entry_rotation.delete(0, Tk.END)
        self.entry_rotation.insert(0, rotate)
        self.entry_start_point.delete(0, Tk.END)
        self.entry_start_point.insert(0, "%s, %s" % (start_point[0], start_point[1]))
        self.entry_line_length.delete(0, Tk.END)
        self.entry_line_length.insert(0, line_length)
        self.entry_iteration.delete(0, Tk.END)
        self.entry_iteration.insert(0, number_of_iteration)
        self.text_rules.delete(0.0, Tk.END)
        for line in rules_list:
            self.text_rules.insert("%s.0" % (rules_list.index(line)), "#%s" % (line))
        
        
    def activate_widget(self, root):
        label_frame = Tk.LabelFrame(root, text="Configure your L-System :")
        frame1 = Tk.LabelFrame(label_frame, text="Variables :")
        frame2 = Tk.LabelFrame(label_frame, text="Actions :")
        
        Tk.Label(frame1, text="Axiom : ").grid(row=0, column=1)
        self.entry_axiom = Tk.Entry(frame1, width=10)
        self.entry_axiom.insert(0, "YYY")
        self.entry_axiom.grid(row=1, column=1)

        Tk.Label(frame1, text="Rotation : ").grid(row=2, column=1)
        self.entry_rotation = Tk.Entry(frame1, width=10)
        self.entry_rotation.insert(0, "50")
        self.entry_rotation.grid(row=3, column=1)

        Tk.Label(frame1, text="Start point : ").grid(row=4, column=1)
        self.entry_start_point = Tk.Entry(frame1, width=10)
        self.entry_start_point.insert(0, "0, -500")
        self.entry_start_point.grid(row=5, column=1)

        Tk.Label(frame1, text="Line length : ").grid(row=6, column=1)
        self.entry_line_length = Tk.Entry(frame1, width=10)
        self.entry_line_length.insert(0, "5")
        self.entry_line_length.grid(row=7, column=1)

        Tk.Label(frame1, text="Number of iteration : ").grid(row=6, column=3)
        self.entry_iteration = Tk.Entry(frame1, width=10)
        self.entry_iteration.insert(0, "6")
        self.entry_iteration.grid(row=7, column=3)

        Tk.Label(frame1, text="Rules (put a '#' between each) : ").grid(row=0, column=3)
        self.text_rules = Tk.Text(frame1, height=5, width=20, font=("Colibri", 10))
        self.text_rules.insert(0.0, "#X:X[-FFF][+FFF]FX\n#Y:YFX[+Y][-Y]")
        self.text_rules.grid(row=1, column=3, rowspan=5)
        
        frame1.pack(padx=10)
        
        Tk.Button(frame2, text="Draw", command=lambda: self.get_variable("Draw")).pack()
        
        Tk.Button(frame2, text="Save your L-System as .lsy", command=lambda: self.get_variable("Save")).pack()
        
        Tk.Button(frame2, text="Take a picture of your L-System", command= self.save_image).pack()
        
        frame2.pack()
        
        label_frame.pack(padx=10, pady=10)
        
        label_frame_2 = Tk.LabelFrame(root, text="Load an L-System from a .lsy file :")
        
        Tk.Button(label_frame_2, text="Please choose your file...", command=open_file).pack()
        
        label_frame_2.pack()
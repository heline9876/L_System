from tkinter import filedialog
from l_system import turtle_interprate
import re

files = [("L-System files", "*.lsy"),
         ("All files", "*")]

def open_file():
    content = ""
    filename = filedialog.askopenfilename(initialdir="/", title="Open...", filetypes=files, defaultextension=files)
    
    with open("%s" % (filename), "r") as file:
        content = file.readlines()
        read_content(content)
    

def read_content(content):
    from App_object import App
    
    rotate, iteration, line_length, number_of_rules = 0, 0, 0, 0
    axiom, key_value_pair, key, value = "", "", "", ""
    rules_list, start_point = [], []
    rules = {}
    
    for i in range(len(content)):
        if "axiom" in content[i]:
            axiom = content[i + 1]
        if "line length" in content[i]:
            line_length = float(content[i + 1])
        if "rotate" in content[i]:
            rotate = float(content[i + 1])
        elif "iteration" in content[i]:
            iteration = int(content[i + 1])
        elif "rules" in content[i]:
            number_of_rules = int(content[i + 1])
            rules_list.extend(content[i + 2 + j] for j in range(number_of_rules))
            for line in rules_list:
                key_value_pair = line.split(":")
                key = key_value_pair[0]
                value = re.sub("\n", "", key_value_pair[1])
                rules[key] = value
        elif "start point" in content[i]:
            start_point = content[i + 1].split(",")
            start_point[0], start_point[1] = float(start_point[0]), float(start_point[1])
    
    App.insert_info(l_string=axiom, rules_list=rules_list, rotate=rotate, number_of_iteration=iteration, line_length=line_length, start_point=start_point)
    turtle_interprate(l_string=axiom, rules=rules, rotate=rotate, number_of_iteration=iteration, line_length=line_length, start_point=start_point)
            

def save_content(l_string, rules_list, line_length, rotate, number_of_iteration, start_point):
    filename = filedialog.asksaveasfilename(initialdir="/", title="Save as...", filetypes=files, defaultextension=files)
    with open(filename, "w") as file:
        file.write("axiom: write below the axiom\n")
        file.write("%s\n" % (l_string))
        file.write("line length: write below the line length\n")
        file.write("%s\n" % (str(line_length)))
        file.write("rotate: write below the degree of rotation\n")
        file.write("%s\n" % (str(rotate)))
        file.write("iteration: write below the number of iterations\n")
        file.write("%s\n" % (str(number_of_iteration)))
        file.write("rules: write below the number of rules, then write them at the rate of one per line\n")
        file.write("%s\n" % (str(len(rules_list))))
        for line in rules_list:
            file.write("%s\n" % (str(line)))
        file.write("start point: you can optionally specify the starting coordinates of the turtle\n")
        file.write("%s, %s\n" % (str(start_point[0]), str(start_point[1])))

from tkinter import filedialog
from l_system import turtle_interprate
import re
import json


files = [("Json files", "*.json"),
         ("All files", "*")]


def open_file():
    content = ""
    filename = filedialog.askopenfilename(initialdir="/", title="Open...", filetypes=files, defaultextension=files)
    
    with open("%s" % (filename), "r") as file:
        content_json = file.read()
        content = json.loads(content_json)
        read_content(content)
    

def read_content(content):
    from App_object import App

    rotate, iteration, line_length = content["rotate"], content["iteration"], content["line_length"]
    axiom = content["axiom"]
    rules_list, start_point = content["rules"], content["start_point"]
    rules = {}
    for line in rules_list:
        key_value_pair = line.split(":")
        key = key_value_pair[0]
        value = re.sub("\n", "", key_value_pair[1])
        rules[key] = value

    App.insert_info(l_string=axiom, rules_list=rules_list, rotate=rotate, number_of_iteration=iteration, line_length=line_length, start_point=start_point)
    turtle_interprate(l_string=axiom, rules=rules, rotate=rotate, number_of_iteration=iteration, line_length=line_length, start_point=start_point)
            

def save_content(l_string, rules_list, line_length, rotate, number_of_iteration, start_point):
    filename = filedialog.asksaveasfilename(initialdir="/", title="Save as...", filetypes=files, defaultextension=files)
    data = {"axiom" : l_string, "line_length" : line_length, "rotate" : rotate, "iteration" : number_of_iteration, "rules" : rules_list, "start_point" : start_point}
    data_json = json.dumps(data) 
    with open(filename, "w") as file:
        file.write(data_json)
    
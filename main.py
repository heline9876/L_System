import tkinter as Tk
from App_object import activate_widget


root = Tk.Tk()
root.title("L-System")
root.resizable(False, False)

activate_widget(root)

root.mainloop()
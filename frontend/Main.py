import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ProjectBB")
root.maxsize(1920, 1080)
root.geometry('1200x720')

def add_to_list(event=None):
    text = entry.get()
    if text:
        text_list.insert(tk.END, text)
        entry.delete(0, tk.END)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = ttk.Frame(root)
frame.grid(row = 0, column = 0, sticky="nsew", padx=5, pady=5)

frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

entry = ttk.Entry(frame)
entry.grid(row = 0, column = 0, sticky="ew")

entry.bind("<Return>", add_to_list)

entry_button = ttk.Button(frame, text = 'Add', command=add_to_list)
entry_button.grid(row = 0, column = 1)

text_list = tk.Listbox(frame)
text_list.grid(row = 1, column = 0, columnspan = 2, sticky="nsew")



"""
def on_click():
   label.config(text="Bubber")

label = tk.Label(root, text="Bubbey")
label.grid(row = 0, column = 0)

button1 = tk.Button(root, text="Click me", command = on_click)
button1.grid(row = 0, column = 1)

print(button1.config().keys())
"""

root.mainloop()
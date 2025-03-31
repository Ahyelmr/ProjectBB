import tkinter as tk

root = tk.Tk()
root.title("ProjectBB")
root.maxsize(1920, 1080)
root.geometry('1920x1080')

def add_to_list(event=None):
    text = entry.get()
    if text:
        text_list.insert(tk.END, text)
        entry.delete(0, tk.END)

frame = tk.Frame(root)
frame.grid(row = 0, column = 0)

entry = tk.Entry(frame)
entry.grid(row = 0, column = 0)

entry.bind("<Return>", add_to_list)

entry_button = tk.Button(frame, text = 'Add', command=add_to_list)
entry_button.grid(row = 0, column = 1)

text_list = tk.Listbox(frame)
text_list.grid(row = 1, column = 0)

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
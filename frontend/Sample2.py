import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("400x400")  # Size of the window

# Configure the grid to make it expandable
root.grid_columnconfigure(0, weight=1)  # The only column should expand
root.grid_rowconfigure(0, weight=1)     # The only row should expand

# Create the frame
frame = tk.Frame(root, bg="lightblue")
frame.grid(row=0, column=0, sticky="nsew")  # Expand in all directions

# Add a widget inside the frame (for demonstration)
label = tk.Label(frame, text="Centered Frame")
label.pack(expand=True)

root.mainloop()
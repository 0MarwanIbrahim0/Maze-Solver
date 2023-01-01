import tkinter as tk

from BFS import graph_BFS
from main import maze

# Create the window
window = tk.Tk()

# Set the window size
window.geometry("400x400")

# Create the text widget
text = tk.Text(window)

# Insert the text into the widget
text.insert(tk.END, f"{maze}")

# Pack the text widget
text.pack()

# Run the main loop
window.mainloop()

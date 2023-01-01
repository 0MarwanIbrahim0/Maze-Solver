import tkinter as tk
import Astar
from BFS import solve_maze_BFS, Display
from DFS import solve_maze_DFS, Display
from tkinter.filedialog import askopenfilename

maze = []
path = []
main_maze = []
start = None
finish = None


def clear_data():
    global maze
    global text
    global path
    maze = main_maze
    text.delete(1.0, tk.END)
    path = []


def open_file():
    with open(filepath) as f:
        content = f.readlines()
    return content


def BSF_Solve():
    # Use the BFS algorithm to solve the maze and get the solution
    solution_BFS = solve_maze_BFS(maze, start, finish)
    l_result["text"] = f"{solution_BFS}"
    # Display the solution on the text widget
    text.insert(tk.END, f"{Display(maze, solution_BFS, lines)}\n")


def DSF_Solve():
    solution_DFS = solve_maze_DFS(maze, start, finish)
    # Update the result label
    l_result["text"] = f"{solution_DFS}"
    # Update the maze display
    text.insert(tk.END, f"{Display(maze, solution_DFS, lines)}\n")


def A():
    solution_A = Astar.solve_maze_Astar(maze, start, finish)
    l_result["text"] = f"{solution_A}"
    text.insert(tk.END, f"{Display(maze, solution_A, lines)}\n")


def on_enter(event):
    # Change the button background color when the mouse enters
    event.widget["background"] = "blue"


def on_leave(event):
    # Change the button background color when the mouse leaves
    event.widget["background"] = "black"


filepath = tk.filedialog.askopenfilename(
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

lines = open_file()
for i, line in enumerate(lines):
    row = []
    for j, ch in enumerate(line.strip()):
        if ch == 'A':
            start = (i, j)
        elif ch == 'B':
            finish = (i, j)
        row.append(ch)
    main_maze.append(row)
    maze.append(row)
# GUI Program
print(main_maze)
Main_Window = tk.Tk()
solve_Window = tk.Tk()
Main_Window.title("Maze_Project")
# window.resizable(width=False, height=False)
Main_Window.config(bg="black")

frm_entry = tk.Frame(master=Main_Window, bg="black")
l_file = tk.Label(master=frm_entry, text="Choice Algorithm", bg="black", fg="white")
l_file.grid(row=0, column=0, sticky="e")
ent_file = tk.Entry(master=frm_entry, width=25)
frm_entry.grid(row=0, column=0, padx=10)

l_result = tk.Label(master=solve_Window, text="")
l_result.grid(row=2, column=0, pady=10, padx=10)

g_result = text = tk.Text(solve_Window)
g_result.grid(row=3, column=0, padx=10)

frm_Button = tk.Frame(master=Main_Window, bg="black", background="black")
frm_Button.grid(row=1, column=0, pady=10)
file_Button = tk.Button(master=frm_entry, text="Choice file", command=open_file, highlightbackground="blue")

butt_BFS = tk.Button(master=frm_Button, text="BFS Search", command=BSF_Solve, fg="white", bg="black")
butt_DFS = tk.Button(master=frm_Button, text="DFS Search", command=DSF_Solve, fg="white", bg="black")
butt_A = tk.Button(master=frm_Button, text="A* Search", command=A, fg="white", bg="black")
butt_A.bind("<Enter>", on_enter), butt_BFS.bind("<Enter>", on_enter), butt_DFS.bind("<Enter>", on_enter)
butt_A.bind("<Leave>", on_leave), butt_BFS.bind("<Leave>", on_leave), butt_DFS.bind("<Leave>", on_leave)
butt_BFS.grid(row=1, column=0, pady=10)
butt_DFS.grid(row=1, column=1, pady=10, padx=10)
butt_A.grid(row=1, column=2, pady=10)
clear_button = tk.Button(Main_Window, text="Clear data", command=clear_data)
clear_button.grid(row=2, column=0, padx=10, pady=10)

# Parse the maze
Main_Window.mainloop()

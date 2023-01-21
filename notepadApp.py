import tkinter as tk
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename()
    with open(filepath, 'r') as file:
        text.delete(1.0, tk.END)
        text.insert(tk.INSERT, file.read())

def save_file():
    filepath = filedialog.asksaveasfilename()
    with open(filepath, 'w') as file:
        file.write(text.get(1.0, tk.END))

def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

root = tk.Tk()
root.title("Notepad")

text = tk.Text(root)
text.pack()

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
edit_menu = tk.Menu(menu)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Exit', command=root.destroy)
menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut', command=cut)
edit_menu.add_command(label='Copy', command=copy)
edit_menu.add_command(label='Paste', command=paste)

root.mainloop()

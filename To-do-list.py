import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("325x400")
window.title("To-Do-List")

def add():
    task = entry.get()
    if task.strip():
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please add valid task")
        
    

def delete():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Selection Error", "please select a task to delete")


        
def clear():
    listbox.delete(0, tk.END)
    


#Creating widget for input
entry = tk.Entry(window, font=('Arial',14),width=25,borderwidth=2)
entry.pack(pady=10)

#Creating Buttons
add_btn = tk.Button(window, text= "Add Task", command= add)
add_btn.pack(pady=8)


delete_btn = tk.Button(window, text="Delete Task", command= delete)
delete_btn.pack(pady=5)


clear_btn = tk.Button(window, text= "Clear All", command=clear)
clear_btn.pack(pady=5)

#Creating ListBox
listbox = tk.Listbox(window, width= 50, height= 15, font=('Arial', 14))
listbox.pack(pady=10)


window.mainloop()


import tkinter as tk
from tkinter import messagebox
import random
import string


def generator():
    try:
        length= int(entry.get())
        if length<4:
            messagebox.showinfo("Input error","please enter password length at least 4")
            return
        characters = ""
        if include_uppercase.get():
            characters +=  string.ascii_uppercase
        if include_lowercase.get():
            characters += string.ascii_lowercase
        if include_digit.get():
            characters += string.digits
        if include_symbol.get():
            characters += string.punctuation

        if not characters:
            messagebox.showinfo("Input Error","Please select at least one character type")
            return

        password = ''.join(random.choice(characters) for i in range(length))
        result_label.config(text=f"Password: {password}")
    except ValueError:
        messagebox.showerror("Input Error","Please enter a valid number")
    




#Create main window   
window = tk.Tk()
window.geometry("400x350")
window.title("Password Generator")



#Length label and entry
label = tk.Label(window, text="Password Length:", font=('Arial', 12))
label.pack(pady=3)

entry = tk.Entry(window, font= ('Arial',12), width=10)
entry.pack(pady=8)


#Create Check boxes
include_uppercase = tk.BooleanVar(value= True)
uppercase_check = tk.Checkbutton(window, text= "Include Uppercase Letters", variable= include_uppercase, font=('Arial',12))
uppercase_check.pack(pady=8, anchor='w')

include_lowercase = tk.BooleanVar(value=True)
lowercase_check = tk.Checkbutton(window, text="Include Lowercase Letters", variable= include_lowercase, font=('Arial',12))
lowercase_check.pack(pady=5,anchor='w')

include_digit = tk.BooleanVar(value=True)
digit_check = tk.Checkbutton(window, text= "Include Digits", variable= include_digit, font=('Arial',12))
digit_check.pack(pady=8, anchor='w')

include_symbol = tk.BooleanVar(value=True)
symbol_check = tk.Checkbutton(window, text= "Include Symbols", variable= include_symbol, font=('Arial',12))
symbol_check.pack(pady=8, anchor='w')


    

generate_btn = tk.Button(window, text="Generate", bg= "lightblue", width=12,font=('Arial',12), command= generator)
generate_btn.pack(pady=8)

result_label = tk.Label(window, text="Generated Password", font=('Arial',14))
result_label.pack(pady=10)


window.mainloop()

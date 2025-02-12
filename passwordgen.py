import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_var.get()
    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()

    if not (include_upper or include_lower or include_digits or include_special):
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    characters = ""
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Set up the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")  # Adjusting window size

# Variables
length_var = tk.IntVar(value=12)
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

# Layout
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
length_entry = tk.Entry(root, textvariable=length_var, width=5)
length_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Include Numbers", variable=digits_var).grid(row=3, column=0, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).grid(row=4, column=0, padx=10, pady=5, sticky="w")

tk.Button(root, text="Generate Password", command=generate_password).grid(row=5, column=0, columnspan=2, pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.grid(row=6, column=0, padx=10, pady=10, sticky="w")

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=6, column=1, padx=10, pady=10, sticky="e")

# Run the application
root.mainloop()

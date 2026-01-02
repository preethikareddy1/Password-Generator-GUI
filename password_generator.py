import random
import string
import tkinter as tk
from tkinter import messagebox

# --- Functions ---
def generate_password():
    try:
        length = int(entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4")
            return

        characters = string.ascii_letters
        if include_numbers.get():
            characters += string.digits
        if include_symbols.get():
            characters += string.punctuation

        password = "".join(random.choice(characters) for _ in range(length))
        result_label.config(text=password)
        strength_label.config(text="Strength: " + check_strength(password))

        # Save to file
        with open("passwords.txt", "a") as file:
            file.write(password + "\n")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def copy_to_clipboard():
    password = result_label.cget("text")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy")

def check_strength(pwd):
    length = len(pwd)
    has_lower = any(c.islower() for c in pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_symbol = any(c in string.punctuation for c in pwd)
    score = sum([has_lower, has_upper, has_digit, has_symbol])
    
    if length >= 12 and score == 4:
        return "Strong 🔒"
    elif length >= 8 and score >= 3:
        return "Medium ⚠️"
    else:
        return "Weak ❌"

def toggle_dark_mode():
    if root.cget("bg") == "#f0f0f0":
        root.config(bg="#2e2e2e")
        for widget in root.winfo_children():
            widget.config(bg="#2e2e2e", fg="white")
    else:
        root.config(bg="#f0f0f0")
        for widget in root.winfo_children():
            widget.config(bg="#f0f0f0", fg="black")

# --- Main Window ---
root = tk.Tk()
root.title("Password Generator")
root.geometry("480x350")
root.config(bg="#f0f0f0")  # Light gray background

# --- Widgets ---
title_label = tk.Label(root, text="💻 Strong Password Generator 💻", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#2a2a2a")
title_label.pack(pady=10)

tk.Label(root, text="Enter Password Length:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=5)

# Checkbuttons for options
include_numbers = tk.IntVar(value=1)
include_symbols = tk.IntVar(value=1)

tk.Checkbutton(root, text="Include Numbers", variable=include_numbers, bg="#f0f0f0").pack()
tk.Checkbutton(root, text="Include Symbols", variable=include_symbols, bg="#f0f0f0").pack()

# Buttons
generate_btn = tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"), bg="#4caf50", fg="white", command=generate_password)
generate_btn.pack(pady=10, ipadx=10, ipady=5)

copy_btn = tk.Button(root, text="Copy to Clipboard", font=("Arial", 12, "bold"), bg="#2196f3", fg="white", command=copy_to_clipboard)
copy_btn.pack(pady=5, ipadx=10, ipady=5)

dark_btn = tk.Button(root, text="Toggle Dark Mode", font=("Arial", 12, "bold"), bg="#607d8b", fg="white", command=toggle_dark_mode)
dark_btn.pack(pady=5, ipadx=10, ipady=5)

# Labels to display password and strength
result_label = tk.Label(root, text="", font=("Courier", 14, "bold"), bg="#f0f0f0", fg="#d32f2f")
result_label.pack(pady=10)

strength_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#ff6f00")
strength_label.pack(pady=5)

root.mainloop()

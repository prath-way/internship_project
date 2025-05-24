import tkinter as tk
from tkinter import ttk, messagebox
import string
import random

def generate_password():
    length = int(length_slider.get())

    charset = ""
    if var_upper.get():
        charset += string.ascii_uppercase
    if var_lower.get():
        charset += string.ascii_lowercase
    if var_digits.get():
        charset += string.digits
    if var_symbols.get():
        charset += string.punctuation

    if not charset:
        messagebox.showwarning("Warning", "Please select at least one character type.")
        return

    password = ''.join(random.choice(charset) for _ in range(length))
    password_entry.config(show="" if show_password.get() else "*")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

def toggle_show():
    password_entry.config(show="" if show_password.get() else "*")

root = tk.Tk()
root.title("Interactive Password Generator")
root.geometry("400x400")
root.resizable(False, False)

frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

# Length
ttk.Label(frame, text="Password Length:").pack(anchor="w")
length_slider = ttk.Scale(frame, from_=4, to=32, orient="horizontal")
length_slider.set(12)
length_slider.pack(fill="x", pady=5)

# Options
ttk.Label(frame, text="Include:").pack(anchor="w", pady=(10, 0))
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

ttk.Checkbutton(frame, text="Uppercase Letters", variable=var_upper).pack(anchor="w")
ttk.Checkbutton(frame, text="Lowercase Letters", variable=var_lower).pack(anchor="w")
ttk.Checkbutton(frame, text="Numbers", variable=var_digits).pack(anchor="w")
ttk.Checkbutton(frame, text="Symbols", variable=var_symbols).pack(anchor="w")


show_password = tk.BooleanVar(value=False)
ttk.Checkbutton(frame, text="Show Password", variable=show_password, command=toggle_show).pack(anchor="w", pady=5)


password_entry = ttk.Entry(frame, font=("Arial", 12), show="*", justify="center")
password_entry.pack(pady=10, fill="x")


ttk.Button(frame, text="Generate Password", command=generate_password).pack(pady=5)
ttk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard).pack()

root.mainloop()

# TASK 3 - PASSWORD GENERATOR (GUI VERSION)
# Generates a random password based on the length and
# character types chosen by the user, using Tkinter checkboxes.
# Colors added to make the GUI look nicer.

import tkinter as tk
from tkinter import messagebox
import random
import string

# ---- Simple color palette (easy to change) ----
BG_COLOR = "#fdf6e3"       # light cream background
TITLE_COLOR = "#6c3483"    # purple text
BUTTON_COLOR = "#8e44ad"   # purple button
TEXT_ON_BUTTON = "white"
RESULT_BG = "#d5f5e3"      # light green result box


def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")
        return

    characters = ""
    if letters_var.get():
        characters += string.ascii_letters
    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showinfo("Info", "No type selected. Using letters by default.")
        characters = string.ascii_letters

    password = ""
    for i in range(length):
        password += random.choice(characters)

    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)


window = tk.Tk()
window.title("Password Generator")
window.geometry("350x340")
window.configure(bg=BG_COLOR)

title_label = tk.Label(
    window, text="Password Generator", font=("Arial", 16, "bold"),
    bg=BG_COLOR, fg=TITLE_COLOR
)
title_label.pack(pady=10)

tk.Label(window, text="Password length:", bg=BG_COLOR, font=("Arial", 10)).pack()
length_entry = tk.Entry(window, width=10, font=("Arial", 11))
length_entry.pack(pady=5)

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)

tk.Checkbutton(window, text="Include letters", variable=letters_var, bg=BG_COLOR, font=("Arial", 10)).pack()
tk.Checkbutton(window, text="Include numbers", variable=numbers_var, bg=BG_COLOR, font=("Arial", 10)).pack()
tk.Checkbutton(window, text="Include symbols", variable=symbols_var, bg=BG_COLOR, font=("Arial", 10)).pack()

tk.Button(
    window, text="Generate Password", command=generate_password,
    bg=BUTTON_COLOR, fg=TEXT_ON_BUTTON, font=("Arial", 10, "bold")
).pack(pady=10)

result_entry = tk.Entry(
    window, width=30, justify="center", font=("Arial", 11),
    bg=RESULT_BG
)
result_entry.pack(pady=10)

window.mainloop()

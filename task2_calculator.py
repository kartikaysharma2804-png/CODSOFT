# TASK 2 - SIMPLE CALCULATOR (GUI VERSION) - IMPROVED
# Takes two numbers and an operation from the user
# and displays the result using Tkinter buttons.
# This version has a bigger, more colorful, nicer-looking layout.

import tkinter as tk
from tkinter import messagebox

# ---- Simple color palette (easy to change) ----
BG_COLOR = "#2c3e50"        # dark blue-grey background
CARD_COLOR = "#34495e"      # slightly lighter panel color
TITLE_COLOR = "white"
ENTRY_BG = "#ecf0f1"
OPERATOR_COLOR = "#f39c12"  # orange for operator buttons
CLEAR_COLOR = "#e74c3c"     # red for clear button
RESULT_BG = "#1abc9c"       # teal for result box
TEXT_ON_BUTTON = "white"


def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")
        return

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero.")
            return
        result = num1 / num2

    result_label.config(text="Result: " + str(result))


def clear_all():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")


window = tk.Tk()
window.title("Simple Calculator")
window.geometry("320x420")
window.configure(bg=BG_COLOR)

# ---- Title ----
title_label = tk.Label(
    window, text="Simple Calculator", font=("Arial", 18, "bold"),
    bg=BG_COLOR, fg=TITLE_COLOR
)
title_label.pack(pady=15)

# ---- Card panel that holds the inputs ----
card = tk.Frame(window, bg=CARD_COLOR, padx=20, pady=20)
card.pack(pady=5, padx=15, fill="x")

tk.Label(card, text="First number:", bg=CARD_COLOR, fg="white", font=("Arial", 10)).pack(anchor="w")
entry1 = tk.Entry(card, width=20, font=("Arial", 12), bg=ENTRY_BG, justify="center")
entry1.pack(pady=(0, 10), fill="x")

tk.Label(card, text="Second number:", bg=CARD_COLOR, fg="white", font=("Arial", 10)).pack(anchor="w")
entry2 = tk.Entry(card, width=20, font=("Arial", 12), bg=ENTRY_BG, justify="center")
entry2.pack(pady=(0, 5), fill="x")

# ---- Operator buttons ----
button_frame = tk.Frame(window, bg=BG_COLOR)
button_frame.pack(pady=15)

tk.Button(
    button_frame, text="+", width=6, height=2, font=("Arial", 12, "bold"),
    bg=OPERATOR_COLOR, fg=TEXT_ON_BUTTON, command=lambda: calculate("+")
).grid(row=0, column=0, padx=5, pady=5)

tk.Button(
    button_frame, text="-", width=6, height=2, font=("Arial", 12, "bold"),
    bg=OPERATOR_COLOR, fg=TEXT_ON_BUTTON, command=lambda: calculate("-")
).grid(row=0, column=1, padx=5, pady=5)

tk.Button(
    button_frame, text="*", width=6, height=2, font=("Arial", 12, "bold"),
    bg=OPERATOR_COLOR, fg=TEXT_ON_BUTTON, command=lambda: calculate("*")
).grid(row=1, column=0, padx=5, pady=5)

tk.Button(
    button_frame, text="/", width=6, height=2, font=("Arial", 12, "bold"),
    bg=OPERATOR_COLOR, fg=TEXT_ON_BUTTON, command=lambda: calculate("/")
).grid(row=1, column=1, padx=5, pady=5)

# ---- Clear button ----
clear_button = tk.Button(
    window, text="Clear", width=12, font=("Arial", 10, "bold"),
    bg=CLEAR_COLOR, fg=TEXT_ON_BUTTON, command=clear_all
)
clear_button.pack(pady=5)

# ---- Result display ----
result_label = tk.Label(
    window, text="Result: ", font=("Arial", 13, "bold"),
    bg=RESULT_BG, fg="white", width=25, pady=10
)
result_label.pack(pady=15)

window.mainloop()

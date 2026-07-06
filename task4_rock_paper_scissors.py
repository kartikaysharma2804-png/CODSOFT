# TASK 4 - ROCK, PAPER, SCISSORS GAME (GUI VERSION)
# The user plays against the computer by clicking buttons.
# Score is tracked across rounds.
# Colors added to make the GUI look nicer.

import tkinter as tk
import random

options = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

# ---- Simple color palette (easy to change) ----
BG_COLOR = "#fef9e7"        # light yellow background
TITLE_COLOR = "#b9770e"     # brown-orange text
ROCK_COLOR = "#7f8c8d"      # grey
PAPER_COLOR = "#5dade2"     # blue
SCISSORS_COLOR = "#ec7063"  # red
TEXT_ON_BUTTON = "white"
SCORE_COLOR = "#1e8449"     # green


def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result_text = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result_text = "You win this round!"
        user_score += 1
    else:
        result_text = "Computer wins this round!"
        computer_score += 1

    choice_label.config(text="You chose: " + user_choice + "   |   Computer chose: " + computer_choice)
    result_label.config(text=result_text)
    score_label.config(text="Score -> You: " + str(user_score) + "   Computer: " + str(computer_score))


window = tk.Tk()
window.title("Rock, Paper, Scissors")
window.geometry("420x320")
window.configure(bg=BG_COLOR)

title_label = tk.Label(
    window, text="Rock, Paper, Scissors", font=("Arial", 16, "bold"),
    bg=BG_COLOR, fg=TITLE_COLOR
)
title_label.pack(pady=10)

button_frame = tk.Frame(window, bg=BG_COLOR)
button_frame.pack(pady=10)

tk.Button(
    button_frame, text="Rock", width=10, font=("Arial", 10, "bold"),
    bg=ROCK_COLOR, fg=TEXT_ON_BUTTON, command=lambda: play("rock")
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame, text="Paper", width=10, font=("Arial", 10, "bold"),
    bg=PAPER_COLOR, fg=TEXT_ON_BUTTON, command=lambda: play("paper")
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame, text="Scissors", width=10, font=("Arial", 10, "bold"),
    bg=SCISSORS_COLOR, fg=TEXT_ON_BUTTON, command=lambda: play("scissors")
).grid(row=0, column=2, padx=5)

choice_label = tk.Label(window, text="", font=("Arial", 11), bg=BG_COLOR)
choice_label.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12, "bold"), bg=BG_COLOR, fg=TITLE_COLOR)
result_label.pack(pady=5)

score_label = tk.Label(
    window, text="Score -> You: 0   Computer: 0", font=("Arial", 11, "bold"),
    bg=BG_COLOR, fg=SCORE_COLOR
)
score_label.pack(pady=10)

window.mainloop()

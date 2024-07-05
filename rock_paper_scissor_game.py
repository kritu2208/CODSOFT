import tkinter as tk
from tkinter import messagebox
import random

# Function to decide the game outcome
def decide_winner(player_choice, ai_choice):
    if player_choice == ai_choice:
        return "It's a draw!"
    elif (player_choice == "Rock" and ai_choice == "Scissors") or \
         (player_choice == "Scissors" and ai_choice == "Paper") or \
         (player_choice == "Paper" and ai_choice == "Rock"):
        return "You win!"
    else:
        return "AI wins!"

# Function to update the scores
def modify_score(outcome):
    global player_score, ai_score
    if outcome == "You win!":
        player_score += 1
    elif outcome == "AI wins!":
        ai_score += 1
    player_score_label.config(text=f"Your Points: {player_score}")
    ai_score_label.config(text=f"AI Points: {ai_score}")

# Function to handle player's selection
def player_selection(selection):
    ai_selection = random.choice(["Rock", "Paper", "Scissors"])
    outcome = decide_winner(selection, ai_selection)
    outcome_label.config(text=f"AI selected: {ai_selection}\n{outcome}")
    modify_score(outcome)

# Initialize the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

# Initialize scores
player_score = 0
ai_score = 0

# Create and place labels and buttons
tk.Label(window, text="Pick Rock, Paper, or Scissors:").pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack()

tk.Button(button_frame, text="Rock", command=lambda: player_selection("Rock")).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Paper", command=lambda: player_selection("Paper")).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Scissors", command=lambda: player_selection("Scissors")).grid(row=0, column=2, padx=10)

outcome_label = tk.Label(window, text="", font=('Helvetica', 12))
outcome_label.pack(pady=20)

player_score_label = tk.Label(window, text=f"Your Points: {player_score}")
player_score_label.pack(side=tk.LEFT, padx=20)

ai_score_label = tk.Label(window, text=f"AI Points: {ai_score}")
ai_score_label.pack(side=tk.RIGHT, padx=20)

# Run the main loop
window.mainloop()


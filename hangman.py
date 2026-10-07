import tkinter as tk
from tkinter import messagebox
import random

# Words for the game
words = ["apple", "tiger", "python", "mango", "chair"]

# Hints for each word
hints = {
    "apple": "A fruit that keeps the doctor away.",
    "tiger": "A large wild cat with stripes.",
    "python": "A programming language and a type of snake.",
    "mango": "A sweet tropical fruit.",
    "chair": "You sit on this."
}


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("500x550")
        self.root.resizable(False, False)

        self.word = ""
        self.guessed_letters = []
        self.attempts = 6
        self.hints_left = 3

        self.create_ui()
        self.new_game()

    def create_ui(self):

        # Title
        title = tk.Label(
            self.root,
            text="🎮 Hangman Game",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=20)

        # Word display
        self.word_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 28, "bold")
        )
        self.word_label.pack(pady=20)

        # Attempts
        self.attempts_label = tk.Label(
            self.root,
            text="Attempts: 6",
            font=("Arial", 14)
        )
        self.attempts_label.pack(pady=10)

        # Guess section
        guess_frame = tk.Frame(self.root)
        guess_frame.pack(pady=15)

        self.guess_entry = tk.Entry(
            guess_frame,
            font=("Arial", 18),
            width=5,
            justify="center"
        )
        self.guess_entry.pack(side="left", padx=10)

        guess_button = tk.Button(
            guess_frame,
            text="Guess",
            font=("Arial", 14, "bold"),
            command=self.check_guess
        )
        guess_button.pack(side="left")

        # Hint button
        hint_button = tk.Button(
            self.root,
            text="💡 Get Hint",
            font=("Arial", 13, "bold"),
            command=self.show_hint
        )
        hint_button.pack(pady=5)

        # Hint counter
        self.hint_label = tk.Label(
            self.root,
            text="Hints left: 3",
            font=("Arial", 12)
        )
        self.hint_label.pack(pady=5)

        # Message
        self.message_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 13),
            wraplength=400
        )
        self.message_label.pack(pady=15)

        # Guessed letters
        self.guessed_label = tk.Label(
            self.root,
            text="Guessed letters: ",
            font=("Arial", 12)
        )
        self.guessed_label.pack(pady=10)

        # New game button
        new_game_button = tk.Button(
            self.root,
            text="🔄 New Game",
            font=("Arial", 14, "bold"),
            command=self.new_game
        )
        new_game_button.pack(pady=20)

    def new_game(self):
        self.word = random.choice(words)
        self.guessed_letters = []
        self.attempts = 6
        self.hints_left = 3

        self.message_label.config(
            text="Guess a letter!"
        )

        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

        self.update_display()

    def update_display(self):

        display = " ".join(
            letter if letter in self.guessed_letters else "_"
            for letter in self.word
        )

        self.word_label.config(
            text=display
        )

        self.attempts_label.config(
            text=f"Attempts: {self.attempts}"
        )

        self.guessed_label.config(
            text=f"Guessed letters: {', '.join(self.guessed_letters)}"
        )

        self.hint_label.config(
            text=f"Hints left: {self.hints_left}"
        )

    def check_guess(self):

        guess = self.guess_entry.get().lower().strip()

        self.guess_entry.delete(0, tk.END)

        # Check input
        if len(guess) != 1 or not guess.isalpha():
            self.message_label.config(
                text="Please enter one letter."
            )
            return

        # Check repeated letter
        if guess in self.guessed_letters:
            self.message_label.config(
                text="You already guessed that letter!"
            )
            return

        self.guessed_letters.append(guess)

        # Correct guess
        if guess in self.word:

            self.message_label.config(
                text="Correct guess! 👍"
            )

        # Wrong guess
        else:

            self.attempts -= 1

            self.message_label.config(
                text="Wrong guess! ❌"
            )

        self.update_display()

        # Check win
        if all(
            letter in self.guessed_letters
            for letter in self.word
        ):

            messagebox.showinfo(
                "You Win!",
                f"Congratulations! 🎉\n\n"
                f"The word was '{self.word}'."
            )

            self.new_game()

        # Check lose
        elif self.attempts == 0:

            messagebox.showinfo(
                "Game Over",
                f"You lost! 😢\n\n"
                f"The word was '{self.word}'."
            )

            self.new_game()

    def show_hint(self):

        # Check if hints are available
        if self.hints_left == 0:

            self.message_label.config(
                text="No hints left! ❌"
            )

            return

        # Show hint
        self.message_label.config(
            text=f"💡 Hint: {hints[self.word]}"
        )

        # Reduce hint count
        self.hints_left -= 1

        self.update_display()


# Start the program
root = tk.Tk()

game = HangmanGame(root)

root.mainloop()

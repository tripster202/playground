import tkinter as tk
from tkinter import messagebox
import random

class OperationGumball:
    def __init__(self, root):
        self.root = root
        self.root.title("Operation Gumball")
        
        self.code_length = 4
        self.max_attempts = 10
        self.attempts = 0
        self.secret_code = ''
        
        # Game Interface
        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        # Instructions
        self.instructions = tk.Label(self.root, 
            text="Guess the 4-digit code!\nGreen: Correct number & position\nRed: Correct number, wrong position",
            wraplength=300)
        self.instructions.pack(pady=10)

        # Attempts counter
        self.attempts_label = tk.Label(self.root, text=f"Attempts left: {self.max_attempts}")
        self.attempts_label.pack()

        # Guess entry
        self.entry = tk.Entry(self.root, validate='key', width=20)
        self.entry['validatecommand'] = (self.entry.register(self.validate_input), '%P')
        self.entry.pack(pady=5)

        # Submit button
        self.submit_btn = tk.Button(self.root, text="Submit Guess", command=self.check_guess)
        self.submit_btn.pack(pady=5)

        # Feedback display
        self.feedback_frame = tk.Frame(self.root)
        self.feedback_frame.pack(pady=10)

        # Reset button
        self.reset_btn = tk.Button(self.root, text="New Game", command=self.reset_game)
        self.reset_btn.pack(pady=5)

    def validate_input(self, text):
        return text.isdigit() and len(text) <= self.code_length or text == ''

    def check_guess(self):
        guess = self.entry.get()
        if len(guess) != self.code_length:
            messagebox.showerror("Error", f"Please enter {self.code_length} digits")
            return

        self.attempts += 1
        green, red = self.calculate_feedback(guess)
        
        # Display feedback
        self.show_gumballs(green, red)
        
        # Update attempts
        remaining = self.max_attempts - self.attempts
        self.attempts_label.config(text=f"Attempts left: {remaining}")
        
        if green == self.code_length:
            messagebox.showinfo("Success!", "You cracked the code!")
            self.reset_game()
        elif self.attempts >= self.max_attempts:
            messagebox.showinfo("Game Over", f"Code was: {self.secret_code}")
            self.reset_game()

    def calculate_feedback(self, guess):
        green = sum(g == s for g, s in zip(guess, self.secret_code))
        matched = sum(min(guess.count(d), self.secret_code.count(d)) for d in set(guess))
        return green, matched - green

    def show_gumballs(self, green, red):
        # Clear previous feedback
        for widget in self.feedback_frame.winfo_children():
            widget.destroy()
            
        # Create colored gumballs
        for _ in range(green):
            tk.Label(self.feedback_frame, text="●", fg="green").pack(side=tk.LEFT, padx=2)
        for _ in range(red):
            tk.Label(self.feedback_frame, text="●", fg="red").pack(side=tk.LEFT, padx=2)

    def reset_game(self):
        self.secret_code = ''.join(random.sample('0123456789', self.code_length))
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.attempts_label.config(text=f"Attempts left: {self.max_attempts}")
        for widget in self.feedback_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = OperationGumball(root)
    root.mainloop()
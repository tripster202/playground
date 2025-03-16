import math
import random
from itertools import product
from collections import Counter
from typing import List

def grr_machine(guess: str, correct: str) -> str:
    """Generate GRR code based on the guess and correct answer."""
    exact = sum(1 for g, c in zip(guess, correct) if g == c)
    guess_counts = Counter(g for g, c in zip(guess, correct) if g != c)
    correct_counts = Counter(c for g, c in zip(guess, correct) if g != c)
    approx = sum(min(guess_counts[d], correct_counts[d]) for d in guess_counts)
    return 'g' * exact + 'r' * approx if (exact + approx) else 'x'

def filter_valid_guesses(valid: List[str], guess: str, grr_code: str) -> List[str]:
    """Filter the pool of valid guesses based on the GRR code."""
    return [v for v in valid if grr_machine(v, guess) == grr_code]

def recommend_guess(valid: List[str]) -> str:
    """Recommend the best guess from the pool of valid guesses."""
    scores = {}
    for guess in valid:
        candy_box = Counter(grr_machine(v, guess) for v in valid if v != guess)
        scores[guess] = max(candy_box.values(), default=0)
    return min(scores, key=scores.get)

def gumball_game():
    """Main function to play the Gumball game."""
    print("🎮 Welcome to the Gumball Game!")
    num_balls = int(input("Enter the number of gumballs for this level: "))
    valid = [''.join(p) for p in product('0123456789', repeat=num_balls)]

    while True:
        guess = input(f"Enter your guess ({num_balls} digits): ")
        if not guess.isdigit() or len(guess) != num_balls:
            print(f"Invalid input! Please enter a {num_balls}-digit number.")
            continue

        grr_code = input("Enter the GRR code for your guess: ").lower()
        if grr_code == 'g' * num_balls:
            print(f"🎉 Congratulations! {guess} is the correct answer!")
            break

        valid = filter_valid_guesses(valid, guess, grr_code)
        if not valid:
            print("❌ No valid guesses left! Something went wrong.")
            break

        print(f"Remaining possibilities: {len(valid)}")
        if len(valid) > 1000:
            print("Too many possibilities! Try a random guess.")
            print(f"Random Guess: {random.choice(valid)}")
        else:
            recommendation = recommend_guess(valid)
            print(f"I recommend: {recommendation}")

if __name__ == "__main__":
    gumball_game()
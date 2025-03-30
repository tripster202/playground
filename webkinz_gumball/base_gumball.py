# Import necessary modules
import math
import random
from itertools import product

def base_gumball():
    # Get the number of gumballs for the current level
    num_balls = int(input('Enter the number of gumballs for this level: '))
    # Calculate if the guess is large enough to warrant a recommendation
    small_guess_flag = max(0, num_balls - 3)

    # valid = list()  # Initialize list to store all possible valid guesses

    # # Generate all possible guesses and add them to the valid list
    # for ex in range(int(math.pow(10, num_balls))):
    #     valid.append((('0' * num_balls) + str(ex))[-num_balls:])

    # Generate all possible guesses using itertools.product
    valid = [''.join(p) for p in product('0123456789', repeat=num_balls)]

    grr_code = str()
    guess = valid[0]

    # Main game loop
    while True:
        # Get user's guess
        user_guess = input('Enter your guess: ')

        # Validate user's input
        if not user_guess.isdigit() or not len(user_guess) == num_balls:
            print(f'Guess must be a number of length {num_balls}!\n')
            continue

        # Get the GRR code for the guess
        grr_code = input('Enter the GRR code for the guess: ')

        # Check if the solution is found
        if grr_code.casefold() == ('g' * num_balls):
            break  # Solution found, exit loop

        # If solution is not yet found, filter remaining valid guesses
        else:
            # Re-establish the list of remaining valid guesses
            new_valid = list()

            # The correct answer and the user guess have the same answer when compared to each other
            # For a remaining guess to be valid, it must return the same GRR code when compared to the user guess
            for remaining in valid:
                if grr_machine(remaining, user_guess) == grr_code:
                    new_valid.append(remaining)

            # Update the valid pool of guesses with those that have the same GRR code as the user guess
            valid = new_valid
            print('Pool: ' + str(len(valid)))

            # Check if the pool is empty
            if len(valid) == 0:
                print('EMPTY POOL')
                return

            # Recommendations for large pools
            if small_guess_flag > 0 and len(valid) > 1000:
                print('No Recommendation')
                print('Random Guess: ' + valid[random.randint(0, len(valid) - 1)])
                small_guess_flag -= 1
                continue

            scores = dict()

            # Calculate scores for each valid guess to determine the best next guess
            for guess in valid:
                idx = 0; high = 0
                candy_box = dict() # all possible GRR codes and their frequencies
                while idx < len(valid):
                    if guess == valid[idx]:
                        idx += 1
                        continue
                    taste = grr_machine(valid[idx], guess)
                    if taste in candy_box:
                        candy_box[taste] += 1
                    else:
                        candy_box[taste] = 1
                    idx += 1
                for value in candy_box.values():
                    if value > high:
                        high = value
                scores[guess] = high

            # Find the guess with the lowest score (best guess)
            low = -1
            best_guesses = []  # List to store guesses with the lowest score
            for guess in scores:
                if low < 0 or scores[guess] < low:
                    low = scores[guess]
                    best_guesses = [guess]  # Reset the list with the new lowest score guess
                elif scores[guess] == low:
                    best_guesses.append(guess)  # Add to the list if the score is equal to the lowest

            # Randomly choose one of the guesses with the lowest score
            result = random.choice(best_guesses)

        # Print the recommended guess
        print('I Recommend: ' + result)

    # Print the correct answer
    print(guess + ' Was The Correct Answer!')

# The GRR machine compares the guess against the control
# The output is the respectve GRR code
def grr_machine(guess, control):
    g = list(guess)
    c = list(control)

    # Check for numbers in the correct position --> G
    exact = sum(1 for gg, cc in zip(g, c) if gg == cc)
    # If g = ['0', '1', '8'] and c = ['0', '1', '4']:
    # zip(g, c) → [('0', '0'), ('1', '1'), ('8', '4')]
    # Matches: '0' == '0' (True), '1' == '1' (True), '8' == '4' (False)
    # sum(1 for ...) → 1 + 1 = 2
    # Result: exact = 2

    # Check for numbers that are in the wrong position --> R
    # produces a list of numbers from g that exist but are not in the same position as c
    temp_g = [gg for gg, cc in zip(g, c) if gg != cc]
    # produces a list of numbers from c that exist but are not in the same position as g
    temp_c = [cc for gg, cc in zip(g, c) if gg != cc]
    # Count the number of gumballs that are in the wrong position
    approx = sum(min(temp_g.count(d), temp_c.count(d)) for d in set(temp_g))

    return 'g' * exact + 'r' * approx if (exact + approx) else 'x'

if __name__ == '__main__':
    base_gumball()
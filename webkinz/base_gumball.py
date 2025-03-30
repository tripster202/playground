# Import necessary modules
import math
import random
from itertools import product

def gumball_optimized():
    # Get the number of gumballs for the current level
    num_balls = int(input('Enter the number of gumballs for this level: '))
    # Calculate if the guess is large enough to warrant a recommendation
    small_guess_flag = max(0, num_balls - 3)

    # valid = list()  # Initialize list to store all possible valid guesses

    # # Generate all possible guesses and add them to the valid list
    # for ex in range(int(math.pow(10, num_balls))):
    #     valid.append((('0' * num_balls) + str(ex))[-num_balls:])

    valid = [''.join(p) for p in product('0123456789', repeat=num_balls)]

    sweet = str()
    guess = valid[0]

    # Main game loop
    while True:
        # Get user's guess
        guess = input('Enter your guess: ')

        # Validate user's input
        if not guess.isdigit() or not len(guess) == num_balls:
            print(f'Guess must be a number of length {num_balls}!\n')
            continue

        # Get the GRR code for the guess
        sweet = input('Enter the GRR code for the guess: ')

        # Check if the solution is found
        if sweet.casefold() == ('g' * num_balls):
            break  # Solution found, exit loop

        # If solution is not found, filter valid guesses
        else:
            new_valid = list()
            # Compare each valid option against the original guess
            for compare in valid:
                if grr_machine(compare, guess) == sweet:
                    new_valid.append(compare)

            valid = new_valid
            scores = dict()
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

            # Calculate scores for each valid guess
            for guess in valid:
                idx = 0; high = 0
                candy_box = dict()
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
            result = 0
            for guess in scores:
                if low < 0:
                    low = scores[guess]
                    result = guess
                elif scores[guess] < low:
                    low = scores[guess]
                    result = guess

        # Print the recommended guess
        print('I Recommend: ' + result)

    # Print the correct answer
    print(guess + ' Was The Correct Answer!')

def grr_machine(guess, correct):
    g = list(guess)
    c = list(correct)

    # First pass for 'g's
    exact = sum(1 for gg, cc in zip(g, c) if gg == cc)

    # Second pass for 'r's
    temp_g = [gg for gg, cc in zip(g, c) if gg != cc]
    temp_c = [cc for gg, cc in zip(g, c) if gg != cc]
    approx = sum(min(temp_g.count(d), temp_c.count(d)) for d in set(temp_g))

    return 'g' * exact + 'r' * approx if (exact + approx) else 'x'
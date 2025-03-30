# The game starts by placing a 3-digit guess (123).
# The game then outputs unordered green and red gumballs based on the number of correct digits and their position (GRR).
# I call the unordered green and red gumballs the 'GRR code'.
# The user wins the game when all gumballs return green (GGG), indicating that the users has guessed all the correct digits in the correct position.

# This program works by iterating over all remaining guesses to compare each guess against the user guess for a matching GRR code.
# GRR codes have a commutative property, meaning the program can compare the GRR codes of all other guesses against the user guess and the single correct guess will have the same GRR code as the user guess each time.
# Incorrect guesses will have different GRR codes and will be filtered out of the pool of remaining guesses.

# The program then recommends a best next guess by determining which of the remaining guesses has the lowest maximum score.
# The score is the maximum number of GRR code matches to other remaining guesses.
# If a certain guess shares the same GRR code with a large number of other guesses, little information is gained from that guess.
# The best guess is the one that minimizes the maximum number of remaining guesses, meaning it shares its GRR code with the fewest number of other guesses.

# Import necessary modules
import math
import random
from itertools import product

def base_gumball():
    num_balls = int(input('Enter the number of gumballs for this level: '))
    
    # generate all possible guesses using itertools.product
    valid = [''.join(p) for p in product('0123456789', repeat=num_balls)]

    # main loop
    while True:
        # collect and validate user input
        user_guess = input('Enter your guess: ')
        if not user_guess.isdigit() or not len(user_guess) == num_balls:
            print(f'Guess must be a number of length {num_balls}!\n')
            continue

        # collect the GRR code for the guess
        grr_code = input('Enter the GRR code for the guess: ')

        # check if the solution is found (GGG)
        if grr_code.casefold() == ('g' * num_balls):
            break # solution found, exit loop

        # the solution is not yet found
        else:
            
            # filter the remaining valid guesses
            filter_valid = list()

            # the correct answer and the user guess have the same GRR code when compared to each other
            # for a remaining guess to be valid, it must return the same GRR code when compared to the user guess
            for remaining in valid:
                if grr_machine(remaining, user_guess) == grr_code:
                    filter_valid.append(remaining)

            # update the pool of remaining valid guesses with the guesses that have the same GRR code as the user guess
            valid = filter_valid
            print('Pool: ' + str(len(valid)))

            # Check if the pool is empty
            if len(valid) == 0:
                print('EMPTY POOL')
                return # BAD

            # avoid recommendations for overly large pools to save compute time
            if len(valid) > 1000:
                print('No Recommendation')
                print('Random Guess: ' + valid[random.randint(0, len(valid) - 1)])
                continue

            # BEST SCORE #
            scores = dict()
            # similar to golf, the lowest score wins

            # calculate scores for each remaining valid guess
            # the best guess is the guess that minimizes the maximum number of remaining valid guesses
            for guess in valid:
                idx = 0; maximum = 0
                # all possible GRR codes and their frequencies
                grr_frequencies = dict()
                while idx < len(valid):
                    if guess == valid[idx]:
                        idx += 1
                        continue
                    grr_code = grr_machine(valid[idx], guess)
                    if grr_code in grr_frequencies:
                        grr_frequencies[grr_code] += 1
                    else:
                        grr_frequencies[grr_code] = 1
                    idx += 1
                for value in grr_frequencies.values():
                    if value > maximum:
                        maximum = value
                scores[guess] = maximum

            # find the guess with the lowest score (best guess)
            low = -1
            best_guesses = [] # list to store guesses with the lowest score
            for guess in scores:
                if low < 0 or scores[guess] < low:
                    low = scores[guess]
                    best_guesses = [guess] # reset the list with the new lowest score guess
                elif scores[guess] == low:
                    best_guesses.append(guess) # add to the list if the score is equal to the lowest

            # randomly choose one of the guesses with the lowest score
            result = random.choice(best_guesses)
        print('I Recommend: ' + result)

    # If the correct answer is found, print the result
    print(guess + ' Was The Correct Answer!')

# The GRR machine compares the guess against the control
# The output is the respectve GRR code
def grr_machine(guess, control):
    g = list(guess)
    c = list(control)

    # Check for numbers in the correct position --> G
    num_exact_matches = sum(1 for gg, cc in zip(g, c) if gg == cc)
    # If g = ['0', '1', '8'] and c = ['0', '1', '4']:
    # zip(g, c) → [('0', '0'), ('1', '1'), ('8', '4')]
    # Matches: '0' == '0' (True), '1' == '1' (True), '8' == '4' (False)
    # sum(1 for ...) → 1 + 1 = 2
    # Result: num_exact_matches = 2

    # Check for numbers that are in the wrong position --> R
    # produces a list of numbers from g that exist but are not in the same position as c
    partial_matches_gg = [gg for gg, cc in zip(g, c) if gg != cc]
    partial_matches_cc = [cc for gg, cc in zip(g, c) if gg != cc]    
    num_partial_matches = sum(min(partial_matches_gg.count(match), partial_matches_cc.count(match)) for match in set(partial_matches_gg))
    # for each match in partial_matches_gg, count the number of times it appears in both lists
    # and take the minimum of the two counts to avoid double counting

    return 'g' * num_exact_matches + 'r' * num_partial_matches if (num_exact_matches + num_partial_matches) else 'x'

if __name__ == '__main__':
    base_gumball()
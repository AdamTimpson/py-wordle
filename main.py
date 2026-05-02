from os import POSIX_SPAWN_CLOSE
import random
import argparse

MODE = "normal"

WORD_FILE = "./words.txt"
WORDS = []
GUESSES = []

GREEN = "🟩"
YELLOW = "🟨"
GREY = "⬜️"

SUCCESS_KEY = [GREEN] * 5

CORRECT_LETTERS = [] 
POSSIBLE_LETTERS = []
USED_LETTERS = [] 

RESULTS = [] 

def valid_guess(guess): 
    if len(guess) != 5:
        return False

    for char in guess:
        if char in "0123456789":
            return False

    return True

def compare(guess, answer):
    correct_letters = []
    possible_letters = []
    used_letters = []

    key = [GREY] * 5

    for i in range(0, 5):
        if guess[i] in answer:
            key[i] = YELLOW
            possible_letters.append(guess[i])

    for i in range (0, 5):
        if guess[i] == answer[i]:
            key[i] = GREEN
            correct_letters.append(guess[i])

    possible_letters = [letter for letter in possible_letters if letter not in correct_letters]

    used_letters.append(letter for letter in guess)
    used_letters = [letter for letter in guess if letter not in used_letters and letter not in possible_letters and letter not in correct_letters]

    POSSIBLE_LETTERS.append([letter for letter in possible_letters])
    CORRECT_LETTERS.append([letter for letter in correct_letters])
    USED_LETTERS.append([letter for letter in used_letters])

    print(f"Used letters: {USED_LETTERS}")
    print(f"Possible letters: {POSSIBLE_LETTERS}")
    print(f"Correct letters: {CORRECT_LETTERS}")

    return key

if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", help="Enable `debug` or `hints` mode")
    args = parser.parse_args()

    if args.mode == "debug":
        print("Debug mode enabled!")
        MODE = "debug"
    elif args.mode == "assisted":
        print("Assisted mode enabled!")
        MODE = "assisted"

    # Populate the words list 
    with open(WORD_FILE) as file:
        for line in file:
            WORDS.append(line.strip().upper())

    # print(WORDS)
    # Determine a word as the answer
    answer = WORDS[random.randint(0, len(WORDS) - 1)]
    if MODE == "debug":
        print(WORDS)
        print(answer)

    word_found = False
    max_guesses = 5
    guesses_taken = 0
    while not word_found and (max_guesses - guesses_taken) > 0:
        # Ask the user for a word
        guess = input(f"(#{guesses_taken + 1}/{max_guesses}) Guess: ").upper()
        GUESSES.append(guess)
        
        # Is the guess valid? 
        if not valid_guess(guess): 
            print(f"Enter a five letter word only! {str(len(guess))}/5")
        else:
            guesses_taken += 1

            result_key = compare(guess, answer)
            print("".join(result_key))
            RESULTS.append("".join(result_key))

            if result_key == SUCCESS_KEY:
                word_found = True
                break 

    if word_found: 
        print("\nYOU WIN!")
    else:
        print(f"\nThe answer was: {answer}")
    
    print("\n".join(RESULTS))

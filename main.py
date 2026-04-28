import random

WORD_FILE = "./words.txt"
WORDS = []
GUESSES = []

GREEN = "🟩"
YELLOW = "🟨"
GREY = "⬜️"

SUCCESS_KEY = [GREEN] * 5

RESULTS = [] 

def valid_guess(guess): 
    if len(guess) != 5:
        return False

    for char in guess:
        if char in "0123456789":
            return False

    return True

def compare(guess, answer):
    key = [GREY] * 5
    
    for i in range(0, 5):
        if guess[i] in answer:
            key[i] = YELLOW

    for i in range (0, 5):
        if guess[i] == answer[i]:
            key[i] = GREEN

    return key

if __name__ == "__main__": 
    # Populate the words list 
    with open(WORD_FILE) as file:
        for line in file:
            WORDS.append(line.strip().upper())

    # print(WORDS)
    # Determine a word as the answer
    answer = WORDS[random.randint(0, len(WORDS) - 1)]
    # print(answer)

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
        print("YOU WIN!")
    else:
        print(f"\nThe answer was: {answer}")
    
    print("\n".join(RESULTS))

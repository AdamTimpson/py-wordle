from round import Round
import word_manager

MAX_GUESSES = 5

word_manager.populate_words()

def valid_guess(guess) -> bool:
    if guess in "0123456789":
        print("Must be a letter!")
        return False
    elif len(guess) > 1:
        print("Must be only one character!")
        return False

    return True
def already_guessed(guess: str, guesses: list[str]) -> bool:
    if guess in guesses:
        print(f"Already guesses: {guess}")
        return True
    else:
        return False


if __name__ == "__main__":
    round = Round(word_manager.get_random_word())
    
    print(round.word)
    
    while len(round.guesses) <= MAX_GUESSES:
        if len(round.guesses) == MAX_GUESSES:
            break
        
        print(f"{str(len(round.guesses))}/{MAX_GUESSES}")

        guess = input().upper()
        if valid_guess(guess) and not already_guessed(guess, round.guesses):
            round.submit(guess)
        else:
            continue
        
        print()
    print(round.guesses)

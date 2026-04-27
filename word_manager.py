import random

WORD_FILE: str = "./words.txt"

words: list[str] = []

def populate_words() -> None:
    with open(WORD_FILE) as file:
        for line in file:
            words.append(line.strip())

def get_random_word() -> list[str]:
    # print(words)
    return words[random.randint(0, len(words) - 1)]

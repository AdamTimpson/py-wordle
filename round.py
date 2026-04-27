class Round:

    def __init__(self, word: list[str]) -> None:
        self.word: list[str] = word 
        self.guesses: list[str] = []

    def submit(self, user_input: str) -> None:
        self.guesses.append(user_input)
        
        for char in user_input:
            if char in self.word:
                print("HIT")


round = Round(word_manager.get_random_word())
while len(round.guesses) <= 5:
    if len(round.guesses) == 5:
        break

    round.submit(user_input)

print(round.guesses)

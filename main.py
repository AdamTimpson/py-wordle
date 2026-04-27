from round import Round
import word_manager

word_manager.populate_words()

round = Round(word_manager.get_random_word())
print(round.word)
while len(round.guesses) <= 5:
    if len(round.guesses) == 5:
        break

    round.submit(input())

print(round.guesses)

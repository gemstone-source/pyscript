import random

print("Welcome to Hangman!")

words = ["bounty","random","hacker"]

secret_word = random.choice(words)
display_word = []
for lett in secret_word:
    display_word += "_"
print(display_word)

game_over = False
chances = 0
while not game_over:
    guess = input("Guess a letter: ").lower()
    chances += 1
    reamining = 5 - chances
    print(f" You have remained with {reamining} chances.")
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    print(display_word)

    if "_" not in display_word:
        print("You won!")
        game_over = True
    if chances >=5:
        print("You lost!")
        game_over = True
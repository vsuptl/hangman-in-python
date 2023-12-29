import random

words = ['zephyr', 'ostrich', 'kaleidoscope', 'paradox', 'wanderlust', 'serendipity', 'chandelier', 'silhouette', 'zucchini', 'nebula']
game = []
guessesleft = 3

print("Welcome to the Hangman")

word = random.choice(words)
for i in word:
    game.append('_')
print(game)
print("You have " + str(guessesleft) + "left to guess the word.")
userchoice = input("Enter a letter(Enter ! to quit):")
while userchoice != '!':
    if userchoice in word:
        for i in range(len(word)):
            if word[i] == userchoice:
                game[i] = userchoice
        print(game)
    else:
        print("Invalid letter, Try again")
        guessesleft -= 1
        print(game)

    if guessesleft == 0:
        print("You have lost")
        userchoice = input("Enter ! to quit or p to play again:")
        if userchoice == 'p':
            word = random.choice(words)
            game = []
            for i in word:
                game.append('_')
            print(game)
        elif userchoice == '!':
            break;

    if '_' not in game:
        print("You guessed the word correctly")
        userchoice = input("Enter ! to quit or p to play again:")
        if userchoice == 'p':
            word = random.choice(words)
            game = []
            for i in word:
                game.append('_')
            print(game)
        elif userchoice == '!':
            break;

    userchoice = input("Enter a letter(Enter ! to quit):")
print("Thanks for playing!")
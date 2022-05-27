import random
from termcolor import cprint

tries = 6
f = open("./words.txt", "r")
legal_words = f.read().split("\n")
f.close()

f = open("./answers.txt", "r")
answers = f.read().split("\n")
f.close()

print("Welcome to Wordle")
answer = answers[random.randint(0, len(answers) - 1)]
while tries != 0:
    word = input("")

    if word in legal_words:
        for letter in range(5):
            if word[letter] == answer[letter]:
                cprint(word[letter], "green", end="")
            elif word[letter] in answer:
                cprint(word[letter], "yellow", end="")
            else:
                print(word[letter], end="")

        print("\n")

        tries -= 1
    else:
        cprint("Try again (Invalid word)", "red")
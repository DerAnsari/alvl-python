import random

words = ("apple","banana","orange","mango")

hangedMan = {
    0:("  ",
       "  ",
       "  "),
    1:(" O ",
       "   ",
       "   "),
    2:(" O ",
       " | ",
       "   "),
    3:(" O ",
       "/| ",
       "   "
        ),
    4:(" O ",
       "/|\\",
       "  "),
    5:(" O ",
       "/|\\",
       "/  "),
    6:(" O ",
       "/|\\",
       "/ \\")
}

def hangStatus(wrongGuess):
    print("--------------------")
    for line in hangedMan[wrongGuess]:
        print(line)
    print("--------------------")

def mainhint(hint):
    print(" ".join(hint))

def displayAns(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrongguess = 0
    guessed = set()
    running = True

    while running:
        hangStatus(wrongguess)
        mainhint(hint)
        guess = input("Enter guess").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("invald input")
            continue
        if guess in guessed:
            print("already entered")
            continue

        guessed.add(guess)

        if guess in answer:
            for index in range(len(answer)):
                if answer[index] == guess:
                    hint[index] = guess
        else:
            wrongguess += 1
            if wrongguess == len(hangedMan):
                print("You Have Lost")
                print(f"Correct answer was: {answer}")
                retry = input("Do you wish to play again,(Y/N)?").upper()
                if retry != "Y":
                    running = False
                else:
                    answer = random.choice(words)
                    hint = ["_"] * len(answer)
                    wrongguess = 0
if __name__ == '__main__':
    main()
import random

def guess(name, numb,count = 1):
    print("Take a guess.")
    yguess = int(input())
    if yguess==numb:
        print("Good job,", name, "! You guessed my number in", count, "guesses!")
        return 0
    else:
        if yguess>numb:
            print("Your guess is too high.")
        else:
            print("Your guess is too low")
        count+=1
        guess(name,numb, count)

name = input("Hello! What is your name?")
numb = random.randrange(1,21)
print("Well,", name, ", I am thinking of a number between 1 and 20.")
guess(name,numb)
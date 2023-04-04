import random
def randomNumber():
    for i in range(0, 10):
        number = random.randrange(0, 100)
        try:
            guess = int(input("Guess A Number From 0 To 100: "))
        except:
            print("Invalid Integer")
        if guess < number:
            differ = number - guess
        elif guess > number:
            differ = guess - number
        if number == guess:
            print("Correct!")
        else:
            print("Incorrect :(")
            print("You are", differ, "away")
            print(you lose)

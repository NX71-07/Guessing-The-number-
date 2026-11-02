import random

print("HI!!!!!\n")
num = random.randint(1,10)
guess=int(input("Guess the Number: "))
while guess is not num:
        print("Oopsie!! guess again :(\n")
        guess=int(input("Guess the Number: "))


print("You gussed correctly :)")


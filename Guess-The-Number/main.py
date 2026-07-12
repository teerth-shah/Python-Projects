## Concepts 
- loops
- list
- random built in function 




import random

print("-----------------------------------------")
print("----------GUESS THE NUMBER --------------")
print("-----------------------------------------")

#list comprehension
numbers = [i for i in range(1,101)]
print("I have selected a number between 1 and 100.")
#selects a random number 
numbers=random.choice(numbers)

print("You have 10 attempts to guess the number.")

for i in range(1,11):
    guess = int (input("Enter your guess:"))

    if(guess < numbers):
        print("Your guess is too low.")
    elif(guess > numbers):
        print("Your guess is too high.")
    else:
        print("Congratulations! You guessed the number correctly.")
        break;

print(f"The number was: {numbers}")

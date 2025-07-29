import random

name = input("Enter your name: \n")

secret_number = random.randint(1, 10)

count = 0

while count < 3:
    number = int(input("Enter your secret number: \n"))

    if number < secret_number:
        print("Too low! Try a higher number.")
        count += 1
    elif number > secret_number:
        print("Too high! Try a lower number.")
        count += 1
    else:
        print(f"You won! \nCongratulations {name}")
        break
else:
    print(f"Count exceeded {name}, you've failed! The secret number was {secret_number}.")
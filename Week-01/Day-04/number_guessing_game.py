import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("===== Number Guessing Game =====")
print("Guess a number between 1 and 100.")

while True:

    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too Low!")

    elif guess > secret_number:
        print("Too High!")

    else:
        print("Congratulations! You guessed the correct number.")
        break
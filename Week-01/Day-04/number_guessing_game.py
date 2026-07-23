# -----------------------------------------
# Number Guessing Game (Two Player Version)
# -----------------------------------------

import getpass


def select_difficulty():

    print("\nChoose Difficulty Level")
    print("1. Easy   (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard   (1-1000)")

    while True:

        choice = input("Enter choice (1-3): ")

        match choice:

            case "1":
                return 50, 5

            case "2":
                return 100, 5

            case "3":
                return 1000, 7

            case _:
                print("Invalid choice! Select 1, 2 or 3.")



def get_secret_number(max_number):

    while True:

        try:

            secret = int(getpass.getpass(
                f"\nPlayer 1, enter secret number (1-{max_number}): "
            ))

            if 1 <= secret <= max_number:
                return secret

            else:
                print(f"Number must be between 1 and {max_number}")

        except ValueError:
            print("Enter numbers only!")



def play_game():

    max_number, max_attempts = select_difficulty()

    secret_number = get_secret_number(max_number)


    print("\n" * 50) 
    # Clears screen visually so Player 2 cannot see the number

    print("===== Player 2 Turn =====")
    print(f"Guess the number between 1 and {max_number}")


    attempts = 0

    low = 1
    high = max_number


    while attempts < max_attempts:


        try:

            guess = int(input(
                f"\nAttempt {attempts+1}/{max_attempts}: Enter guess: "
            ))


            if guess < low or guess > high:
                print(
                    f"Please guess between {low} and {high}"
                )
                continue


            attempts += 1


            if guess < secret_number:

                low = guess + 1

                print("Too Low!")
                print(
                    f"Try between {low} and {high}"
                )


            elif guess > secret_number:

                high = guess - 1

                print("Too High!")
                print(
                    f"Try between {low} and {high}"
                )


            else:

                print("\n🎉 Congratulations!")
                print(
                    f"You guessed it in {attempts} attempts."
                )
                break


        except ValueError:

            print("Invalid input! Enter numbers only.")



    else:

        print("\nGame Over!")
        print("You used all attempts.")

        # Secret number is not displayed
        # to keep fairness



def main():

    while True:

        play_game()


        again = input(
            "\nPlay Again? (Y/N): "
        ).lower()


        if again != "y":

            print("\nThank you for playing!")
            break



main()
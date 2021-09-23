# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Sept 2021
# This program asks the user to ask a number between 0-9


import random


def main():
    # this function checks if the user picked the computer generated number, and responds to a non valid integer

    # input
    die = random.randint(0, 9)  # a number between 0 and 9
    number = input("Guess a number between 0-9: ")
    print("")

    # process & output
    try:
        integer_as_number = int(number)

        if number != die:
            print("You guessed incorrectly.")

        else:
            print("You guessed correctly!")

    except Exception:
        print("You did not enter in an integer.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()

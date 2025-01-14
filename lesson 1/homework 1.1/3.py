import random


def guess_the_number():

    number_to_guess = random.randint(1, 10)
    attempts = 3

    print("Welcome to 'Guess the Number'!")
    print("I have guessed a number between 1 and 10. Can you guess it?")
    print(f"You have {attempts} attempts.")

    while attempts > 0:
        try:

            user_guess = int(input("Enter your guess: "))

            if user_guess == number_to_guess:
                print("Congratulations! You guessed the number correctly.")
                break
            elif user_guess < number_to_guess:
                print("More")
            else:
                print("Less")

            attempts -= 1

            if attempts > 0:
                print(f"You have {attempts} attempts left.")
            else:
                print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")


guess_the_number()
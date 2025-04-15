# guass game
import random


def generate_random_number():
    number = random.randint(1, 10)
    return number


def guess_number():
    guass_number = int(input('guass a number in range 1 to 10.....'))
    return guass_number


def result():
    hide_number = generate_random_number()
    user_number = guess_number()

    if hide_number == user_number:
        return 'You Won'
    else:
        return f"\nOops!, You Lose. \nThe Hidden Number is {hide_number}\n"


if __name__ == "__main__":
    print(result())

import random

def get_number():
    """
    Get a number from the user.

    Try until the user will input proper number.

    :rtype: int
    :return: given number as int
    """
    while True:
        try:
            result = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number!")

    return result

def game():
    """The main function of the game."""
    random_number = random.randint(1, 100)
    user_number = get_number()

    while user_number != random_number:
        if user_number < random_number:
            print("Too small!")
        else:
            print("Too big!")
        user_number = get_number()
    print("You win!")

if __name__ == "__main__":
    game()
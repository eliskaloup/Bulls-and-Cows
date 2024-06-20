import random

def introduction():
    print("Hi there!", separator, "I've generated a random 4 digit number for you","Enter four unique numbers that doesn't START with zero","Let's play a bulls and cows game", separator, sep="\n")
separator = "-" * 55

"""
Generates a random 4-digit secret number with unique digits and no leading zero.

The function continues to generate random 4-digit numbers until it finds one that:
    1. Has no repeated digits.
    2. Does not start with a zero.

Returns:
    str: A string representing a valid 4-digit secret number.
"""
def generate_secret_number():
    while True:
        secret_number = str(random.randint(1000, 9999))
        if len(set(secret_number)) == 4 and secret_number[0] != '0':
            return secret_number
"""
Validate a player's 4-digit number.

Args:
    players_number (str): The number entered by the player.

Returns:
    bool: True if valid, False otherwise.

Criteria:
- Must not be empty.
- Must not start with '0'.
- Must contain only digits.
- Must be exactly 4 digits long.
- Must have all unique digits.
"""
def number_validation(players_number):
    if players_number == "":
        print("Enter a 4 digit number", separator, sep="\n")
    elif players_number[0] == "0":
        print("Number '0' can not be selected as first digit", separator, sep="\n")
    elif players_number.isdigit() == False:
        print("Enter only digits", separator, sep="\n")     
    elif len(players_number) != 4:
        print("You must enter 4 digit number", separator, sep="\n")
    elif len(set(players_number)) != 4:
        print("Your number contains two or more same digits", separator, sep="\n")
    else:
        return True
    return False

if __name__ == "__main__":
    secret_number = generate_secret_number()
    introduction()
    my_guess_count = 0
    maximum_guesses_attempt = int(input("Choose the maximum number of your guessing attempt: "))
    print(f"{separator}\nEnter a number:",sep="\n")
    while maximum_guesses_attempt > 0:
        choosen_number = input(">>>")
        if number_validation(choosen_number):
            bulls = 0
            cows = 0
            for i in range(len(secret_number)):
                if choosen_number[i] in secret_number:
                    if choosen_number[i] == secret_number[i]:
                        bulls += 1
                    else:
                        cows += 1
            print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")
            my_guess_count += 1
            counting_end_of_game = maximum_guesses_attempt - my_guess_count
            if bulls == 4:
                print(f"{separator}\nCorrect, you've guessed the right number in {my_guess_count} guesses! \n{separator}")
                break
            if counting_end_of_game  == 0:
                print(f"{separator}\nYou have lost! The number was {secret_number}\n{separator}")
                break
            print(f"You have {counting_end_of_game} {'attempt' if counting_end_of_game == 1 else 'attempts'} left \n{separator}")
        else:
            continue

import random
SEPARATOR = "-" * 55

def introduction():
    print("Hi there!", 
          SEPARATOR, 
          "I've generated a random 4 digit number for you",
          "Enter four unique numbers that doesn't START with zero",
          "Let's play a bulls and cows game", 
          SEPARATOR, 
          sep="\n")

def generate_secret_number():
    while True:
        secret_number = str(random.randint(1000, 9999))
        if len(set(secret_number)) == 4 and secret_number[0] != '0':
            return secret_number

def validate_number(players_number):
    if not players_number:
        print("Enter a 4 digit number", SEPARATOR, sep="\n")
    elif players_number[0] == "0":
        print("Number '0' can not be selected as first digit", SEPARATOR, sep="\n")
    elif not players_number.isdigit():
        print("Enter only digits", SEPARATOR, sep="\n")     
    elif len(players_number) != 4:
        print("You must enter 4 digit number", SEPARATOR, sep="\n")
    elif len(set(players_number)) != 4:
        print("Your number contains two or more same digits", SEPARATOR, sep="\n")
    else:
        return True
    return False

def play_bulls_and_cows(secret_number, max_attempts):
    guess_count = 0

    print(f"{SEPARATOR}\nEnter a number:", sep="\n")

    while max_attempts > 0:
        player_guess = input(">>>")

        if validate_number(player_guess):
            bulls, cows = 0, 0

            for i in range(len(secret_number)):
                if player_guess[i] == secret_number[i]:
                    bulls += 1
                elif player_guess[i] in secret_number:
                    cows += 1

            print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")
            guess_count += 1
            remaining_attempts = max_attempts - guess_count
            
            if bulls == 4:
                print(f"{SEPARATOR}\nCorrect, you've guessed the right number in {guess_count} guesses! \n{SEPARATOR}")
                break
            elif remaining_attempts == 0:
                print(f"{SEPARATOR}\nYou have lost! The number was {secret_number}\n{SEPARATOR}")
                break
            else:
                print(f"You have {remaining_attempts} {'attempt' if remaining_attempts == 1 else 'attempts'} left \n{SEPARATOR}")

if __name__ == "__main__":
    introduction()
    secret_number = generate_secret_number()
    max_attempts = int(input("Choose the maximum number of your guessing attempt: "))
    play_bulls_and_cows(secret_number, max_attempts)

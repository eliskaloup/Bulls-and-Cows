import random

"""
Generating a secret number
"""
def generate_secret_number():
    digits = list(range(1,10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))

secret_number = generate_secret_number()

separator = "-" * 47
print("Hi there!", separator, "I've generated a random 4 digit number for you.", "Let's play a bulls and cows game.", separator, "Enter a number:", separator, sep="\n")

my_guess_count= 1
maximum_guesses_attempt = 10
while maximum_guesses_attempt > 0:
    choosen_number=input(">>>")
    if int(len(choosen_number)) == 4:
        pass
    if choosen_number[0] == '0':          #word can not start with 0
        print("You can't start with 0")
    elif len(choosen_number) != 4:        #word must be 4 letters long
        print("You must enter 4 digit numbers")
    elif len(set(choosen_number)) != 4:   #word can not have duplicates
        print("You can't enter duplicates")
    elif not choosen_number.isdigit():    #word can not be a letter
        print("You can't enter letter")
    else:
        bulls = 0
        cows = 0
        for i in range(len(secret_number)):
            if choosen_number[i] in secret_number:
                if choosen_number[i] == secret_number[i]:
                    bulls += 1
                else:
                    cows += 1
        print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'} \n{separator}")
        if bulls == 4:
            print(f"Correct, you've guessed the right number \nin {my_guess_count} guesses! \n{separator}")
            break
        my_guess_count += 1

if not maximum_guesses_attempt > 0:
    print(f"You have lost! The number was {secret_number}")

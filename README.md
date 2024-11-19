# Game Bulls and Cows

### Project Description
The program simulates the game Bulls and Cows. After displaying an introductory message, the user attempts to guess a randomly generated four-digit number. The game can be repeated as many times as desired. An added feature allows the user to specify the number of attempts, and upon guessing the number correctly, the program displays how many attempts remain.

### Program Functionality:
Welcome and Introduction:
The program greets the user and displays introductory information.

### Generating the Secret Number:
The program generates a unique four-digit number. The digits must be distinct, and the number cannot start with zero.

### Setting the Number of Attempts:
The user selects the desired number of attempts (or "lives") for the game.

### User Guessing:

- The user attempts to guess the number.
- The program validates the input to ensure it is exactly four digits long, does not contain duplicate digits, does not start with zero, and contains only numeric characters.
- If the input is invalid, it does not count as an attempt.
  
### Evaluating the Guess:
- The program evaluates the user's guess:
  - Bulls: The number of digits guessed correctly in both value and position.
  - Cows: The number of digits guessed correctly but in the wrong position.
- The feedback adapts to singular and plural forms in the output (e.g., 1 bull vs. 2 bulls, 1 cow vs. 2 cows).

### Displaying Remaining Attempts:
After providing feedback on the number of bulls and cows, the program also displays the remaining attempts.

### Game End:

- The game ends when the user guesses the number correctly (win) or runs out of attempts (loss).
- The user can restart the game if desired.

import random
from art import logo

print(logo)

def check_answer(guess, answer):
    correct_guess = False
    if (guess < answer):
        print("Too low")
    elif (guess > answer):
        print("Too high")
    else:
        print(f"You got it! The answer was {guess}")
        correct_guess = True
    return correct_guess



def play_game(attempts):
    correct_guess = False
    while not correct_guess and attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        your_guess = int(input("Make a guess: "))
        correct_guess = check_answer(your_guess, answer)
        attempts-=1
        if (attempts == 0 and correct_guess == False):
            print("You have run out of guesses, you lose.")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1,100)
print(f"Pssst, the correct answer is {answer}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if (difficulty == 'hard'):
    attempts = 5
    play_game(attempts)

elif (difficulty == 'easy'):
    attempts = 10
    play_game(attempts)

else:
    print("Invalid Input")
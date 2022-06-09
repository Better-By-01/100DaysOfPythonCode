import os                                   # for clearing the screen
import random

from numpy import choose

from hangman_art import logo, stages
from hangman_word import word_list
print(logo)

choosen_word = random.choice(word_list)
word_length = len(choosen_word)

lives = 6

result_list = []
for i in range(word_length):
    result_list.append("_")

end_of_game = False 

while not end_of_game:                        
    guess = input("Guess a letter: ").lower() 

    os.system('clear')

    if guess in result_list:
        print(f"You have already guessed {guess}")

    for i in range(0, word_length):
        if choosen_word[i] == guess:
            result_list[i] = guess

    if guess not in choosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives-=1
        if lives == 0:
            end_of_game = True
            print("You Lose!!!")

    print(f"{' '.join(result_list)}")        

    if "_" not in result_list:
        end_of_game = True
        print("You Win !!!")

    print(stages[lives])


print("The choosen word is: " + choosen_word)

# NOTE
# if "_" not in display:
    # print("_ present in display")

# print(f"{' '.join(result_list)}")
# if guess not in choosen_word:

# import os
# os.system('clear') for clearing screen
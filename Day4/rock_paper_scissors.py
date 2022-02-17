import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: " ))
game_images = [rock, paper, scissors]
if (user_choice > 2 or user_choice < 0):
    print("You typed an invalid number, you lose !!")
else:
    print(game_images[user_choice])
    randInt = random.randint(0, 2)
    print("\nComputer Chose: ")
    print(game_images[randInt])

    if ((user_choice == 0 and randInt == 2) 
        or (user_choice == 1 and randInt == 0)
        or (user_choice == 2 and randInt == 1)):
        print("\nYou Win !!!")
    elif (user_choice == randInt):
        print("It's Draw !!!")
    else:
        print("\nYou Lose !!!")
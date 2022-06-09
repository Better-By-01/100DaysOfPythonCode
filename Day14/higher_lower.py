import random
import os
from art import logo, vs
from game_data import data


print(logo)

"""################################ MY-TRY #####################################
def whom_to_compare():
    total = len(game_data.data)
    a = random.randint(0, total-1)
    b = random.randint(0, total-1)
    if b == a:
        while b == a:
            b = random.randint(0, total-1)
    return [a,b]

def result(val1, val2, score): 
    if (game_data.data[val1]['follower_count'] > game_data.data[val2]['follower_count']):
        score += 1
        os.system('clear')
        print(art.logo)
        print(f"You're right! Current Score: {score}.")
        celebs_choice(score)
    else:
        os.system('clear')
        print(art.logo)
        print(f"Sorry, that's wrong. Final Score {score}.")

    return score

def celebs_choice(score):
    times = 0
    to_compare = whom_to_compare()
    a = to_compare[0]
    b = to_compare[1]
    print(f"Compare A: {game_data.data[a]['name']}, a {game_data.data[a]['description']}, from {game_data.data[a]['country']}.")
    print(art.vs)
    print(f"Against B: {game_data.data[b]['name']}, a {game_data.data[b]['description']}, from {game_data.data[b]['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ")

    if choice == 'A':
        score = result(a, b, score)
    if choice == 'B':
        score = result(b, a, score)


celebs_choice(score = 0)
"""

def get_random_account():
    """Get data from random account"""
    return random.choice(data)

def format_data_account(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """"Check followers against user's guess and returns True
        if they got it right. Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()
        
        print(f"Compare A: {format_data_account(account_a)}.")
        print(vs)
        print(f"Against B: {format_data_account(account_b)}.")
    
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
        os.system("clear")
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score {score}")
game()
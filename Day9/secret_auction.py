from art import logo 
import os

print(logo)

print("Welcome to the secret auction program.")

to_end = False
bidders = {}

while not to_end: 
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    bidders[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if(choice == "no"):
        to_end = True
    os.system('clear')

max = 0
for bidder in bidders:
    if (bidders[bidder] > max):
        max = bidders[bidder]
        max_bidder_name = bidder

os.system('clear')

print(f"The winner is {max_bidder_name} with a bid of ${max}.")

import os
from art import logo
import sys

print(logo)

def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {
    '+': add,               # (Remember) these are not string 
    '-': subtract,          # it's of type <class 'function'> 
    '*': multiply,
    '/': divide
}
def calculator():
    curr_value = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)

    def next_step(curr_value):
        choice = input("Pick an operation: ")
        snum = float(input("What's the next number? "))
        fun_value = operations[choice](curr_value, snum)
        print(f"{curr_value} {choice} {snum} = {fun_value}")
        return fun_value

    curr_value = next_step(curr_value)
    should_continue = True
    char = input(f"Type 'y' to continue calculating with {curr_value}, or 'n' for new or type 'x' to exit.\n").lower()
    while should_continue: 
        if char == 'x':
            sys.exit()
        elif char == 'y':
            os.system('clear')
            print(logo)
            curr_value = next_step(curr_value)
            char = input(f"Type 'y' to continue calculating with {curr_value}, or 'n' for new or type 'x' to exit.\n").lower()
        elif char == 'n':
            os.system('clear')
            print(logo)
            calculator()
calculator()


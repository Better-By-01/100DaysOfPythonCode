# Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
           'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U',
          'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        
lst = []
lst.append(letters)
lst.append(numbers)
lst.append(symbols)

password = ""

print("\n\t\tWelcome to the PyPassword Generator!\n")
n_letter = int(input("How many letters would you like in your password?\n"))
temp_nl = n_letter
n_symbol = int(input("How many symbols would you like?\n"))
temp_ns = n_symbol
n_number = int(input("How many numbers would you like?\n"))
temp_nn = n_number
total_n = n_letter + n_symbol + n_number


for i in range(1, total_n+1):
    value_type = random.randint(0, len(lst)-1)      # -1 as len(lst) is inclusive
    if (value_type == 0 and temp_nl == 0):          # if value_type is 0 i.e. letter
        while (value_type == 0): 
            value_type = random.randint(0, len(lst)-1)     
    elif (value_type == 0 and temp_nl != 0):
        temp_nl -= 1
    if (value_type == 1 and temp_nn == 0):          # if value_type is 1 i.e. number
        while (value_type == 1): 
            value_type = random.randint(0, len(lst)-1)     
    elif (value_type == 1 and temp_nn != 0):
        temp_nn -= 1
    if (value_type == 2 and temp_ns == 0):          # if value_type is 2 i.e. symbol
        while (value_type == 2): 
            value_type = random.randint(0, len(lst)-1)     
    elif (value_type == 2 and temp_ns != 0):
        temp_ns -= 1

    password += random.choice(lst[value_type])

print("Here is your password: " + str(password) + "\n")

# Note:
#   > random.shuffle() could be used as well for ordered password like
#           list[] = 9382Abde)#*# if used with random.shuffle() generates
#           e.g. g3sdg7(29&)
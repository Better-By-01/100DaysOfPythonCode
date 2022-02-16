# if-else conditional statement
height = 100
if height >= 120:
    print("You can ride the roller coaster\n")
else:
    print("You can't ride the roller coaster\n")


# Nested if/else
# if condition:
#   if another condition:
#       do this
#   else:
#       do this
# else:
#   do this 


# if/elif/else 
# if condition1:
#   do A
# elif condition2:
#   do B
# else:
#   do this


# combining conditions
# if cond1 and cond2
# if cond1 or cond2
# if not cond1:         # negation of cond1


#lower() & count() function
lower_case_name = "Alphabet".lower()
print(f"Without lowering the 'Alphabet': {'Alphabet'.count('a')}")
lower_a_count = lower_case_name.count('a')
print(f"After lowering the 'Alphabet': {lower_a_count}")


# using \ before ' escapes the string and it sees it as text
# print('you\'re are "Ashutosh" or "Asutosh"')


#for multiline string
print('''
  88
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  ,adPPYba, 
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8 a8P_____88 
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88         8PP""""""" 
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88         "8b,   ,aa 
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          `"Ybbd8"' 
                                                                           
                                                                           
                                                               
88           88                                 88  
""           88                                 88  
             88                                 88  
88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8  
''')
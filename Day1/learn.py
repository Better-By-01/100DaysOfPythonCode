# ' ' or "" can be used interchangeably 
from doctest import OutputChecker


print('hello "world"')
print("hello 'world'")

# similar ' or " " can't be used in the same print line
# print('hello 'world'')
# print("hello "world"")

# Indentation needs to be taken care of
#    print("hello world")    #Ex. of wrong indentation

print("\nHello World\nHello World\nHello World\n")

# string concatenation
print("Ashutosh" + " " + "Singh" + " " + "Patel\n")     

# input function
print("Hello, " + input("What is your name ? ") + "!\n")   # input(prompt for the user)
# Output:
# What is your name ? Ashutosh
# Hello, Ashutosh!

#length of the string
print(len(input("What is your name ? ")))
# Output
# What is your name ? Ashutosh
# 8

# variables
name = input("What is your name ? ")
name = "Jack"
print(name)         # name overwritten
length = len(name)
print(length)
# Output
# Jack
# 4






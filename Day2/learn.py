# Data-Types

print("String")
print("Hello"[0])
hello = "Hello"
length = len("Hello")
print("Hello"[length-1])   # way to access a char. from string (called subscripting)
print(hello[length-1] + "\n")


print("Integer")
a = 123
print(a + 345)
# use _ (for ,) in large nos. for making it more readable
print(1_00_000 + 1)
print("\n")


print("Float")
print(3.14159)      # as decimal point can float around the number
print("\n")


# Boolean
True
False


print("Type-Error")
num_char = len(input("What is your name? "))
# print("Your name has  " + num_char + " characters.")
# Output: error as we are trying to concatenate string to int


print("Type-Checking")
print(type(num_char))


print("\nType-conversion/casting")
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
#Output: Your name has 8 characters.
print(70 + float("100.5"))
# Output: 170.5
print(70 + int("20"))
# Output: 90


print("\nMathematical operations")
print(2 ** 3)                # 2 to the power 3
# Output: 8
# Precedence
######################## PEMDAS ####################
# ()
# **
# * /       (L to R)
# + -       (L to R)


print("\nNumber Manipulation")
print(int(8/2))
print(round(8/3))           # 2
print(round(8/3, 2))        # 2.667
# Floor Division
print(8 // 3)               # no need of converting to integer


######################### f-string #################
print("\nf-string")
score = 0               # int
height = 1.8            # float
isWinning = True        # boolean
print(f"your score is {score}, your height is {height}, you are winnings is {isWinning}\n")


import random

# LOOPING

# for loop

# for item in list_of_items:
    # do something to each item

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
print("\n")

student_heights = input("Input a list of student height: ").split()
# by default split() uses " " for separating
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i]) 
print(student_heights)

print("Max: " + str(max(student_heights)))
print("Min: " + str(min(student_heights)))
print("Sum: " + str(sum(student_heights)))

print("\n")
              # n, n > 0, n-=1
for num in range(5,0,-1):
                # by default the step-size(c) is 1
    #5, 4, 3, 2, 1
    print(num)           
             # 0, n < 5, n+=1
print("\n")

for n in range(0,5,1): 
    #0,1,2,3,4
    print(n)

print("\n")
# to print elements on the same line
a = [1, 2, 3, 4]
for i in range(0,4):
    print(a[i], end = " ")
print("\n")


# shuffling the existing list
x = [1,2,3,4,5]
random.shuffle(x)
print(x)

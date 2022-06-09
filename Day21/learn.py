# Inheritence

class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, Exhale.")

class Fish(Animal):

    def __init__(self):
        super().__init__()      # to get hold of everything that an animal has and does
        # (RECOMMENDED BUT NOT COMPULSORY)
    
    # for adding extra functionality to the function in super class
    def breathe(self):
        super().breathe()       # gets all the functionality breath() in super class have 
        print("doing this underwater.")

    def swim(self):
        print("Moving in water.")
    
nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

# List/Tuple Slicing

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print(piano_keys[1:4])  # [a:b)
# ['b', 'c', 'd'] 
print(piano_keys[0:5:2]) # 2 here is step-size
# ['a', 'c', 'e']


# IMPORTANT
print(piano_keys[::2])
# ['a', 'c', 'e', 'g']              # elements from beg to end with step size of 2
print(piano_keys[::-1])
# ['g', 'f', 'e', 'd', 'c', 'b', 'a'] # from end to beg




########################### QUESTION #########################
# Given this code:

# class Dog:
#     def __init__(self):
#         self.temperament = "loyal"
 
#     def bark(self):
#         print("Woof, woof!")
 
# class Labrador(Dog):
#     def __init__(self):
#         super().__init__()
#         self.is_a_good_boy = True
 
#     def bark(self):
#         super().bark()
#         print("Greetings, good sir. How do you do?")


# What will this print?

# sparky = Labrador()
# sparky.bark()

########################## SOLUTION ###########################
# Woof, woof!
# Greetings, good sir, How do you do ?

######## Explanation: We are extending the functionality of bark() method
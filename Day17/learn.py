# types of cases:
# PascalCase
# camelCase
# snake_case

# Classes

class User:
    # pass                       # allows us to write other things outside the classes without showing any error
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0      # setting a default value 
        self.following = 0

    # Example of class method 
    # def enter_race_mode():
        # self.seats = 2

    def follow(self, user):           # allows need to have self parameter
        user.followers += 1           # SEE PROPERLY HOW attribute is used with a parameter and self
        self.following += 1

# Constructor

# class Car:
    # def __init__(self):         # constructor
    #initialise attributes

    # settings attributes in the constructor
    # def __init__ (self, seats):
    #     self.seats = seats
    # my_car = Car(5)       #creating an object



user_1 = User("001", "Ashutosh")
user_2 = User("002", "Jack")

print(user_1.id)        # 001 
print(user_1.username)  # Ashutosh
print(user_1.followers) # 0

user_1.follow(user_2)

print(user_1.followers) # 0
print(user_1.following) # 1

print(user_2.followers) # 1
print(user_2.following) # 0



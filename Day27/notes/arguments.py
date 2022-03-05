#----------------------------------------------------------------------------------------------------------------------#
# Arguments with default values
def my_function(a=1, b=2, c=3):
    #do this with a
    #do this with b
    #do this with c
    pass
my_function(b=5)
# Ex.
# def foo(a, b=4, c=6): 
#     print(a, b, c)
 
# foo(1)
# output: 1 4 6



# Unlimited positional arguments
def add(*args):            # (* is must as it tells python that this fun. can accept any no. of arguments) (args can be replaced with any other name)
    sum=0                
    print(type(args))      # args is a tuple
    for n in args:
        sum += n
    print(sum) 

add(1,2,3,4,5)              


# Unlimited keyboard arguments
def calculate(n, **kwargs):

    print(type(kwargs))             # a dictionary
    print(kwargs)                   # {'add': 3, 'multiply': 5}

    # for key, value in kwargs.items():
    #     print(key, value)
    # OR
    # print(kwargs["add"]

    n += kwargs["add"]      # 6+3
    print(n)

calculate(6, add=3, multiply=5)        

class Car:
    # def __init__(self,**kwargs):        # **kwargs is going to be all the optional arguments that we pass in when we are initializing a new object of this class
    #     self.make = kwargs["make"]
    #     self.model = kwargs["model"]

    # if we leave model the print statement will give the error and in order to get correct output we will use kwards.get() method as it returns None if key not present
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("color")
        self.seats = kwargs.get("seats")

my_car = Car(make="Nissan")
print(my_car.make, my_car.model)

#----------------------------------------------------------------------------------------------------------------------#
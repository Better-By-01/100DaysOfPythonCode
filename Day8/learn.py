# Functions with input

def greet(name):        # "name" being the function parameter
    print(f"Hello, {name}")

greet("Ashutosh")       # "Ashutosh" passed as argument


# Functions with multiple input

def greet(name, location):
    print(f"\nHello, {name}")
    print(f"What is it like in {location}?")

greet("Ashutosh", "Rewa")      
# greet("Rewa", "Ashutosh")     # concept of positional argument
                                # arguments that needs to be included 
                                # in the proper position or order.

# keyword argument to be used to avoid confusion like ..
greet(location="Rewa", name="Ashutosh")
# Output
# Hello, Ashutosh
# What is it like in Rewa?

print('\n')
# index()
fruits = ['apple', 'banana', 'cherry', 'banana', 'cherry']
print(fruits.index('cherry'))
# returns only the 1st occurrence





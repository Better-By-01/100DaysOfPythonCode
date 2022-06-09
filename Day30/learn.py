# Catching exceptions in case something unexpected happens with our program.

# keywords helpful in handling exceptions

# try: Something that might cause an exception

# except: Do this if there was an exception

# else: Do this if there was no exceptions 

# finally: Do this no matter what happens


# Ex.

try:
    file = open("a_file.txt")
except: 
    # print("There was an error")         # as the above opening of file failed
    file = open("a_file.txt",'w')         # it will create the file if it doesn't exist (a much safer thing)



try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["hello"])
except FileNotFoundError:                 # it's imp. to put the type of error when there is a chance of occurrence of more than 1 type of error. 
    file = open("a_file.txt", "w")        # else the except code will be executed even if the KeyError is there 
# except KeyError:
#     print("That key doesn't exist")
# OR
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
    # The key 'hello' does not exist.

else:                                    # if file DOESN'T EXIST then this code will not execute
    content = file.read()
    print(content)

# finally:                                # no matter what this code will be executed
#     file.close()




# Raising own exceptions

# finally:
#     raise KeyError("Keyerror that I created")                      # an error will be generated and crash the program



# Real World Example

height = float(input("Height: "))               # if someones enters a huge value like 45 m
weight = int(input("Weight: ")) 

if height > 3:
    raise ValueError(f"Human height should not be over 3 meters. ")

bmi = weight/(height**2)
print(bmi)



# Working with json data (just like python dictionaries)

# Write -> json.dump()
# Read -> json.load()
# Update -> json.update()


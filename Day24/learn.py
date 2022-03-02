# Opening, Reading and Writing to files using the 'with' keyword


# Reading

file = open("my_file.txt")
contents = file.read()
print(contents)     # type string

file.close()        # when it's open means it's taking resources of computer.
                    # this will close the file manually and free the resources.

# OR
# a better way which automatically closes the file

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)


# Writing
# if file not present if will create and open a new file 

# with open("my_file.txt") as file:
#         file.write("New Text.")     # this won't work the first time as the file is by default 
                                    # opened in readonly (mode = 'r')

with open("my_file.txt", mode="w") as file:
    file.write("New Text in write mode")

# use mode = "a" for appending instead of completely deleting the content
with open("my_file.txt", mode = "a") as file:
    file.write("\nText with append")


# create a new file using with
with open("new_file.txt", mode="w") as file:
    file.write("New Text.")
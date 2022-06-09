# Functions with Outputs
def format_name(fname, lname):
    """return the concatenated first and 
       the last name"""
    if (fname == "" or lname == ""):
        print("You didn't provide valid inputs.") 
        return
    return (f"{fname} {lname}".title())

print(format_name("AshUtOsH", "PATEL"))


# Docstring -> to create documentation for what we create
def Sum(a,b):
    """given 2 input Sum() 
        returns sum of 2 numbers"""
    return a*b

print(Sum(2,3))
    
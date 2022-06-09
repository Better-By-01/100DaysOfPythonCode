import random
# List Data Structure

# one-dimension
fruits = ['Apple', 'Banana', 'Cherry']
print(fruits[0] + " " + fruits[2])
#0, 2 are the offsets (here it means distance from beginning)
print(fruits[-1])      # starts from end
fruits.append("Orange")
print(f"List after appending orange : {fruits}")

#using split method
names_string = input("Enter names: ")
names = names_string.split(', ')
print(names)

#choice method
random_person = random.choice(names)
print("Random Person: " + random_person)


# Nested List
fruits = ['Apple', 'Banana', 'Pears']
vegetables = ["Spanish", "Kale", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
#[['Apple', 'Banana', 'Pears'], ['Spanish', 'Kale', 'Potatoes']]

# OR

dirty_dozen = [['Apple', 'Banana', 'Cherry'],
          ["Spanish", "Kale", "Potatoes"]]
print(fruits[0][0] + " " + fruits[1][1])


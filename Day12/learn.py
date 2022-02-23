# Scope

enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
    # 2
increase_enemies()
print(f"enemies outstide function: {enemies}")
# 1

# namespace - system that has a unique name for each 
# and every object in python

# Modifying the global scope
def modify_global_scope():
    global enemies
    enemies += 15
    print(f"Modified global value: {enemies}")
modify_global_scope()

# there is no block scope in python 
# (Inside a if/else/for/while code block is the same as outside it)

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
   new_enemy = enemies[0]

print(new_enemy)        # a valid code
# Skeleton

# def create_enemies():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]

# print(new_enemy)        # a INVALID code



# Global Constants
PI = 3.14159        # in capitals

def calc():
    print(f"{PI}")
calc()
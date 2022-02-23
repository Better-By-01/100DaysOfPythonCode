# Quarter - 25 cents = $0.25
# Dime    - 10 cents = $0.10
# Nickel  - 5  cents = $0.05
# Penny   - 1 cents  = $0.01

from coffee_data import MENU, resources

def display_report(): 
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}gm")
    print(f"Money: ${resources['profit']}")

def resource_check(choice):
    order_ingredients = MENU[choice]["ingredient"]
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]: 
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def money_required(choice):
    return MENU[choice]["cost"]

def resource_change(choice):
    resources["water"] -= MENU[choice]["ingredient"]["water"] 
    resources["coffee"] -= MENU[choice]["ingredient"]["coffee"] 
    resources["milk"] -= MENU[choice]["ingredient"]["milk"] 
    resources["profit"] += MENU[choice]["cost"] 

is_on = True
while is_on:
    choice = input("What would you like? (expresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        display_report()
    elif choice in MENU:
        if resource_check(choice):
            sum = 0
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))*0.1
            nickles = int(input("How many nickles?: "))*0.05
            pennies = int(input("How many pennies?: "))*0.01
            sum += (quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01)
            if (money_required(choice) <= sum):
                diff = round(sum - money_required(choice), 2)
                print(f"Here is ${diff} in change.")
                print(f"Here is your {choice} ☕ . Enjoy!")
                resource_change(choice)
            else:
                print("Sorry that's not enough money. Money refunded.")
                continue
    else:
        print("Invalid input")


# check if machine have enough resources
# if resources are enough proceed -> 

# asking them to pay the amount 
# summing up and checking if the coins they have inserted if enough
# if not don't process further and refund the money
# else
# print the (change amount to be returned) and decrease the resources amount
# print the required drink 
# loop again

# on typing report it should display the resources left

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not Enough {item}")
            is_enough = False
        return is_enough


def process_coin():
    """Return the total coin"""
    print("Insert the coins")
    total = int(input("How many quarters ?")) * 0.25
    total += int(input("How many dimes ?")) * 0.1
    total += int(input("How many nickles ?")) * 0.05
    total += int(input("How many pennies ?")) * 0.1
    return total


def is_transaction_succesful(money_recived, drink_cost):
    """Return true when payment is accepted or False if money is not sufficient"""
    if money_recived >= drink_cost:
        change = round(money_recived - drink_cost, 2)
        print(f"Here is many ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from resource"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "of":
        is_on = False
    elif choice == "report":
        # TODO 1: print the report of all coffee machine resource
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = menu[choice]
        if is_resource(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_succesful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

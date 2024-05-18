MENU = {
    "espresso": {
        "Ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "Ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "Ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

current_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25,
}


def check_resources(drink):
    """Checks if there are resources for a drink."""
    water_required = MENU[drink]["Ingredients"]["water"]
    coffee_required = MENU[drink]["Ingredients"]["coffee"]
    water_available = current_resources["water"]
    coffee_available = current_resources["coffee"]
    milk_available = current_resources["milk"]
    if drink != "espresso":
        milk_required = MENU[drink]["Ingredients"]["milk"]
        if water_available < water_required or milk_available < milk_required or coffee_available < coffee_required:
            if water_available < water_required:
                print("Sorry, there isn't enough water.")
            if coffee_available < coffee_required:
                print("Sorry, there isn't enough coffee.")
            if milk_available < milk_required:
                print("Sorry, there isn't enough milk.")
            return False
        else:
            current_resources["water"] = water_available - water_required
            current_resources["coffee"] = coffee_available - coffee_required
            current_resources["milk"] = milk_available - milk_required
            return True
    else:
        if water_available < water_required or coffee_available < coffee_required:
            if water_available < water_required:
                print("Sorry, there isn't enough water.")
            if coffee_available < coffee_required:
                print("Sorry, there isn't enough coffee.")
            return False
        else:
            current_resources["water"] = water_available - water_required
            current_resources["coffee"] = coffee_available - coffee_required
            return True


def coin_check(drink):
    """Checks if the amount of coins expended is able to get a drink."""
    print("Please insert coins.")
    penny = float(input("How many pennies? "))
    nickel = float(input("How many nickels? "))
    dime = float(input("How many dimes? "))
    quarter = float(input("How many quarters? "))

    coins_pended = (penny * coins['penny']) + (nickel * coins['nickel']) + (dime * coins['dime']) + \
                   (quarter * coins['quarter'])
    price = MENU[drink]['cost']
    if coins_pended < price:
        print("Sorry, that is not enough money. Money refunded")
        if drink != "espresso":
            current_resources["water"] += MENU[drink]["Ingredients"]['water']
            current_resources["coffee"] += MENU[drink]["Ingredients"]["coffee"]
            current_resources["milk"] += MENU[drink]["Ingredients"]['milk']
        else:
            current_resources["water"] += MENU[drink]["Ingredients"]['water']
            current_resources["coffee"] += MENU[drink]["Ingredients"]["coffee"]
    elif coins_pended > price:
        change = coins_pended - price
        print(f"Here is your {drink} ☕. Enjoy!")
        print(f"Here is ${change} in change")
        current_resources["money"] += price
    else:
        print(f"Here is your {drink}. Enjoy!")
        print("No change")
        current_resources["money"] += price


constant_supply = True
while constant_supply:
    prompt = input("What would you like? (espresso/latte/cappuccino):  ")
    if prompt == "report":
        print(f"Water: {current_resources['water']}ml")
        print(f"Milk: {current_resources['milk']}ml")
        print(f"Coffee: {current_resources['coffee']}g")
        print(f"Money: ${current_resources['money']}")
    elif prompt == "off":
        constant_supply = False
    else:
        choice = prompt
        resources_available = check_resources(drink=choice)
        if resources_available:
            coin_check(choice)

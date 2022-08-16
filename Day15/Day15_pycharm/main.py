MENU = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}


def promptForCoins():
    quarters = int(input("Insert an amount of quarters: "))
    dimes = int(input("Insert an amount of dimes: "))
    nickles = int(input("Insert an amount of nickles: "))
    pennies = int(input("Insert an amount of pennies: "))

    totalCoinage = round((0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies), 2)

    return totalCoinage


userInput = str(input("What would you like? (espresso/latte/cappuccino): "))

while not userInput == "off":
    if userInput == 'report':
        # do report stuff
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")

    if userInput == 'espresso' or userInput == 'latte' or userInput == 'cappuccino':
        if resources['water'] - MENU[userInput]["ingredients"]["water"] >= 0:

            try:
                if resources['milk'] - MENU[userInput]["ingredients"]["milk"] >= 0:
                    if resources['coffee'] - MENU[userInput]["ingredients"]["coffee"] >= 0:
                        totalMoney = promptForCoins()
                        if totalMoney >= MENU[userInput]["cost"]:
                            resources['water'] -= MENU[userInput]["ingredients"]["water"]
                            resources['milk'] -= MENU[userInput]["ingredients"]["milk"]
                            resources['coffee'] -= MENU[userInput]["ingredients"]["coffee"]
                            resources['money'] += MENU[userInput]["cost"]
                            change = totalMoney - MENU[userInput]["cost"]
                            change = round(change, 2)
                            if change > 0:
                                print(f"Here is your change: ${change}")
                            print(f"Here is your {userInput} ☕️. Enjoy!")
                        else:
                            print("Not enough money.")
                    else:
                        print("Sorry there is not enough coffee.")
                else:
                    print("Sorry there is not enough milk.")
            except KeyError:
                if resources['coffee'] - MENU[userInput]["ingredients"]["coffee"] >= 0:
                    totalMoney = promptForCoins()
                    if totalMoney >= MENU[userInput]["cost"]:
                        resources['water'] -= MENU[userInput]["ingredients"]["water"]
                        resources['coffee'] -= MENU[userInput]["ingredients"]["coffee"]
                        resources['money'] += MENU[userInput]["cost"]
                        change = totalMoney - MENU[userInput]["cost"]
                        change = round(change, 2)
                        if change > 0:
                            print(f"Here is your change: ${change}")
                        print(f"Here is your {userInput} ☕️. Enjoy!")
                    else:
                        print("Not enough money.")
                else:
                    print("Sorry there is not enough coffee.")

        else:
            print("Sorry there is not enough water.")

    userInput = str(input("What would you like? (espresso/latte/cappuccino): "))



print("Powering off...")


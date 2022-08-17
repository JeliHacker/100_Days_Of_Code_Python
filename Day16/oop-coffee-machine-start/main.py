from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


MENU = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

is_on = True

while is_on == True:

    prompt = str(input(f"What would you like to drink? {MENU.get_items()}: "))

    if prompt == "off":
        is_on = False
        print("Turning off...")
        break


    if prompt == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        itemOrdered = MENU.find_drink(prompt)
        if itemOrdered:
            if coffeeMaker.is_resource_sufficient(itemOrdered):
                paymentMaid = moneyMachine.make_payment(itemOrdered.cost)
                if paymentMaid:
                    coffeeMaker.make_coffee(itemOrdered)




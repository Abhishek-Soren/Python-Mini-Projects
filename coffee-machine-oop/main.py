from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money_machine = MoneyMachine()

turn_off = False

while not turn_off:
    choice = input("\n\nWhat would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        turn_off = True
    elif choice == "report":
        coffee.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee.make_coffee(drink)

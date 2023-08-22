# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 18:41:20 2023

@author: potato chan
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
}


def find_resources(choice):

    resources["water"] -= MENU[choice]["ingredients"]["water"]
    resources["milk"] -= MENU[choice]["ingredients"]["milk"]
    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]

    if resources["water"] < 0:
        print("Sorry water is less than required.")
        return False

    elif resources["milk"] < 0:
        print("Sorry milk is less than required.")
        return False

    elif resources["coffee"] < 0:
        print("Sorry coffee is less than required.")
        return False

    else:
        return True


def money_deposit(choice):
    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01
    num_quarters = int(input("How many quarters?: "))
    num_dimes = int(input("How many dimes?: "))
    num_nickels = int(input("How many nickels?: "))
    num_pennies = int(input("How many pennies?: "))
    total_amount = quarter*num_quarters + dime * \
        num_dimes + nickel*num_nickels + penny*num_pennies

    left_amount = 0

    for item in MENU:
        if choice == item:
            left_amount = total_amount - MENU[item]["cost"]

    if left_amount < 0:
        print("Sorry amount entered less than needed.")
        return 0

    left_amount = round(left_amount, 2)
    print(f"Here is your ${left_amount} change.")

    return MENU[choice]["cost"]


# coffee_machine = "off"
money = 0


def coffee_machine():
    global money
    user_choice = input(
        "\n\nWhat would you like? (espresso/latte/cappuccino):").lower()

    if user_choice not in ["espresso", "latte", "cappuccino"]:
        print("Wrong Input!")
        return

    should_continue = find_resources(user_choice)

    if not should_continue:
        print("Please Try again.")

    else:

        money += money_deposit(user_choice)

        print("total money : ", money)

    coffee_machine()


coffee_machine()

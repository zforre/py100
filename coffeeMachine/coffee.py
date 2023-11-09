MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.0
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}

# What would you like? (espresso/latte/cappuccino)

order = input("What would you like?")

if order == "report":
    for k, v in resources.items():
        print(f"{k}: {v}")
elif order == "espresso":
    print("espresso")
elif order == "latte":
    print("latte")
elif order == "cappuccino":
    print("cappuccino")


# Please insert coins

# How many quarters, dimes, nickels, and pennies

# give change

# give drink


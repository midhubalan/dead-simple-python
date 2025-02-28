#! /usr/bin/env python


def say_hello():
    """Asks user for their name and prints a greeting"""
    print("Hello, world!")
    name = input("What's your name?\n")
    print("Hi, " + name)


class Special:
    TODAY = "lasagna"


def lunch_order():
    """Asks user for a lunch item and prints retort based on the item"""
    lunch = input("What would you like for lunch?\n")
    # if " " in lunch:
    #     lunch = lunch.split(" ", maxsplit=1)
    match lunch:
        case "pizza":
            print("Pizza!, Pizza!")
        case Special.TODAY:
            print("Today's special is awesome!")
        case "sandwich":
            print("Don't want come between you two!")
        case "tacos":
            print("Taco, taco, TACO, tacotacotaco!")
        case "salad" | "soup":
            print("Eating healthy, eh?")
        # case (flavor, "icecream"):
        #     print(f"Here's your very grown-up {flavor}...lunch.")
        case ice_cream if "ice cream" in ice_cream:
            ice_cream = ice_cream.replace("ice cream", "")
            print(f"Here's your very grown-up {ice_cream}...lunch.")
        case item:
            print(f"Yummy! enjoy your {item}!")


if __name__ == "__main__":
    say_hello()

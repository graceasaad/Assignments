import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance= Cashier()

def main():
    is_on= True
    while is_on:
        choice = input("What would you like? (Small/ Medium/ Large/ Report/ Off): ").lower()
        if choice == "off":
            is_on= False

        elif choice == "report":
            sandwich_maker_instance.report()

        elif choice in recipes:
            sandwich = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
